# Quellen-Report – Testlauf KW 47 / 2026

Gestartet: 25. November 2026, 15:41 Uhr (Zürich)

Prüfzeitraum: 16.–22. November 2026. Abruf per HTTP-GET (curl, Browser-User-Agent), danach Auswertung des Seiteninhalts. Geprüft wurden alle 42 aktiven Quellen aus `SOURCES.md`; die Tabelle «Ausgesetzt» wird laut SOURCES.md nicht geprüft. Neue Regeln angewendet: keine Benchmarks, keine personenbezogenen News, ein Thema pro Eintrag.

| Quelle (aus SOURCES.md) | URL | Status | Treffer letzte 7 Tage | Bemerkung |
|---|---|---|---|---|
| OpenAI News | https://openai.com/news | ✅ OK | 39 | HTTP 200; Auswertung über RSS (gleicher Inhalt) |
| OpenAI News (RSS) | https://openai.com/news/rss.xml | ✅ OK | 39 | Viele Kundenstorys; GPT-6.2 Astra/Sol (17.11.), «Combatting adversarial distillation» (20.11.), «Managing frontier AI risk» (18.11.) – Platzregel, nicht übernommen |
| OpenAI ChatGPT Release Notes | https://learn.chatgpt.com/docs/whats-new | ✅ OK | 1 | GPT-6.2 (17.11.), identisch mit News |
| Anthropic News | https://www.anthropic.com/news | ✅ OK | 2 | IPO-Preisfestsetzung (18.11.) und -Abschluss (20.11.); Abschluss übernommen |
| Anthropic Claude Code Changelog (Raw) | https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md | ✅ OK | n/a | Keine Datumsangaben, nur reguläre Releases (2.1.332) – nicht übernommen |
| Anthropic API Release Notes | https://platform.claude.com/docs/en/release-notes/overview | ✅ OK | 5 | Text-Wasserzeichen für ältere Modelle (16.11.), Linked billing Beta (17.11.), Analytics-API-Fixes – keine Breaking News |
| Google Gemini API Changelog | https://aistudio.google.com/docs/changelog | ✅ OK | 3 | Neon GA (18.11.), Genie 4 GA (19.11.), Transcribe-Update (17.11.) |
| Google Developer Tools Blog | https://blog.google/innovation-and-ai/technology/developers-tools/ | ⚠️ teilweise | 3 | Liste per JavaScript; über Sitemap: Tool Retrieval, Genie 4 in Gemini API (19.11.), EmbeddingGemma 2 (17.11.) – nicht übernommen |
| Google Gemini App Updates | https://gemini.google/release-notes/ | ✅ OK | 6 | Tasks gratis in sechs Ländern (17.11.), Computer use für Mac (19.11.), Google-Pay-Checkout, Anrufe – Platzregel, nicht übernommen |
| Google Gemini Notebook Blog | https://blog.google/innovation-and-ai/products/gemini-notebook/ | ⚠️ teilweise | 1 | Liste per JavaScript; über Sitemap: interaktive Sites (16.11.) – nicht übernommen |
| Google AI Blog | https://blog.google/innovation-and-ai/technology/ai/ | ⚠️ teilweise | 1 | Liste per JavaScript; über Sitemap, nicht relevant |
| Google Blog-Sitemap | https://blog.google/en-us/sitemap.xml | ✅ OK | ~60 | Hauptquelle Google. Neon-Artikel `lastmod` 24.11., `datePublished` 18.11.; Hydrogen `lastmod` 16.11., erschienen 12.11. (KW 46) |
| DeepSeek API Change Log | https://api-docs.deepseek.com/updates | ✅ OK | 0 | Letzter Eintrag 13.11.2026 |
| Hugging Face Blog | https://huggingface.co/blog | ✅ OK | n/a | Seite geladen, Datumsangaben nicht maschinell auswertbar; keine Top-News gefunden |
| GitHub Copilot Changelog | https://github.blog/changelog/label/copilot/ | ✅ OK | mehrere | Modell-Abkündigungen (16.11.), MAI Code 2 – nicht separat übernommen |
| LangChain Blog | https://www.langchain.com/blog | ✅ OK | n/a | Ausserhalb Fokus |
| Perplexity Blog | https://www.perplexity.ai/hub/blog | ✅ OK | n/a | Ausserhalb Fokus |
| Microsoft AI News | https://microsoft.ai/news/ | ✅ OK | 7 | Ignite (17.11.): sieben MAI-Modelle → «Weltweit» übernommen |
| Microsoft Azure Blog AI (RSS) | https://azure.microsoft.com/en-us/blog/category/ai-machine-learning/feed/ | ✅ OK | 5 | Ignite-Enterprise-Posts (17.11.) – nicht übernommen |
| Microsoft – Hugging Face API | https://huggingface.co/api/models?author=microsoft&sort=createdAt&direction=-1&limit=10 | ✅ OK | 2 | Aion-1.0-Instruct-2.3B (18.11.) – kleines Modell |
| Qwen – Hugging Face API | https://huggingface.co/api/models?author=Qwen&sort=createdAt&direction=-1&limit=10 | ✅ OK | 0 | Letztes Modell 9.10.; Qwen4-Max ist geschlossen |
| Alibaba Cloud Press Room | https://www.alibabacloud.com/press-room | ✅ OK | 1 | Qwen4-Max (16.11.), Datum im Artikel bestätigt → übernommen |
| Qwen Research | https://qwen.ai/research | ⚠️ teilweise | 0 | HTTP 200, Inhalt lädt nur per JavaScript |
| Tencent – Hugging Face API (`search=Hy`) | https://huggingface.co/api/models?author=tencent&search=Hy&sort=createdAt&direction=-1&limit=20 | ✅ OK | 14 | Filter wirkt: Hy4-flash (17.11.), Hy4-base/FP8 (18.11.), Hy-MT3-Übersetzungsmodelle – kleineres offenes Modell, nicht übernommen |
| Hugging Face Trending (API) | https://huggingface.co/api/models?sort=trendingScore&limit=30 | ✅ OK | 17 | Inkling 2 Mini (17.11.), Tencent Hy4-flash, Aleph Alpha Kolibri-1.1 (20.11.), ERNIE 5.5 Flash Preview (Gewichte 23.11., KW 48) – nicht übernommen |
| The Decoder (DE) | https://the-decoder.de | ✅ OK | ~10 | Zur Absicherung; keine zusätzlichen Kandidaten |
| Simon Willison Weblog | https://simonwillison.net | ✅ OK | ~6 | Nicht übernommen |
| Last Week in AI (RSS) | https://lastweekin.ai/feed | ✅ OK | 1 | #348 (21.11.): IPO, GPT-6.2, Neon, MAI, Klage Kaliforniens gegen OpenAI (16.11.), US-Exportregel (16.11.); Klage übernommen und verlinkt |
| The Batch (DeepLearning.AI) | https://www.deeplearning.ai/the-batch/ | ✅ OK | 1 | Ausgabe 20.11.: Nvidia (personenbezogen), Fable 5.2 (KW 46), Anthropic-IPO |
| SCMP Tech (RSS) | https://www.scmp.com/rss/36/feed | ✅ OK | ~30 | Viel Nvidia/Huang (personenbezogen, raus), Tencent Hy4 Sicherheitstests (22.11.), Anthropic-IPO aus China-Sicht |
| Rest of World | https://restofworld.org/ | ❌ Fehler (HTTP 429) | – | Zwei Abrufe im Abstand von mehreren Minuten, beide «Too Many Requests» |
| UNO – Medienmitteilungen | https://press.un.org/en | ✅ OK | 0 | KI-Themen erst am 24.11. (Second Committee, Sicherheitsrat) – Kandidaten für KW 48 |
| EU AI Act – Kommission | https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai | ✅ OK | 0 | Statische Übersicht (Referenz) |
| EU Digital Strategy – News | https://digital-strategy.ec.europa.eu/en/news | ✅ OK | 14 | Ohne Parameter nur 1 Treffer (25.11.) sichtbar; mit `?page=0`/`?page=1` vollständig. Art.-27-Vorlage (16.11.) übernommen; Apply AI Summit (16.11.), Aufruf an europäische KI-Anbieter (17.11.), Temu-DSA (17.11.) nicht |
| Mistral AI News | https://mistral.ai/news | ✅ OK | 0 | Letzter Eintrag 5.11.2026 |
| Bund – Digitale Schweiz (BAKOM) | https://www.bakom.admin.ch | ✅ OK | 0 | Medienförderung (18.11.), keine KI-Meldung |
| EDÖB – Mitteilungen | https://www.edoeb.admin.ch/de/mitteilungen | ✅ OK | 0 | Keine Mitteilung im Zeitraum (6.11., dann 24.11. – Personalie) |
| Swiss AI Initiative (ETH/EPFL) | https://www.swiss-ai.org | ✅ OK | 0 | Keine datierten neuen Meldungen |
| Swiss AI Anwenderverband | https://www.swissai.ch/blog | ✅ OK | 1 | Weekly Case (20.11.) – Praxisbeispiel, nicht übernommen |
| inside-it.ch | https://www.inside-it.ch | ✅ OK | ~6 | Fedpol Anti-Deepfake-Modul für E-ID (19.11.) – Beschaffung, gestrichen; Cyberangriff Baselbieter Verwaltung (20.11.) – kein KI-Bezug |
| Netzwoche | https://www.netzwoche.ch | ✅ OK | ~5 | KI-Cyberangriff auf EU-Kommission (20.11.) → Europa übernommen; NDB-KI-Software, BACS zu KI-Agenten erst 24./25.11. (KW 48) |
| swissinfo.ch | https://www.swissinfo.ch | ✅ OK | 0 | Anthropic-Büro in Zürich erst 25.11. (KW 48, «reportedly») |
| Websuche (CRITERIA) | WebSearch | ✅ OK | 2 | Gesucht: Alibaba/Qwen, DeepSeek, Moonshot/Kimi, Zhipu/GLM, MiniMax, Baidu/ERNIE, ByteDance, Tencent. Treffer in der Woche: Qwen4-Max (16.11., Alibaba Cloud, SCMP, Constellation Research, Techloy). Keine neuen Modelle von DeepSeek, Kimi, GLM, MiniMax, ByteDance; ERNIE 5.5 Flash (12.11.) und Tencent Hy4 (4.11.) ausserhalb. Zusätzlich abgesichert: Klage Kaliforniens gegen OpenAI (KPBS/NPR, BleepingComputer, SF Standard) und KI-Angriff auf EU-Kommission (AP, The Register, Brussels Times). oag.ca.gov und kpbs.org vom Environment blockiert. |

