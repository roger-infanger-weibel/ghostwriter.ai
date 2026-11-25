# Routine-Prompt: Podcast – TESTLAUF

**Cloud Routine:** `TEST: Podcast` (nur manuell starten, kein Zeitplan)
**Repo:** roger-infanger-weibel/ghostwriter.ai

Zweck: Eine Podcast-Folge erzeugen, die **nicht** im Feed erscheint. Roger prüft damit Skript,
Stimmen, Länge und den Gemini-Key.

---

## Ablauf

1. **Woche bestimmen:** die zuletzt abgeschlossene ISO-Kalenderwoche `YYYY-Www`.
2. **Vorlage wählen** (erste vorhandene Datei gewinnt):
   1. `test-runs/YYYY-Www/YYYY-Www.md` (aus dem Test «KI-Wochenrückblick»)
   2. `posts/YYYY-Www.md` (echter Post)
   Gibt es keine von beiden: abbrechen und melden, nichts committen.
3. **Skripte:** Für jede Sprache das vorhandene Test-Skript verwenden, sonst aus der Vorlage nach
   **Phase 4b** in `agent-source/routines/weekly-post.md` schreiben und speichern:

   | Sprache | Skript | MP3 |
   |---|---|---|
   | be (Berndeutsch) | `test-runs/YYYY-Www/podcast-script.md` | `test-runs/YYYY-Www/podcast.mp3` |
   | de (Hochdeutsch) | `test-runs/YYYY-Www/podcast-script-de.md` | `test-runs/YYYY-Www/podcast-de.mp3` |
   | en (Englisch) | `test-runs/YYYY-Www/podcast-script-en.md` | `test-runs/YYYY-Www/podcast-en.mp3` |

4. **Audio erzeugen** (Testmodus – ändert weder Feeds noch Episodenlisten noch `docs/`), Reihenfolge be → de → en:

   ```bash
   pip install -q requests pyyaml
   python podcast/tools/build_episode.py --week YYYY-Www --lang be \
     --script test-runs/YYYY-Www/podcast-script.md --out test-runs/YYYY-Www/podcast.mp3 --dry-run
   python podcast/tools/build_episode.py --week YYYY-Www --lang be \
     --script test-runs/YYYY-Www/podcast-script.md --out test-runs/YYYY-Www/podcast.mp3
   # gleich für --lang de (podcast-script-de.md → podcast-de.mp3) und --lang en (… -en)
   ```

   - Der Gemini-Key ist als Network Secret im Environment hinterlegt; der Proxy setzt ihn selbst.
     Nicht nach einem Key suchen, keinen Key in Dateien oder Umgebungsvariablen schreiben.
   - Schlägt der Aufruf fehl: **nicht** erneut versuchen (Gratis-Kontingent). Die vollständige
     Fehlermeldung in `test-runs/YYYY-Www/podcast-fehler.txt` speichern (mit Sprache), die übrigen
     Sprachen trotzdem versuchen und committen.
   - Dauer der MP3 mit `ffprobe -v error -show_entries format=duration -of csv=p=0 <datei>` messen.

## Commit

Direkt auf `main`, kein Branch, kein PR (Rogers ausdrückliche Vorgabe):

1. `git pull --rebase origin main`
2. **Nur** `git add test-runs/YYYY-Www/` – nie `posts/`, `podcast/`, `docs/` oder `agent-source/`
3. Commit-Titel: `TEST: Podcast KW ww/YYYY`
4. Commit-Body: Vorlage (Test-Post oder echter Post), Dauer, Grösse – oder die Fehlermeldung
5. `git push origin main`. Bei Ablehnung einmal `git pull --rebase origin main` und erneut pushen. Nie `--force`.

## Abschluss

Kurze Zusammenfassung als letzte Ausgabe: Woche, verwendete Vorlage, Dauer und Grösse der MP3
(oder vollständige Fehlermeldung), Pfad `test-runs/YYYY-Www/podcast.mp3`.
