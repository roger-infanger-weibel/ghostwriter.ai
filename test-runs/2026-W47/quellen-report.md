# Quellen-Report – Testlauf KW 47 / 2026

Gestartet: 25. November 2026 (Zürich, geplanter Routinelauf)

Prüfzeitraum: 16.–22. November 2026. Abruf per HTTP-GET (curl, Browser-User-Agent), danach Auswertung des Seiteninhalts. Geprüft wurden alle 41 aktiven Quellen aus `SOURCES.md`; die Tabelle «Ausgesetzt» wird laut SOURCES.md nicht geprüft.

| Quelle (aus SOURCES.md) | URL | Status | Treffer letzte 7 Tage | Bemerkung |
|---|---|---|---|---|
| OpenAI News | https://openai.com/news | ✅ OK | 31 | HTTP 200; Auswertung über RSS (gleicher Inhalt) |
| OpenAI News (RSS) | https://openai.com/news/rss.xml | ✅ OK | 31 | Viele Kundenstorys/Partnerschaften; GPT-6.2 Astra/Sol (17.11.) übernommen |
| OpenAI ChatGPT Release Notes | https://learn.chatgpt.com/docs/whats-new | ✅ OK | 1 | GPT-6.2 (identisch mit News) |
| Anthropic News | https://www.anthropic.com/news | ✅ OK | 2 | IPO-Preisfestsetzung (18.11.) und -Abschluss (20.11.); Abschluss übernommen |
| Anthropic Claude Code Changelog (Raw) | https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md | ✅ OK | n/a | Keine Datumsangaben, nur reguläre Releases – nicht übernommen |
| Anthropic API Release Notes | https://platform.claude.com/docs/en/release-notes/overview | ✅ OK | 3 | Detail-Updates (Wasserzeichen, Webhooks, Linked billing) – nicht übernommen |
| Google Gemini API Changelog | https://aistudio.google.com/docs/changelog | ⚠️ teilweise | 0 | HTTP 200, Inhalt lädt nur per JavaScript |
| Google Developer Tools Blog | https://blog.google/innovation-and-ai/technology/developers-tools/ | ⚠️ teilweise | 3 | Liste per JavaScript; über Sitemap: Tool Retrieval (19.11.) u. a. – Platzregel, nicht übernommen |
| Google Gemini App Updates | https://gemini.google/release-notes/ | ✅ OK | 2 | 17.11. Tasks gratis, 19.11. Computer use für Mac – nicht übernommen |
| Google Gemini Notebook Blog | https://blog.google/innovation-and-ai/products/gemini-notebook/ | ⚠️ teilweise | 1 | Liste per JavaScript; über Sitemap: interaktive Sites (16.11.) – Platzregel, nicht übernommen |
| Google AI Blog | https://blog.google/innovation-and-ai/technology/ai/ | ⚠️ teilweise | 1 | Liste per JavaScript; über Sitemap, nicht relevant |
| Google Blog-Sitemap | https://blog.google/en-us/sitemap.xml | ✅ OK | ~30 | Hauptquelle Google; Gemini 4 Neon (18.11.) übernommen |
| DeepSeek API Change Log | https://api-docs.deepseek.com/updates | ✅ OK | 0 | Letzter Eintrag 13.11.2026 |
| Hugging Face Blog | https://huggingface.co/blog | ✅ OK | ~7 | u. a. Inkling 2 Mini (20.11.) |
| GitHub Copilot Changelog | https://github.blog/changelog/label/copilot/ | ✅ OK | mehrere | Sekundärbestätigung (MAI Code 2 in Copilot) |
| LangChain Blog | https://www.langchain.com/blog | ✅ OK | ~10 | Ausserhalb Fokus |
| Perplexity Blog | https://www.perplexity.ai/hub/blog | ✅ OK | 3 | Ausserhalb Fokus |
| Microsoft AI News | https://microsoft.ai/news/ | ✅ OK | 7 | 17.11. Ignite: sieben MAI-Modelle → «Weltweit» übernommen |
| Microsoft Azure Blog AI (RSS) | https://azure.microsoft.com/en-us/blog/category/ai-machine-learning/feed/ | ✅ OK | ~5 | Ignite-Enterprise-Posts – nicht übernommen |
| Microsoft – Hugging Face API | https://huggingface.co/api/models?author=microsoft&sort=createdAt&direction=-1&limit=10 | ✅ OK | 2 | Aion-1.0-Instruct-2.3B (18.11.) – kleines Modell |
| Qwen – Hugging Face API | https://huggingface.co/api/models?author=Qwen&sort=createdAt&direction=-1&limit=10 | ✅ OK | 0 | Neuestes Modell 9.10.2026 |
| Qwen Research | https://qwen.ai/research | ⚠️ teilweise | 0 | HTTP 200, Inhalt lädt nur per JavaScript |
| Tencent – Hugging Face API | https://huggingface.co/api/models?author=tencent&sort=createdAt&direction=-1&limit=10 | ✅ OK | 0 (Top 10) | Top 10 alle vom 23.–25.11.; Hy4 flash (17.11.) über Trending gefunden → «Weltweit» übernommen |
| Hugging Face Trending (API) | https://huggingface.co/api/models?sort=trendingScore&limit=30 | ✅ OK | ~18 | Inkling 2 Mini (Platz 1), Tencent Hy4-flash, SenseNova-Loop-9B, Aleph-Alpha Kolibri-1.1; ERNIE-5.5-Flash-Preview erst 23.11. |
| The Decoder (DE) | https://the-decoder.de | ✅ OK | ~10 | Zur Absicherung; Axios-Bericht zu internen Modellen erst 24.11. |
| Simon Willison Weblog | https://simonwillison.net | ✅ OK | ~5 | Nicht übernommen |
| Last Week in AI (RSS) | https://lastweekin.ai/feed | ✅ OK | 1 | #348 (21.11.): bestätigt IPO, GPT-6.2, Gemini 4 Neon, MAI-Modelle, Nvidia-CEO-Rücktritt |
| The Batch (DeepLearning.AI) | https://www.deeplearning.ai/the-batch/ | ✅ OK | 1 | Ausgabe 20.11.: Nvidia, Claude Fable 5.2, Anthropic-IPO, World Labs Atlas |
| SCMP Tech (RSS) | https://www.scmp.com/rss/36/feed | ✅ OK | ~22 | Tencent Hy4 (22.11.), US-Chip-Exportregeln, Anthropic-IPO aus China-Sicht |
| Rest of World | https://restofworld.org/ | ✅ OK | ~2 | Keine KI-Top-News |
| UNO – Medienmitteilungen | https://press.un.org/en | ✅ OK | 0 | KI-Meldungen erst 23./24.11. – Kandidat für KW 48 |
| EU AI Act – Kommission | https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai | ✅ OK | 0 | Statische Übersicht (Referenz) |
| EU Digital Strategy – News | https://digital-strategy.ec.europa.eu/en/news | ✅ OK | ~7 | Art.-27-Vorlage (16.11.) übernommen; Apply AI Summit, AI Board, Advisory Forum, CRA-Norm nicht |
| Mistral AI News | https://mistral.ai/news | ✅ OK | 0 | Letzter Eintrag 5.11.2026 |
| Bund – Digitale Schweiz (BAKOM) | https://www.bakom.admin.ch | ✅ OK | 0 | Keine KI-Meldung im Zeitraum |
| EDÖB – Mitteilungen | https://www.edoeb.admin.ch/de/mitteilungen | ✅ OK | 0 | Mitteilungen vom 6.11. und 24.11. |
| Swiss AI Initiative (ETH/EPFL) | https://www.swiss-ai.org | ✅ OK | 0 | Keine datierten neuen Meldungen |
| Swiss AI Anwenderverband | https://www.swissai.ch/blog | ✅ OK | ~1 | Praxisbeispiel – nicht übernommen |
| inside-it.ch | https://www.inside-it.ch | ✅ OK | ~4 | Sekundärquelle, keine Top-News |
| Netzwoche | https://www.netzwoche.ch | ✅ OK | ~5 | Keine Top-News |
| swissinfo.ch | https://www.swissinfo.ch | ✅ OK | ~1 | Keine Top-News |

