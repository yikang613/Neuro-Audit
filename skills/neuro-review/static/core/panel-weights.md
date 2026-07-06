# Section → reviewer weighting

Different manuscript sections need different reviewers. Use this table to
select which of the four read-only reviewer personas fire for a given
section, and which one carries the load. A `●` means the reviewer should
run for that section; the Notes column names the load-bearing check.

Section names are generalised — map the manuscript's actual headings
onto the closest row (e.g. a "Benchmark comparison" section maps to Main
Results; a "Model architecture" section maps to Methods).

| Section             | Style | Method | Biology | Coherence | Notes                                                        |
|---------------------|:-----:|:------:|:-------:|:---------:|--------------------------------------------------------------|
| Abstract            |   ●   |        |    ●    |     ●     | Style + biology + coherence with the body. Skip method.      |
| Introduction        |   ●   |        |    ●    |     ●     | Same as Abstract.                                            |
| Methods             |   ●   |   ●    |         |     ●     | Method completeness is paramount; biology less central here. |
| Experimental Setup  |   ●   |   ●    |         |     ●     | Method + coherence are the load-bearing checks.              |
| Main Results        |   ●   |   ●    |         |     ●     | Watch for overclaim in the results narrative.                |
| Ablation            |   ●   |   ●    |         |     ●     | Method reviewer is critical.                                 |
| Interpretability    |   ●   |   ●    |    ●    |     ●     | All four reviewers. Biology especially.                      |
| Discussion          |   ●   |        |    ●    |     ●     | Biology is the main load-bearing reviewer here.              |
| Conclusion          |   ●   |        |    ●    |     ●     | Like the Abstract — concise, claim-bounded.                  |

Notes on use:

- **Style and coherence fire for every section.** Prose quality and
  cross-section consistency are always in scope.
- **Method fires wherever procedure is asserted** (Methods, Setup,
  Results, Ablation, Interpretability) — anywhere a reader would need
  enough detail to reproduce.
- **Biology fires wherever a claim is interpreted** (Abstract, Intro,
  Interpretability, Discussion, Conclusion) — anywhere the prose moves
  from what was measured to what it means.
- **Interpretability is the only "all four" section**, because it makes
  procedural, biological, and cross-section claims at once.

The weighting selects *which* reviewers run; the depth each applies is
in `../../references/reviewer-rubrics.md`.
