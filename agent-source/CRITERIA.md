# CRITERIA – Was in den Wochenpost gehört

Deine Top-News aus Claude, ChatGPT, Gemini, Google AI Studio, NotebookLM – dazu die wichtigsten KI-News weltweit, EU AI Act und Schweizer Datenschutz.
Alle relevanten Quellen sind im SOURCES.md

---

## Grundregel

Nur **Top-News**, nicht Hype. Ein Post mit 3–4 starken Einträgen ist besser als einer mit 10 schwachen.

---

## NICHT relevant (raus)

- Funding-Runden, Bewertungen, Personalwechsel (ausser CEO)
- "X ist das Ende von Y" – reine Meinung ohne Fakten
- Benchmark-Rankings ohne konkrete Relevanz für deine Arbeit
- Ankündigungen ohne Verfügbarkeit oder Datum ("coming soon")
- Dinge ohne Primärquelle oder Link
- normale Release Updates ohne major changes

---

## Regionale Zuordnung

Ein Thema erscheint in **genau einer** Region (engste gewinnt):

### Global

Zwei Teile im selben Abschnitt `## Global`, Werkzeuge zuerst:

**1. Deine Werkzeuge (Vorrang, max. 4 Einträge)**
- Claude / Anthropic, ChatGPT / OpenAI, Gemini, Google AI Studio, Gemini Notebook (ehem. NotebookLM)
- Neue Modelle, wichtige Features, Preisänderungen, Sicherheitsthemen dieser Werkzeuge

**2. Weltweit (1–2 Einträge, wenn es eine echte Top-News gibt)**
- Neue Spitzenmodelle anderer Anbieter mit Verfügbarkeit (API, App oder Gewichte), z. B.
  Qwen (Alibaba), DeepSeek, Kimi (Moonshot), GLM (Z.ai), Grok (xAI), Llama (Meta), Microsoft
- Internationale Regulierung und Governance (UNO, OECD, G7, China, USA, UK)
- Grosse Markt-News (Fusionen, Börsengänge, Übernahmen) und technische Durchbrüche
- Bewusst **nicht nur USA**: Gibt es eine gleichwertige Meldung aus Asien oder einem anderen
  Weltteil, bekommt diese den Platz.
- Fundstellen: die Quellen in SOURCES.md, insbesondere The Decoder, Hugging Face, DeepSeek,
  Simon Willison. Ist eine Anbieterseite in der Cloud nicht erreichbar, darf die Meldung über eine
  seriöse Einordnungsquelle (z. B. The Decoder) gefunden und verlinkt werden; in diesem Fall
  im Eintrag «laut <Quelle>» schreiben. Keine Meldung ohne Link.
- Gibt es in einer Woche keine weltweite Top-News, entfällt dieser Teil.

### Europa
- EU AI Act Umsetzung & Änderungen
- Europäische Anbieter (Mistral, etc.)
- EU-spezifische Verfügbarkeit/Einschränkungen
- Datenschutz auf EU-Ebene

### Schweiz
- EDÖB (Eidgenössischer Datenschutz- und Öffentlichkeitsbeauftragter)
- Kantone, Bund, Behördenentscheide
- Schweizer Hochschulen (ETH, EPFL, HWZ, etc.)
- Schweizer Unternehmen & Initiativen
- Schweizer Verfügbarkeit / Einschränkungen der Tools

---

## Format des Posts

Dateiname: `posts/YYYY-Www.md` (ISO-Woche, z. B. `posts/2026-W37.md`)

```markdown
# KI-Wochenrückblick – KW 37 / 2026

Zeitraum: 7.–13. September 2026

## Global

### Anthropic: Claude 3.6 veröffentlicht
2–3 Sätze: Was ist neu? Welche Auswirkung hat es auf meine Arbeit?
Quelle: [Anthropic News](https://www.anthropic.com/news), 12. September 2026

### OpenAI: GPT-o1 Preview verfügbar
...

## Europa

### EU AI Act: Artikel 12 tritt in Kraft
...

## Schweiz

### EDÖB: Richtlinie zu LLM-Einsatz in Behörden
...

### Zurich PLS AG: Neue Sensoren für Parkleitsystem
...

## Für mich relevant

2–4 Sätze: Wie betrifft mich das?

Beispiel: "Claude 3.6 mit besserer Reasoning-Fähigkeit könnte die Vorhersage-Genauigkeit meines
Parking-Forecasting-Modells verbessern. Zudem relevant für mein CAS-Projekt zur Fehlertoleranz in
agentischen Systemen."

## Nicht erreichbare Quellen

- [Gemini API Release Notes](https://ai.google.dev/release-notes) – 403 Forbidden
- Oder: "keine"
```

---

## Umfang & Qualität

| Region | Max. Einträge | Anmerkung |
|---|---|---|
| **Global** | 5 | Werkzeuge max. 4, dann Weltweit 1–2 (wenn vorhanden) |
| **Europa** | 3 | EU AI Act, wenn aktiv; sonst "Keine Top-News" OK |
| **Schweiz** | 3 | PLS-News, EDÖB, Behörden; sonst "Keine Top-News" OK |

### Sprache & Stil
- **Deutsch**, sachlich, präzise
- Keine Superlative ("revolutionär", "game-changing")
- Zahlen, Versionsnummern **wörtlich wie in der Quelle**
- Keine Spekulationen

### Zu-Vermeiden
- "Könnte bald" / "Wird wahrscheinlich"
- Marketing-Sprache von der Website kopiert
- Eigene Interpretationen

---

## Checkliste vor PR-Push

- [ ] Dateiname: `posts/YYYY-Www.md` (ISO-Woche)
- [ ] Überschrift: `# KI-Wochenrückblick – KW ww / YYYY`
- [ ] Zeitraum: `Zeitraum: D.–D. Monat YYYY`
- [ ] Jeder Eintrag: Titel + 2–3 Sätze + Link
- [ ] "Für mich relevant" Sektion: Mit Bezug zu Parking-Forecasting / CAS / Claude-Config
- [ ] "Nicht erreichbare Quellen": Liste oder "keine"
- [ ] Umfang: Global max. 5 (Werkzeuge max. 4, Weltweit 1–2), Europa max. 3, Schweiz max. 3
- [ ] Keine Spekulationen, nur Primärquellen

---

## Fragen im Zweifelsfall?

- *Ist das "Top-News" für mich?* → Nein → streichen
- *Habe ich einen Link?* → Nein → streichen
- *Ist das spekulativ?* → Ja → streichen/faktencheck

