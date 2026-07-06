# Grounded-citation search protocol (anti-hallucination)

Purpose: ground every `[CITE:]` placeholder in a real, verifiable reference —
or leave it unresolved for the user. A fabricated citation is worse than a bare
placeholder. This protocol governs how the writer and the biology/claims
reviewer use search tools to attach a real paper to a claim.

This protocol is about **references**, not **numbers**. Statistics come only
from the project's results (the run-ledger / captured tool-calls) and are never
searched for or guessed. Do not use this protocol to source a number.

## When it fires

A load-bearing biological, clinical, or methodological claim needs a reference
and you cannot recall a *specific* paper you are confident exists. General
common-knowledge statements do not need this; genuinely load-bearing assertions
that a reviewer would demand a citation for, do.

## Tools

- `WebSearch` and `WebFetch` (or the workspace web-fetch) for the open
  literature.
- Hugging Face paper search where available (`paper_search`, `hf_doc_search`).

## Protocol

1. **Search before writing the placeholder.** Query for a paper that actually
   supports the specific claim — not merely one in the same topic area.
2. **Verify the hit is real and on-point.** Confirm the title, first author,
   venue, and year resolve to an actual paper (a DOI or a stable record), and
   that its findings support *this* claim, not a neighbouring one. Discard hits
   you cannot verify.
3. **Encode the hit as a hint, keep the placeholder.** If a paper clearly
   supports the claim, write `[CITE: short-description, ~FirstAuthor Year]`. The
   `~` marks it as a *suggestion to verify*, not a confirmed citation.
4. **If nothing verifiable is found**, fall back to the plain
   `[CITE: short-description]` form. A missing citation is a task for the user,
   not a prompt to invent one.

## Hard rules

- **Never** invent a BibTeX key or an author–year string.
- **Never** copy a citation from search results into the prose as if it were
  confirmed. The `[CITE: …]` placeholder always remains; the user makes the
  final call and inserts the real key.
- **Never** cite a paper you have not verified exists — no "it is likely that
  someone showed…" attributions.
- Prefer primary sources over reviews when the claim is a specific empirical
  result; prefer a well-cited authoritative reference over an obscure preprint
  when either would serve.
- The rendered citation form (author–year vs. numeric) is the venue's business,
  not yours — the placeholder is form-neutral and the build resolves it.

## Reviewer use

The biology/claims reviewer applies the same protocol in reverse: for each
load-bearing claim, check that a `[CITE:]` placeholder is present and, where it
can, suggest the specific verified `~FirstAuthor Year` that best supports the
claim — or flag the claim as unsupported if no such reference can be grounded.
