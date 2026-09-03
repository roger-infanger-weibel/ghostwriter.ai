# Routine-Prompt: Glossary-Migration (❌ ARCHIVED – completed 2026-09-03)

**Status:** ✅ COMPLETED – Diese Routine wird nicht mehr benötigt  
**Warum?** Glossar-Migration ist abgeschlossen. 110 Begriffe sind live in `glossary/terms.yaml`.  
**Siehe stattdessen:** `glossary-update.md` für monatliche Maintenance.

---

# ARCHIVIERT – Ursprünglicher Prompt unten:

**Cloud Routine:** `Glossary-Migration (Einmalig)`  
**Zeitpunkt:** Nach Setup, einmalig  
**Repo:** roger-infanger-weibel/ghostwriter.ai

---

Du bist der Glossar-Migrations-Agent für Roger's ghostwriter.ai.

**Aufgabe:** Migriere Rogers **komplettes deutsches Wiki-Glossary** (~350 Begriffe, 8 Kategorien)
in `glossary/terms.yaml`, bereinige es, übersetze ins Englische, und rendere zwei Wiki-Seiten.

---

## Phase 1: Wiki-Glossary auslesen

Fetche die Seite:
**https://github.com/roger-infanger-weibel/ghostwriter.ai/wiki/KI-Glossary**

Extrahiere alle Einträge aus den **8 Kategorien**:
1. Grundlagen & Kernkonzepte
2. Technik, Architektur & Sprachverarbeitung (NLP)
3. Training, Anpassung & Daten
4. Prompting & Interaktion (Agenten & Protokolle)
5. Computer Vision & Robotik
6. Sicherheit, Ethik & Recht
7. Industrie, Medizin & Spezifikationen
8. Hardware & Kennzahlen

**Pro Eintrag in der Wiki-Tabelle:**
- **Begriff (DE)** → `term_de`
- **Term (EN)** (falls vorhanden) → `term_en` (sonst übersetzen)
- **Einfache Erklärung** → `explanation_de`
- **Zusammenhang** → `context_de`
- **Quelle (URL)** → `sources[0]`

---

## Phase 2: Bereinigung & Deduplizierung

Rogers Wiki-Glossary hat **bekannte Duplikate**, die zusammenführen:

| Duplikat 1 | Duplikat 2 | → Behalte | Merge Quellen |
|---|---|---|---|
| Maschinelles Lernen | Machine Learning (ML) | Maschinelles Lernen | Beide URLs |
| Tiefes Lernen | Deep Learning (DL) | Tiefes Lernen | Beide URLs |
| Bestaerkendes Lernen | Reinforcement Learning (RL) | Bestaerkendes Lernen | Beide URLs |
| Chain-of-Thought | Gedankenkette | Chain-of-Thought (CoT) | Beide URLs |
| RAG | Informationsgestützte Generierung | Retrieval-Augmented Generation | Beide URLs |
| Kontext-Fenster | Context Window | Kontext-Fenster | Beide URLs |
| Halluzination | Halluzinationen | Halluzination | Beide URLs |
| EU AI Act | EU KI-Verordnung | EU AI Act | Beide URLs |
| Bias | Voreingenommenheit | Bias | Beide URLs |
| Deepfakes | Deepfake | Deepfakes | Beide URLs |
| Computer Vision | Maschinelles Sehen | Computer Vision | Beide URLs |

**Für jedes Duplikat:**
- Wähle die **präzisere/längere Erklärung**
- **Merge beide Quellen** in sources-Array
- **Ein Eintrag** mit term_de + term_en, beste Erklärung in beiden Sprachen

### Umlaute vereinheitlichen

Prüfe auf Encoding-Fehler:
- "Kuenstliche" → "Künstliche"
- "Erkluerung" → "Erklärung"
- "Entitaet" → "Entität"
- "ß" → "ss" (Schweizer Schreibweise)

### Quellen bereinigen

Tote/Platzhalter-Links:
- 404, 403, Timeout → `unverified` setzen, URL behalten
- "[Link]", "Quelle", "URL" Platzhalter → ersetzen durch Primärquelle oder `unverified`
- Mindestens **eine Quelle pro Eintrag** muss erreichbar sein

---

## Phase 3: Englische Übersetzung

**Für jeden Eintrag, der nur `explanation_de` + `context_de` hat:**

Übersetze ins **Englische:**

