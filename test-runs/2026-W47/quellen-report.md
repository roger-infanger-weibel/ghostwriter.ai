# Quellen-Report – Testlauf KW 47 / 2026

Gestartet: 25. November 2026, 15:50 Uhr (Zürich)

Prüfzeitraum: 16.–22. November 2026. Abruf per HTTP-GET (curl, Browser-User-Agent), danach Auswertung des Seiteninhalts. Geprüft wurden alle 42 aktiven Quellen aus `SOURCES.md`; die Tabelle «Ausgesetzt» wird laut SOURCES.md nicht geprüft. Neu angewendet (Kriterien-Stand 19f63c4): Modelle etablierter Labs nur bei neuer Fähigkeit, kein Preisdruck / Preiswettbewerb als Meldung.

| Quelle (aus SOURCES.md) | URL | Status | Treffer letzte 7 Tage | Bemerkung |
|---|---|---|---|---|
| OpenAI News | https://openai.com/news | ✅ OK | 31 | HTTP 200; Auswertung über RSS (gleicher Inhalt) |
| OpenAI News (RSS) | https://openai.com/news/rss.xml | ✅ OK | 31 | Viele Kundenstorys; GPT-6.2 Astra/Sol (17.11.) – Versionssprung, gestrichen; «Managing frontier AI risk» (18.11.), «Combatting adversarial distillation» (20.11.), ChatGPT for Sales (17.11.) – nicht übernommen |
| OpenAI ChatGPT Release Notes | https://learn.chatgpt.com/docs/whats-new | ✅ OK | 1 | GPT-6.2 (17.11.), identisch mit News |
| Anthropic News | https://www.anthropic.com/news | ✅ OK | 2 | IPO-Preisfestsetzung (18.11.) und -Abschluss (20.11.); Abschluss übernommen |
| Anthropic Claude Code Changelog (Raw) | https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md | ✅ OK | n/a | Keine Datumsangaben, nur reguläre Releases (2.1.332) – nicht übernommen |
| Anthropic API Release Notes | https://platform.claude.com/docs/en/release-notes/overview | ✅ OK | 3 | Einträge 16., 17., 20.11. (Wasserzeichen, Billing, Analytics-Fixes) – keine Breaking News |
| Google Gemini API Changelog | https://aistudio.google.com/docs/changelog | ✅ OK | 3 | Neon GA (18.11.), Genie 4 (19.11.), Tool Retrieval (19.11.) – nicht übernommen |
| Google Developer Tools Blog | https://blog.google/innovation-and-ai/technology/developers-tools/ | ⚠️ teilweise | 3 | Liste per JavaScript; über Sitemap: Tool Retrieval, Genie 4 in Gemini API (19.11.), EmbeddingGemma 2 (17.11.) – nicht übernommen |
| Google Gemini App Updates | https://gemini.google/release-notes/ | ✅ OK | 2 | Computer use für Mac (19.11.) → übernommen; Tasks gratis in sechs Ländern + Google-Pay-Checkout (17.11.) – nicht übernommen |
| Google Gemini Notebook Blog | https://blog.google/innovation-and-ai/products/gemini-notebook/ | ⚠️ teilweise | 1 | Liste per JavaScript; über Sitemap: interaktive Sites (16.11.) – nicht übernommen |
| Google AI Blog | https://blog.google/innovation-and-ai/technology/ai/ | ⚠️ teilweise | 1 | Liste per JavaScript; über Sitemap nur Interview (19.11.), nicht relevant |
| Google Blog-Sitemap | https://blog.google/en-us/sitemap.xml | ✅ OK | ~90 | Hauptquelle Google. Computer use Mac (`datePublished` 19.11.), «Transfer history» (ICYMI, ältere Funktion), GTIG AI Threat Tracker (16.11.), «Mirror Dimension» für Agenten-Tests (19.11.) – geprüft, nur Computer use übernommen |
| DeepSeek API Change Log | https://api-docs.deepseek.com/updates | ✅ OK | 0 | Kein Eintrag im Zeitraum |
| Hugging Face Blog | https://huggingface.co/blog | ✅ OK | n/a | Seite geladen, Datumsangaben nicht maschinell auswertbar; keine Top-News gefunden |
| GitHub Copilot Changelog | https://github.blog/changelog/label/copilot/ | ✅ OK | mehrere | MAI Code 2 in Copilot – im Microsoft-Eintrag enthalten |
| LangChain Blog | https://www.langchain.com/blog | ✅ OK | n/a | Ausserhalb Fokus |
| Perplexity Blog | https://www.perplexity.ai/hub/blog | ✅ OK | n/a | Ausserhalb Fokus |
| Microsoft AI News | https://microsoft.ai/news/ | ✅ OK | 7 | Ignite (17.11.): sieben MAI-Modelle → «Weltweit» übernommen (Ausnahme «neuer Anbieter») |
| Microsoft Azure Blog AI (RSS) | https://azure.microsoft.com/en-us/blog/category/ai-machine-learning/feed/ | ✅ OK | 5 | Ignite-Enterprise-Posts (17.11.) – nicht übernommen |
| Microsoft – Hugging Face API | https://huggingface.co/api/models?author=microsoft&sort=createdAt&direction=-1&limit=10 | ✅ OK | 2 | Kleine Modelle – nicht übernommen |
| Qwen – Hugging Face API | https://huggingface.co/api/models?author=Qwen&sort=createdAt&direction=-1&limit=10 | ✅ OK | 0 | Kein neues offenes Modell im Zeitraum |
| Alibaba Cloud Press Room | https://www.alibabacloud.com/press-room | ✅ OK | 1 | Qwen4-Max (16.11.) – neu gestrichen: «neues Spitzenmodell» eines etablierten Labs ohne neue Fähigkeit |
| Qwen Research | https://qwen.ai/research | ⚠️ teilweise | 0 | HTTP 200, Inhalt lädt nur per JavaScript |
| Tencent – Hugging Face API (`search=Hy`) | https://huggingface.co/api/models?author=tencent&search=Hy&sort=createdAt&direction=-1&limit=20 | ✅ OK | mehrere | Hy4-Varianten, Übersetzungsmodelle – Varianten, nicht übernommen |
| Hugging Face Trending (API) | https://huggingface.co/api/models?sort=trendingScore&limit=30 | ✅ OK | mehrere | Kleinere offene Modelle – nicht übernommen |
| The Decoder (DE) | https://the-decoder.de | ✅ OK | ~10 | Zur Absicherung; keine zusätzlichen Kandidaten |
| Simon Willison Weblog | https://simonwillison.net | ✅ OK | ~6 | Nicht übernommen |
| Last Week in AI (RSS) | https://lastweekin.ai/feed | ✅ OK | 1 | #348 (21.11.): IPO, GPT-6.2, Neon, MAI, Klage Kaliforniens gegen OpenAI → übernommen und verlinkt; ChatGPT Wallet (13.11.) und Klage der Non-Profits (12.11.) liegen in KW 46; Nvidia/Huang (Personalie, Hardware) und Trump-Xi (Aussage) ausgeschlossen |
| The Batch (DeepLearning.AI) | https://www.deeplearning.ai/the-batch/ | ✅ OK | 1 | Ausgabe 20.11.: keine zusätzlichen Kandidaten |
| SCMP Tech (RSS) | https://www.scmp.com/rss/36/feed | ✅ OK | 22 | Viel Nvidia/Chips (Hardware/Personalie, raus), Tencent Hy4 Sicherheitstests (22.11.), Anthropic-IPO aus China-Sicht |
| Rest of World | https://restofworld.org/ | ❌ Fehler (HTTP 429) | – | «Too Many Requests», wie im vorigen Testlauf |
| UNO – Medienmitteilungen | https://press.un.org/en | ✅ OK | 0 | Keine KI-Meldung im Zeitraum |
| EU AI Act – Kommission | https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai | ✅ OK | 0 | Statische Übersicht (Referenz) |
| EU Digital Strategy – News | https://digital-strategy.ec.europa.eu/en/news | ✅ OK | 14 | Vollständig erst mit `?page=0`/`?page=1`. Art.-27-Vorlage (16.11.) übernommen; Apply AI Summit (16.11.), Aufruf an europäische KI-Anbieter (17.11.), Temu-DSA (17.11.) nicht |
| Mistral AI News | https://mistral.ai/news | ✅ OK | 0 | Kein Eintrag im Zeitraum |
| Bund – Digitale Schweiz (BAKOM) | https://www.bakom.admin.ch | ✅ OK | 0 | Keine KI-Meldung |
| EDÖB – Mitteilungen | https://www.edoeb.admin.ch/de/mitteilungen | ✅ OK | 0 | Keine Mitteilung im Zeitraum |
| Swiss AI Initiative (ETH/EPFL) | https://www.swiss-ai.org | ✅ OK | 0 | Keine datierten neuen Meldungen |
| Swiss AI Anwenderverband | https://www.swissai.ch/blog | ✅ OK | 1 | Weekly Case – Praxisbeispiel, nicht übernommen |
| inside-it.ch | https://www.inside-it.ch | ✅ OK | ~6 | Fedpol Anti-Deepfake-Modul (Beschaffung) gestrichen; übrige ohne KI-Bezug |
| Netzwoche | https://www.netzwoche.ch | ✅ OK | ~5 | KI-Cyberangriff auf EU-Kommission (20.11.) → Europa übernommen; NDB-KI-Software, «Cyberangriffe mit KI-Agenten erreichen die Schweiz» erst KW 48 |
| swissinfo.ch | https://www.swissinfo.ch | ✅ OK | 0 | Keine Top-News im Zeitraum |
| Websuche (CRITERIA) | WebSearch | ✅ OK | 1 | Gesucht: Alibaba/Qwen, DeepSeek, Moonshot/Kimi, Zhipu/GLM, MiniMax, ByteDance, Baidu/ERNIE, Tencent. Treffer in der Woche nur Qwen4-Max (16.11., gestrichen nach neuer Regel). DeepSeek (letztes Update Oktober), Kimi K3.1 Pro (Okt., Gewichte 4.11.), GLM (August), ERNIE 5.5 Flash Preview (12.11.) ausserhalb. Zusätzlich geprüft: ChatGPT Wallet (13.11.) und Non-Profit-Klage auf KI-Stopp (12.11.) – beide KW 46 |

