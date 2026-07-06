---
name: neuro-write
description: >-
  Drafts and revises neuroimaging manuscript sections (Methods, Results,
  Discussion, Abstract, Introduction, Conclusion) in a target journal's style,
  grounded in exemplar papers, using a writer + reviewer-panel loop. Part of the
  neuroscribe plugin. INVOKE EXPLICITLY via the /neuro-write command or when the
  user names "neuroscribe" / "neuro-write". This skill does NOT auto-trigger on
  generic "write my section" requests, so that a user's existing manuscript
  skill remains the default during neuroscribe development.
---

# neuro-write — journal-styled neuroimaging manuscript drafting

A short **router**. It loads a lean, journal-agnostic core plus exactly the
journal fragment and references a given request needs, overlays the user's
runtime venue/project profiles, then runs a writer → reviewers → revise loop.

Read `manifest.yaml` first. Follow these steps in order.

## Step 1 — Load the core
`Read` every path in the manifest's `always_load` (the `_shared` neuroimaging
layer + `static/core/{stance,workflow,style-rules}`). These hold the invariants,
the modality taxonomy, the discipline style tier, and the writing machinery.

## Step 2 — Detect the request
From the user's request determine:
- **journal** (the `journal` axis) — the venue named, else `generic`.
- **section(s)** being written (may be several: abstract / intro / methods /
  results / discussion / conclusion).
- **paper_type** — algorithmic / clinical / methods.

**Echo the detected values back in one line** so the user can cheaply correct
them before drafting (e.g. "Writing: Methods + Results for <the venue you
named>, paper_type = algorithmic — correct?").

## Step 3 — Load only the mapped journal fragment
`Read` the fragment for the detected `journal` value (`generic`, or the
synthetic `example` fixture). No real journal ships as a fragment — a real
venue uses `generic` prose plus its runtime profile overlay (Step 3.5). Do
**not** read every fragment.

## Step 3.5 — Overlay the runtime profiles (the venue's real rules)
The shipped journal fragment is prose guidance; the venue's *declared rules* are
user data outside this plugin. Resolve the overlay:
1. Honor `$NEUROSCRIBE_HOME`; else walk up from the working directory for a
   `.neuroscribe/` directory; else **halt and ask** the user where it is (or to
   create one via `/neuro-venue`). Never guess a path.
2. `Read` `.neuroscribe/journal/<slug>/{venue,format,style}.yaml` (venue rules,
   layout, and the calibrated style profile) and
   `.neuroscribe/project/<name>/project.yaml` (terminology, notation, figure
   plan, placeholder conventions).
3. Treat these as the **highest-priority data**. On any conflict, the declared
   venue profile overrides the shipped fragment; an unstated rule is
   **NOT-CHECKED**, never a guessed default.

If no venue profile exists yet, proceed with the `generic` fragment and tell
the user which rules are running as NOT-CHECKED (they can create a profile via
`/neuro-venue`).

## Step 4 — Apply in priority order
Resolve style by: **discipline tier (HARD) > declared journal profile (STRONG) >
author's personal/style-calibration profile (SOFT, only where no conflict)**.
Keep all numbers grounded (see `neuro-invariants.md`): use `[STAT: …]`,
`[CITE: …]`, `[FIG: N]`, `[TABLE: N]` placeholders; never invent a statistic.

## Step 5 — Load references on demand
Pull a `references.on_demand` file only when its `condition` holds (e.g.
`methods-structure.md` when writing a Methods architecture section;
`grounded-citation-search.md` when grounding citations).

## Step 6 — Write, review, revise
1. Spawn the **`writer`** subagent (Task tool). Pass, in the invocation prompt:
   the section number/title, the outline (what each subsection covers), the data
   to report (as placeholders unless grounded), cross-references, and the loaded
   journal/discipline rules. The writer is a persona — do not assume it can see
   this skill's working directory; give it what it needs in the prompt.
2. Save the draft to a known path, then invoke the review panel (see the
   `neuro-review` skill) on it: the relevant reviewers in parallel + optional
   editor desk-screen.
3. Spawn the writer again with the draft + all critiques to produce a revised
   draft. Stop when reviewers pass, changes are only cosmetic, or after three
   iterations.
4. Hand the user the final draft plus a short summary of what each reviewer
   flagged and what changed.

## Reminders
- **Grounded numbers only** and **declared-never-inferred** journal rules
  (`neuro-invariants.md`).
- Save intermediate drafts under a clear scheme so the history is auditable.
- Don't hide critique from the user.
