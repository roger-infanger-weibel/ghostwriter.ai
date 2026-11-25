# Quellen-Report – Testlauf KW 47 / 2026

Gestartet: 25. November 2026, 15:19 Uhr (Zürich)

Prüfzeitraum: 16.–22. November 2026. Abruf per HTTP-GET (curl, Browser-User-Agent), danach Auswertung des Seiteninhalts. Geprüft wurden alle 41 aktiven Quellen aus `SOURCES.md`; die Tabelle «Ausgesetzt» wird laut SOURCES.md nicht geprüft. Neue Regeln «Breaking News statt Modell-Details» angewendet.

| Quelle (aus SOURCES.md) | URL | Status | Treffer letzte 7 Tage | Bemerkung |
|---|---|---|---|---|
| OpenAI News | https://openai.com/news | ✅ OK | 31 | HTTP 200; Auswertung über RSS (gleicher Inhalt) |
| OpenAI News (RSS) | https://openai.com/news/rss.xml | ✅ OK | 31 | Viele Kundenstorys/Partnerschaften; GPT-6.2 Astra/Sol (17.11.) übernommen |
| OpenAI ChatGPT Release Notes | https://learn.chatgpt.com/docs/whats-new | ✅ OK | 1 | GPT-6.2 (identisch mit News) |
| Anthropic News | https://www.anthropic.com/news | ✅ OK | 2 | IPO-Preisfestsetzung (18.11.) und -Abschluss (20.11.); Abschluss übernommen |
| Anthropic Claude Code Changelog (Raw) | https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md | ✅ OK | n/a | Keine Datumsangaben, nur reguläre Releases – nicht übernommen |
| Anthropic API Release Notes | https://platform.claude.com/docs/en/release-notes/overview | ✅ OK | mehrere | Detail-Updates – keine Breaking News |
| Google Gemini API Changelog | https://aistudio.google.com/docs/changelog | ✅ OK | 4 | Diesmal lesbar (Markdown im HTML): Neon (18.11.), Tool Retrieval, Genie 4 GA (19.11.), Transcribe-Update (17.11.) |
| Google Developer Tools Blog | https://blog.google/innovation-and-ai/technology/developers-tools/ | ⚠️ teilweise | 3 | Liste per JavaScript; über Sitemap: Tool Retrieval, Genie 4 in Gemini API, EmbeddingGemma 2 – nicht übernommen |
| Google Gemini App Updates | https://gemini.google/release-notes/ | ✅ OK | ~5 | Tasks gratis, Computer use für Mac, Chatverlauf-Übernahme – nicht übernommen |
| Google Gemini Notebook Blog | https://blog.google/innovation-and-ai/products/gemini-notebook/ | ⚠️ teilweise | 1 | Liste per JavaScript; über Sitemap: interaktive Sites (16.11.) – Platzregel, nicht übernommen |
| Google AI Blog | https://blog.google/innovation-and-ai/technology/ai/ | ⚠️ teilweise | 1 | Liste per JavaScript; über Sitemap, nicht relevant |
| Google Blog-Sitemap | https://blog.google/en-us/sitemap.xml | ✅ OK | ~38 | Hauptquelle Google. Achtung: Neon-Artikel hat `lastmod` 24.11. (nachträglich aktualisiert), Datum aus dem Artikel (18.11.) |
| DeepSeek API Change Log | https://api-docs.deepseek.com/updates | ✅ OK | 0 | Letzter Eintrag 13.11.2026 |
| Hugging Face Blog | https://huggingface.co/blog | ✅ OK | ~10 | u. a. Inkling 2 Mini – nicht übernommen |
| GitHub Copilot Changelog | https://github.blog/changelog/label/copilot/ | ✅ OK | mehrere | Bestätigt MAI Code 2 in Copilot |
| LangChain Blog | https://www.langchain.com/blog | ✅ OK | ~10 | Ausserhalb Fokus |
| Perplexity Blog | https://www.perplexity.ai/hub/blog | ✅ OK | ~3 | Ausserhalb Fokus |
| Microsoft AI News | https://microsoft.ai/news/ | ✅ OK | 7 | Ignite (17.11.): sieben MAI-Modelle → «Weltweit» übernommen |
| Microsoft Azure Blog AI (RSS) | https://azure.microsoft.com/en-us/blog/category/ai-machine-learning/feed/ | ✅ OK | 5 | Ignite-Enterprise-Posts – nicht übernommen |
| Microsoft – Hugging Face API | https://huggingface.co/api/models?author=microsoft&sort=createdAt&direction=-1&limit=10 | ✅ OK | 2 | Aion-1.0-Instruct-2.3B (18.11.) – kleines Modell |
| Qwen – Hugging Face API | https://huggingface.co/api/models?author=Qwen&sort=createdAt&direction=-1&limit=10 | ✅ OK | 0 | Qwen4-Max ist geschlossen, daher nicht auf HF |
| Qwen Research | https://qwen.ai/research | ⚠️ teilweise | 0 | HTTP 200, Inhalt lädt nur per JavaScript; Qwen4-Max nur über Websuche gefunden |
| Tencent – Hugging Face API | https://huggingface.co/api/models?author=tencent&sort=createdAt&direction=-1&limit=40 | ✅ OK | 27 | Meist WeMM-Ecom-Varianten; Hy4-flash (17.11.) auch mit `limit=40` nicht mehr enthalten, nur über Trending |
| Hugging Face Trending (API) | https://huggingface.co/api/models?sort=trendingScore&limit=30 | ✅ OK | 15 | Inkling 2 Mini, Tencent Hy4-flash, Qwen3.8-Derivate – Platzregel, nicht übernommen |
| The Decoder (DE) | https://the-decoder.de | ✅ OK | ~10 | Zur Absicherung; kein Qwen4-Max-Artikel auf der Startseite |
| Simon Willison Weblog | https://simonwillison.net | ✅ OK | ~5 | Nicht übernommen |
| Last Week in AI (RSS) | https://lastweekin.ai/feed | ✅ OK | 1 | #348 (21.11.): IPO + Börsenkorrektur, GPT-6.2-Kritik, Gemini 4 Neon, MAI-Modelle; für Einordnung verlinkt |
| The Batch (DeepLearning.AI) | https://www.deeplearning.ai/the-batch/ | ✅ OK | 1 | Ausgabe 20.11.: Nvidia, Anthropic-IPO |
| SCMP Tech (RSS) | https://www.scmp.com/rss/36/feed | ✅ OK | 22 | Tencent Hy4 (22.11.), US-Chip-Exportdaten, Anthropic-IPO aus China-Sicht. Einzelartikel liefern HTTP 403 (Cloudflare) |
| Rest of World | https://restofworld.org/ | ✅ OK | ~2 | Keine KI-Top-News |
| UNO – Medienmitteilungen | https://press.un.org/en | ✅ OK | 0 | KI-Resolution Second Committee erst 24.11. – Kandidat für KW 48 |
| EU AI Act – Kommission | https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai | ✅ OK | 0 | Statische Übersicht (Referenz) |
| EU Digital Strategy – News | https://digital-strategy.ec.europa.eu/en/news | ✅ OK | ~5 | Art.-27-Vorlage (16.11.) übernommen; Apply AI Summit (16.11.), Temu-DSA (17.11.), Bildungs-Konsortium (20.11.) nicht |
| Mistral AI News | https://mistral.ai/news | ✅ OK | 0 | Letzter Eintrag 5.11.2026 |
| Bund – Digitale Schweiz (BAKOM) | https://www.bakom.admin.ch | ✅ OK | 0 | Keine KI-Meldung im Zeitraum |
| EDÖB – Mitteilungen | https://www.edoeb.admin.ch/de/mitteilungen | ✅ OK | 0 | Keine Mitteilung im Zeitraum |
| Swiss AI Initiative (ETH/EPFL) | https://www.swiss-ai.org | ✅ OK | 0 | Keine datierten neuen Meldungen |
| Swiss AI Anwenderverband | https://www.swissai.ch/blog | ✅ OK | 0–1 | Praxisbeispiel – nicht übernommen |
| inside-it.ch | https://www.inside-it.ch | ✅ OK | ~5 | Fedpol beschafft Anti-Deepfake-Modul für E-ID (19.11.) – Beschaffung, Sekundärquelle, gestrichen; BACS zu KI-Angriffen erst 25.11. (KW 48) |
| Netzwoche | https://www.netzwoche.ch | ✅ OK | ~5 | Keine Top-News |
| swissinfo.ch | https://www.swissinfo.ch | ✅ OK | ~1 | Keine Top-News |
| Websuche (CRITERIA) | WebSearch | ✅ OK | 1 | Gesucht: Alibaba/Qwen, DeepSeek, Moonshot/Kimi, Zhipu/GLM, MiniMax, Baidu/ERNIE, ByteDance, Tencent. Treffer in der Woche: **Qwen4-Max (16.11.)**, bestätigt durch Alibaba-Cloud-Pressemitteilung, SCMP, Constellation Research, Techloy → übernommen. ERNIE 5.5 Flash (12.11.) liegt in KW 46. Alibaba-Cloud-Seite selbst vom Environment blockiert (HTTP 403 Proxy). |

