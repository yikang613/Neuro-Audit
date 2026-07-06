---
description: Draft or revise a neuroimaging manuscript section with neuroscribe (writer + reviewer-panel loop).
argument-hint: [section + target journal, e.g. "Methods for <your journal>" or "Discussion"]
---

Use the **neuro-write** skill to draft or revise the requested manuscript section.

Request: $ARGUMENTS

Follow the neuro-write router in `skills/neuro-write/SKILL.md`:
1. Load the core (`always_load`).
2. Detect journal / section(s) / paper_type and **echo them back** for confirmation.
3. Load the matched journal fragment, then overlay the runtime `.neuroscribe/`
   venue and project profiles (discovery: `$NEUROSCRIBE_HOME` → walk up → halt
   and ask).
4. Run the writer → reviewer-panel → revise loop, passing the writer everything
   it needs in the invocation prompt.

Keep every number **grounded** (use `[STAT:]`/`[CITE:]`/`[FIG:]`/`[TABLE:]`
placeholders unless the value is in the run-ledger) and every journal rule
**declared, never inferred**.
