---
description: Review a neuroimaging manuscript section with the neuroscribe reviewer panel (style, methodology, biology, coherence) + optional editor screen.
argument-hint: [path or pasted draft, and the section, e.g. "review my Discussion"]
---

Use the **neuro-review** skill to run the reviewer panel over the supplied draft.

Request: $ARGUMENTS

Follow the neuro-review router in `skills/neuro-review/SKILL.md`:
1. Load the core (`always_load`).
2. Detect the section(s), use `panel-weights.md` to select which reviewers fire,
   and **echo the selection back**.
3. Overlay the runtime `.neuroscribe/` venue + project profiles so reviewers
   check against the **declared** venue rules (unstated → NOT-CHECKED).
4. Spawn the selected reviewers **in parallel**; optionally run the editor
   desk-reject screen.
5. Present a consolidated report: per-reviewer verdict + prioritized issues.

Reviewers are read-only — they critique, never edit.
