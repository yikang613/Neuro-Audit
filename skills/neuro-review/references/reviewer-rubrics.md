# Reviewer rubrics and critique formats (loaded on demand)

The deep material behind the four read-only reviewer personas and the
editor desk-reject screen. The persona files in `agents/` carry the
working instructions; this reference collects the full flag taxonomies,
the calibration ladders, the structured critique output formats, and a
manuscript-wide pre-submission checklist. Load it when a reviewer needs
the detail, or when running a whole-manuscript pass.

Two rules bind every rubric here:

- **Read-only.** Reviewers critique; they never edit the manuscript.
- **Declared, never inferred.** Venue-specific values (abstract limit,
  citation form, figure-reference form, required sections and back
  matter) come from the runtime venue profile. Where the profile is
  silent, report **NOT-CHECKED** rather than guessing a value. General
  neuroimaging conventions come from the `_shared/` discipline style
  tier, modality taxonomy, and terminology ledger; manuscript-specific
  canonical terms and notation come from the runtime project profile.

---

## 1. Style reviewer

**Flag taxonomy**

1. Anti-pattern hits (from the discipline style tier): parenthetical
   numerical breakdowns, inline pseudocode, bullet lists for
   non-enumerable content, factorial-design arithmetic, magic-number
   enumeration, colloquialisms, chained "we did X / we did Y" openers,
   forward figure references.
2. Voice and tense: past/present slips, passive-where-active,
   "I" instead of "we".
3. Sentence rhythm and length: repeated openers, comma splices,
   >40-word sentences. Apply the **paragraph-position rule** — the
   paragraph-final sentence is the highest-risk slot; flag it if it
   exceeds 30 words or joins more than two clauses with "and"/"but"/
   "while".
4. Citation placement: flow-breaking mid-sentence citations, missing or
   over-dense citations. (Citation *form* is venue-declared;
   NOT-CHECKED if unstated.)
5. Acronym hygiene: used before defined; redefined within a section.
6. Numerical reporting: inconsistent decimals, missing units, effect
   sizes without companion p-values.

**Output format**

```
# Style review of {section_id} draft
## Verdict
[pass | minor revision needed | substantive revision needed | major revision needed]
## Anti-pattern hits
## Voice / tense issues
## Sentence rhythm and length
## Citation placement
## Numerical reporting
## Overall impression
```
Each finding: **Location** (paragraph/sentence or quote) · **Issue** ·
**Suggestion**. Use "None observed." for a clean category.

---

## 2. Methodology reviewer

**Flag taxonomy**

1. Missing procedural detail: unspecified hyperparameters; training-
   schedule omissions (epochs, LR schedule, optimizer, weight decay);
   fold composition / CV specifics; statistical-threshold definitions
   (q < 0.05 under which correction?); unstated architectural details.
2. Inconsistency with the Methods section: differing hyperparameters,
   statistical conventions, notation, or fold definitions.
3. Unstated assumptions: which statistic, which model, which averaging.
4. Missing comparator detail: baseline tuning, validation set, fold
   parity.
5. Statistical reporting completeness: SD/CIs on means, effect sizes on
   p-values, explicit n, named multiple-comparison correction.
6. Reproducibility gaps: could a reader clone the experiment on their
   own data?

Where a reported number is load-bearing, treat the project's grounding
ledger as source of truth — a prose statistic with no ledger record is a
reproducibility flag.

**Output format**

```
# Methodology review of {section_id} draft
## Verdict
[pass | minor gaps | substantive gaps | major gaps]
## Missing procedural detail
## Inconsistencies with the Methods section
## Unstated assumptions
## Missing baseline configuration
## Statistical reporting completeness
## Overall impression
```
Each finding: **Location** · **Gap** (what the draft asserts) · **Needs**
(the specific detail to add). Distinguish "detail is missing" (a gap)
from "detail is in Methods, cross-referenced" (not a gap).

---

## 3. Biology / claims reviewer

**Grounded citation verification (anti-hallucination).** For every
load-bearing claim: search → verify the paper exists → check it supports
the claim → recommend. Ground `[CITE: ...]` placeholders against real
literature (web/paper-search tools, then the project reference list).
For "first"/scope/absolute claims, search the exact phrase within a
~5-year window for a counter-example. On tool failure, flag
"unverified, needs user-supplied citation" — never invent a citation.

**Flag taxonomy**

