# Quellen-Report – Testlauf KW 47 / 2026

Gestartet: 25. November 2026, ca. 10:00 Uhr (Zürich)

Prüfzeitraum: 16.–22. November 2026. Abruf per HTTP-GET (curl, Browser-User-Agent), danach Auswertung des Seiteninhalts. Geprüft wurden alle aktiven Quellen aus `SOURCES.md` (die Tabelle «Ausgesetzt» wird laut SOURCES.md nicht geprüft).

| Quelle (aus SOURCES.md) | URL | Status | Treffer letzte 7 Tage | Bemerkung |
|---|---|---|---|---|
| OpenAI News | https://openai.com/news | ✅ OK | 31 | HTTP 200; Auswertung über RSS (gleicher Inhalt) |
| OpenAI News (RSS) | https://openai.com/news/rss.xml | ✅ OK | 31 | Viele Kundenstorys/Partnerschaften; 1 Eintrag übernommen (GPT-6.2 Astra/Sol, 17.11.) |
| OpenAI ChatGPT Release Notes | https://learn.chatgpt.com/docs/whats-new | ✅ OK | 1 | 17.11.: GPT-6.2 (identisch mit News) |
| Anthropic News | https://www.anthropic.com/news | ✅ OK | 2 | IPO-Preisfestsetzung (18.11.) und -Abschluss (20.11.); Abschluss übernommen |
| Anthropic Claude Code Changelog | https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md | ⚠️ teilweise | n/a | GitHub-Ansicht HTTP 403; über raw.githubusercontent.com gelesen. Keine Datumsangaben, neueste Version 2.1.332, nur reguläre Releases |
| Anthropic API Release Notes | https://platform.claude.com/docs/en/release-notes/overview | ✅ OK | 3 | 16.11. Text-Wasserzeichen, Webhook-Events; 17.11. Linked billing (Beta); 20.11. Analytics-API-Zählregel – nicht übernommen (Detail-Updates) |
| Google Gemini API Changelog | https://aistudio.google.com/docs/changelog | ⚠️ teilweise | 0 | HTTP 200, Inhalt lädt nur per JavaScript (kein Text im HTML) |
| Google Developer Tools Blog | https://blog.google/innovation-and-ai/technology/developers-tools/ | ⚠️ teilweise | 3 | Liste lädt per JavaScript; über Sitemap gefunden: EmbeddingGemma 2 (17.11.), Genie 4 in Gemini API (19.11.), Tool Retrieval (19.11.) – nicht übernommen (Platzlimit Werkzeuge) |
| Google Gemini App Updates | https://gemini.google/release-notes/ | ✅ OK | 2 | 17.11. Tasks in Gemini gratis, 19.11. Computer use für Mac – nur USA/ausgewählte Länder, nicht Schweiz |
| Google Gemini Notebook Blog | https://blog.google/innovation-and-ai/products/gemini-notebook/ | ⚠️ teilweise | 1 | Liste lädt per JavaScript; über Sitemap: interaktive Sites (16.11.) übernommen |
| Google AI Blog | https://blog.google/innovation-and-ai/technology/ai/ | ⚠️ teilweise | 1 | Liste lädt per JavaScript; über Sitemap nur «Dialogues» (19.11.), nicht relevant |
| Google Blog-Sitemap | https://blog.google/en-us/sitemap.xml | ✅ OK | 31 | Mit `lastmod`; Hauptquelle für Google. Gemini 4 Neon (18.11.) übernommen; Gemini 4 Hydrogen erschien bereits 12.11. (nur Update 16.11.) |
| DeepSeek API Change Log | https://api-docs.deepseek.com/updates | ✅ OK | 0 | Letzter Eintrag 13.11.2026 |
| Hugging Face Blog | https://huggingface.co/blog | ✅ OK | 7 | U. a. «Welcome Inkling 2 Mini» (20.11.), DaisyRose-27B (18.11.) |
| GitHub Copilot Changelog | https://github.blog/changelog/label/copilot/ | ✅ OK | mehrere | Datumsformat «Nov.18»; Sekundärbestätigung neuer Modelle in Copilot, nicht übernommen |
| LangChain Blog | https://www.langchain.com/blog | ✅ OK | ~10 | Produkt-/Technikposts, ausserhalb Fokus |
| Perplexity Blog | https://www.perplexity.ai/hub/blog | ✅ OK | 3 | Frontier Research (16.11.), Multiagent und Orchestrator-API (17.11.) – ausserhalb Fokus |
| Microsoft AI News | https://microsoft.ai/news/ | ✅ OK | 7 | 17.11. (Ignite): sieben MAI-Modelle (MAI Code 2, Cyber 2 Flash, Image 2.7, Realtime 1, Licensed Weights …) – Kandidat «Weltweit», zugunsten Tencent (Asien) nicht übernommen |
| Microsoft Azure Blog AI (RSS) | https://azure.microsoft.com/en-us/blog/category/ai-machine-learning/feed/ | ✅ OK | 5 | 17.11. Ignite-Posts (Foundry, Microsoft IQ, Azure Catalyst) – Enterprise, nicht übernommen |
| Microsoft auf Hugging Face | https://huggingface.co/microsoft | ✅ OK | 2 | Aion-1.0-Instruct-2.3B (18.11., über HF-API ermittelt) – kleines Modell, nicht übernommen |
| Alibaba Qwen Research | https://qwen.ai/research | ⚠️ teilweise | 0 | HTTP 200, Inhalt lädt nur per JavaScript (keine Meldungen im HTML) |
| Hugging Face Trending (API) | https://huggingface.co/api/models?sort=trendingScore&limit=30 | ✅ OK | 20 | Platz 1 Inkling 2 Mini (→ Radar); Tencent Hy4-flash (17.11.) → Weltweit; ERNIE-5.5-Flash-Preview (23.11., ausserhalb Zeitraum) |
| Hugging Face (Hub) | https://huggingface.co | ✅ OK | 0 | Plattform, keine datierten Meldungen |
| Civitai | https://civitai.com | ✅ OK | 0 | Community-Plattform, keine Nachrichten |
| Global AI Community | https://globalai.community | ✅ OK | 0 | Keine datierten Meldungen |
| Stack Exchange (AI) | https://ai.stackexchange.com | ✅ OK | 0 | Q&A, keine Meldungen |
| Alignify | https://alignify.co | ✅ OK | 0 | Keine datierten Meldungen |
| The Decoder (DE) | https://the-decoder.de | ✅ OK | ~10 | Sekundärquelle; u. a. Anthropic-IPO, GPT-6.2-Prompting-Tipps – nur zur Absicherung |
| Simon Willison Weblog | https://simonwillison.net | ✅ OK | ~5 | Blog, nicht übernommen |
| Last Week in AI (RSS) | https://lastweekin.ai/feed | ✅ OK | 1 | #348 (21.11.): bestätigt IPO, GPT-6.2, Gemini 4 Neon/Hydrogen, Microsoft-Modelle, Nvidia-CEO-Rücktritt, US-Chip-Exportregeln |
| The Batch (DeepLearning.AI) | https://www.deeplearning.ai/the-batch/ | ✅ OK | 1 | Ausgabe 20.11.: Nvidia, Claude Fable 5.2, Anthropic-IPO, World Labs Atlas |
| SCMP Tech (RSS) | https://www.scmp.com/rss/36/feed | ✅ OK | ~22 | Tencent Hy4 (22.11.), US-Exportkontrollen, Anthropic-IPO aus China-Sicht – zur Absicherung |
| Rest of World | https://restofworld.org/ | ✅ OK | 2 | Keine KI-Top-News im Zeitraum |
| UNO – Medienmitteilungen | https://press.un.org/en | ✅ OK | 0 | KI-Meldungen erst 23./24.11. (Special Summit on AI Safety, Sicherheitsrat) – ausserhalb Zeitraum, Kandidat für KW 48 |
| EU AI Act – Kommission | https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai | ✅ OK | 0 | Statische Übersichtsseite; Details über /en/news |
| EU Digital Strategy – News | https://digital-strategy.ec.europa.eu/en/news | ✅ OK | 6 | Art.-27-Vorlage (16.11.) übernommen; AI Board (18.11.), Advisory Forum (16.11.), CRA-Norm (19.11.) nicht |
| Mistral AI News | https://mistral.ai/news | ✅ OK | 0 | Letzter Eintrag 5. November 2026 |
| Bund – Digitale Schweiz (BAKOM) | https://www.bakom.admin.ch | ✅ OK | 1 | 18.11. Medienförderung – kein KI-Bezug |
| EDÖB – Mitteilungen | https://www.edoeb.admin.ch/de/mitteilungen | ✅ OK | 0 | Mitteilungen vom 6.11. und 24.11. – keine im Zeitraum |
| Swiss AI Initiative (ETH/EPFL) | https://www.swiss-ai.org | ✅ OK | 0 | Keine neuen Meldungen |
| Swiss AI Anwenderverband | https://www.swissai.ch/blog | ✅ OK | 1 | 20.11. «Weekly Case» (Praxisbeispiel) – nicht übernommen |
| inside-it.ch | https://www.inside-it.ch | ✅ OK | 4 | Fedpol Anti-Deepfake-Modul für E-ID (19.11., Abo-Artikel), Zug M365, Cyberangriff Baselland – Sekundärquelle, nicht übernommen |
| Netzwoche | https://www.netzwoche.ch | ✅ OK | ~5 | KI-Meldungen im Zeitraum ohne Top-News-Charakter; NDB-KI-Software erst 24.11. |
| swissinfo.ch | https://www.swissinfo.ch | ✅ OK | ~1 | Novartis zu KI in der Krebsforschung – keine Top-News |

