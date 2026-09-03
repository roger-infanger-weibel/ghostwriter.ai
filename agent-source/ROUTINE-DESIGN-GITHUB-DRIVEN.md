# Cloud Routine – Basis-Design (GitHub-driven)

Statt hardcodierte Prompts → Routines lesen ihre Instructions direkt von GitHub.

---

## Design für alle 3 Routines

### Cloud Routine #1: KI-Wochenrückblick
```
Schedule: 0 4 * * 1 (Montag 06:00 CH)
Repository: roger-infanger-weibel/ghostwriter.ai

Instructions:
---
Fetch your task instructions from:
https://raw.githubusercontent.com/roger-infanger-weibel/ghostwriter.ai/main/agent-source/routines/weekly-post.md

Read and execute that content as your complete task.
Also read SOURCES.md and agent-source/CRITERIA.md from the same repo for context.
---
```

**Benefit:**
- ✅ Change prompt → edit GitHub only
- ✅ Routine always uses latest version
- ✅ No copy-paste, no sync issues

---

### Cloud Routine #2: Glossary-Migration (❌ GELÖSCHT)
**Status:** ✅ COMPLETED – Nicht mehr nötig

This was a one-time migration task:
- ✅ Parsed Wiki-Glossary (120 terms parsed, 110 after dedup)
- ✅ Deduplicated (10 duplicates merged)
- ✅ Translated to English
- ✅ Generated terms.yaml + KI-Glossar.md + AI-Glossary.md
- ✅ Merged to main on 2026-09-03

**Why deleted?** Migration is complete. Glossary now lives in `glossary/terms.yaml` (110 terms, 8 categories).

---

### Cloud Routine #3: Glossary-Update (Monatlich)
```
Schedule: 0 6 1 * * (1st of month, 06:00 CH)
Repository: roger-infanger-weibel/ghostwriter.ai

Instructions:
---
Fetch your task instructions from:
https://raw.githubusercontent.com/roger-infanger-weibel/ghostwriter.ai/main/agent-source/routines/glossary-update.md

Read and execute that content completely.
This is a monthly maintenance task:
1. Read glossary/terms.yaml (current state)
2. Scan recent posts/ for new terminology
3. Add/update max 15 entries per run
4. Regenerate KI-Glossar.md + AI-Glossary.md
5. Create PR on branch glossary/YYYY-MM
6. Push and wait for human review
---
```

**Use:** Runs automatically 1st of month → keeps glossary fresh with new terms from posts

---

## Workflow für 2 aktive Routines

```
┌─────────────────────────────────────────────┐
│   Cloud Routines (claude.ai/code/routines)  │
│                                             │
│  1. KI-Wochenrückblick (Mo 06:00 CH)       │
│     ↓ reads from GitHub                    │
│     ├─ weekly-post.md (Instructions)       │
│     ├─ SOURCES.md (Quellenliste)           │
│     └─ CRITERIA.md (Filter-Regeln)         │
│     ↓ creates PR                           │
│     └─ posts/YYYY-Www.md                   │
│                                             │
│  (Routine #2 Migration: GELÖSCHT)          │
│  (Was: einmalige Wiki→YAML Konversion)     │
│  (Status: ✅ Completed, merged 2026-09-03)  │
│                                             │
│  3. Glossary-Update (1st of month 06:00)   │
│     ↓ reads from GitHub                    │
│     ├─ glossary-update.md (Instructions)   │
│     ├─ glossary/terms.yaml (Current)       │
│     └─ posts/ (New terms)                  │
│     ↓ updates & creates PR                 │
│     └─ terms.yaml + KI-Glossar + AI-Glossary
│                                             │
└─────────────────────────────────────────────┘
        ↓ all PRs to review
        └─ You merge
```

---

## Advantages

| Vorteil | Vorher | Nachher |
|---|---|---|
| **Prompt ändern** | Edit Routine in claude.ai | Edit GitHub, Routine auto-reads |
| **Wartbarkeit** | 3x Prompts in 3x Routines | 3x Prompts in 1x Repo |
| **Sync** | Manual (risk: out-of-sync) | Automatic (GitHub = truth) |
| **Versionskontrolle** | No | Yes (git history) |
| **Team-Arbeit** | Difficult | Easy (PRs to update prompts) |

---

## Implementation Checklist

- [ ] Routine #1: Replace Instructions with GitHub fetch
- [ ] Routine #2: Replace Instructions with GitHub fetch  
- [ ] Routine #3: Replace Instructions with GitHub fetch
- [ ] Test each routine with "Run Now"
- [ ] Delete old hardcoded prompts (optional cleanup)
- [ ] Document in README or SETUP.md

---

## Beispiel: Weekly-Post Routine in claude.ai

### Current (hardcoded)
```
Instructions: [1000+ lines of markdown pasted here]
```

### New (GitHub-driven)
```
Instructions:
Fetch and execute:
https://raw.githubusercontent.com/roger-infanger-weibel/ghostwriter.ai/main/agent-source/routines/weekly-post.md
```

**That's it!** Routine reads the rest from GitHub. ✅

---

**Ready to implement?** 🚀