## Zusammenfassung
- Quellen geprüft: 41, davon OK: 37, teilweise: 4, Fehler: 0
- Kandidaten vor Filter: 17, Einträge nach Filter: 6 (Global 5 – davon Werkzeuge 3, Weltweit 2 –, Europa 1, Schweiz 0, Auf dem Radar 0)
- Platzregel: zwei starke weltweite Meldungen (Alibaba Qwen4-Max, Microsoft MAI), daher 3 Werkzeug-Einträge. Gestrichen u. a.: Gemini Notebook interaktive Sites, Gemini API Tool Retrieval, Genie 4, Tencent Hy4 flash (kleineres offenes Modell, Rang 3 bei Weltweit), Inkling 2 Mini.
- Breaking-News-Regel: Einträge ohne Parameter, Token-Preise, Modell-IDs und Abo-Stufen; max. eine Zahl pro Eintrag.
- Nicht in KW 47: Nvidia-CEO-Rücktritt (12.11.), Gemini 4 Hydrogen (12.11.), ERNIE 5.5 Flash (12.11.).

## Vorschläge
- **Alibaba Cloud Press Room** als Quelle prüfen: https://www.alibabacloud.com/press-room – hätte Qwen4-Max direkt geliefert; Host `www.alibabacloud.com` ist im Environment zurzeit blockiert und müsste freigegeben werden.
- **Tencent – Hugging Face API:** auch `limit=40` reicht nicht (27 neue Modelle in einer Woche, v. a. WeMM-Ecom-Varianten). Vorschlag: zusätzlich `&search=Hy` an die URL hängen, z. B. https://huggingface.co/api/models?author=tencent&search=Hy&sort=createdAt&direction=-1&limit=20
- **Gemini API Changelog** war diesmal ohne JavaScript lesbar – den Hinweis «lädt nur per JavaScript» in SOURCES.md beim nächsten Lauf nochmals prüfen.
- **Google-Blog-Sitemap:** `lastmod` ändert sich bei nachträglichen Updates (Neon: 24.11. statt 18.11.); den Filter auf ±7 Tage erweitern und das Datum im Artikel prüfen.
