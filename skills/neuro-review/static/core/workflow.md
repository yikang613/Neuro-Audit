# neuro-review — review-panel orchestration

This is the standalone orchestration for the review panel: given a draft
section (or a whole manuscript) plus its manuscript context and the
runtime venue/project profiles, spawn the relevant reviewer agents in
parallel, collect their structured critiques, optionally run the editor
desk-reject screen, and summarise. The panel **critiques** — it never
edits the manuscript. Revision is the author's job (or `neuro-write`'s);
re-review a revised draft only when the caller supplies one.

## Inputs the caller provides

- The **draft** under review (a section, or the assembled manuscript).
- The **manuscript context** — the other sections, the reference list,
  and the figure/table inventory (paths).
- The **venue profile** (runtime journal profile) and **project
  profile** (runtime terminology/notation glossaries), if available.
  Reviewers read declared rules from these; where a rule is unstated
  they report NOT-CHECKED rather than guessing.
- The `_shared/` layer (loaded by the manifest) supplies the
  neuroimaging modality taxonomy, the terminology ledger, and the
  discipline style tier that reviewers consult by default.

## Phase 1 — Select the panel

Decide which reviewers fire for this draft using
`panel-weights.md` (the section→reviewer weighting table). Not every
section needs all four; e.g. the Abstract skips the methodology
reviewer, Methods skips the biology reviewer. Selecting the relevant
subset keeps each run focused.

The four reviewer personas live in the plugin's `agents/`:

1. **reviewer_style** — voice, tense, anti-patterns (parenthetical
   numerical breakdowns, inline pseudocode, magic-number enumeration,
   chained "we did X / we did Y" openers, bullet abuse), sentence
   rhythm, citation placement, acronym hygiene, numerical reporting.
2. **reviewer_method** — whether every procedural choice is described
   in enough detail to reproduce; missing hyperparameters, fold
   composition, statistical thresholds; consistency with the Methods
   section.
3. **reviewer_biology** — every biological/clinical claim supported by
   a citation, by the reported results, or by accepted domain
   knowledge; grounded citation verification against real literature;
   overclaims, hedging-ladder violations, effect-size adjective
   calibration; the model-discovery overclaim.
4. **reviewer_coherence** — terminology, notation, numerical claims,
   figure/table placeholders, and narrative consistent with the rest of
   the manuscript and the project glossaries.

## Phase 2 — Spawn the selected reviewers in parallel

In a **single message with multiple Agent invocations**, launch the
reviewers selected in Phase 1. They are independent, so parallel launch
is meaningfully faster and gives independent perspectives. Give each
reviewer:

- the path to the draft,
- the paths to the manuscript context it needs (Methods, Introduction,
  other sections, reference list, figure/table inventory),
- the venue and project profile locations,
- the section id for the report header.

Each reviewer returns a structured Markdown critique with a top-line
verdict followed by paragraph- or sentence-level pointers. The exact
per-reviewer output formats and rubrics are in
`../../references/reviewer-rubrics.md`.

## Phase 3 — (Optional) editor desk-reject screen

When the caller is screening a whole assembled manuscript (not a single
section mid-draft), also run the **editor** persona. See
`desk-reject-screen.md` for when and how. The editor screen is an
orthogonal, manuscript-level pass — run it before or alongside the panel,
not as a substitute for it.

## Phase 4 — Collect and summarise

Weave the reviewer outputs together for the caller:

- Lead with each reviewer's top-line verdict.
- Group the concrete findings by reviewer, preserving their locations
  and suggested fixes.
- Flag any place where two reviewers disagree (style vs. methodology can
  occasionally trade off) so the author can adjudicate.
- Do **not** hide critique or silently resolve it — surface it so the
  author can catch reviewer blind spots.

If the caller hands back a revised draft, re-run the relevant subset on
the new draft and report convergence.

## Stopping criteria

Stop iterating the panel when any one of these is true:

- All firing reviewers report a "pass" verdict on the latest draft.
- The only remaining changes are stylistic adjustments with no
  substantive content change.
- Two consecutive iterations have produced near-identical drafts.
- Three iterations have completed (a hard cap to avoid runaway).

When you stop, hand the result to the caller with a short summary of
what each reviewer found on the first pass and what changed in response.

## Invariants

- **Read-only reviewers.** Every reviewer persona critiques; none edits
  the manuscript. This is a hard invariant.
- **Declared, never inferred.** Reviewers apply the venue profile's
  declared rules; for any unstated rule they report NOT-CHECKED.
- **Parallel by default.** Fire the selected reviewers in one message.
- **Save intermediate critiques.** Persist each round's critiques under
  a clear naming scheme so the caller can audit the history.