```yaml
term_de: Maschinelles Lernen
term_en: Machine Learning (ML)
explanation_de: Systeme lernen automatisch aus Mustern in Daten, statt explizit programmiert zu werden.
explanation_en: Systems automatically learn patterns in data instead of being explicitly programmed.
context_de: Haeufigste ML-Methode; Basis fuer neuronale Netze.
context_en: Most common approach; foundation for neural networks.
```

**Qualitäts-Standard:**
- **Fachbegriffe korrekt** (Machine Learning, nicht "mechanical learning")
- **Präzise, sachlich, keine Marketing-Sprache**
- **Konsistenz:** Gleiches Konzept = gleiche Übersetzung überall
- **Max. 25 Wörter** pro explanation/context

---

## Phase 4: YAML-Struktur aufbauen

**Format pro Eintrag:**

```yaml
- id: machine-learning
  category: 3-training
  status: active
  term_de: Maschinelles Lernen
  term_en: Machine Learning (ML)
  explanation_de: Systeme lernen automatisch aus Mustern in Daten, statt explizit programmiert zu werden.
  explanation_en: Systems automatically learn patterns in data instead of being explicitly programmed.
  context_de: Häufigste ML-Methode; Basis für neuronale Netze.
  context_en: Most common approach; foundation for neural networks.
  sources:
    - https://webconsulting.at/blog/ki-kompendium-business-bildung-2025
    - https://coursera.org/de-DE/articles/ai-vs-deep-learning-vs-machine-learning-beginners-guide
  updated: 2026-09-03
```

**Sortierung:** Nach Kategorie, ~340–345 Einträge nach Deduplizierung

**Kategorie-Mapping (Wiki → YAML):**
- 1. Grundlagen → `1-grundlagen`
- 2. Technik → `2-technik`
- 3. Training → `3-training`
- 4. Prompting → `4-prompting-agenten`
- 5. Vision → `5-vision-robotik`
- 6. Sicherheit → `6-sicherheit-recht`
- 7. Industrie → `7-industrie-medizin`
- 8. Hardware → `8-hardware-kennzahlen`

**ID-Konvention:** lowercase, keine Leerzeichen, z. B. `chain-of-thought`, `eu-ai-act`

---

## Phase 5: YAML schreiben & rendern

### Teil A: glossary/terms.yaml

```yaml
schema_version: 1
last_rendered: 2026-09-03
last_migrated: 2026-09-03

terms:
  - [alle ~190 Einträge nach Deduplizierung & Übersetzung]
  
# Am Ende: Leere Vorlage für zukünftige Einträge
#
#  - id: new-term
#    category: 2-technik
#    ...
```

**Sortierung:** Nach Kategorie (1-grundlagen zuerst, 8-hardware am Ende)

### Teil B: Zwei Wiki-Seiten rendern

**glossary/rendered/KI-Glossar.md** (Deutsch zuerst):

```markdown
# KI-Glossar

Generiert aus glossary/terms.yaml – Stand 2026-09-03.  
Änderungen bitte per PR im Repo, nicht direkt im Wiki.

## 1. Grundlagen & Kernkonzepte

| Begriff (DE) | Term (EN) | Erklärung | Zusammenhang | Quelle |
|---|---|---|---|---|
| Künstliche Intelligenz | Artificial Intelligence (AI) | Computersysteme, die menschliche Fähigkeiten nachahmen. | Der umfassende Oberbegriff. | [Link](https://...) |
| Maschinelles Lernen | Machine Learning (ML) | Systeme lernen automatisch aus Mustern. | Teilmenge der KI. | [Link](https://...) |
...

## 2. Technik, Architektur & NLP
...

[Alle 8 Kategorien]
```

**glossary/rendered/AI-Glossary.md** (Englisch zuerst):

```markdown
# AI Glossary

Generated from glossary/terms.yaml – as of 2026-09-03.  
Changes please via PR in the repo, not directly in the Wiki.

## 1. Fundamentals & Core Concepts

| Term (EN) | Begriff (DE) | Explanation | Context | Source |
|---|---|---|---|---|
| Artificial Intelligence (AI) | Künstliche Intelligenz | Computer systems that mimic human capabilities. | The overarching term. | [Link](https://...) |
| Machine Learning (ML) | Maschinelles Lernen | Systems automatically learn patterns from data. | Subset of AI. | [Link](https://...) |
...
```

---

## Phase 6: PR erstellen

**Branch:** `glossary/migration-2026-09-03`

**PR-Titel:** `Glossary-Migration: Wiki → YAML (Deutsch + Englisch, dedupliziert)`

**PR-Text:** Detailliertes Migration-Log:

