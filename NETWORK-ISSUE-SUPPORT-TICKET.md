# Cloud Routine Network Issue – Support Ticket

**Datum:** 3. September 2026  
**Symptom:** Cloud Routine KI-Wochenrückblick blockiert bei Quellenzugriff  
**Severity:** 🔴 CRITICAL – Routine kann nicht funktionieren

---

## Problem-Beschreibung

**Cloud Routine:** `KI-Wochenrückblick` (weekly-post.md)  
**Status:** Läuft lokal/teilweise, aber **18 von 20 kurierten Quellen sind durch Netzwerk-Egress blockiert**

### Blockierte Domains (18 Stück)

#### OpenAI / ChatGPT
- ❌ **openai.com** (OpenAI News, Release Notes)
- ❌ **help.openai.com** (ChatGPT Release Notes)

#### Anthropic / Claude
- ❌ **anthropic.com** (Anthropic News)
- ❌ **github.com/anthropics** (Claude Code Changelog, API Release Notes)

#### Google / Gemini
- ❌ **gemini.google.com** (Gemini Release Notes)
- ❌ **ai.google.dev** (Gemini API, NotebookLM Updates)
- ❌ **google.com** (Google AI Blog)
- ❌ **support.google.com** (NotebookLM Support)

#### Europäische/Schweizer Quellen
- ❌ **edoeb.admin.ch** (Eidg. Datenschutzbeauftragter – KRITISCH für CH-News)
- ❌ **digital-strategy.ec.europa.eu** (EU AI Act)
- ❌ **swissinfo.ch** (Schweizer News)
- ❌ **inside-it.ch** (Schweizer IT/KI-News)
- ❌ **netzwoche.ch** (Schweizer Tech-News)

#### Weitere Quellen
- ❌ **mistral.ai** (Mistral AI News)
- ❌ **thedecoder.com** (KI-News & Analysis)
- ❌ **euractiv.com** (EU Tech News)

### Funktionierung
- ✅ 2 Domains erreichbar: github.com (teilweise), some generic domains
- ❌ Web-Search-Fallback funktioniert, aber **nicht ausreichend für Quellenverlässlichkeit**
- ❌ Europa/Schweiz-Sektion bleibt leer (keine validierten Quellen)

---

## Test-Resultat (KW35, 2026-09-03)

**Cloud Routine Execution:** `KI-Wochenrückblick` (Run Now)

```
Ausgeführt: 3 Befehle (1 fehlgeschlagen)
Benutzte Tools: 3 (1 fehlgeschlagen)

Resultat:
- ✅ Post geschrieben & committed lokal (weekly/2026-W35)
- ✅ 4 Global-Einträge via Web-Search ersetzt
- ❌ 18 von 20 Quellen BLOCKIERT (403/timeout)
- ❌ Push zu GitHub: 403 (GitHub Access)
- ❌ PR-Erstellung: 403 (GitHub Access)
- ⚠️ Europa/Schweiz: LEER (keine erreichbaren Quellen)
```

### Blockade-Errors (Sample)
```
Error: Unable to fetch https://www.anthropic.com/news – Network error (Egress policy)
Error: Unable to fetch https://openai.com/news – Network error (Egress policy)
Error: Unable to fetch https://ai.google.dev – Network error (Egress policy)
Error: Unable to fetch https://www.edoeb.admin.ch – Network error (Egress policy)
```

---

## Impact

| Auswirkung | Schweregrad | Details |
|---|---|---|
| **Quellenzugriff** | 🔴 CRITICAL | 90% der Hauptquellen nicht erreichbar |
| **News-Qualität** | 🔴 CRITICAL | Web-Search-Fallback ist unsicher für News-Verifikation |
| **Schweiz-Berichterstattung** | 🔴 CRITICAL | EDÖB/Regulator-News komplett blockiert |
| **EU AI Act Updates** | 🟠 HIGH | EU-Quellen blockiert (digital-strategy.ec.europa.eu) |
| **Routine-Funktion** | 🟠 HIGH | Cloud Routine läuft, aber mit unzureichenden Daten |

---

## Was funktioniert aktuell (Workaround, NICHT nachhaltig)

Die Routine kann **über Web-Search fallback** arbeiten, aber:
- ❌ Nur für hochvisible News (große Ankündigungen)
- ❌ Nicht für News-Zuverlässigkeit
- ❌ Europäische/Schweizer News unmöglich
- ⚠️ **Nicht für Produktion geeignet**

---

## Support-Anforderung

### Lösung 1: Network Egress Whitelist (EMPFOHLEN)

**Bitte whitelisten Sie folgende Domains für Cloud Routines:**

```
openai.com
anthropic.com
github.com/anthropics (falls nicht schon)
gemini.google.com
ai.google.dev
google.com
support.google.com
mistral.ai
thedecoder.com
edoeb.admin.ch
digital-strategy.ec.europa.eu
euractiv.com
swissinfo.ch
inside-it.ch
netzwoche.ch
```

**Priorität:**
- 🔴 CRITICAL: openai.com, anthropic.com, ai.google.dev, edoeb.admin.ch
- 🟠 HIGH: Alle anderen

### Lösung 2: Alternative (TEMPORÄR)

Falls Whitelist nicht möglich:
- Provide API-Keys für OpenAI/Anthropic/Google statt direct fetching
- Oder: Cloud Routine mit API-Access (nicht web scraping)

---

## Zusätzlich erkanntes Problem

**GitHub Access blockiert** (403 beim Push/PR):
- Cloud Routine kann lokal committen
- Aber: Push zu GitHub + PR-Erstellung schlägt fehl
- **Wahrscheinliche Ursache:** Claude GitHub App nicht installiert/authorized für Cloud Routines

**Fix:** GitHub App unter https://github.com/apps/claude/installations/select_target für Repo installieren/verifizieren

---

## Reproduktion

```bash
# Starte Cloud Routine KI-Wochenrückblick
# Beobachte: 18 von 20 Quellen aus SOURCES.md sind nicht erreichbar
# Erwartung: 5 Global + 3 Europa + 3 Schweiz Einträge
# Realität: ~4 Global (via Web-Search) + 0 Europa + 0 Schweiz
```

---

## Support Ticket Info

**Repo:** roger-infanger-weibel/ghostwriter.ai  
**Cloud Routine:** KI-Wochenrückblick  
**Prompt:** agent-source/routines/weekly-post.md  

**SOURCES.md Lage:** Alle 20+ Quellen in Repo dokumentiert  
**Impact:** Routine unbrauchbar für Produktionsnutzung bis gelöst

---

## Roger's Kontakt

**Anfrage wegen:** Claude Cloud Routine Network Egress Policy  
**Repo:** https://github.com/roger-infanger-weibel/ghostwriter.ai  
**Dringlich:** Ja – Blockade macht Routines nicht nutzbar

---

## Nächste Schritte

1. **Support kontaktieren** mit dieser Beschreibung
2. **Warten auf Whitelist-Freigabe** (ETA?)
3. **Dann:** Cloud Routine #1 neu testen
4. **Danach:** Glossary-Routines (#2, #3) aufsetzen

---

**Status: BLOCKED – Wartet auf Anthropic Support zu Egress Policy**
