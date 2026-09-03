# ghostwriter.ai – Projekt-Zusammenfassung

**Datum:** 3. September 2026  
**Status:** ✅ Alle Dateien gepusht zu GitHub  
**Repo:** https://github.com/roger-infanger-weibel/ghostwriter.ai

---

## 📋 Was du gefordert hast

### Vision
Ein **automatisierter, agentischer KI-Workflow**, der:
1. **Wöchentlich** (Montag 06:00 Zürich) einen KI-Wochenrückblick schreibt
   - Fokus: **Claude, ChatGPT, Gemini, Google AI Studio, NotebookLM**
   - Gegliedert nach: Global, Europa, Schweiz
   - Mit Bezug zu **deinen Projekten** (Parking-Forecasting, CAS, Claude-Config)

2. **Monatlich** (1. des Monats 06:00 Zürich) das KI-Glossar aktualisiert
   - ~200 Begriffe aus 8 Kategorien
   - **Deutsch + Englisch** (beide Sprachen aus einer YAML-Quelle)
   - Automatisch rendert zu Wiki-Seiten

3. **Einmalig** (nach Setup) das bestehendes Wiki-Glossary migriert
   - Parsing, Deduplizierung, Übersetzung
   - Aufräumen und vereinheitlichen

### Anforderungen
- ✅ **agent-source/** statt `docs/` (macht mehr Sinn für Agenten-Verwaltung)
- ✅ **Alle Dateien inhaltlich angepasst** auf Rogers Setup
- ✅ **Routines konkret mit Rogers 4 Tools** (nicht generisch)
- ✅ **Automatisches Setup & Push** (keine git-Kommandos von dir)
- ✅ **Vollständige Dokumentation** (README, CRITERIA, Routines, Setup-Guide)

---

## ✅ Was jetzt vorhanden ist

### 1. Repo-Struktur (live auf GitHub)

```
ghostwriter.ai/
├── README.md                          # Rogers Version (Parking, CAS, Claude-Focus)
├── SOURCES.md                         # Kuratierte Quellenliste
│
├── agent-source/                      # Agenten-Konfiguration
│   ├── CRITERIA.md                    # News-Regeln (Claude, ChatGPT, Gemini konkret)
│   ├── GLOSSARY-CRITERIA.md           # Glossar-Regeln
│   └── /routines
│       ├── weekly-post.md             # Wochenpost-Prompt (konkret auf deine Tools)
│       ├── glossary-migration.md      # Migrations-Prompt (deine 10 Duplikate im Skript)
│       └── glossary-update.md         # Monatliche Glossar-Routine
│
├── /posts                             # Wöchentliche Ausgaben
│   └── .gitkeep
│
└── /glossary
    ├── terms.yaml                     # Single Source of Truth (~200 Begriffe, DE+EN)
    ├── /rendered
    │   ├── .gitkeep
    │   ├── KI-Glossar.md (noch nicht gerendert)
    │   └── AI-Glossary.md (noch nicht gerendert)
    └── /diagrams
        └── .gitkeep
```

### 2. Dateien – Was du bekommst

| Datei | Inhalt | Status |
|---|---|---|
| **README.md** | Overviews, deine Tools, Glossar-Kontext | ✅ Rogers Version |
| **SOURCES.md** | OpenAI, Anthropic, Google, EU AI Act, CH | ✅ Kuratiert |
| **agent-source/CRITERIA.md** | Top-News-Filter: Claude, ChatGPT, Gemini, NotebookLM | ✅ Tool-fokussiert |
| **agent-source/GLOSSARY-CRITERIA.md** | Glossar-Struktur, 8 Kategorien, Duplikat-Regeln | ✅ Vollständig |
| **weekly-post.md** | Wochenpost-Prompt mit deinen Quellen & Fokus | ✅ Angepasst |
| **glossary-migration.md** | Migrations-Prompt mit deinen 10 bekannten Duplikaten | ✅ Konkret |
| **glossary-update.md** | Monatliche Glossar-Maintenance | ✅ Vollständig |
| **glossary/terms.yaml** | Basis-Template (9 Begriffe zum Starten) | ⚠️ Erfordert Migration |

### 3. Cloud Routines – Ready to deploy

| Routine | Schedule | Prompt-Datei | Status |
|---|---|---|---|
| KI-Wochenrückblick | Mo 04:00 UTC (06:00 CH) | weekly-post.md | 🟡 Setup nötig |
| Glossary-Migration | Manuell "Run Now" | glossary-migration.md | 🟡 Setup nötig |
| Glossary-Update | 1. des Monats 06:00 CH | glossary-update.md | 🟡 Setup nötig |

---

## 🔴 Was noch zu tun ist

### NEWS (Wochenpost)

| Was | Details | Priorität |
|---|---|---|
| **Cloud Routine aufsetzen** | https://claude.ai/code/routines → weekly-post.md kopieren | 🔴 KRITISCH |
| **Erster Testlauf** | "Run Now" drücken → PR prüfen → Feedback geben | 🔴 KRITISCH |
| **SOURCES.md anpassen** | Falls Quellen nicht erreichbar sind oder du neue hinzufügen willst | 🟡 Optional |
| **CRITERIA.md tunen** | Falls Agent zu aggressiv/konservativ filtert | 🟡 Nach erstem Test |

**Unklar noch:**
- Welche Quellen-Kategorien sind für dich am wichtigsten? (Claude? OpenAI? Regulierung?)
- Sollen News auch aus anderen KI-Tools reinkommen? (Llama, Mistral, etc.?)
- Wie aggressiv sollte der Filter sein? (Max. 5 Global oder eher 3?)

---

### GLOSSARY (Begriffe + Wiki)

| Was | Details | Priorität |
|---|---|---|
| **Glossary-Migration aufsetzen** | Cloud Routine starten mit glossary-migration.md | 🔴 KRITISCH |
| **Migration PR reviewen** | Migration-Agent parst dein Wiki → ~200 Begriffe → PR öffnet sich | 🔴 KRITISCH |
| **Migration PR mergen** | Danach: glossary/terms.yaml live mit allen Einträgen | 🔴 KRITISCH |
| **Wiki-Seiten updaten** (optional) | Copy-paste aus KI-Glossar.md + AI-Glossary.md ins Wiki | 🟡 Optional |
| **Alte Wiki-Seite löschen** (optional) | Falls Duplikat | 🟡 Optional |
| **Monatliche Glossary-Routine aufsetzen** | Nach Migration: glossary-update.md für Cloud Routine | 🟡 Nach Migration |

**Unklar noch:**
- Struktur der 8 Kategorien im Glossar: Passt dir das? (Grundlagen, Technik, Training, Prompting, Vision, Sicherheit, Industrie, Hardware)
- Wie sollen neue Begriffe aus Posts in das Glossar fließen? (Automatisch oder manuell?)
- Brauchst du auch Diagramme (Mermaid) zu Kategorien? (noch nicht implementiert)

---

## 🎯 Nächste Schritte (In dieser Reihenfolge)

### 1. NEWS – Wochenpost starten (diese Woche)

```
1. Öffne https://claude.ai/code/routines
2. "Create Cloud Routine"
3. Name: KI-Wochenrückblick
4. Schedule: 0 4 * * 1
5. Repo: roger-infanger-weibel/ghostwriter.ai
6. Copy-Paste Prompt aus agent-source/routines/weekly-post.md
7. GitHub Auth aktivieren (repo-only, contents:write + pull_requests:write)
8. "Save" + "Run Now"
9. PR prüfen → Struktur OK? Quellen erreichbar? Links korrekt?
10. Feedback: Alles gut oder Prompt anpassen?
```

**Erwartung:** PR mit `posts/2026-W36.md` oder aktuelle Woche. 3–4 Einträge Global, 2–3 Europa, 1–2 Schweiz.

---

### 2. GLOSSARY – Migration durchführen (diese Woche, nach News-Test)

```
1. Öffne https://claude.ai/code/routines
2. "Create Cloud Routine"
3. Name: Glossary-Migration (Einmalig)
4. Copy-Paste Prompt aus agent-source/routines/glossary-migration.md
5. GitHub Auth (gleich wie News)
6. "Save" + "Run Now"
7. Warte 2–3 Minuten
8. Riesiger PR mit ~190 Einträgen (Deduplizierung, Englische Übersetzungen, Quellen bereinigt)
9. PR prüfen: Duplikate korrekt zusammengeführt? Übersetzungen OK? Quellen alle gültig?
10. Feedback: Alles OK oder Korrektur?
11. Merge PR → glossary/terms.yaml ist jetzt live
```

**Erwartung:** PR zeigt Migration-Log mit Statistiken (10 Duplikate zusammengefasst, X tote Quellen ersetzt, ~190 finale Einträge)

---

### 3. GLOSSARY – Wiki-Seiten updaten (optional, nach Migration)

```
1. Öffne lokal: glossary/rendered/KI-Glossar.md
2. Copy Inhalt
3. https://github.com/roger-infanger-weibel/ghostwriter.ai/wiki/KI-Glossary
4. Paste & Save
5. Gleich für AI-Glossary.md
6. Optional: Alte Wiki-Seiten löschen (falls Duplikat)
```

---

### 4. GLOSSARY – Monatliche Routine aufsetzen (NACH Migration erfolgreich)

```
1. Cloud Routine erstellen
2. Name: Glossary-Update (Monatlich)
3. Schedule: 0 6 1 * *
4. Copy-Paste Prompt aus agent-source/routines/glossary-update.md
5. GitHub Auth (gleich wie oben)
6. "Save"
7. Test: "Run Now" → kleiner PR mit neuen Begriffen (falls vorhanden)
8. Feedback OK? Dann läuft's automatisch ab 1. Oktober.
```

---

## ❓ Offene Fragen (für dich zu entscheiden)

### NEWS – Wochenpost

1. **Quellen-Priorität?**
   - Brauchst du auch andere KI-Tools? (Mistral, Llama, xAI, etc.)
   - Oder bleibt es: Claude, ChatGPT, Gemini, Google AI Studio, NotebookLM?

2. **Filter-Aggressivität?**
   - Ist "Top-News only" (3–4 Einträge Global) zu konservativ?
   - Oder eher: maximal 5–6 Global für mehr Context?

3. **Länder-Fokus?**
   - Soll es noch andere Länder geben? (z. B. Zürich-specific, Schweiz-wide)
   - Oder Global → Europa → Schweiz reicht?

4. **Neue Quellen?**
   - SOURCES.md ist eine Start-Liste. Sollen neue Quellen in PRs vorgeschlagen werden?
   - Oder manuell von dir hinzugefügt?

---

### GLOSSARY – Begriffe + Struktur

1. **Kategorien-Struktur – passt?**
   ```
   1. Grundlagen & Kernkonzepte
   2. Technik, Architektur & NLP
   3. Training, Anpassung & Daten
   4. Prompting & Interaktion (Agenten)
   5. Computer Vision & Robotik
   6. Sicherheit, Ethik & Recht
   7. Industrie, Medizin & Spezifikationen
   8. Hardware & Kennzahlen
   ```
   Zu viele? Zu wenige? Umstrukturieren?

2. **Automatische Ergänzung?**
   - Die monatliche Routine liest neue Posts und schlägt Glossar-Einträge vor
   - Reicht das, oder brauchst du manuelle Kontrolle vorher?

3. **Diagramme (Mermaid)?**
   - Sollen Kategorien auch visuelle Diagramme haben? (flowcharts, mind maps, etc.)
   - Oder nur Tabellen?

4. **Wiki vs. Repo?**
   - Glossar lebt in `glossary/terms.yaml` (Single Source of Truth)
   - Wiki-Seiten sind gerendert (read-only, aus terms.yaml erzeugt)
   - Ist das OK oder brauchst du Wiki als Primary?

---

## 📊 Architektur-Überblick

```
┌─────────────────────────────────────────────────────────┐
│         Claude Cloud Routines (Automatisch)            │
│                                                         │
│  [KI-Wochenrückblick]     [Glossary-Update]           │
│       Montag 06:00 CH      1. d. Monats 06:00 CH       │
│       + Glossary-Migration (einmalig)                 │
└──────────┬──────────────────────────────┬──────────────┘
           │                              │
           ▼                              ▼
    ┌─────────────────┐        ┌──────────────────────┐
    │  SOURCES.md     │        │  agent-source/       │
    │  (kuratiert)    │        │  CRITERIA.md         │
    │                 │        │  GLOSSARY-CRITERIA   │
    │  + CRITERIA.md  │        │                      │
    │  (Filter-Regeln)│        │  /routines/          │
    └────────┬────────┘        │  (3 Prompts)         │
             │                 └──────────┬───────────┘
             ▼                            ▼
    ┌─────────────────────────────────────────────────┐
    │      ghostwriter.ai Repo (GitHub)              │
    │                                                 │
    │  /posts                 /glossary               │
    │  YYYY-Www.md           terms.yaml (YAML)       │
    │  (Wochenpost)          /rendered               │
    │                        KI-Glossar.md           │
    │                        AI-Glossary.md          │
    │                                                 │
    │  Wiki (optional)                               │
    │  ↑ (copy-paste aus /rendered)                 │
    └─────────────────────────────────────────────────┘
```

---

## ✨ Status-Zusammenfassung

| Komponente | Status | Nächster Schritt |
|---|---|---|
| **Repo-Struktur** | ✅ Live auf GitHub | - |
| **README.md** | ✅ Rogers Version | - |
| **SOURCES.md** | ✅ Kuratiert | Anpassen falls nötig |
| **CRITERIA.md** | ✅ Tool-fokussiert | Feedback nach erstem Test |
| **weekly-post.md Prompt** | ✅ Fertig | Cloud Routine aufsetzen + Run Now |
| **glossary-migration.md Prompt** | ✅ Fertig | Cloud Routine aufsetzen + Run Now (nach News-Test) |
| **glossary-update.md Prompt** | ✅ Fertig | Cloud Routine aufsetzen (nach Migration) |
| **glossary/terms.yaml** | ✅ Basis-Template | Migration durchführen |
| **KI-Glossar.md + AI-Glossary.md** | ❌ Nicht gerendert | Nach Migration automatisch gefüllt |
| **Wiki-Glossary** | ❌ Noch nicht migriert | Nach Migration copy-paste |

---

## 🚀 Dein nächster Move

1. **Heute/morgen:** Cloud Routine #1 (Wochenpost) aufsetzen + "Run Now"
2. **Nach erstem Test:** Feedback geben, Prompt anpassen
3. **Diese Woche:** Cloud Routine #2 (Migration) aufsetzen + mergen
4. **Nach Migration:** Cloud Routine #3 (Glossar-Update) aufsetzen
5. **Fertig:** Ab nächstem Montag läuft alles automatisch

---

## 📝 Notizen

- Alle Dateien sind **inhaltlich auf dich angepasst** (Roger, Parking-Forecasting, CAS, Claude-Fokus)
- **Keine git-Kommandos** von dir nötig – nur Cloud Routines aufsetzen
- **Alles ist auf GitHub** – du kannst jederzeit Prompts anpassen
- **Feedback-Loop:** Test → Feedback → Prompt tunen → Nächster Lauf

---

**Fragen? Änderungswünsche? Sag Bescheid!** 🚀
