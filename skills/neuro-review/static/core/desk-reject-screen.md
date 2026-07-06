# Editor desk-reject screen — when and how

The desk-reject screen is a **manuscript-level** pass run by the
`editor` persona (in the plugin's `agents/`). It answers a
different question from the four peer reviewers: not "is this paragraph
good?" but "would a handling editor send this manuscript to peer review
at all, or return it first?"

## When to run it

Run the editor screen when the caller is screening a **whole assembled
manuscript** — for example a submission-readiness check, a mock desk
review before submitting, or a triage of a manuscript the caller did not
write. Do **not** run it on a single mid-draft section; the four
reviewers cover section-level critique.

Run it **in addition to** the reviewer panel, not as a substitute. The
editor screens scope, novelty, significance, methodology adequacy,
presentation, and submission-form completeness at editor altitude; the
panel does the fine-grained per-section critique. They are orthogonal.

## How to run it

Spawn the `editor` persona once, giving it:

- the manuscript prose in order (title through conclusion),
- the back matter (data/code availability, author contributions,
  funding, competing interests, AI declaration),
- the highlights / plain-language summary if the venue requires one,
- the figure/table inventory,
- the **venue profile** — the editor reads its declared scope statement,
  abstract limit, required section order, and required submission-form
  elements. For any rule the profile does not declare, the editor marks
  that check NOT-CHECKED rather than guessing.

The editor does **not** verify citations or recompute statistics (that
is the methodology reviewer's job) and does **not** rewrite the
manuscript. It returns one of three verdicts — **Send to peer review**,
**Conditional revision before peer review**, or **Desk reject** — with a
criterion-by-criterion PASS / CONCERN / FAIL / NOT-CHECKED table and an
ordered pre-peer-review action list. The full output format is defined
in the `editor` agent.
