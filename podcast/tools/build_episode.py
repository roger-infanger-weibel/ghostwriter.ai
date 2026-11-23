#!/usr/bin/env python3
"""Erzeugt Podcast-Episoden aus podcast/scripts/*.md via Gemini TTS.

Läuft in der Claude Cloud Routine (Key als Network Secret, nie im Repo).

Ablauf pro Skript ohne bestehende Episode:
  Skript parsen -> in Teile zerlegen -> Gemini TTS (2 Sprecher) -> WAV zusammensetzen
  -> MP3 (ffmpeg) -> docs/podcast/episodes/ -> podcast/episodes.json -> feed.xml

Aufruf:
  python podcast/tools/build_episode.py               # alle Skripte ohne Episode
  python podcast/tools/build_episode.py --week 2026-W46
  python podcast/tools/build_episode.py --dry-run     # nur parsen, kein API-Aufruf

Testmodus (ändert weder episodes.json noch feed.xml noch docs/):
  python podcast/tools/build_episode.py --week 2026-W47 \
      --script test-runs/2026-W47/podcast-script.md --out test-runs/2026-W47/podcast.mp3
"""
from __future__ import annotations

import argparse
import base64
import io
import json
import os
import re
import subprocess
import sys
import tempfile
import time
import wave
from datetime import date, datetime, timedelta, timezone
from email.utils import format_datetime
from pathlib import Path

import requests
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_feed import build_feed  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
PODCAST = ROOT / "podcast"
SCRIPTS = PODCAST / "scripts"
EPISODES_JSON = PODCAST / "episodes.json"
SITE = ROOT / "docs" / "podcast"
EPISODE_DIR = SITE / "episodes"

API_URL = "https://generativelanguage.googleapis.com/v1beta/interactions"
SAMPLE_RATE = 24000
WEEK_RE = re.compile(r"^\d{4}-W\d{2}$")
TURN_RE = re.compile(r"^(?P<speaker>[^\s:\[\]]+)\s*(?:\[(?P<style>[^\]]+)\])?\s*:\s*(?P<text>.*)$")


# ---------------------------------------------------------------- Skript

def parse_script(path: Path, speaker_names: list[str]) -> tuple[dict, list[dict]]:
    raw = path.read_text(encoding="utf-8")
    meta: dict = {}
    body = raw
    if raw.startswith("---"):
        _, fm, body = raw.split("---", 2)
        meta = yaml.safe_load(fm) or {}
    for key in ("title", "description"):
        if not meta.get(key):
            raise ValueError(f"{path.name}: Frontmatter-Feld '{key}' fehlt")

    turns: list[dict] = []
    for lineno, line in enumerate(body.splitlines(), 1):
        s = line.strip()
        if not s or s.startswith("#") or s.startswith("<!--"):
            continue
        s = s.replace("**", "")
        m = TURN_RE.match(s)
        if m and m.group("speaker") in speaker_names:
            turns.append({
                "speaker": m.group("speaker"),
                "style": (m.group("style") or "").strip(),
                "text": m.group("text").strip(),
            })
        elif turns:
            turns[-1]["text"] += " " + s  # Fortsetzungszeile
        else:
            raise ValueError(f"{path.name}:{lineno}: Zeile ohne bekannten Sprecher: {s[:60]}")
    turns = [t for t in turns if t["text"]]
    if not turns:
        raise ValueError(f"{path.name}: keine Dialogzeilen gefunden")
    return meta, turns


def chunk_turns(turns: list[dict], max_chars: int) -> list[list[dict]]:
    chunks: list[list[dict]] = []
    cur: list[dict] = []
    size = 0
    for t in turns:
        n = len(t["text"])
        if cur and size + n > max_chars:
            chunks.append(cur)
            cur, size = [], 0
        cur.append(t)
        size += n
    if cur:
        chunks.append(cur)
    return chunks


# ---------------------------------------------------------------- TTS

def _find_audio_b64(obj) -> str | None:
    """Sucht die Audiodaten in der Antwort (steps[].content[].data, letzter Treffer)."""
    found = None
    if isinstance(obj, dict):
        steps = obj.get("steps")
        if isinstance(steps, list):
            for step in steps:
                for c in (step or {}).get("content", []) or []:
                    if isinstance(c, dict) and isinstance(c.get("data"), str):
                        found = c["data"]
        if found:
            return found
        for key in ("output_audio", "outputAudio"):
            if isinstance(obj.get(key), dict) and isinstance(obj[key].get("data"), str):
                return obj[key]["data"]
        for v in obj.values():
            r = _find_audio_b64(v)
            if r:
                found = r
    elif isinstance(obj, list):
        for v in obj:
            r = _find_audio_b64(v)
            if r:
                found = r
    return found


