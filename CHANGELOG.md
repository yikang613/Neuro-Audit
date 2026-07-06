# Changelog

All notable changes to neuroscribe are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/), and the project aims to follow
[Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added
- **Phase 0 — scaffold.** Plugin packaging (`plugin.json`, `marketplace.json`
  with `owner` + `source: "./"`), Apache-2.0 `LICENSE` + `NOTICE` documenting
  the public-framework / private-content boundary, `README` with the origin
  story and positioning, `CONTRIBUTING`, `requirements.txt` (graceful-degrade
  deps), `.gitignore` enforcing the content boundary, and a wired
  `eval-gate` CI workflow with minimal green helper scripts.
- **Phase 1 — neuro-write + neuro-review.** The writing core, ported from the
  MIA writing skill and generalized to Layer A (journal-agnostic): a `_shared/`
  neuroimaging layer (invariants, modality taxonomy, terminology ledger, the
  HARD discipline style tier); `neuro-write` and `neuro-review` as router skills
  (short `SKILL.md` + `manifest.yaml`, explicit-invocation-only so they don't
  collide with an existing manuscript skill); six agent personas (`writer` +
  four reviewers + desk-reject `editor`); the `journal` axis shipping `generic`
  and a provenance-stamped `mia` worked example; the runtime venue/project
  overlay convention; `/neuro-write` and `/neuro-review` commands; and three
  evals wired into the gate (a MIA-style parity draft + anti-pattern and
  biological-overclaim detection). No TissueFormer/Layer-C content ships.

### Planned
- **v1.0** — `neuro-write` + `neuro-review` (ported from the MIA writing skill)
  and `neuro-rigor` with the `neuro-stats` MCP server + grounding hook.
- **v1.1** — `neuro-venue` (runtime journal profiles) + `neuro-preprocess`.
- **v1.2** — `neuro-litscan` + first public release.

[Unreleased]: https://github.com/CHANGE-ME/neuroscribe/commits/main
