# Routine-Prompt: KI-Wochenrückblick – TESTLAUF

**Cloud Routine:** `TEST: KI-Wochenrückblick` (nur manuell starten, kein Zeitplan)
**Repo:** roger-infanger-weibel/ghostwriter.ai

Zweck: Den Wochenrückblick genau wie im Produktivlauf erstellen, aber **nichts veröffentlichen**.
Roger prüft damit, ob die Quellen funktionieren und wie der Post aussieht.

---

## Ablauf

1. Lies `agent-source/routines/weekly-post.md` und führe **Phase 1 bis 4b** genau so aus
   (gleiche Quellen, gleiche Kriterien, gleiches Format). Phase 4c (Audio) entfällt: dafür gibt es
   den separaten Test `podcast-test.md`.
2. **Woche:** die zuletzt abgeschlossene ISO-Kalenderwoche (wie im Produktivlauf). Es spielt keine
   Rolle, ob es für diese Woche schon einen echten Post gibt – der Test wird trotzdem erstellt.
3. **Ausgabe – nur in diesen Pfaden** (`YYYY-Www` = Testwoche):

   | Datei | Inhalt |
   |---|---|
   | `test-runs/YYYY-Www/YYYY-Www.md` | Post im exakt gleichen Format wie `posts/YYYY-Www.md` |
   | `test-runs/YYYY-Www/podcast-script.md` | Podcast-Skript nach Phase 4b |
   | `test-runs/YYYY-Www/quellen-report.md` | Prüfbericht zu den Quellen (siehe unten) |

   Bestehende Dateien im selben Testordner werden überschrieben (jeder Testlauf ersetzt den vorigen).

## Quellen-Report (`quellen-report.md`)

```markdown
# Quellen-Report – Testlauf KW ww / YYYY

Gestartet: <Datum, Uhrzeit Zürich>

| Quelle (aus SOURCES.md) | URL | Status | Treffer letzte 7 Tage | Bemerkung |
|---|---|---|---|---|
| Anthropic News | https://… | ✅ OK / ⚠️ teilweise / ❌ Fehler (HTTP 403, Timeout, …) | 2 | z. B. «Seite lädt nur per JavaScript» |

## Zusammenfassung
- Quellen geprüft: n, davon OK: n, teilweise: n, Fehler: n
- Kandidaten vor Filter: n, Einträge nach Filter: n (Global n, Europa n, Schweiz n)

## Vorschläge
- Konkrete Hinweise, welche Quelle in SOURCES.md ersetzt oder ergänzt werden sollte (mit
  alternativer URL, falls gefunden). **Nur vorschlagen, SOURCES.md nicht ändern.**
```

- **Jede** Quelle aus `SOURCES.md` bekommt eine Zeile, auch die ohne Treffer.
- Status ehrlich angeben: ❌ heisst, die Seite war nicht abrufbar (HTTP-Code oder Fehler nennen).
- Blockiert der Netzwerk-Proxy einen Host («no rule allows host» o. ä.), in der Bemerkung
  «vom Environment blockiert» schreiben.

## Commit

Direkt auf `main`, kein Branch, kein PR (Rogers ausdrückliche Vorgabe):

1. `git pull --rebase origin main`
2. **Nur** `git add test-runs/YYYY-Www/` – nie `posts/`, `podcast/`, `docs/`, `SOURCES.md` oder `agent-source/`
3. Commit-Titel: `TEST: KI-Wochenrückblick KW ww/YYYY`
4. Commit-Body: Zusammenfassung aus dem Quellen-Report (geprüft / OK / Fehler, Einträge)
5. `git push origin main`. Bei Ablehnung einmal `git pull --rebase origin main` und erneut pushen. Nie `--force`.

## Abschluss

Gib als letzte Ausgabe eine kurze Zusammenfassung (max. 10 Zeilen): Testwoche, Anzahl
Quellen OK/Fehler mit Namen der fehlerhaften, Anzahl Einträge, Pfad des Testordners.
