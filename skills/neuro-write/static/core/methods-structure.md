# Methods structure: per-component template + structural scorecard

Use this when drafting or revising a Methods *architecture* section, so each
component reads like a published layer description rather than an AI-generated
wall of detail. The conventions are drawn from the structural habits of strong
brain-network methods sections; calibrate against the venue exemplars supplied
at runtime (see `references/exemplar_patterns.md`), which show these habits in a
concrete paper.

## The §X.1 "Overview" = a problem→component roadmap (not a data-flow list)

Introduce each component by the limitation it removes, in parallel structure,
tied to the paper's thesis: "Standard X does Y, which has limitation Z; we
therefore add component C that …". A strong overview reads as a chain of such
statements — "we have two goals: on the one hand …; we first propose A, which
…; meanwhile we propose B …; on the other hand … we propose C …". A pure
"self-attention → pool → readout" data-flow recital is the AI failure mode here.

## Per-component 4-beat template (one numbered subsection per component)

Every component subsection follows the same four beats, in order:

1. **Problem** (*the why*, 1–2 sentences) — the limitation of the standard or
   prior approach this component removes (e.g. "instead of applying the same
   weights to every node", or "the a priori division of regions is too
   stereotypical"). The *why* precedes the *what*.
2. **High-level role** (1 sentence, before any math) — what the component does,
   conceptually, to address the problem.
3. **Mechanism** (equations + prose) — track ONE central object through every
   equation ("what does X become here?"). Number display equations and reference
   them as "Eq. (N)" (consecutive numbering). Give symbol intuition only where
   non-obvious. Give explicit dimensions for (a) learnable parameter matrices
   and (b) tensors that change shape along the pipeline — this is part of
   tracking the central object. Don't size scalars or unchanged quantities. Keep
   one matrix convention (e.g. node-mixing matrices left-multiply, feature
   transforms right-multiply: $Mz$ vs $zW^{\top}$).
4. **Why this design** (1–2 sentences, ties back to beat 1) — prefer a CONCRETE
   or quantified benefit (e.g. "reduces the learnable parameters to K·d·d + N·K
   while still assigning a separate kernel per region"), not an abstract slogan.
   End by handing off to the next component.

## Run-in labels (optional but high-leverage)

Bold run-in paragraph labels make the structure scannable. Two accepted styles
(author's choice — a venue that requires numbered subsections and puts any
*subsection heading* on its own line does not constrain these in-paragraph
lead-ins):

- **Function labels**: "**Overview.**" (beats 1–2) + "**Design.**" (beats 3–4).
  Best for a single-mechanism component.
- **Component-name labels**: "**Region Activation Zone:**". Best when a
  component has several distinct named sub-parts.

## Calibration: beginner-followable ≠ exhaustive

Explain the paper-specific and non-obvious — the central-object flow, the novel
mechanism, fixed-vs-learnable parameters. SKIP standard primitives every deep-
learning reader knows (query/key/value, softmax, LayerNorm, GELU, convolution —
name them, don't define them) and don't re-define objects defined earlier.
Over-explaining commodity knowledge reads as padding.

## Methods structural scorecard (content-agnostic)

Score a draft to turn a vague quality feeling into "X/10 + exactly which to fix".

| # | Property |
|---|----------|
| 1 | Each component opens with its problem (why before what) |
| 2 | Each states the high-level role before the math |
| 3 | Each mechanism tracks one central object through the equations |
| 4 | Each closes with an explicit, concrete "why this design" tied to the problem |
| 5 | §X.1 overview is a problem→component roadmap (not a data-flow list) |
| 6 | Parallel structure / run-in labels make the beats visible |
| 7 | Components tie back to the Introduction's contributions / thesis |
| 8 | Display equations numbered consecutively and referenced as "Eq. (N)" |
| 9 | One named component per subsection |
| 10 | No anti-patterns (noun-piles, dry parameter soup, fragmented "where: …is…", magic numbers, over-explained primitives) |

Score each as satisfied / partial / missing. This is the Methods card of a
planned per-section scorecard set (Abstract / Introduction / Results /
Discussion to follow).