## Zusammenfassung
- Quellen geprüft: 42, davon OK: 37, teilweise: 4, Fehler: 1 (Rest of World, HTTP 429)
- Kandidaten vor Filter: 23, Einträge nach Filter: 7 (Global 5 – davon Werkzeuge 3, Weltweit 2 –, Europa 2, Schweiz 0, Auf dem Radar 0)
- Platzregel: zwei starke weltweite Meldungen (Alibaba Qwen4-Max, Microsoft MAI), daher 3 Werkzeug-Einträge (Anthropic-IPO, Klage gegen OpenAI, Gemini 4 Neon). Gestrichen u. a.: GPT-6.2 Astra/Sol, Gemini Tasks gratis, Computer use für Mac, Gemini Notebook interaktive Sites, Tool Retrieval, Genie 4, Claude-Text-Wasserzeichen, OpenAI-Distillation-Bericht.
- Neue Regeln: Benchmark-Vergleich bei Neon (frühere Version «nahe an Claude Opus 5.5») entfernt; Privatplatzierung beim IPO als Zweitthema weggelassen; Nvidia/Jensen Huang (Personalie) und Trump-Xi-Absprache (Aussage, kein Text veröffentlicht) ausgeschlossen.
- US-Exportregel für Fernzugriff auf KI-Chips (16.11.) nur über Last Week in AI gefunden, Primärquelle nicht geprüft – nicht übernommen.

## Vorschläge
- **Rest of World:** liefert wiederholt HTTP 429. Vorschlag: RSS-Feed testen (https://restofworld.org/feed/) oder vorübergehend unter «Ausgesetzt» führen.
- **EU Digital Strategy – News:** Die Seite ohne Parameter zeigte nur einen Treffer; `https://digital-strategy.ec.europa.eu/en/news?page=0` lieferte die vollständige Liste. Vorschlag: URL in SOURCES.md mit `?page=0` hinterlegen.
- **Kalifornien Attorney General:** `oag.ca.gov` ist vom Environment blockiert. Für Klagen/Regulierung in den USA als Primärquelle freigeben (https://oag.ca.gov/news) und ggf. in SOURCES.md aufnehmen.
- **Hugging Face Blog:** Datumsangaben im HTML nicht auswertbar; Vorschlag: Feed https://huggingface.co/blog/feed.xml verwenden.
