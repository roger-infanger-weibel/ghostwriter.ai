#!/usr/bin/env python3
"""Erzeugt die Radar-Startmusik (podcast/assets/intro-radar.wav), rein synthetisch.

Aufbau (ca. 4 s, 24 kHz mono 16 Bit, gleiches Format wie die TTS-Stimmen):
  - leiser, warmer Drone mit langsamem «Sweep» (Filter-Bewegung wie ein Radarstrahl)
  - drei Sonar-Pings mit Hall/Echo, der letzte etwas höher
  - kurzes Ausblenden, damit die Begrüssung sauber anschliesst

Aufruf: python podcast/tools/make_jingle.py
"""
from __future__ import annotations

import wave
from pathlib import Path

import numpy as np

SR = 24000
DUR = 4.2
OUT = Path(__file__).resolve().parents[1] / "assets" / "intro-radar.wav"


def env_exp(n: int, tau: float) -> np.ndarray:
    return np.exp(-np.arange(n) / (tau * SR))


def ping(freq: float, length: float = 1.6) -> np.ndarray:
    n = int(length * SR)
    t = np.arange(n) / SR
    tone = np.sin(2 * np.pi * freq * t) + 0.35 * np.sin(2 * np.pi * freq * 2.01 * t)
    attack = np.minimum(1.0, t / 0.004)
    return tone * attack * env_exp(n, 0.32)


def add(buf: np.ndarray, sig: np.ndarray, at: float, gain: float) -> None:
    i = int(at * SR)
    j = min(len(buf), i + len(sig))
    buf[i:j] += gain * sig[: j - i]


def main() -> None:
    n = int(DUR * SR)
    t = np.arange(n) / SR
    out = np.zeros(n)

    # Drone: zwei leicht verstimmte Töne, Lautstärke «kreist» wie ein Radarstrahl
    drone = np.sin(2 * np.pi * 110 * t) + 0.6 * np.sin(2 * np.pi * 110.7 * t) \
        + 0.25 * np.sin(2 * np.pi * 220 * t)
    sweep = 0.55 + 0.45 * np.sin(2 * np.pi * 0.45 * t - np.pi / 2)
    fade_in = np.minimum(1.0, t / 0.6)
    out += 0.16 * drone * sweep * fade_in

    # Sonar-Pings mit zwei Echos
    for at, f, g in ((0.35, 1320, 0.42), (1.45, 1320, 0.36), (2.55, 1760, 0.40)):
        p = ping(f)
        add(out, p, at, g)
        add(out, p, at + 0.23, g * 0.35)
        add(out, p, at + 0.46, g * 0.15)

    # Ausblenden
    fade_out = np.ones(n)
    k = int(0.9 * SR)
    fade_out[-k:] = np.linspace(1.0, 0.0, k) ** 2
    out *= fade_out

    out /= max(1e-9, np.max(np.abs(out)))
    pcm = (out * 0.7 * 32767).astype("<i2")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with wave.open(str(OUT), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(pcm.tobytes())
    print(f"{OUT} ({DUR:.1f} s)")


if __name__ == "__main__":
    main()
