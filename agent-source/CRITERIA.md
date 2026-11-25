# CRITERIA – Was in den Wochenpost gehört

Deine Top-News aus Claude, ChatGPT, Gemini, Google AI Studio, NotebookLM – dazu die wichtigsten KI-News weltweit, EU AI Act und Schweizer Datenschutz.
Alle relevanten Quellen sind im SOURCES.md

---

## Grundregel

Nur **Top-News**, nicht Hype. Ein Post mit 3–4 starken Einträgen ist besser als einer mit 10 schwachen.

---

## Breaking News statt Modell-Details

Gefragt ist, **was die Nachricht der Woche ist** – nicht das Datenblatt.

- **Auswahl:** Was verändert den Markt, die Branche, die Gesellschaft oder die Regeln? Zum Beispiel
  ein Börsengang, ein neues Spitzenmodell, das die Konkurrenz unter Druck setzt, ein grosser Deal,
  ein Verbot, ein Sicherheitsvorfall, eine neue Regulierung. Ein weiteres Modell-Update ohne
  Folgen ist keine Breaking News.
- **Pro Eintrag:** 2–3 Sätze: *Was ist passiert?* und *Warum ist es wichtig?* (Folgen, Einordnung).
- **Ein Thema pro Eintrag:** keine angehängte Zweitmeldung (z. B. nicht noch einen Chip an eine
  Modell-Meldung hängen). Ist das zweite Thema wichtig, ist es ein eigener Eintrag.
- **Weglassen:** Parameterzahlen, Kontextfenster, Token- und API-Preise, Modell-IDs und
  Code-Bezeichner, Architektur (MoE, aktive Parameter …), Lizenznamen, Benchmarks und
  Vergleiche mit anderen Modellen, Listen
  von Abo-Stufen oder Zielgruppen («für Plus-, Pro-, Enterprise-Nutzer …»), Plattform-Listen.
- **Erlaubt:** höchstens **eine** Zahl pro Eintrag, und nur wenn sie die Nachricht selbst ist
  (z. B. der Erlös eines Börsengangs).

---


## NICHT relevant (raus)

- Funding-Runden, Bewertungen
- **Personenbezogene News:** Personalwechsel aller Art (auch CEO-Rücktritte und -Wechsel),
  Abgänge, Aussagen, Interviews, Posts oder Streit einzelner Personen. Entscheide von Firmen,
  Behörden und Organisationen sind erlaubt (z. B. «die UNO fordert …»), aber ohne Personen ins
  Zentrum zu stellen.
- "X ist das Ende von Y" – reine Meinung ohne Fakten
- **Benchmarks:** keine Benchmark-Ergebnisse, Ranglisten-Plätze, Testvergleiche oder «so gut
  wie Modell X»-Aussagen – weder als Meldung noch als Detail in einer Meldung
- Ankündigungen ohne Verfügbarkeit oder Datum ("coming soon")
- Dinge ohne Primärquelle oder Link
- normale Release Updates ohne major changes

---

## Regionale Zuordnung

Ein Thema erscheint in **genau einer** Region (engste gewinnt):

### Global

Zwei Teile im selben Abschnitt `## Global`, Werkzeuge zuerst:

**1. Deine Werkzeuge (Vorrang, 3–4 Einträge)**
- Claude / Anthropic, ChatGPT / OpenAI, Gemini, Google AI Studio, Gemini Notebook (ehem. NotebookLM)
- Neue Modelle, wichtige Features, Preisänderungen, Sicherheitsthemen dieser Werkzeuge

**2. Weltweit (bis 2 Einträge, wenn es echte Top-News gibt)**
- **Platzregel:** Gibt es zwei starke weltweite Meldungen, bekommen die Werkzeuge nur 3 Plätze
  und Weltweit 2. Gibt es nur eine oder keine, gehen die freien Plätze an die Werkzeuge zurück.
  Zusammen immer max. 5.
- Neue Spitzenmodelle anderer Anbieter mit Verfügbarkeit (API, App oder Gewichte), z. B.
  Qwen (Alibaba), DeepSeek, Kimi (Moonshot), GLM (Z.ai), Grok (xAI), Llama (Meta), Microsoft
- Internationale Regulierung und Governance (UNO, OECD, G7, China, USA, UK)
- Grosse Markt-News (Fusionen, Börsengänge, Übernahmen) und technische Durchbrüche
- **Rangfolge nach Bedeutung:** zuerst, wie wichtig die Meldung weltweit ist (Spitzenmodell eines
  grossen Labs > kleineres offenes Modell; Regulierung mit Wirkung > Absichtserklärung).
  Erst bei **gleichwertigen** Meldungen gewinnt die aus Asien oder einem anderen Weltteil
  ausserhalb der USA.
- **Gezielte Suche jede Woche:** ausdrücklich nach Releases der grossen Labs ausserhalb der USA
  suchen – Alibaba (Qwen), DeepSeek, Moonshot (Kimi), Zhipu (GLM), Tencent (Hunyuan / Hy),
  Baidu (ERNIE), ByteDance, MiniMax – in SCMP Tech, Last Week in AI, The Decoder und den
  Hugging-Face-APIs. Auch geschlossene Modelle (ohne Gewichte) zählen, wenn sie per API oder App
  verfügbar sind.
