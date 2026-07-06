---
name: neuro-review
description: >-
  Runs a panel of independent reviewer agents (style, methodology, biological
  claims, coherence) plus an optional desk-reject editor screen over a
  neuroimaging manuscript section or draft, and returns structured critiques.
  Part of the neuroscribe plugin. INVOKE EXPLICITLY via the /neuro-review command
  or when the user names "neuroscribe" / "neuro-review". It does NOT auto-trigger
  on generic "review my draft" requests during neuroscribe development. Usable
  standalone on an externally-written draft, or as the review step of neuro-write.
---

# neuro-review — independent reviewer panel + editor screen

A short **router**. It loads the panel machinery, decides which reviewers a given
section needs, overlays the user's declared venue rules, spawns the reviewers in
parallel, and synthesizes their critiques. Reviewers are **read-only** — they
critique, never edit.

Read `manifest.yaml` first. Follow these steps.

## Step 1 — Load the core
`Read` the manifest's `always_load` (invariants, discipline style tier,
terminology, `static/core/{workflow,panel-weights}`).

## Step 2 — Detect the section(s) and select reviewers
Determine which section(s) are under review. Use `panel-weights.md` to decide
which of the four reviewers fire for each section (e.g. Methods → style +
methodology + coherence; Discussion → style + biology + coherence). **Echo the
selection back** in one line so the user can correct it.

## Step 3 — Overlay the runtime profiles
Resolve `.neuroscribe/` (`$NEUROSCRIBE_HOME` → walk up → halt and ask) and
`Read` the venue + project profiles. Reviewers check the draft against the
**declared** venue rules (abstract limit, citation style, required sections);
an unstated rule is **NOT-CHECKED**, never a guessed default.

## Step 4 — Spawn the panel in parallel
In a single message, spawn the selected reviewer subagents (Task tool):
`reviewer_style`, `reviewer_method`, `reviewer_biology`, `reviewer_coherence`.
Pass each: the draft, the section context, and the loaded discipline + venue
rules. Each returns a structured critique with a top-line verdict.

Optionally (pre-submission), also run the **`editor`** desk-reject screen — load
`static/core/desk-reject-screen.md` and spawn the `editor` agent for a
scope/novelty/significance/methodology/presentation/completeness verdict.

## Step 5 — Synthesize
Collect the critiques, note where reviewers agree vs disagree, and present the
user a consolidated report: per-reviewer verdict + the prioritized issues. Do
not hide critique. If invoked by `neuro-write`, return the critiques for the
writer's revision pass.

## Reminders
- Reviewers are read-only personas; they never edit the manuscript.
- Run reviewers **in parallel** (one message, multiple Task calls).
- Every biological/clinical claim must be citation-supported or results-supported
  (the biology reviewer's job); numbers must be grounded (the methodology
  reviewer flags unverifiable stats).