1. Unsupported biological claims — asserted biology/clinical facts that
   are not cited, not supported by the reported data, and not
   field-general enough to skip citation.
2. Overclaims, four categories:
   - **2a Absolutes** ("uniquely", "only", "definitively") → soften to
     "to our knowledge, the first …".
   - **2b Unwarranted causation** — causal verbs on correlational
     evidence → "is associated with (ρ = …, p = …)".
   - **2c Scope expansion** — generalising beyond the tested
     population/modality/disease → bound to what was evaluated.
   - **2d Unverified "first" claims** → prefer "to our knowledge" over a
     bare "first".
   - **Model-discovery overclaim** — attributing to the *trained model*
     a property that belongs to the *data* or to *predefined input
     structures* (ROIs, atlas regions, circuits). E.g. "the model
     discovered region X as a novel biomarker" when X was a predefined
     ROI → "the model's region-level ablation identified region X — a
     predefined ROI — as a top contributor to classification".
3. **Hedging ladder** (match verb to evidence):
   - replicated / multi-cohort → *demonstrate, show, establish*
   - direct, single-cohort → *reveal, indicate, find*
   - correlational → *be associated with, correlate with, track*
   - moderate + interpretive → *suggest, point to, are consistent with*
   - speculative → *may, could, might reflect*
   - future-directional → *could enable, might allow*
   Reserve "demonstrate"/"show" for robust, ideally replicated results;
   never "prove". Flag both over- and under-hedging.
4. **Effect-size adjective calibration**:
   - ρ ≈ 0.10-0.20 → "modest" / "small but consistent"
   - ρ ≈ 0.20-0.40 → "moderate"
   - ρ ≈ 0.40-0.60 → "substantial"
   - ρ > 0.60 → "strong"
5. Narrative consistency — the framing promised in the Introduction must
   be the one the Results and Discussion deliver.
6. Discussion-only claims — anything in the Discussion with no anchor in
   the Results.

**Output format**

```
# Biological / claims review of {section_id} draft
## Verdict
[pass | minor revision needed | substantive revision needed | major revision needed]
## Unsupported biological claims
## Overclaim — Absolutes
## Overclaim — Unwarranted causation
## Overclaim — Scope expansion beyond what was tested
## Overclaim — Unverified "first" claims
## Overclaim — Model-discovery confusion
## Hedging-ladder violations
## Effect-size adjective mismatch
## Narrative consistency
## Discussion-only claims (Discussion sections only)
## Overall impression
```
For claims: **Location** · **Claim** · **Needs** · **Suggested citation**
(grounded, or "unverified, needs user-supplied citation"). For hedging:
**Location** · **Verb used** · **Evidence type** · **Appropriate verb**.

---

## 4. Coherence reviewer

**Flag taxonomy**

1. Terminology inconsistency — deviations from the project profile's
   canonical terms (central-concept name, modality/tissue spelling,
   ordered input-condition labels) or the `_shared/` terminology ledger.
2. Notation inconsistency — symbols must match those defined in Methods
   (mirrored in the project notation glossary); flag reused or newly
   invented symbols for existing quantities.
3. Numerical inconsistency — cohort sizes vs. the demographics table,
   metrics vs. the benchmark table, ρ / effect sizes vs. the section
   that first reported them.
4. Figure/table placeholder validity — every `[FIG: ...]` / `[TABLE:
   ...]` resolves to an object and panel in the inventory; no
   missing-from-inventory, wrong-panel, literal-not-placeholder,
   out-of-order, or expected-but-not-cited issues.
5. Acronym-definition consistency — defined once, used thereafter.
6. Cross-section narrative consistency — Discussion interprets Results
   without introducing new empirical facts.
7. Citation-key consistency — one paper, one `[CITE: ...]` placeholder.

**Output format**

```
# Coherence review of {section_id} draft
## Verdict
[pass | minor inconsistencies | substantive inconsistencies | major inconsistencies]
## Terminology inconsistencies
## Notation inconsistencies
## Numerical inconsistencies
## Figure / table placeholder validity
## Acronym hygiene
## Cross-section narrative consistency
## Citation-key consistency
## Overall impression
```
Terminology findings: **Location** · **Used** · **Canonical** ·
**Reference**. Figure/table findings: **Location** · **Issue** ·
**Inventory entry** · **Suggested fix**.

---

## 5. Editor desk-reject screen

