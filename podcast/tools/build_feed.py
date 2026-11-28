"""Schreibt docs/podcast/feed.xml (RSS 2.0 + iTunes-Tags) aus show.yaml und episodes.json."""
from __future__ import annotations

from email.utils import format_datetime
from datetime import datetime, timezone
import re
from pathlib import Path
from xml.sax.saxutils import escape


def _dur(sec: int) -> str:
    h, rem = divmod(int(sec), 3600)
    m, s = divmod(rem, 60)
    return f"{h:02d}:{m:02d}:{s:02d}"


REGIONS = ("global", "europa", "schweiz", "radar")
ICONS = {"global": "🌍", "europa": "🇪🇺", "schweiz": "🇨🇭", "radar": "📡"}
DEFAULT_LABELS = {"global": "Global", "europa": "Europa", "schweiz": "Schweiz", "radar": "Auf dem Radar",
                  "none": "Keine Top-News", "shownotes": "Ausführliche Shownotes",
                  "sources": "Alle durchsuchten Quellen",
                  "ai": "Recherchiert und geschrieben von KI-Agenten, gesprochen von KI-Stimmen (HOOTL – Human Out of the Loop)."}


def news_from_post(post: Path) -> list[dict]:
    """Fallback für ältere Folgen: Titel und Link jeder Meldung aus dem Wochenpost (hochdeutsch)."""
    if not post.exists():
        return []
    items, region, title = [], None, None
    names = {"global": "global", "europa": "europa", "schweiz": "schweiz", "auf dem radar": "radar"}
    for line in post.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            region = names.get(line[3:].strip().lower())
        elif line.startswith("### ") and region:
            title = line[4:].strip()
        elif line.startswith("Quelle:") and region and title:
            m = re.search(r"\]\((https?://[^)\s]+)\)", line)
            items.append({"region": region, "title": title, "url": m.group(1) if m else ""})
            title = None
    return items


def shownotes(ep: dict, cfg: dict, root: Path) -> tuple[str, str]:
    """Shownotes als Text (für <description>, z. B. Spotify) und als HTML (für <content:encoded>, z. B. Apple)."""
    L = {**DEFAULT_LABELS, **cfg.get("shownotes_labels", {})}
    news = ep.get("news") or news_from_post(root / ep["post"])
    post_url = f"{cfg['website']}/blob/main/{ep['post']}"
    src_url = f"{cfg['website']}/blob/main/SOURCES.md"
    txt, html = [ep["description"]], [f"<p>{escape(ep['description'])}</p>"]
    if news:
        for r in REGIONS:
            part = [n for n in news if n.get("region") == r]
            if not part and r == "radar":
                continue
            txt.append(f"\n{ICONS[r]} {L[r]}")
            html.append(f"<p><b>{ICONS[r]} {escape(L[r])}</b></p>")
            if not part:
                txt.append(f"• {L['none']}")
                html.append(f"<ul><li>{escape(L['none'])}</li></ul>")
                continue
            lis = []
            for n in part:
                txt.append(f"• {n['title']}" + (f"\n  {n['url']}" if n.get("url") else ""))
                t = escape(n["title"])
                lis.append(f'<li><a href="{escape(n["url"])}">{t}</a></li>' if n.get("url") else f"<li>{t}</li>")
            html.append("<ul>" + "".join(lis) + "</ul>")
    txt.append(f"\n🤖 {L['ai']}")
    html.append(f"<p>🤖 {escape(L['ai'])}</p>")
    txt.append(f"\n📄 {L['shownotes']}: {post_url}\n🔎 {L['sources']}: {src_url}")
    html.append(f'<p>📄 <a href="{escape(post_url)}">{escape(L["shownotes"])}</a><br>'
                f'🔎 <a href="{escape(src_url)}">{escape(L["sources"])}</a></p>')
    return "\n".join(txt), "".join(html)


