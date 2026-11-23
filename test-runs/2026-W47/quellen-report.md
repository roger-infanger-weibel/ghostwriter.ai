# Quellen-Report – Testlauf KW 47 / 2026

Gestartet: 23. November 2026, 14:40 Uhr (Zürich)

Prüfzeitraum: 16.–22. November 2026. Abruf per HTTP-GET (curl, Browser-User-Agent), danach Auswertung des Seiteninhalts.

| Quelle (aus SOURCES.md) | URL | Status | Treffer letzte 7 Tage | Bemerkung |
|---|---|---|---|---|
| OpenAI News | https://openai.com/news | ✅ OK | 30 | HTTP 200 (früher 403); Auswertung über RSS, 1 Eintrag übernommen (GPT-6.2) |
| OpenAI News (RSS) | https://openai.com/news/rss.xml | ✅ OK | 30 | Viele Kundenstorys/Partnerschaften, gefiltert |
| OpenAI ChatGPT Release Notes | https://learn.chatgpt.com/docs/whats-new | ✅ OK | 1 | 17. Nov: GPT-6.2 (identisch mit News) |
| Anthropic News | https://www.anthropic.com/news | ✅ OK | 2 | IPO-Preisfestsetzung (18.11.) und -Abschluss (20.11.) |
| Anthropic Claude Code Changelog | https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md | ✅ OK | n/a | Keine Datumsangaben im Changelog; neueste Versionen 2.1.326–2.1.330, nur reguläre Releases |
| Anthropic API Release Notes | https://platform.claude.com/docs/en/release-notes/overview | ✅ OK | 2 | 16.11. Text-Wasserzeichen, Webhook-Events; 17.11. Linked billing (Beta) – nicht übernommen |
| Google Gemini API Changelog | https://aistudio.google.com/docs/changelog | ⚠️ teilweise | 0 | HTTP 200, aber Inhalt lädt nur per JavaScript (nur Seitentitel im HTML) |
| Google Gemini App Updates | https://gemini.google/release-notes/ | ✅ OK | 2 | 17.11. Tasks in Gemini, 19.11. Computer use für Mac – nur USA/ausgewählte Länder, nicht Schweiz |
| Google NotebookLM (Gemini Notebook) Updates | https://support.google.com/gemininotebook/ | ⚠️ teilweise | 0 | HTTP 200, aber nur Hilfe-Übersicht ohne Release Notes; Neuigkeit (interaktive Sites) über Google Blog gefunden |
| Google AI Blog | https://blog.google/innovation-and-ai/technology/ai/ | ⚠️ teilweise | 33 | Artikelliste lädt per JavaScript, RSS liefert nur 1 Eintrag; Auswertung über blog.google/en-us/sitemap.xml, 3 Einträge übernommen |
| Meta AI / Llama Blog | https://ai.meta.com/blog/ | ❌ Fehler (HTTP 400) | – | Meta liefert Fehlerseite an Nicht-Browser-Clients |
| Meta Llama GitHub Releases | https://github.com/meta-llama/llama-models/releases | ❌ Fehler (HTTP 403) | – | Vom Environment blockiert: GitHub-Zugriff der Session ist auf das eigene Repo beschränkt |
| Microsoft AI News | https://microsoft.ai/blog/ | ❌ Fehler (Proxy 403) | – | Vom Environment blockiert («no rule or network setting allows this host») |
| DeepSeek API / Docs | https://api-docs.deepseek.com/news/ | ❌ Fehler (HTTP 404) | – | Pfad existiert nicht mehr; https://api-docs.deepseek.com/ liefert HTTP 200 |
| Hugging Face Blog | https://huggingface.co/blog | ✅ OK | 5 | Modell- und Technik-Blogposts (z. B. Inkling 2 Mini), nicht relevant für Fokus |
| GitHub Copilot Changelog | https://github.blog/changelog/label/copilot/ | ✅ OK | 21 | U. a. GPT-6.2 und Gemini 4 Neon in Copilot (Sekundärbestätigung) |
| LangChain Blog | https://www.langchain.com/blog | ✅ OK | 3 | LangSmith-Umbau, Essays – nicht übernommen |
| Perplexity Blog | https://www.perplexity.ai/hub/blog | ✅ OK | 5 | Multiagent, Orchestrator-API, Frontier Research – ausserhalb Fokus |
| Hugging Face (Hub) | https://huggingface.co | ✅ OK | 0 | Plattform, keine datierten Meldungen |
| Civitai | https://civitai.com | ✅ OK | 0 | Community-Plattform, keine Nachrichten |
| Global AI Community | https://globalai.community | ✅ OK | 1 | Event-Hinweis, nicht relevant |
| Stack Exchange (AI) | https://stackexchange.com | ✅ OK | 0 | Startseite des Netzwerks, nicht die AI-Site; keine datierten Meldungen |
| Alignify | https://alignify.co | ✅ OK | 0 | Keine datierten Meldungen |
| The Decoder (DE) | https://the-decoder.de | ✅ OK | ~10 | Sekundärquelle; u. a. Signal und KI-Agenten (17.11.) – nicht übernommen |
| Simon Willison Weblog | https://simonwillison.net | ✅ OK | ~5 | Sekundärquelle/Blog, nicht übernommen |
| EU AI Act – Kommission | https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai | ✅ OK | 1 | 16.11. Apply AI Summit; Detail-Auswertung über /en/news: Art.-27-Vorlage übernommen, AI Board (18.11.) und Advisory Forum (16.11.) nicht |
| Rapporteur (ehem. Euractiv) | https://www.rapporteur.com | ❌ Fehler (HTTP 403) | – | Cloudflare-Sperre («Attention Required») |
| Mistral AI News | https://mistral.ai/news | ✅ OK | 0 | Letzter Eintrag 5. November 2026 |
| Mistral AI News & Announcements | https://mistral.ai/news/ | ✅ OK | 0 | Duplikat der Zeile darüber |
| Bund – Digitale Schweiz (BAKOM) | https://www.bakom.admin.ch | ✅ OK | 1 | 18.11. Medienförderung – kein KI-Bezug |
| EDÖB (Datenschutz) | https://www.edoeb.admin.ch | ✅ OK | 0 | Startseite zeigt alte Meldungen; /de/mitteilungen: letzte Meldung 6. November 2026 |
| Swiss AI Initiative (ETH/EPFL) | https://www.swiss-ai.org | ✅ OK | 0 | Keine neuen Meldungen |
| Swiss AI Anwenderverband | https://www.swissai.ch/blog | ✅ OK | 1 | 20.11. «Weekly Case» (Praxisbeispiel) – nicht übernommen |
| inside-it.ch | https://www.inside-it.ch | ✅ OK | 2 | 16.11. Zürcher Cloud-Strategie, M365-Ausfall – kein KI-Schwerpunkt |
| Netzwoche | https://www.netzwoche.ch | ✅ OK | ~15 | KI-Meldungen: Empa-KI-Agent (22.11.), Angriff auf EU-Kommission mit KI-Tool (20.11., via Politico), Interview EPFL (18.11.) – Sekundärquellen, nicht übernommen |
| swissinfo.ch | https://www.swissinfo.ch | ✅ OK | ~16 | Features zu KI-Assistenten, keine Top-News |

