# Podcast: KI-Wochenrückblick

Der Wochenrückblick wird automatisch zu einem berndeutschen Podcast mit zwei Stimmen
(Lena und Marc) und als RSS-Feed auf GitHub Pages veröffentlicht – ohne Hoster.

## Links

<img width="128" height="128" alt="cover (1)" src="https://github.com/user-attachments/assets/ef4e684e-783a-40f9-9f36-fda4e6ace387" />

* User Doku: https://roger-infanger-weibel.github.io/ghostwriter.ai/podcast/
* RSS Feed: https://roger-infanger-weibel.github.io/ghostwriter.ai/podcast/feed.xml
* Spotify: https://open.spotify.com/show/3C4tP9QIc022wpRr49xEsY

## Ablauf

```
Mo 06:00  Cloud Routine «KI-Wochenrückblick»
          → posts/YYYY-Www.md
          → podcast/scripts/YYYY-Www.md          (Dialog-Skript)
          → podcast/tools/build_episode.py       (Gemini TTS, Key via Agent-Proxy)
          → docs/podcast/episodes/YYYY-Www.mp3 + feed.xml   → ein Commit direkt auf main
GitHub    Pages veröffentlicht docs/ (Deploy from branch main /docs)
Podcast-App  holt neue Episoden selbständig über den RSS-Feed
```

## Einmalige Einrichtung

1. **Gemini API Key** (gratis, ohne Kreditkarte): Google AI Studio → «Get API key» → Key erstellen. Der Gemini-Key liegt **nicht** in GitHub, sondern als Network Secret im Claude-Cloud-Environment.
2. **Network Secret in der Claude-Cloud:** claude.ai/code → Environment der Routine bearbeiten →
   **Network secrets** → **Add secret**
   - Name: `Gemini API`
   - Allowed websites: `generativelanguage.googleapis.com`
   - Custom header: Name `x-goog-api-key`, Prefix leer, Value = der Key
   Der Proxy hängt den Key ausserhalb der Session an; Claude sieht ihn nie, und er landet weder im
   Repo noch in Umgebungsvariablen. Den Key **nicht** unter «Environment variables» eintragen
   (dort ist er für jede Session lesbar).
3. **GitHub Pages:** Repo → Settings → Pages → Source: **Deploy from a branch** → `main` / `/docs`.
4. **Erste Episode:** In einer Cloud-Session mit diesem Environment ausführen:
   `python podcast/tools/build_episode.py --week 2026-W46`, Ergebnis committen und pushen.
5. **Abonnieren:** Feed-URL in einer Podcast-App einfügen, die eigene Feeds annimmt:
   Apple Podcasts (Mediathek → «…» → «Sendung per URL folgen»), Pocket Casts, Overcast,
   AntennaPod, Podcast Addict. Auf Spotify: https://open.spotify.com/show/3C4tP9QIc022wpRr49xEsY

Verzeichnisse: `owner_email` in `show.yaml` ist gesetzt (für die Bestätigung nötig, im Feed
öffentlich). Spotify: eingereicht, Link in `show.yaml` (`spotify_url`). Apple Podcasts: noch nicht.

## Dateien

| Datei | Zweck |
|---|---|
| `podcast/show.yaml` | Titel, Beschreibung, Stimmen, TTS-Modell |
| `podcast/scripts/YYYY-Www.md` | Dialog-Skript pro Woche (schreibt die Routine) |
| `podcast/episodes.json` | Episodenliste (schreibt `build_episode.py`) |
| `podcast/tools/` | Build-Skripte (TTS, MP3, Feed) |
| `docs/podcast/` | Öffentliche Dateien: Feed, Cover, MP3s |

## Bedienung

- **Episode neu erzeugen** (z. B. nach Skriptkorrektur): in einer Cloud-Session
  `python podcast/tools/build_episode.py --week 2026-W46 --force`
- **Lokal:** mit `GEMINI_API_KEY` als Umgebungsvariable gleich aufrufen.
- **Skript prüfen ohne API:** `python podcast/tools/build_episode.py --dry-run`
- **Startmusik:** `podcast/assets/intro-radar.wav` (ca. 4 s, rein synthetisch, Radar-Sweep mit
  Sonar-Pings) läuft vor jeder Folge. Neu erzeugen/anpassen: `python podcast/tools/make_jingle.py`;
  abschalten: `audio.intro` in `show.yaml` leeren.
- **Länge:** Ziel fast 3 Minuten (`length` in `show.yaml`, 2400–2800 Zeichen). Der Dry-Run meldet
  «ZU KURZ» / «ZU LANG».
- **Testfolge ohne Feed:** `--script <datei> --out test-runs/.../podcast.mp3` (siehe `test-runs/README.md`).
- **Stimmen ändern:** `tts.speakers[].voice` in `show.yaml` (30 vordefinierte Stimmen, z. B. Kore,
  Puck, Charon, Aoede, Leda, Orus).

## Grenzen

- Gratis-Kontingent der Gemini API: Limits ändert Google laufend, aktueller Stand in AI Studio.
  Bei HTTP 429 wartet das Skript und versucht es erneut. Inhalte im Gratis-Kontingent darf Google
  zur Produktverbesserung nutzen.
- MP3s liegen im Repo (ca. 3–4 MB pro Folge, rund 200 MB pro Jahr).