def _to_pcm(audio: bytes) -> bytes:
    if audio[:4] == b"RIFF":
        with wave.open(io.BytesIO(audio)) as w:
            if w.getframerate() != SAMPLE_RATE or w.getnchannels() != 1 or w.getsampwidth() != 2:
                raise ValueError(
                    f"Unerwartetes Audioformat: {w.getframerate()} Hz, "
                    f"{w.getnchannels()} Kanäle, {w.getsampwidth() * 8} Bit")
            return w.readframes(w.getnframes())
    return audio  # rohes PCM (audio/l16, 24 kHz mono)


def synthesize(chunk: list[dict], cfg: dict, api_key: str | None) -> bytes:
    tts = cfg["tts"]
    default_style = {s["name"]: s.get("style", "") for s in tts["speakers"]}
    content = []
    for t in chunk:
        ann = {"type": "speech_metadata", "speaker": t["speaker"]}
        style = t["style"] or default_style.get(t["speaker"], "")
        if style:
            ann["style"] = style
        content.append({"type": "text", "text": t["text"], "annotations": [ann]})
    body = {
        "model": tts["model"],
        "input": [{"type": "user_input", "content": content}],
        "response_format": {"type": "audio"},
        "generation_config": {"speech_config": {"speakers": [
            {"speaker": s["name"], "voice": s["voice"]} for s in tts["speakers"]
        ]}},
    }
    headers = {"Content-Type": "application/json"}
    if api_key:  # sonst setzt der Claude-Agent-Proxy den Key (Network Secret)
        headers["x-goog-api-key"] = api_key

    for attempt in range(1, 7):
        r = requests.post(API_URL, headers=headers, json=body, timeout=600)
        if r.status_code in (429, 500, 502, 503, 504):
            wait = 30 * attempt
            print(f"  HTTP {r.status_code}, neuer Versuch in {wait}s …", flush=True)
            time.sleep(wait)
            continue
        if r.status_code in (401, 403):
            raise RuntimeError(
                f"Gemini TTS HTTP {r.status_code}: Key fehlt oder ungültig. In der Claude-Cloud "
                "muss das Environment ein Network Secret für generativelanguage.googleapis.com "
                f"(Header x-goog-api-key) haben. Antwort: {r.text[:300]}")
        if r.status_code != 200:
            raise RuntimeError(f"Gemini TTS HTTP {r.status_code}: {r.text[:500]}")
        b64 = _find_audio_b64(r.json())
        if not b64:
            raise RuntimeError(f"Keine Audiodaten in der Antwort: {r.text[:500]}")
        return _to_pcm(base64.b64decode(b64))
    raise RuntimeError("Gemini TTS: zu viele Fehlversuche (Rate-Limit?)")


# ---------------------------------------------------------------- Datum

MONATE = ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August",
          "September", "Oktober", "November", "Dezember"]
KW_PREFIX_RE = re.compile(r"^\s*KW\s*\d+\s*/\s*\d{4}\s*[:·–-]\s*")


def week_range(week: str) -> tuple[date, date]:
    y, w = int(week[:4]), int(week[6:])
    return date.fromisocalendar(y, w, 1), date.fromisocalendar(y, w, 7)


def zeitraum(week: str) -> str:
    """z. B. «9.–15. November 2026» oder «31. August – 6. September 2026»."""
    a, b = week_range(week)
    if a.year != b.year:
        return f"{a.day}. {MONATE[a.month - 1]} {a.year} – {b.day}. {MONATE[b.month - 1]} {b.year}"
    if a.month != b.month:
        return f"{a.day}. {MONATE[a.month - 1]} – {b.day}. {MONATE[b.month - 1]} {b.year}"
    return f"{a.day}.–{b.day}. {MONATE[b.month - 1]} {b.year}"


def episode_title(week: str, title: str) -> str:
    """«KW 46 · 9.–15. November 2026: <Themen>» – Datum steht so in jeder Podcast-App."""
    topics = KW_PREFIX_RE.sub("", title).strip()
    return f"KW {int(week[6:])} · {zeitraum(week)}: {topics}"


def pub_date(week: str) -> str:
    """Erscheinungsdatum = Sonntag der Woche, 18:00 Zürich (17:00 UTC)."""
    _, sunday = week_range(week)
    return format_datetime(datetime(sunday.year, sunday.month, sunday.day, 17, 0, tzinfo=timezone.utc))


# ---------------------------------------------------------------- Episode

def encode_mp3(pcm: bytes, out: Path, meta: dict, cfg: dict) -> None:
    with tempfile.TemporaryDirectory() as tmp:
        wav_path = Path(tmp) / "episode.wav"
        with wave.open(str(wav_path), "wb") as w:
            w.setnchannels(1)
            w.setsampwidth(2)
            w.setframerate(SAMPLE_RATE)
            w.writeframes(pcm)
        subprocess.run([
            "ffmpeg", "-y", "-loglevel", "error", "-i", str(wav_path),
            "-ac", "1", "-codec:a", "libmp3lame", "-b:a", cfg["audio"]["bitrate"],
            "-id3v2_version", "3",
            "-metadata", f"title={meta['episode_title']}",
            "-metadata", f"artist={cfg['author']}",
            "-metadata", f"album={cfg['title']}",
            str(out),
        ], check=True)