## Zusammenfassung
- Quellen geprüft: 36, davon OK: 28, teilweise: 3, Fehler: 5
- Kandidaten vor Filter: 19, Einträge nach Filter: 6 (Global 5, Europa 1, Schweiz 0)

## Vorschläge
- **OpenAI News:** Die HTML-Seite liefert wieder HTTP 200; der Hinweis «HTML-Seite liefert 403» in SOURCES.md ist überholt. Die RSS-Zeile bleibt trotzdem die bessere Quelle.
- **Gemini API Changelog:** https://aistudio.google.com/docs/changelog lädt nur per JavaScript. Die Alternative https://ai.google.dev/gemini-api/docs/changelog ist in diesem Environment nicht erreichbar (Verbindungsfehler). Für Netzwerk-Freigabe prüfen oder ersatzweise den Google-Blog-Bereich «Developer tools» nutzen.
- **NotebookLM / Gemini Notebook:** Die Support-Startseite enthält keine Release Notes. Vorschlag: https://blog.google/innovation-and-ai/products/gemini-notebook/ ergänzen (dort erschien die Meldung zu interaktiven Sites).
- **Google AI Blog:** Liste lädt per JavaScript. Vorschlag: https://blog.google/en-us/sitemap.xml (mit `lastmod`) als technische Zusatzquelle notieren.
- **DeepSeek:** URL auf https://api-docs.deepseek.com/ ändern (der Pfad /news/ liefert 404).
- **Microsoft AI:** Host microsoft.ai im Netzwerk-Policy des Environments freigeben, sonst Zeile streichen.
- **Meta AI Blog:** Liefert HTTP 400 an Skript-Clients; ersatzweise https://about.fb.com/news/ prüfen oder Zeile streichen.
- **Llama GitHub Releases:** Nur abrufbar, wenn das Repo der Session freigegeben ist; sonst Zeile streichen (Fokus liegt ohnehin auf Claude/ChatGPT/Gemini).
- **Rapporteur:** Cloudflare blockt automatisierte Abrufe dauerhaft; Zeile streichen oder durch https://artificialintelligenceact.eu ersetzen.
- **Mistral:** Doppelte Zeile in SOURCES.md (mit und ohne Schrägstrich) zusammenführen.
- **Community-Quellen** (Hugging Face Hub, Civitai, Global AI Community, Stack Exchange, Alignify) liefern keine datierten Meldungen; Streichung gemäss Pflegeregel («8 Wochen nichts geliefert») prüfen.
- **EDÖB:** Statt Startseite direkt https://www.edoeb.admin.ch/de/mitteilungen eintragen (Startseite zeigt keine aktuellen Meldungen).
