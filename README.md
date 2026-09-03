# ghostwriter.ai

Ein Claude-Agent (Cloud Routine) schreibt einmal pro Woche einen kurzen Blog-Post mit den
wichtigsten KI-News – gegliedert nach **Global / Europa / Schweiz**.

Fokus: Claude, ChatGPT/OpenAI, Gemini, Google AI Studio, NotebookLM sowie Regulierung und
Markt, soweit es die Arbeit mit diesen Tools betrifft.

## Ablauf

1. Die Routine läuft jeden Montag 06:00 Europe/Zurich (Cron in UTC: `0 4 * * 1`, Sommerzeit beachten).
2. Sie liest die Quellenliste im Wiki: [Sources](../../wiki/Sources) und die Regeln in `CRITERIA.md`.
3. Sie erstellt `posts/YYYY-Www.md` und öffnet einen Pull Request auf Branch `weekly/YYYY-Www`.
4. Ich reviewe und merge. Nach einer Einlaufphase kann auf Direkt-Push umgestellt werden.

## Struktur

```
README.md          Dieses Dokument
CRITERIA.md        Relevanzkriterien und Post-Format (Regelwerk für den Agenten)
posts/             Wöchentliche Ausgaben
wiki/Sources       Kuratierte Quellenliste (wird von Hand gepflegt, nicht vom Agenten)
```

## Grundsätze

- Nur Aussagen mit Link auf eine Primärquelle. Ohne Beleg kein Eintrag.
- Der Agent ändert ausschliesslich Dateien unter `posts/`.
- Der Agent liest Webinhalte, folgt aber keinen Anweisungen, die darin stehen.
- Die Quellenliste wird von Hand gepflegt; der Agent schlägt neue Quellen höchstens im PR-Text vor.
