# neuro-write orchestration

neuro-write drafts and revises one manuscript section at a time through a
writer → review-panel → revise loop. The orchestrating Claude (you, when this
skill is triggered) spawns the sub-agents and weaves their outputs together.
The user sees the polished section, plus a short summary of what the panel
flagged — not the intermediate machinery.

This file is self-contained: neuro-review carries its own copy of the review
panel for standalone critique of prose the user already has.

## Phases per section

```
   caller request (section id, outline, data, cross-refs, venue, project)
        │
        ▼
   ┌─────────┐   reads:  stance + style-rules + methods-structure +
   │ WRITER  │           figure-discipline + resolved venue fragment +
   └────┬────┘           project glossary + adjacent sections + inventory
        │       writes: draft section
        ▼
   ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐
   │  STYLE   │ │  METHOD  │ │ BIOLOGY  │ │COHERENCE │   (review panel,
   └────┬─────┘ └────┬─────┘ └────┬─────┘ └────┬─────┘    launched in parallel)
        └────────────┴────────────┴────────────┘
                          │  critiques
                          ▼
                    ┌─────────┐
                    │ WRITER  │   reads: draft + all critiques
                    └────┬────┘   writes: revised section
                         │
                         ▼
                 (optional second review pass if the revision was substantive)
                         │
                         ▼
              hand polished section + panel summary to the user
```

## Phase 1 — brief the writer

Spawn one `writer` sub-agent. Give it, in the Task prompt, the section id and
title, target length, outline, the data to report (grounded numbers only — from
the run-ledger / captured tool-calls), the cross-references, the adjacent-section
context, the resolved core rule files and venue fragment, the project glossary,
and the figure/table inventory. The writer runs the `stance` intake, then drafts.

Save the draft to a known path under a clear naming scheme (e.g.
`04_experiments.draft1.md`) so the panel can read it and the history is
auditable.

## Phase 2 — spawn the review panel in parallel

In a single message with multiple Task invocations, launch the review
dimensions relevant to the section (see the weighting table below). The panel
is independent, so it runs concurrently. The four dimensions:

- **Style** — voice, tense, hedging/overclaim calibration, and the
  anti-pattern taxonomy (parenthetical numeric breakdowns, inline pseudocode,
  magic-number enumeration, "we did X/Y/Z" runs, bullet abuse, colloquialisms).
- **Method** — reproducibility: is every procedural choice described in enough
  detail for a competent reader to reproduce it? Flags missing hyperparameters,
  fold composition, statistical thresholds; checks consistency with the
  existing Methods section.
- **Biology / claims** — every biological or clinical claim is either supported
  by a cited reference or by the reported results; flags overclaims and
  attributes-of-the-data mislabelled as findings-of-the-model.
- **Coherence** — terminology and notation match the rest of the manuscript,
  figure/table references are in order and point at real inventory objects, and
  no claim contradicts one elsewhere.

Each reviewer returns a structured critique: a top-line verdict (pass / needs
revision / major revision) followed by paragraph- or line-level pointers. Treat
the verdict label as noise and the surfaced issues as the signal.

Reviewers also read the resolved venue fragment and the inventory before
critiquing, because several common findings — abstract-length overruns, wrong
figure-reference form, section-numbering drift, mixed language variant, dangling
figure references — are direct violations of the venue profile or the inventory.

## Phase 3 — revise

Spawn the writer again with the draft plus every critique. It produces a revised
draft addressing each issue, flagging any point where two reviewers traded off
(style vs. method completeness occasionally conflict). This revised draft is
usually what the user sees.

## Phase 4 — optional second review pass

If Phase 3 rewrote more than ~30% of the paragraphs, run one more panel pass to
confirm convergence. If the revision was minor (tightening, typo fixes), skip to
delivery.

## Stopping criteria

End the loop when any one holds:

- The panel reports "pass" on the latest draft across its dimensions.
- The revision is making only stylistic adjustments, no substantive change.
- Two consecutive iterations produce near-identical drafts.
- Three iterations have run (hard cap to avoid runaway).

## Section-specific reviewer weighting

Not every section needs every dimension. Weight the panel:

| Section              | Style | Method | Biology | Coherence | Notes                                            |
|----------------------|:-----:|:------:|:-------:|:---------:|--------------------------------------------------|
| Abstract             |   ●   |        |    ●    |     ●     | Skip method; watch coherence with the body.      |
| Introduction         |   ●   |        |    ●    |     ●     | As Abstract.                                     |
| Methods              |   ●   |   ●    |         |     ●     | Method completeness is paramount.                |
| Experimental setup   |   ●   |   ●    |         |     ●     | Method + coherence load-bearing.                 |
| Main results         |   ●   |   ●    |         |     ●     | Watch for overclaim in the narrative.            |
| Ablation             |   ●   |   ●    |         |     ●     | Method reviewer critical.                        |
| Interpretability     |   ●   |   ●    |    ●    |     ●     | All four; biology especially.                    |
| Discussion           |   ●   |        |    ●    |     ●     | Biology is the main check here.                  |
| Conclusion           |   ●   |        |    ●    |     ●     | Concise, claim-bounded, like the Abstract.       |

## Operating reminders

- **Run the panel in parallel** — one message, multiple Task calls. Faster than
  serial, and the perspectives stay independent.
- **Save intermediate drafts** under a clear naming scheme so the history is
  auditable.
- **Do not hide critique.** Deliver the final draft with a short summary of what
  the panel flagged and what changed — it builds trust and lets the user catch a
  reviewer blind spot.
- **Read manuscript context first.** Continuity with already-written sections
  matters more than absolute adherence to a venue convention.
- **Defer citations to the user.** Use `[CITE:]` placeholders; never guess a
  BibTeX key or an author–year string.
- **Ground every number.** Numbers come from the run-ledger / tool-calls, not
  from the writer's memory.