Manuscript-level, not section-level. Criteria, each scored PASS /
CONCERN / FAIL (or NOT-CHECKED where the venue profile is silent):

1. **Scope fit** — against the venue profile's declared scope statement.
2. **Novelty claim** — the named contribution is materially distinct
   from the nearest published works.
3. **Significance / clinical relevance** — a real "so what".
4. **Methodology adequacy** — baselines, evaluation protocol, cohort
   reporting, reproducibility statements.
5. **Presentation quality** — figures, tables, abstract within the
   declared limit, declared section order.
6. **Submission-form completeness** — the elements the venue declares as
   required (highlights, author contributions, data/code availability,
   competing interests, funding, AI declaration, compilable references).
7. **Reviewer-readiness** — Send to peer review / Conditional revision /
   Desk reject.

Output: verdict + one-line justification; the criterion table; an
ordered pre-peer-review action list ([HIGH]/[MEDIUM]/[LOW]); strengths
for the cover letter; risks to flag to peer reviewers. The editor does
not verify citations, recompute statistics, or rewrite prose.

---

## 6. Manuscript-wide pre-submission checklist

Run after all sections pass section-level review and before assembling
the final submission. Catches manuscript-wide issues that section-level
review misses. Values marked "(venue)" come from the declared venue
profile; if unstated, mark the item NOT-CHECKED.

**Completeness**
- [ ] Title page: full author list, affiliations, corresponding author.
- [ ] Abstract within the declared word limit (venue); keywords listed
      (venue count if declared).
- [ ] Section and subsection numbers sequential with no gaps.
- [ ] Every figure/table number matches its inline references and is
      referenced at least once.
- [ ] Equation numbers sequential.
- [ ] Every citation resolves to a reference-list entry; no `[CITE: …]`
      placeholders remain.
- [ ] No `<!-- TODO … -->` or planning markers remain.

**Numerical consistency**
- [ ] Performance metrics in the body match the benchmark table.
- [ ] Cohort sizes match the demographics table.
- [ ] Correlation ρ / effect sizes consistent between Results and
      Discussion.
- [ ] Statistical thresholds stated consistently (e.g. BH-FDR q < 0.05).
- [ ] Sample sizes (n) reported wherever a statistical claim depends on
      them.
- [ ] Every reported statistic traces to a grounding-ledger record.

**Style and terminology**
- [ ] First-person plural throughout body prose.
- [ ] Tense conventions respected (past for what was done, present for
      what the method is).
- [ ] Canonical terms (project glossary) used consistently; input
      conditions in canonical order.
- [ ] Acronyms defined on first use, not redefined.
- [ ] No anti-patterns remain (numerical breakdowns, inline pseudocode,
      magic-number enumeration, colloquialisms).
- [ ] No forward figure references.

**Biological / clinical claims**
- [ ] Every biological claim cited or supported by reported results.
- [ ] No model-discovery overclaims — claims are about what the trained
      model relies on, not what it "discovered" among predefined inputs.
- [ ] Effect-size adjectives calibrated to actual magnitudes.
- [ ] Causal language reserved for causal results; correlational results
      described as "associated with".

**Figures and tables**
- [ ] All figures are final versions, not preliminary drafts.
- [ ] Captions begin with the content noun phrase (not "Fig. N shows…").
- [ ] Panel markers explained; table captions placed per venue rule.
- [ ] Self-reference label used consistently in comparison tables.
- [ ] Best result per column highlighted; table rule style per venue.

**Reproducibility**
- [ ] All hyperparameter values stated somewhere in the manuscript.
- [ ] Statistical procedures named with specific tests and corrections.
- [ ] Data sources cited with the required data-use / compliance
      statements.
- [ ] Code availability stated if the repository is public.

**Cross-section coherence**
- [ ] Each stated contribution is tested by an experiment and discussed.
- [ ] The Discussion's "principal findings" recap matches the Results.
- [ ] The limitations paragraph addresses dataset size, single-cohort
      evaluation, and modest effect-size magnitudes where applicable.
- [ ] The Conclusion introduces no new claims.
- [ ] The Abstract's headline numbers match the benchmark table.

**Final read-through**
After the above pass, read the assembled manuscript end-to-end once, for
issues only a full read catches: topic-sentence repetition, a claim made
twice with subtly different phrasings, two figures showing the same
thing, a Discussion paragraph that does not earn its place.
