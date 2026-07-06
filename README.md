<!-- Badges (wire up once the GitHub repo exists):
[![eval-gate](https://github.com/CHANGE-ME/neuroscribe/actions/workflows/eval-gate.yml/badge.svg)](../../actions)
![license](https://img.shields.io/badge/license-Apache--2.0-blue)
-->

# neuroscribe

**An AI-agent _auditor_ for neuroimaging manuscripts.** It grounds every
statistic in your paper to a real, captured tool-call — so a number can never
be hallucinated or silently drift from the code that produced it.

I built neuroscribe after I nearly shipped a **seed-fold provenance bug** in my
own paper: a cross-validation number in the draft no longer matched the code
that generated it, and three rounds of human proofreading missed it. neuroscribe
is the reviewer I wish I'd had. It refuses to write a number it can't trace to a
tool call, flags data leakage and biological overclaim, and enforces journal
rules that are **declared, never guessed**.

It **complements** neuroimaging pipeline _runners_ (NeuroClaw, NeuroAgent,
NEURA): they _produce_ results; neuroscribe _audits them and writes them up_ to
journal standard. It is the missing rigor-and-writing layer, **not another
runner**.

> **Status:** early build (v0.0.1). v1.0 ships the defensible core —
> `neuro-write`, `neuro-review`, `neuro-rigor`. See
> [the plan](#roadmap) and [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md).

<!-- [architecture diagram] · [75s demo] · [why an agent, not a script] · [evals] — added with v1.0 -->

## What it does

| Stage | Skill | What it does |
|---|---|---|
| Write | `neuro-write` | Drafts manuscript sections in a target journal's style, grounded in exemplar papers you provide. |
| Review | `neuro-review` | A panel of independent reviewer agents (style, methodology, biological-claims, coherence) + a desk-reject editor screen. |
| **Audit** | **`neuro-rigor`** | The differentiator: flags data leakage, harmonization/site confounds, circular analysis, effect-size inflation, and "the model discovered X" overclaim — grounding every statistic in a captured tool-call. |
| Venue | `neuro-venue` | Builds a reusable journal profile from the venue's public guidelines + your exemplars. Declared-never-inferred. _(v1.1)_ |
| Preprocess | `neuro-preprocess` | Documents and QC-checklists a preprocessing pipeline for the Methods section. Scaffolds, never runs, the pipeline. _(v1.1)_ |
| Literature | `neuro-litscan` | Neuroimaging-framed literature scan + exemplar harvest. _(v1.2)_ |

## Design principles

- **Grounded, not asserted.** A companion MCP server computes statistics and
  records each as `{value, ci, n, seed, input_hash, code_version}`; a
  `PreToolUse` hook blocks any manuscript write containing a number that isn't
  in that ledger. The agent _cannot_ write an ungrounded stat.
- **Declared, never inferred.** Journal rules (word limits, citation style,
  required sections) are recorded only from values you state or confirm —
  neuroscribe never guesses a limit from a journal's name.
- **Public framework, private content.** The framework is Apache-2.0 and open;
  your exemplar PDFs and unpublished manuscript content stay in a private,
  never-committed overlay (see [`NOTICE`](NOTICE)).
- **Specialize, don't reinvent.** The moat is neuroimaging domain knowledge (the
  rigor pitfall catalog, atlas/modality conventions), not generic audit
  machinery.

## Roadmap

- **v1.0** — `neuro-write` + `neuro-review` + `neuro-rigor` (evaluated, CI-gated).
- **v1.1** — `neuro-venue` (runtime journal profiles) + `neuro-preprocess`.
- **v1.2** — `neuro-litscan` + public release.

## Install

_Not yet published. Once released:_

```
/plugin marketplace add CHANGE-ME/neuroscribe
/plugin install neuroscribe@neuroscribe
```

## License

Apache-2.0 (framework). See [`LICENSE`](LICENSE) and [`NOTICE`](NOTICE) for the
public-framework / private-content boundary.