## Zusammenfassung
- Quellen geprüft: 41, davon OK: 36, teilweise: 5, Fehler: 0
- Kandidaten vor Filter: 16, Einträge nach Filter: 6 (Global 5 – davon Werkzeuge 3, Weltweit 2 –, Europa 1, Schweiz 0, Auf dem Radar 0)
- Platzregel angewendet: zwei starke weltweite Meldungen (Microsoft MAI, Tencent Hy4 flash), daher nur 3 Werkzeug-Einträge. Gestrichen: Gemini Notebook interaktive Sites, Gemini API Tool Retrieval, Inkling 2 Mini (verfügbar → kein Radar; kleineres Modell, Rang 3 bei Weltweit).
- Auf dem Radar: kein passender, noch nicht verfügbarer Kandidat im Zeitraum.

## Vorschläge
- **Tencent – Hugging Face API:** `limit=10` reicht nicht, weil Tencent viele kleine Varianten hochlädt; Hy4 flash (17.11.) war nach drei Tagen schon aus den Top 10 verdrängt. Vorschlag: `limit=40` oder zusätzlich die Tencent-Hy-Seite https://hy.tencent.ai/research prüfen.
- **Qwen Research** bleibt JavaScript-only; die HF-API-Zeile genügt für offene Modelle, geschlossene Qwen-Modelle weiter über SCMP / Last Week in AI.
- **Google-Blog-Listen** (Developer Tools, Gemini Notebook, Google AI) könnten in SOURCES.md als «nur über Sitemap» markiert werden, da sie ohne JavaScript nichts liefern.
- **Thinking Machines Lab** (Inkling) als mögliche neue Quelle prüfen: https://huggingface.co/api/models?author=thinkingmachines&sort=createdAt&direction=-1&limit=10
