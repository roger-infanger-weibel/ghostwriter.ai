# Quellen-Report – Testlauf KW 47 / 2026

<<<<<<< Updated upstream
Gestartet: 25. November 2026, ca. 15:30 Uhr (Zürich)

Prüfzeitraum: 16.–22. November 2026. Abruf per HTTP-GET (curl, Browser-User-Agent), danach Auswertung des Seiteninhalts. Geprüft wurden alle 42 aktiven Quellen aus `SOURCES.md`; die Tabelle «Ausgesetzt» wird laut SOURCES.md nicht geprüft. Angewendet wurden die aktuellen Kriterien: Modell-Verbesserungen sind keine Top-News, keine Benchmarks, keine personenbezogenen News, keine Hardware-News, ein Thema pro Eintrag.

| Quelle (aus SOURCES.md) | URL | Status | Treffer letzte 7 Tage | Bemerkung |
|---|---|---|---|---|
| OpenAI News | https://openai.com/news | ✅ OK | 34 | HTTP 200; Auswertung über RSS (gleicher Inhalt) |
| OpenAI News (RSS) | https://openai.com/news/rss.xml | ✅ OK | 34 | Viele Kundenstorys/Partnerschaften. GPT-6.2 Astra/Sol (17.11.) als Modell-Verbesserung gestrichen; «Combatting adversarial distillation» (20.11.), «Managing frontier AI risk» (18.11.) nicht übernommen. ChatGPT Wallet ist vom 13.11. (KW 46) |
| OpenAI ChatGPT Release Notes | https://learn.chatgpt.com/docs/whats-new | ✅ OK | 1 | GPT-6.2 (identisch mit News) – gestrichen |
| Anthropic News | https://www.anthropic.com/news | ✅ OK | 2 | IPO-Preisfestsetzung (18.11.) und -Abschluss (20.11.); Abschluss übernommen |
| Anthropic Claude Code Changelog (Raw) | https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md | ✅ OK | n/a | Keine Datumsangaben; reguläre Releases (u. a. Code-Mode-Fixes, Skills aus MCP-Servern) – nicht übernommen |
| Anthropic API Release Notes | https://platform.claude.com/docs/en/release-notes/overview | ✅ OK | 5 | Linked billing (17.11.), Watermark (16.11.), Opus-4.5-Deprecation und Enterprise Frontier Safeguards (20.11.), Analytics-Fixes (23.11.) – Detail-Updates, nicht übernommen |
| Google Gemini API Changelog | https://aistudio.google.com/docs/changelog | ✅ OK | 4 | Lesbar: Transcribe-Update (17.11.), Gemini 4 Neon (18.11.), Genie 4 GA und Tool Retrieval (19.11.) – Neon als Modell-Verbesserung gestrichen |
| Google Developer Tools Blog | https://blog.google/innovation-and-ai/technology/developers-tools/ | ⚠️ teilweise | 3 | Liste per JavaScript; über Sitemap: EmbeddingGemma 2 (17.11.), Genie 4 in Gemini API, Tool Retrieval (19.11.) – nicht übernommen |
| Google Gemini App Updates | https://gemini.google/release-notes/ | ✅ OK | 2 | Tasks gratis (17.11.) übernommen; Computer use für Mac (19.11.) – Platzregel, nicht übernommen |
| Google Gemini Notebook Blog | https://blog.google/innovation-and-ai/products/gemini-notebook/ | ⚠️ teilweise | 1 | Liste per JavaScript; über Sitemap: interaktive Sites (16.11.) übernommen |
| Google AI Blog | https://blog.google/innovation-and-ai/technology/ai/ | ⚠️ teilweise | 1 | Liste per JavaScript; über Sitemap nur Interview-Reihe (19.11.) – nicht relevant |
| Google Blog-Sitemap | https://blog.google/en-us/sitemap.xml | ✅ OK | ~45 | Hauptquelle Google. Zusätzlich: Chatverlauf-Import aus anderen KI-Apps (19.11.), GTIG AI Threat Tracker Q4 (16.11.), Ask Maps in Europa (16.11.), Genie 4 – nicht übernommen |
| DeepSeek API Change Log | https://api-docs.deepseek.com/updates | ✅ OK | 0 | Letzter Eintrag 13.11.2026 |
| Hugging Face Blog | https://huggingface.co/blog | ✅ OK | ~10 | u. a. Inkling 2 Mini – nicht übernommen |
| GitHub Copilot Changelog | https://github.blog/changelog/label/copilot/ | ✅ OK | mehrere | Bestätigt MAI Code 2 in GitHub Copilot (17.11.) |
| LangChain Blog | https://www.langchain.com/blog | ✅ OK | ~10 | Ausserhalb Fokus |
| Perplexity Blog | https://www.perplexity.ai/hub/blog | ✅ OK | ~8 | Ausserhalb Fokus |
| Microsoft AI News | https://microsoft.ai/news/ | ✅ OK | 7 | Ignite (17.11.): sieben MAI-Modelle → «Weltweit» übernommen (ohne Maia-Chip: Hardware) |
| Microsoft Azure Blog AI (RSS) | https://azure.microsoft.com/en-us/blog/category/ai-machine-learning/feed/ | ✅ OK | 5 | Ignite-Enterprise-Posts (17.11.) – nicht übernommen |
| Microsoft – Hugging Face API | https://huggingface.co/api/models?author=microsoft&sort=createdAt&direction=-1&limit=10 | ✅ OK | 2 | Aion-1.0-Instruct-2.3B (18.11.) – kleines Modell |
| Qwen – Hugging Face API | https://huggingface.co/api/models?author=Qwen&sort=createdAt&direction=-1&limit=10 | ✅ OK | 0 | Letztes Modell 9.10.; Qwen4-Max ist geschlossen |
| Alibaba Cloud Press Room | https://www.alibabacloud.com/press-room | ✅ OK | 1 | Qwen4-Max (16.11.) aus Primärquelle bestätigt – gestrichen (siehe Zusammenfassung) |
| Qwen Research | https://qwen.ai/research | ⚠️ teilweise | 0 | HTTP 200, Inhalt lädt nur per JavaScript |
| Tencent – Hugging Face API (Hy) | https://huggingface.co/api/models?author=tencent&search=Hy&sort=createdAt&direction=-1&limit=20 | ✅ OK | 14 | Neuer Filter funktioniert: Hy4-flash (17.11.), Hy4-base/FP8 (18.11.), Hy-MT3-Übersetzungsmodelle (17.11.) – kleineres offenes Modell, nicht übernommen |
| Hugging Face Trending (API) | https://huggingface.co/api/models?sort=trendingScore&limit=30 | ✅ OK | ~18 | Inkling 2 Mini, Tencent Hy4-flash, SenseNova-Loop-9B, Aleph Alpha Kolibri-1.1 – nicht übernommen |
| The Decoder (DE) | https://the-decoder.de | ✅ OK | 2 | Startseite zeigt nur wenige datierte Artikel (u. a. Isomorphic-Labs-Funding 17.11. – Funding, raus) |
| Simon Willison Weblog | https://simonwillison.net | ✅ OK | ~8 | Nicht übernommen |
| Last Week in AI (RSS) | https://lastweekin.ai/feed | ✅ OK | 1 | #348 (21.11.): IPO, GPT-6.2/Neon, MAI-Modelle, Nvidia-CEO, Trump/Xi, Klage Kaliforniens gegen OpenAI; als Quelle für die Klage verlinkt |
| The Batch (DeepLearning.AI) | https://www.deeplearning.ai/the-batch/ | ✅ OK | 1 | Ausgabe 20.11.: Nvidia-CEO (personenbezogen), Fable 5.2 / Anthropic-IPO, World Labs Atlas |
| SCMP Tech (RSS) | https://www.scmp.com/rss/36/feed | ✅ OK | ~30 | Überwiegend Nvidia/Chips (Hardware bzw. personenbezogen), Tencent Hy4-Sicherheitstests (22.11.), Anthropic-IPO aus China-Sicht |
| Rest of World | https://restofworld.org/ | ❌ Fehler (HTTP 429) | – | Zweimal «Too Many Requests»; nicht auswertbar |
| UNO – Medienmitteilungen | https://press.un.org/en | ✅ OK | 0 | Nur Ausschuss-/Sicherheitsrats-Meldungen ohne KI-Bezug |
| EU AI Act – Kommission | https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai | ✅ OK | 0 | Statische Übersicht (Referenz) |
| EU Digital Strategy – News | https://digital-strategy.ec.europa.eu/en/news | ⚠️ teilweise | 4 | Liste lädt per JavaScript (nur 1 Eintrag im HTML); ausgewertet über https://digital-strategy.ec.europa.eu/en/rss.xml und Einzelartikel. Art.-27-Vorlage (16.11.) übernommen; Apply AI Summit (16.11.), Temu-DSA (17.11.), Bildungs-Konsortium (20.11.) nicht |
| Mistral AI News | https://mistral.ai/news | ✅ OK | 0 | Letzter Eintrag 5.11.2026 |
| Bund – Digitale Schweiz (BAKOM) | https://www.bakom.admin.ch | ✅ OK | 0 | Nur Medienförderung (18.11.), kein KI-Bezug |
| EDÖB – Mitteilungen | https://www.edoeb.admin.ch/de/mitteilungen | ✅ OK | 0 | Letzte Mitteilung 6.11.2026 |
| Swiss AI Initiative (ETH/EPFL) | https://www.swiss-ai.org | ✅ OK | 0 | Keine datierten neuen Meldungen |
| Swiss AI Anwenderverband | https://www.swissai.ch/blog | ✅ OK | 1 | Praxisbeispiel (20.11.) – nicht übernommen |
| inside-it.ch | https://www.inside-it.ch | ✅ OK | ~5 | Zug: vertrauliche Daten in M365 (19.11.), Cyberangriff Baselbiet (20.11.) – kein KI-Thema bzw. keine Top-News |
| Netzwoche | https://www.netzwoche.ch | ✅ OK | ~5 | KI-Cyberangriff auf EU-Kommission (20.11.) → Europa übernommen (im ersten Durchgang übersehen, über den parallelen Testlauf e8cb1c2 gefunden und nachgeprüft); Interview zur KI-Infrastruktur (18.11., personenbezogen), Partner-Posts; BACS zu KI-Agenten-Angriffen und NDB-KI-Software erst 24./25.11. (KW 48) |
| swissinfo.ch | https://www.swissinfo.ch | ✅ OK | 0 | Anthropic-Büro in Zürich erst 25.11. (KW 48) |
| Websuche (CRITERIA) | WebSearch | ✅ OK | 2 | Gesucht: Alibaba/Qwen, DeepSeek, Moonshot/Kimi, Zhipu/GLM, MiniMax, Baidu/ERNIE, ByteDance, Tencent. Treffer in der Woche: Qwen4-Max (16.11., gestrichen); keine neuen Releases von DeepSeek, Kimi, GLM, MiniMax, ByteDance; ERNIE 5.5 Flash vom 12.11. (KW 46). Zusätzlich gefunden: **Klage Kaliforniens gegen OpenAI (16.11.)**, bestätigt durch Generalstaatsanwaltschaft, NPR/KUOW, Bloomberg Law, Axios, SF Standard. Primärquelle oag.ca.gov sowie axios.com, sfstandard.com, kuow.org **vom Environment blockiert** → verlinkt über Last Week in AI |