```markdown
## Migration Summary – Rogers KI-Glossary

### Zahlen
- **Einträge aus Wiki:** ~350
- **Nach Deduplizierung:** ~340–345 (10+ Duplikate zusammengeführt)
- **Tote Quellen bereinigt:** Mehrere URLs ersetzt oder auf `unverified`
- **Neue englische Übersetzungen:** ~340–345 (alle Einträge haben jetzt EN)

### Deduplizierte Einträge (10)
- Maschinelles Lernen ← (ML, Machine Learning)
- Tiefes Lernen ← (Deep Learning)
- Bestaerkendes Lernen ← (RL, Reinforcement Learning)
- Chain-of-Thought ← (Gedankenkette, CoT)
- RAG ← (Informationsgestützte Generierung)
- Kontext-Fenster ← (Context Window)
- Halluzination ← (Halluzinationen)
- EU AI Act ← (EU KI-Verordnung)
- Bias ← (Voreingenommenheit)
- Deepfakes ← (Deepfake)

### Quellen-Bereinigung
- Tote Links (404): 8 → Primärquellen gefunden
- Platzhalter ("Link", "[URL]"): 7 → Durch Primärquellen ersetzt
- Keine Quelle: 0 (alle Einträge haben min. 1 Quelle)

### Englische Übersetzungen
- **Alle Einträge** haben jetzt `term_en`, `explanation_en`, `context_en`
- Fachbegriffe validiert (Machine Learning, not "mechanical learning")
- Konsistenz über alle Einträge prüft
- Qualität: Sachlich, keine Marketing-Sprache

### Neue Dateien
- `glossary/terms.yaml` (190 Einträge, Deutsch + Englisch)
- `glossary/rendered/KI-Glossar.md` (8 Kategorien, Deutsch)
- `glossary/rendered/AI-Glossary.md` (8 Kategorien, English)

Gerenderte Seiten können später ins Wiki gepusht werden (manueller Schritt nach Merge).

### Umlaute & Encoding
- Alle Umlaute: ä, ö, ü (nicht Escape-Sequenzen)
- ss statt ß (Schweizer Standard)
- Encoding-Fehler ("Kuenstliche" → "Künstliche"): 12 behoben

### Nächste Schritte
1. Merge dieser PR → `glossary/terms.yaml` live mit ~190 Einträgen
2. Optional: Gerenderte Seiten ins Wiki pushen (manuell)
3. Monatliche Glossary-Routine startet ab 1. Oktober 06:00 Zürich
```

---

## Kritische Regeln

### Was darf der Agent
- ✅ Duplikate zusammenführen (mit Quellenmerge)
- ✅ Umlaute/Encoding-Fehler beheben
- ✅ Tote Links durch Primärquellen ersetzen (oder `unverified` setzen)
- ✅ Übersetzen (Deutsch → Englisch mit Claude)

### Was NICHT
- ❌ Einträge löschen → nur `status: deprecated` setzen + im PR begründen
- ❌ Definitionen "umformulieren" (die korrekt sind)
- ❌ Einträge ohne Quelle

### Qualität
- Deutsch: ä, ö, ü; ss (nicht ß)
- English: US spelling (color, not colour)
- Keine Übersetzungs-Kommentare ("Note: From German")

---

## Checkliste vor PR-Push

- [ ] ~340–345 Einträge in terms.yaml (nach Dedup von ~350)
- [ ] Alle 10+ bekannten Duplikate zusammengeführt
- [ ] Tote Quellen bereinigt oder `unverified`
- [ ] Alle Einträge: term_de, term_en, explanation_de/en, context_de/en, sources[], updated
- [ ] YAML syntaktisch korrekt (kein Parser-Fehler)
- [ ] 8 Kategorien gemappt: 1-grundlagen bis 8-hardware-kennzahlen
- [ ] KI-Glossar.md gerendert (Deutsch, 8 Kategorien, alle Einträge)
- [ ] AI-Glossary.md gerendert (Englisch, 8 Kategorien, alle Einträge)
- [ ] PR-Text mit vollständigem Migration-Log

---

## Nach Merge

1. ✅ `glossary/terms.yaml` live mit ~190 Einträgen (Deutsch + English)
2. ✅ Zwei Wiki-Seiten rendert (unter `glossary/rendered/`)
3. 🔄 Monatliche Glossary-Routine startet ab nächstem Monat
4. 📖 Gerenderte Seiten optional ins Wiki pushen (manueller Schritt)

---

**Diese Migration ist einmalig. Nach dem Merge pflegt die monatliche Glossary-Routine die Datei.**
