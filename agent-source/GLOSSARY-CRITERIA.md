# GLOSSARY-CRITERIA – Regeln für die Glossar-Pflege

## Struktur

- Quelle der Wahrheit: `glossary/terms.yaml` im Repo. Nur diese Datei wird editiert.
- Daraus werden zwei Wiki-Seiten gerendert:
  - `KI-Glossar` – deutsch geführt (Begriff DE zuerst, Erklärung DE)
  - `AI-Glossary` – englisch geführt (Term EN zuerst, Erklärung EN)
- Beide Seiten enthalten dieselben Begriffe in derselben Reihenfolge und dieselben
  Kategorien. Die Mermaid-Diagramme je Kategorie bleiben erhalten und stehen in
  `glossary/diagrams/<kategorie>.mmd`.
- `glossary/diagrams.yaml` ist die Übersicht aller Diagramme (Kategorie- und
  Übersichtsdiagramme, siehe "Diagramme" unten). Jeder Eintrag verweist per `file` auf die
  passende `.mmd`-Datei in `glossary/diagrams/` (oder per `image_url` auf ein Bild, falls kein
  Mermaid-Code vorliegt).

## Eintrag (YAML)

```yaml
- id: rag
  category: 2-technik
  term_de: Retrieval-Augmented Generation (RAG)
  term_en: Retrieval-Augmented Generation (RAG)
  explanation_de: Die KI sucht vor der Antwort in externen Quellen und stützt die Antwort darauf.
  explanation_en: The model retrieves from external sources before answering and grounds its reply on them.
  context_de: Reduziert Halluzinationen; Basis vieler Firmen-Chatbots.
  context_en: Reduces hallucinations; the basis of most enterprise chatbots.
  sources:
    - https://example.org/primary-source
  updated: 2026-09-03
```

## Kategorien (fix)

1-grundlagen · 2-technik · 3-training · 4-prompting-agenten · 5-vision-robotik ·
6-sicherheit-recht · 7-industrie-medizin · 8-hardware-kennzahlen

Neue Kategorien nur nach Rücksprache (im PR vorschlagen, nicht anlegen).

## Was der Agent darf

- **Ergänzen:** Begriffe, die in mindestens einem Wochenpost vorkamen oder in den
  Primärquellen der Anbieter (OpenAI, Anthropic, Google) offiziell eingeführt wurden.
- **Aktualisieren:** Einträge, deren Kontext veraltet ist (z. B. Modellnamen, "neu",
  "erstes Gesetz"). Die Definition selbst nur ändern, wenn sie sachlich falsch ist.
- **Zusammenführen:** Duplikate zu einem Eintrag, die bessere Definition behalten,
  beide Quellen übernehmen.
- **Quellen bereinigen:** tote oder Platzhalter-Links durch echte Primärquellen ersetzen;
  wenn keine gefunden wird, Quelle auf `unverified` setzen, nicht löschen.

## Was der Agent nicht darf

- Begriffe löschen. Stattdessen `status: deprecated` setzen und im PR begründen.
- Definitionen umformulieren, die korrekt sind ("Stil-Verbesserungen").
- Mehr als 15 Einträge pro Lauf ändern oder ergänzen. Grössere Umbauten im PR vorschlagen.
- Einträge ohne mindestens eine belegbare Quelle anlegen.

## Sprache und Stil

- Deutsch mit echten Umlauten (ä, ö, ü), Schweizer Schreibweise (ss statt ß).
- Erklärung: ein Satz, max. 25 Wörter, für Nicht-Techniker verständlich.
- Kontext: ein Satz, warum der Begriff relevant ist.
- Keine Superlative, keine Jahreszahlen im Kontext ("2025 wichtig"), keine Produktwerbung.

## Diagramme

- `glossary/diagrams.yaml` ist die Quelle der Wahrheit für alle Diagramme. Zwei `scope`-Typen:
  - `category`: genau ein Diagramm pro Kategorie (1–8), erscheint direkt unter der
    Kategorie-Überschrift, vor der Tabelle. `category_id` verweist auf die Kategorie aus
    "Kategorien (fix)" oben.
  - `overview`: zusätzliche, kategorieübergreifende Diagramme (z. B. Agent-Loop, RAG vs.
    Fine-tuning, EU-AI-Act-Risikoklassen). Diese stehen gesammelt im Abschnitt
    "Visuelle Übersichtsbilder" (DE) / "Visual Overview Diagrams" (EN) am Ende jeder Seite,
    in der Reihenfolge aus `diagrams.yaml`.
- Jeder Eintrag mit `type: mermaid` hat eine zugehörige Datei `glossary/diagrams/<id>.mmd` mit
  dem reinen Mermaid-Code (ohne ```` ```mermaid ````-Fences). Einträge mit `type: image` verweisen
  stattdessen auf `image_url` (z. B. Screenshots, die nicht als Mermaid nachgebaut werden können)
  und werden als `<img>` eingebunden.
- **Ergänzen:** Neue Übersichtsdiagramme dürfen hinzugefügt werden, wenn ein neuer Begriff/
  Themencluster das rechtfertigt (z. B. ein neues Protokoll wie MCP). Neue `.mmd`-Datei +
  Eintrag in `diagrams.yaml` + Einbindung in beiden gerenderten Seiten.
- **Nicht:** Bestehende Diagramme umformulieren oder Knoten/Kanten "verbessern", wenn sie
  fachlich korrekt sind. Bei Bedarf im PR begründen, nicht in der `.mmd`-Datei direkt still ändern.

## Rendering

- Pro Kategorie: Überschrift, Mermaid-Diagramm (aus `glossary/diagrams.yaml`, `scope: category`),
  Tabelle.
- Tabelle KI-Glossar: Begriff (DE) | Term (EN) | Erklärung | Zusammenhang | Quelle
- Tabelle AI-Glossary: Term (EN) | Begriff (DE) | Explanation | Context | Source
- Kopfzeile jeder Seite: "Generiert aus glossary/terms.yaml – Stand YYYY-MM-DD. Änderungen
  bitte per PR im Repo, nicht direkt im Wiki."
- Am Ende jeder Seite: Abschnitt mit allen `scope: overview`-Diagrammen aus
  `glossary/diagrams.yaml`, je mit Überschrift, kurzer Beschreibung, Diagramm/Bild und
  optionaler Quellenzeile.
