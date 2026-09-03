# CRITERIA – Was in den Wochenpost gehört

Deine Top-News aus Claude, ChatGPT, Gemini, Google AI Studio, NotebookLM, EU AI Act, Schweizer Datenschutz.

---

## Grundregel

Nur **Top-News**, nicht Hype. Ein Post mit 3–4 starken Einträgen ist besser als einer mit 10 schwachen.

---

## Relevant (rein)

### Eure vier Haupttools
- **Claude (Anthropic):** Neue Modelle (Claude 3.5, Opus, Sonnet), Feature-Releases (Code, Routines, Cowork), API-Changes, Preise, Limits
- **ChatGPT / OpenAI:** GPT-4o, GPT-o1, API-Updates, Preise, Verfügbarkeit, Plugins, Memory
- **Gemini / Google:** Neue Gemini-Modelle, API-Updates, Google AI Studio, NotebookLM (neu?), Verfügbarkeit, Integration
- **Google AI Studio:** Neue Features, Release Notes, Integration mit anderen Tools

### Sicherheit & Regulierung
- **Sicherheitsrelevant:** Prompt Injection Patches, Agenten-Safety, Datenabfluss, Jailbreak-Reports
- **EU AI Act:** Umsetzungsschritte, Änderungen, neue Anforderungen
- **Schweiz:** EDÖB-Entscheide, Datenschutz-Urteile, HWZ/ETH/EPFL KI-Initiativen, Schweizer PLS-Systeme (Zurich PLS AG, Signal AG, LTS AG)

### Deine Spezial-Themen
- **Parking-Forecasting (PLS):** Neue Sensoren, Datenquellen, ML-Ansätze für Parkleitsysteme, länderspezifische Systeme
- **Vibe Coding & Risk Scaling:** Best Practices, Fehler, Lessons Learned im Web-Dev mit KI
- **CAS-Kontext:** Innovation-Management, Design Thinking in KI-Projekten

---

## NICHT relevant (raus)

- Funding-Runden, Bewertungen, Personalwechsel (ausser CEO bei OpenAI/Anthropic/Google)
- "X ist das Ende von Y" – reine Meinung ohne Fakten
- Benchmark-Rankings ohne konkrete Relevanz für deine Arbeit
- Ankündigungen ohne Verfügbarkeit oder Datum ("coming soon")
- Dinge ohne Primärquelle oder Link

---

## Regionale Zuordnung

Ein Thema erscheint in **genau einer** Region (engste gewinnt):

### Global
- OpenAI, Anthropic, Google News (zentrale Meldungen)
- Internationale Regulierung (UN, OECD)
- Markt-News (Fusionen, Neubewertungen)
- Technische Durchbrüche (neue Architekturen, Modelle)

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
- Parking-Systeme (Zurich PLS AG, Signal AG, LTS AG, Digitalparking)

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
| **Global** | 5 | Tool-News zuerst, dann Markt & Regulierung |
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
- [ ] Umfang: Global max. 5, Europa max. 3, Schweiz max. 3
- [ ] Keine Spekulationen, nur Primärquellen

---

## Fragen im Zweifelsfall?

- *Ist das "Top-News" für mich?* → Nein → streichen
- *Habe ich einen Link?* → Nein → streichen
- *Ist das spekulativ?* → Ja → streichen/faktencheck