## Zusammenfassung
- Quellen geprüft: 44, davon OK: 38, teilweise: 6, Fehler: 0
- Kandidaten vor Filter: 21, Einträge nach Filter: 7 (Global 5, Europa 1, Schweiz 0, Auf dem Radar 1)

## Vorschläge
- **Google-Blog-Listen** (Developer Tools, Gemini Notebook, Google AI) laden weiterhin nur per JavaScript. Die Sitemap https://blog.google/en-us/sitemap.xml ist die verlässliche Quelle; in SOURCES.md könnte sie von «Fallback» zur Hauptquelle für Google hochgestuft werden.
- **Qwen Research** (https://qwen.ai/research) liefert kein auswertbares HTML. Alternative: https://huggingface.co/api/models?author=Qwen&sort=createdAt&direction=-1 (offene Qwen-Modelle mit Datum).
- **Microsoft auf Hugging Face:** Die Org-Seite enthält keine Datumsangaben im HTML. Besser die API-Variante eintragen: https://huggingface.co/api/models?author=microsoft&sort=createdAt&direction=-1&limit=10
- **Tencent Hunyuan** neu prüfen: https://huggingface.co/api/models?author=tencent&sort=createdAt&direction=-1 – lieferte diese Woche eine «Weltweit»-Meldung (Hy4 flash) und ist eine Asien-Quelle mit Datum.
- **Claude Code Changelog:** In SOURCES.md die Raw-URL https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md eintragen (die GitHub-Ansicht liefert 403).
- **EU AI Act – Kommission:** Die Policy-Seite ist statisch; die News-Zeile (/en/news) liefert die datierten Meldungen. Die Policy-Zeile kann als Referenz bleiben, zählt aber nicht als Meldungsquelle.
- **Community-Quellen** (Hugging Face Hub, Civitai, Global AI Community, Stack Exchange, Alignify) liefern weiterhin keine datierten Meldungen; Streichung gemäss Pflegeregel prüfen.