## Zusammenfassung
- Quellen geprüft: 42, davon OK: 37, teilweise: 4, Fehler: 1 (Rest of World, HTTP 429)
- Kandidaten vor Filter: 24, Einträge nach Filter: 6 (Global 4 – davon Werkzeuge 3, Weltweit 1 –, Europa 2, Schweiz 0, Auf dem Radar 0)
- Änderungen gegenüber dem vorigen Testlauf durch die neuen Kriterien: **Gemini 4 Neon** (Preisdruck) und **Qwen4-Max** (neues Spitzenmodell ohne neue Fähigkeit) gestrichen. Neu aufgenommen: **Computer use in der Gemini-App für Mac** (neue Fähigkeit des Werkzeugs). Microsoft bleibt (Ausnahme «neuer Anbieter»), ohne Preisaussagen.
- Nur eine weltweite Top-News → Platzregel: Werkzeuge hätten 4 Plätze; der vierte bleibt frei, weil kein weiterer Kandidat stark genug war (Tasks gratis, interaktive Sites, Tool Retrieval, Genie 4 gestrichen).

## Vorschläge
- **Rest of World:** liefert erneut HTTP 429. Vorschlag: RSS-Feed testen (https://restofworld.org/feed/) oder unter «Ausgesetzt» führen.
- **EU Digital Strategy – News:** URL in SOURCES.md mit `?page=0` hinterlegen (ohne Parameter unvollständige Liste).
- **Hugging Face Blog:** Feed https://huggingface.co/blog/feed.xml statt HTML verwenden (Datum auswertbar).
- **Kalifornien Attorney General** (https://oag.ca.gov/news) als Primärquelle für US-Klagen freigeben; ist vom Environment blockiert (laut vorigem Testlauf).