def build_feed(cfg: dict, episodes: list[dict], site: Path) -> Path:
    base = cfg["base_url"].rstrip("/")
    e = escape
    items = []
    for ep in sorted(episodes, key=lambda x: x["id"], reverse=True):
        # ?v=<Grösse>: neue Adresse, sobald eine Folge neu erzeugt wird (umgeht Browser-/CDN-Cache)
        url = f"{base}/{ep['file']}?v={ep['bytes']}"
        post_url = f"{cfg['website']}/blob/main/{ep['post']}"
        desc, desc_html = shownotes(ep, cfg, site.parents[1])
        items.append(f"""    <item>
      <title>{e(ep['title'])}</title>
      <description>{e(desc)}</description>
      <content:encoded><![CDATA[{desc_html.replace(']]>', ']]&gt;')}]]></content:encoded>
      <link>{e(post_url)}</link>
      <guid isPermaLink="false">ghostwriter-ai-{e(ep['id'])}</guid>
      <pubDate>{e(ep['pub_date'])}</pubDate>
      <enclosure url="{e(url)}" length="{ep['bytes']}" type="audio/mpeg"/>
      <itunes:duration>{_dur(ep['duration_seconds'])}</itunes:duration>
      <itunes:episodeType>full</itunes:episodeType>
      <itunes:explicit>{'true' if cfg.get('explicit') else 'false'}</itunes:explicit>
    </item>""")

    # E-Mail nur, wenn in show.yaml gesetzt (nötig erst für Verzeichnisse wie Spotify/Apple)
    owner = ""
    if cfg.get("owner_email"):
        owner = (f"    <itunes:owner>\n      <itunes:name>{e(cfg['author'])}</itunes:name>\n"
                 f"      <itunes:email>{e(cfg['owner_email'])}</itunes:email>\n    </itunes:owner>\n")
    now = format_datetime(datetime.now(timezone.utc).replace(microsecond=0))
    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0"
     xmlns:itunes="http://www.itunes.com/dtds/podcast-1.0.dtd"
     xmlns:atom="http://www.w3.org/2005/Atom"
     xmlns:content="http://purl.org/rss/1.0/modules/content/">
  <channel>
    <title>{e(cfg['title'])}</title>
    <link>{e(cfg['website'])}</link>
    <atom:link href="{e(base)}/{e(cfg.get('feed_file', 'feed.xml'))}" rel="self" type="application/rss+xml"/>
    <description>{e(cfg['description'])}</description>
    <language>{e(cfg['language'])}</language>
    <lastBuildDate>{now}</lastBuildDate>
    <itunes:subtitle>{e(cfg.get('subtitle', ''))}</itunes:subtitle>
    <itunes:summary>{e(cfg['description'])}</itunes:summary>
    <itunes:author>{e(cfg['author'])}</itunes:author>
{owner}    <itunes:image href="{e(base)}/{e(cfg['cover_file'])}"/>
    <image>
      <url>{e(base)}/{e(cfg['cover_file'])}</url>
      <title>{e(cfg['title'])}</title>
      <link>{e(cfg['website'])}</link>
    </image>
    <itunes:category text="{e(cfg['category'])}"/>
    <itunes:explicit>{'true' if cfg.get('explicit') else 'false'}</itunes:explicit>
    <itunes:type>episodic</itunes:type>
{chr(10).join(items)}
  </channel>
</rss>
"""
    site.mkdir(parents=True, exist_ok=True)
    out = site / cfg.get("feed_file", "feed.xml")
    out.write_text(xml, encoding="utf-8")
    return out


if __name__ == "__main__":
    # Nur Feed neu schreiben (z. B. nach Änderung von show.yaml), ohne Audio/API:
    #   python podcast/tools/build_feed.py
    #   python podcast/tools/build_feed.py --lang de
    import argparse
    import json
    import sys
    import yaml
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import build_episode as be  # noqa: E402
    ap = argparse.ArgumentParser()
    ap.add_argument("--lang", default="be")
    lang = ap.parse_args().lang
    root = Path(__file__).resolve().parents[2]
    cfg = be.apply_lang(yaml.safe_load((root / "podcast" / "show.yaml").read_text(encoding="utf-8")), lang)
    eps = json.loads(be.EPISODES_JSON.read_text(encoding="utf-8")) if be.EPISODES_JSON.exists() else []
    out = build_feed(cfg, eps, root / "docs" / "podcast")
    print(f"{out.relative_to(root)}: «{cfg['title']}», {len(eps)} Episoden")
