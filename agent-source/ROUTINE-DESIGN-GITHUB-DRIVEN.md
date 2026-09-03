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

### Cloud Routine #2: Glossary-Migration (Einmalig)
```
Schedule: Manual "Run Now"
Repository: roger-infanger-weibel/ghostwriter.ai

Instructions:
---
Fetch your task instructions from:
https://raw.githubusercontent.com/roger-infanger-weibel/ghostwriter.ai/main/agent-source/routines/glossary-migration.md

Read and execute that content completely.
This is a one-time migration task:
1. Parse Wiki-Glossary (~350 terms, 8 categories)
2. Deduplicate (10+ known duplicates)
3. Translate to English
4. Generate terms.yaml + KI-Glossar.md + AI-Glossary.md
5. Create PR on branch glossary/migration-YYYY-MM-DD
---
```

**Use:** After initial setup, run "Run Now" once → migrate your entire Wiki glossary

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

## Workflow für alle 3

```
┌─────────────────────────────────────────────┐
│   Cloud Routines (claude.ai/code/routines)  │
│                                             │
│  1. KI-Wochenrückblick (Mo 06:00 CH)       │
│     ↓ reads                                 │
│     ├─ weekly-post.md (GitHub)             │
│     ├─ SOURCES.md (GitHub)                 │
│     └─ CRITERIA.md (GitHub)                │
│     ↓ creates                              │
│     └─ posts/YYYY-Www.md → PR              │
│                                             │
│  2. Glossary-Migration (Manual Run Now)    │
│     ↓ reads                                 │
│     ├─ glossary-migration.md (GitHub)      │
│     ├─ Wiki-Glossary (github.com/wiki)     │
│     └─ 8 categories config                 │
│     ↓ creates                              │
│     └─ terms.yaml + 2x .md → PR            │
│                                             │
│  3. Glossary-Update (1st of month 06:00)   │
│     ↓ reads                                 │
│     ├─ glossary-update.md (GitHub)         │
│     ├─ glossary/terms.yaml (GitHub)        │
│     └─ posts/ (GitHub)                     │
│     ↓ updates                              │
│     └─ terms.yaml + 2x .md → PR            │
│                                             │
└─────────────────────────────────────────────┘
        ↓ all PRs
        └─ You review & merge
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