def load_episodes() -> list[dict]:
    if EPISODES_JSON.exists():
        return json.loads(EPISODES_JSON.read_text(encoding="utf-8"))
    return []


def save_episodes(eps: list[dict]) -> None:
    EPISODES_JSON.write_text(json.dumps(eps, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def build(week: str, cfg: dict, api_key: str | None, dry_run: bool,
          script: Path | None = None, out: Path | None = None) -> dict | None:
    path = script or SCRIPTS / f"{week}.md"
    names = [s["name"] for s in cfg["tts"]["speakers"]]
    meta, turns = parse_script(path, names)
    chunks = chunk_turns(turns, int(cfg["tts"]["max_chars_per_request"]))
    chars = sum(len(t["text"]) for t in turns)
    print(f"{episode_title(week, meta['title'])} | {pub_date(week)}")
    print(f"{week}: {len(turns)} Wortmeldungen, {chars} Zeichen, {len(chunks)} API-Aufrufe")
    if dry_run:
        return None

    silence = b"\x00\x00" * int(SAMPLE_RATE * 0.35)
    pcm = b""
    for i, chunk in enumerate(chunks, 1):
        if i > 1:
            time.sleep(float(cfg["tts"].get("pause_seconds", 0)))
            pcm += silence
        print(f"  Teil {i}/{len(chunks)} …", flush=True)
        pcm += synthesize(chunk, cfg, api_key)

    mp3 = out or EPISODE_DIR / f"{week}.mp3"
    mp3.parent.mkdir(parents=True, exist_ok=True)
    meta["episode_title"] = episode_title(week, meta["title"])
    encode_mp3(pcm, mp3, meta, cfg)
    return {
        "id": week,
        "title": meta["episode_title"],
        "description": f"Zeitraum: {zeitraum(week)}. " + str(meta["description"]).strip(),
        "post": f"posts/{week}.md",
        "file": f"episodes/{week}.mp3",
        "bytes": mp3.stat().st_size,
        "duration_seconds": round(len(pcm) / 2 / SAMPLE_RATE),
        "pub_date": pub_date(week),
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--week", help="ISO-Woche, z. B. 2026-W46")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--force", action="store_true", help="bestehende Episode neu erzeugen")
    ap.add_argument("--script", type=Path, help="Testmodus: Skript-Datei (statt podcast/scripts/)")
    ap.add_argument("--out", type=Path, help="Testmodus: Ziel-MP3; Feed und episodes.json bleiben unverändert")
    args = ap.parse_args()

    cfg = yaml.safe_load((PODCAST / "show.yaml").read_text(encoding="utf-8"))
    if len(cfg["tts"]["speakers"]) != 2:
        print("show.yaml: genau zwei Sprecher nötig", file=sys.stderr)
        return 1

    if args.script or args.out:
        if not (args.script and args.out and args.week and WEEK_RE.match(args.week)):
            print("Testmodus braucht --week, --script und --out", file=sys.stderr)
            return 1
        if args.out.resolve().is_relative_to(SITE.resolve()):
            print("Testmodus: --out darf nicht unter docs/podcast liegen", file=sys.stderr)
            return 1
        ep = build(args.week, cfg, os.environ.get("GEMINI_API_KEY"), args.dry_run,
                   script=args.script, out=args.out)
        if ep:
            print(f"  -> {args.out} ({ep['duration_seconds']} s, {ep['bytes'] // 1024} KB) [Test]")
        return 0

    episodes = load_episodes()
    done = {e["id"] for e in episodes}
    if args.week:
        if not WEEK_RE.match(args.week):
            print(f"Ungültige Woche: {args.week}", file=sys.stderr)
            return 1
        weeks = [args.week]
    else:
        weeks = sorted(p.stem for p in SCRIPTS.glob("*.md") if WEEK_RE.match(p.stem))
    if not args.force:
        weeks = [w for w in weeks if w not in done]
    if not weeks:
        print("Keine neuen Skripte.")
        build_feed(cfg, episodes, SITE)
        return 0

    # In der Claude-Cloud fügt der Agent-Proxy den Key als Network Secret hinzu;
    # GEMINI_API_KEY ist nur für lokale Läufe nötig.
    api_key = os.environ.get("GEMINI_API_KEY")

    for week in weeks:
        ep = build(week, cfg, api_key, args.dry_run)
        if ep:
            episodes = [e for e in episodes if e["id"] != week] + [ep]
            episodes.sort(key=lambda e: e["id"])
            save_episodes(episodes)
            print(f"  -> {ep['file']} ({ep['duration_seconds']} s, {ep['bytes'] // 1024} KB)")
    build_feed(cfg, episodes, SITE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
