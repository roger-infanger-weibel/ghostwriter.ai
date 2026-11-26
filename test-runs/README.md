# Testläufe

Hier schreiben die manuell gestarteten Test-Routinen ihre Ergebnisse hin. Nichts davon wird
veröffentlicht: GitHub Pages zeigt nur `docs/`, der Podcast-Feed enthält keine Testfolgen.

| Datei in `test-runs/YYYY-Www/` | Erzeugt von |
|---|---|
| `YYYY-Www.md` | TEST: KI-Wochenrückblick (gleiches Format wie `posts/YYYY-Www.md`) |
| `quellen-report.md` | TEST: KI-Wochenrückblick (Status jeder Quelle aus `SOURCES.md`) |
| `podcast-script.md` | TEST: KI-Wochenrückblick oder TEST: Podcast (Berndeutsch) |
| `podcast-script-de.md`, `podcast-script-en.md` | dito, Hochdeutsch und Englisch |
| `podcast.mp3` | TEST: Podcast (Berndeutsch) |
| `podcast-de.mp3`, `podcast-en.mp3` | TEST: Podcast, Hochdeutsch und Englisch |
| `podcast-fehler.txt` | TEST: Podcast, nur bei Fehler |

Anleitungen: `agent-source/routines/weekly-post-test.md`, `agent-source/routines/podcast-test.md`.
Ein neuer Testlauf für dieselbe Woche überschreibt den vorigen. Alte Ordner können gelöscht werden.