- **Websuche als Absicherung:** Viele Anbieterseiten laden nur per JavaScript (z. B. qwen.ai), und
  die Wochenrückblicke decken nicht alles ab – Qwen4-Max (16.11.2026) fehlte in allen. Darum, wenn
  das Werkzeug WebSearch verfügbar ist, pro Lab eine Suche wie «<Lab> new model release <Monat Jahr>»
  (z. B. «Alibaba Qwen new model release November 2026») und nur Treffer aus der Berichtswoche
  nehmen. Eine Meldung gilt als gesichert, wenn sie von der Primärquelle oder von mindestens zwei
  unabhängigen seriösen Medien bestätigt wird; verlinkt wird die beste erreichbare Quelle, mit
  «laut <Quelle>», wenn es nicht die Primärquelle ist. Im Quellen-Report eine Zeile «Websuche»
  mit den gesuchten Labs und Treffern.
- Fundstellen: die Quellen in SOURCES.md, insbesondere The Decoder, Last Week in AI, The Batch,
  SCMP Tech, Hugging Face, Microsoft AI News, DeepSeek. Ist eine Anbieterseite in der Cloud nicht erreichbar, darf die Meldung über eine
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

### Auf dem Radar (optional)

Nur für Neues, das **noch nicht nutzbar** ist, aber weltweit auffällt:
- Modelle oder Anbieter ohne Verfügbarkeit (z. B. ein geheimes Modell an der Spitze einer
  Rangliste – die Rangliste darf Fundstelle sein, im Text aber keine Plätze oder Werte nennen),
  angekündigte Modelle mit konkretem Signal (Training abgeschlossen, Beta gestartet)
- **Was schon verfügbar ist** (API, App oder Gewichte zum Download – auch ein Aufsteiger auf
  Hugging Face Trending), gehört **nicht** hierher, sondern ist ein Kandidat für «Weltweit»
- Max. **2 Einträge**, je 1–2 Sätze, klar als «noch nicht verfügbar» / «angekündigt» bezeichnet
- Auch hier: jeder Eintrag mit Link, keine Spekulation über Leistung oder Datum
- Kein passender Kandidat → Abschnitt weglassen

---

## Format des Posts

Dateiname: `posts/YYYY-Www.md` (ISO-Woche, z. B. `posts/2026-W37.md`)

```markdown
# KI-Wochenrückblick – KW 37 / 2026

Zeitraum: 7.–13. September 2026

## Global

### Anthropic: Claude 3.6 veröffentlicht
2–3 Sätze: Was ist passiert? Warum ist es wichtig? (keine technischen Details, siehe oben)
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

## Auf dem Radar

- Optional, max. 2 Einträge, je 1–2 Sätze + Link
...

## Für mich relevant

2–4 Sätze: Wie betrifft mich das?

Beispiel: "Claude 3.6 mit besserer Reasoning-Fähigkeit könnte die Vorhersage-Genauigkeit meines
Parking-Forecasting-Modells verbessern. Zudem relevant für mein CAS-Projekt zur Fehlertoleranz in
agentischen Systemen."

```

**Kein Abschnitt «Nicht erreichbare Quellen»** im Post – weder im Test noch produktiv. Der Post endet
mit «Für mich relevant». Nicht erreichbare Quellen stehen nur im Quellen-Report (Test) bzw. in der
Commit-Message (produktiv).

---

## Umfang & Qualität

| Region | Max. Einträge | Anmerkung |
|---|---|---|
| **Global** | 5 | Werkzeuge 3–4, Weltweit bis 2 (Platzregel) |
| **Europa** | 3 | EU AI Act, wenn aktiv; sonst "Keine Top-News" OK |
| **Schweiz** | 3 | PLS-News, EDÖB, Behörden; sonst "Keine Top-News" OK |

**Region ohne Meldung:** Im Post nur die Zeile «Keine Top-News.» – **keine Aufzählung**, welche
Seiten geprüft wurden oder nichts hatten. Diese Details gehören nur in den Quellen-Report bzw. die
Commit-Message.
| **Auf dem Radar** | 2 | optional; Abschnitt weglassen, wenn nichts Passendes |

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
- [ ] Jeder Eintrag: Titel + 2–3 Sätze (Was ist passiert? Warum wichtig?) + Link
- [ ] Keine Modell-Details: keine Parameter, Preise, Token, Modell-IDs, Abo-Stufen, Benchmarks
- [ ] Keine personenbezogenen News (Personalwechsel inkl. CEO, Aussagen einzelner Personen)
- [ ] Ein Thema pro Eintrag (keine angehängten Zweitmeldungen)
- [ ] "Für mich relevant" Sektion: Mit Bezug zu Parking-Forecasting / CAS / Claude-Config
- [ ] Kein Abschnitt «Nicht erreichbare Quellen» (Post endet mit «Für mich relevant»)
- [ ] Umfang: Global max. 5 (Werkzeuge 3–4, Weltweit bis 2), Europa max. 3, Schweiz max. 3
- [ ] Weltweit: gezielt nach Qwen, DeepSeek, Kimi, GLM, Tencent, ERNIE, ByteDance, MiniMax gesucht
- [ ] Auf dem Radar: nur noch nicht Verfügbares
- [ ] Keine Spekulationen, nur Primärquellen

---

## Fragen im Zweifelsfall?

- *Ist das "Top-News" für mich?* → Nein → streichen
- *Habe ich einen Link?* → Nein → streichen
- *Ist das spekulativ?* → Ja → streichen/faktencheck