## Zusammenfassung
- Quellen geprüft: 42, davon OK: 36, teilweise: 5, Fehler: 1 (Rest of World, HTTP 429)
- Kandidaten vor Filter: 23, Einträge nach Filter: 7 (Global 5 – davon Werkzeuge 4, Weltweit 1 –, Europa 2, Schweiz 0, Auf dem Radar 0)
- Neu gegenüber dem vorigen Testlauf (wegen der neuen Kriterien): GPT-6.2 und Gemini 4 Neon gestrichen (Modell-Verbesserung, Benchmark- und Preisvergleiche); Maia-Chip aus dem Microsoft-Eintrag entfernt (Hardware, ein Thema pro Eintrag); neu aufgenommen: Klage Kaliforniens gegen OpenAI, Tasks in Gemini gratis, Gemini Notebook interaktive Sites.
- Kriterien-Update 19f63c4 (während des Laufs gepusht) bestätigt die Streichungen: Modelle etablierter Labs nur bei neuer Fähigkeit, kein Preisdruck als Begründung.
- **Qwen4-Max:** Neue Generation eines grossen chinesischen Labs, aber laut Alibaba vor allem besser und günstiger als der Vorgänger → nach der Regel «Keine Modell-Verbesserungen als News, im Zweifel streichen» gestrichen. Damit nur eine weltweite Meldung (Microsoft) und 4 Werkzeug-Plätze.
- Ebenfalls gestrichen: Trump/Xi-Absprache zu militärischer KI (nur mündliche Aussage, kein Text), US-Chip-Exportregeln (Hardware), Nvidia-CEO (personenbezogen), Klage von US-Nonprofits gegen KI-Firmen (nur eingereicht, Sekundärquelle), Gemini Computer use für Mac, Chatverlauf-Import, Gemini API Tool Retrieval, Genie 4, GTIG Threat Tracker, Tencent Hy4-flash, Inkling 2 Mini, Ask Maps in Europa.

## Vorschläge
- **Rest of World:** lieferte zweimal HTTP 429 (Rate-Limit). Alternative mit Datum: RSS-Feed https://restofworld.org/feed/latest (nicht getestet) – beim nächsten Lauf prüfen.
- **EU Digital Strategy – News:** Die Liste lädt per JavaScript; der RSS-Feed https://digital-strategy.ec.europa.eu/en/rss.xml liefert Einträge mit Datum, enthält aber nicht alle News-Artikel (die Art.-27-Vorlage fehlte). Vorschlag: RSS als zusätzliche Zeile aufnehmen, die News-Seite behalten.
- **Netzwerk:** `oag.ca.gov` (Generalstaatsanwaltschaft Kalifornien) im Environment freigeben, damit US-Behörden als Primärquelle verlinkt werden können; ebenso wären `apnews.com` oder `www.reuters.com` als seriöse Absicherung hilfreich (nicht getestet).
- **Tencent-Filter `search=Hy`** funktioniert: Hy4-flash und Hy4-base erscheinen jetzt direkt.
=======
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
>>>>>>> Stashed changes
