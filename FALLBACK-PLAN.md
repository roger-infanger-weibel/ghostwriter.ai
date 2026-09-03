# Fallback-Plan – Während du auf Support wartest

**Status:** Cloud Routine #1 (Wochenpost) ist **BLOCKIERT** wegen Netzwerk-Policy  
**Wartezeit:** 24h–2 Wochen auf Support-Antwort

---

## 3 Optionen für die Zwischenzeit

### Option A: EMPFOHLEN – Manuelle News + Claude-Formatting

**Wie:**
1. Du sammelst **News manuell** von deinen 4 Tools
   - Claude: https://www.anthropic.com/news
   - ChatGPT: https://openai.com/news
   - Gemini: https://gemini.google.com/release-notes
   - Google AI Studio: https://ai.google.dev

2. Sendest mir die News (URL + 1–2 Sätze)

3. Ich formatiere sie nach `agent-source/CRITERIA.md` in `posts/YYYY-Www.md`

4. Commit & Push → PR → Du reviewst & mergst

**Vorteil:** 
- ✅ Volle Kontrolle über Quellen
- ✅ Manuelle Qualitätskontrolle
- ✅ Bereitet dich auf zukünftige Anpassungen vor

**Nachteil:** 
- ❌ Nicht automatisch (du musst News sammeln)

**Zeitaufwand:** ~15–20 Min/Woche

---

### Option B: Warten + Test mit eingeschränkten Quellen

**Wie:**
1. Ich passe `SOURCES.md` an (entferne blockierte Domains)
2. Cloud Routine läuft mit nur erreichbaren Quellen
3. Ergebnis: Sehr sparsame Posts (vielleicht 1–2 Global-Einträge)
4. Test läuft, aber nicht produktiv nutzbar

**Vorteil:**
- ✅ Sehen wie die Routine arbeitet
- ✅ Können Prompt iterieren

**Nachteil:**
- ❌ Post-Qualität sehr schlecht
- ❌ Europa/Schweiz komplett leer
- ❌ Nicht für echte Nutzung

**Zeitaufwand:** ~5 Min (Ich anpassen)

---

### Option C: Einfach warten

**Wie:**
1. Support-Ticket einreichen
2. Keine weitere Aktion bis Fix

**Vorteil:**
- ✅ Kein Aufwand

**Nachteil:**
- ❌ Keine Posts bis Support-Fix
- ❌ Glossary-Routines sind auch blockiert (parallel-Problem)
- ❌ Längerer Stillstand

---

## 🎯 **Meine Empfehlung**

**Kurzfristig: Option A (Manuelle News)**
- Du hast volle Kontrolle
- Posts sind high-quality
- Lerneffekt für dein Team
- Nur 15 Min/Woche

**Mittelfristig:** Support-Fix sollte in 1–2 Wochen kommen

**Langfristig:** Dann läuft Routine vollautomatisch

---

## Wenn du Option A wählst (Manuelle News)

### Jeden Montag vor 06:00 Zürich:

1. **Sammle News** von diesen 4 Quellen (letzten 7 Tage):

   **Global:**
   - https://www.anthropic.com/news (Claude News)
   - https://openai.com/news (OpenAI/ChatGPT)
   - https://ai.google.dev (Gemini/NotebookLM)
   - https://blog.google/technology/ai/ (Google AI)

   **Europa:**
   - https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai (EU AI Act)
   - https://www.mistral.ai (Mistral, falls interessant)

   **Schweiz:**
   - https://www.edoeb.admin.ch (EDÖB)
   - https://www.swiss-ai.org (ETH/EPFL)
   - https://inside-it.ch (Tech News)

2. **Format:** Für jede News
   ```
   - [Titel](URL)
   - 2–3 Sätze: Was ist passiert?
   - Region: Global / Europa / Schweiz
   ```

3. **Sende an mich** → Ich schreibe den Post

4. **PR Review:** Du prüfst → Ich merge

---

## Beispiel (was der Post aussieht)

```markdown
# KI-Wochenrückblick – KW 36 / 2026

Zeitraum: 1.–7. September 2026

## Global

### Anthropic: Claude 3.6 mit besserer Reasoning
Claude 3.6 wurde veröffentlicht mit verbesserter Chain-of-Thought.
Das verbessert Multi-Step Reasoning für Parking-Forecasting.
Quelle: [Anthropic News](https://www.anthropic.com/news), 5. Sept 2026

... etc
```

---

## Status-Board

| Komponente | Status | Nächster Schritt |
|---|---|---|
| **Cloud Routine #1 (Wochenpost)** | 🔴 BLOCKIERT | Support-Ticket + Fallback A/B/C |
| **Cloud Routine #2 (Migration)** | 🔴 BLOCKIERT | Gleicher Grund (blockierte Quellen) |
| **Cloud Routine #3 (Update)** | 🔴 BLOCKIERT | Gleicher Grund |
| **Glossary-Template** | ✅ Ready | Wartet auf Migration |
| **Network Fix** | ⏳ PENDING | Support-Ticket |

---

## Was willst du machen?

Schreib mir:
1. **Option A** (manuell) → Ich zeige dir das Format
2. **Option B** (test) → Ich passe SOURCES.md an
3. **Option C** (warten) → Nur Support-Ticket

**Oder: Alle drei parallel?** (A jetzt starten, B testen, C im Hintergrund)

---

**Let's Go! 🚀**
