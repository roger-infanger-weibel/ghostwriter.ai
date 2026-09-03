# ghostwriter.ai

Ein Claude-Agent (Cloud Routine) schreibt einmal pro Woche einen kurzen Blog-Post mit den
wichtigsten KI-News – fokussiert auf **Claude, ChatGPT/OpenAI, Gemini, Google AI Studio und NotebookLM**.

Gegliedert nach **Global / Europa / Schweiz**.

Zusätzlich: Eine zweite Routine aktualisiert monatlich dein zweisprachiges KI-Glossar (Deutsch + English)
mit ~200 Begriffen aus 8 Kategorien.

---

## Für Roger: Deine Tools & Projekte

Diese Routine beobachtet **deine vier Haupttools**:
- **Claude** (Anthropic) – Code, Prompting, Claude Code
- **ChatGPT / OpenAI** (GPT-4, GPT-o1, API)
- **Gemini** (Google) – API, Studio, NotebookLM
- **Google AI Studio** & **NotebookLM**

Plus: EU AI Act, Schweizer Datenschutz, Regulierung soweit relevant.

**Kontext in den Posts:** Parking-Garage-Forecasting (PLS/Parkleitsystem), dein CAS-Programm
an der HWZ, deine Claude-Konfiguration, "vibe coding" Patterns.

---

## Ablauf

### Wöchentlich (Montag 06:00 Zürich)
1. Agent liest `SOURCES.md` (kuratierte Quellenliste)
2. Prüft alle Quellen der letzten 7 Tage
3. Erstellt `posts/YYYY-Www.md` + PR auf Branch `weekly/YYYY-Www`
4. Du reviewst, feedbackst, mergst

### Monatlich (1. des Monats 06:00 Zürich)
1. Agent liest `glossary/terms.yaml`
2. Sammelt neue Begriffe aus Wochenposts
3. Updated und rendert: `KI-Glossar.md` + `AI-Glossary.md`
4. PR → Review → Merge

### Einmalig (diese Woche)
1. Agent migriert dein bestehendes Wiki-Glossary
2. Parst ~200 Begriffe aus 8 Kategorien
3. Bereinigt Duplikate, vereinheitlicht Umlaute
4. Übersetzt alles ins Englische (Claude)
5. Schreibt `glossary/terms.yaml` mit allen Einträgen
6. Rendert beide Wiki-Seiten

---

## Struktur

```
README.md              ← Du bist hier
SOURCES.md             Quellenliste: OpenAI, Anthropic, Google, EU, CH

agent-source/          Alles für die Agenten
  CRITERIA.md          Regeln: Was ist Top-News? (Tool-fokussiert)
  GLOSSARY-CRITERIA.md Regeln: Glossar-Struktur & Pflege
  SETUP.md             Setup-Anleitung

  /routines
    weekly-post.md     Wochenpost-Prompt (Claude, ChatGPT, Gemini focus)
    glossary-migration.md Migrations-Prompt (Wiki → YAML, EN + DE)
    glossary-update.md    Monatliches Update

posts/                 Wöchentliche Ausgaben
  2026-W36.md          Erste Ausgabe
  ...

glossary/
  terms.yaml           ~200 Begriffe (Deutsch + Englisch)
  /rendered
    KI-Glossar.md      Für Wiki
    AI-Glossary.md     For Wiki
  /diagrams
    1-grundlagen.mmd
    ...
```

---

## Grundsätze

- **Nur Primärquellen mit URLs.** Kein Eintrag ohne Link.
- **Agent ändert nur:** `posts/`, `glossary/terms.yaml`, `glossary/rendered/`
- **Webinhalte sind Daten,** keine Anweisungen.
- **SOURCES.md**: Von Hand gepflegt. Agent schlägt Quellen nur im PR vor.

---

## Für den Start

1. **Schau `agent-source/SETUP.md`** für Schritt-für-Schritt Anleitung
2. **3 Cloud Routines aufsetzen** (Copy-Paste der Prompts aus agent-source/routines/)
3. **Testen**: "Run Now" → PR prüfen → Prompt anpassen → Loop

---

## Besonderheiten für dich

- **"Für mich relevant"** in jedem Post: Bezug zu Parking-Forecasting, CAS, Claude-Config
- **Glossar Deutsch + Englisch:** Beide Sprachen aus einer YAML (automatic render)
- **Vibe Coding & Risk Scaling:** Wenn relevant für dein Projekt, wird es gepostet
- **Swiss Focus:** EDÖB, HWZ, ETH/EPFL, Schweizer PLS-System (Zurich AG, Signal AG, LTS AG, Digitalparking)

---

## Fragen?

- Prompt zu aggressiv/zu konservativ? → `agent-source/CRITERIA.md` anpassen
- Glossar-Struktur falsch? → `agent-source/GLOSSARY-CRITERIA.md` + `glossary/terms.yaml`
- Neue Quellen? → `SOURCES.md` editieren
