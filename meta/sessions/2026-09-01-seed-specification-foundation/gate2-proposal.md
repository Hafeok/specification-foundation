# Gate 2 proposal — validators

**`[PROPOSED]` in full.** Built and run in `gate2-draft/`; nothing lands at root until ratified.
On ratification the placement is: the three scripts to `scripts/`, the CI workflow to
`.github/workflows/validate.yml`, the pin record to `meta/canon-governance-ref.yaml`, plus
`canon/claims/README.md` establishing the claim-record path the claims validator runs over, and a
present-tense amendment to the README's validator section (currently marked *not built*).

Register discipline: rulings in force applied here are CG-R-2's reasoning by analogy (see §5),
CG-R-10 (the pin check), CG-rule-04 (the decision checks' bite point), CG-rule-03 (falsifier
presence, in its extracted wording), and the Gate 1 caution. `[OPEN]` items in §7.

---

## 1. What was adapted, from where

Both validators adapted from `Hafeok/decision-driven-design` at commit
**`d89ed55724c55f26a995b067907add2bcb580290`** (head of `main` at read time; the repository was
read, not modified). The instruments do not move: the source validators stay in their repository,
per CG-rule-03's note on non-relocation.

| Draft | Source | Adaptation |
|---|---|---|
| `validate-claims.py` | `scripts/validate-claims.py` | `SF-` identifier space; missing-target refusal; header and check-class comments rewritten for an empty corpus (see §3) |
| `validate-core-order.py` | `validate-core-order.py` | `sf:` doc markers; `canon/` as document root; `SF_UPSTREAM_DIR`; scan scoped to `canon/` only; **E14, the relation guard** — new |
| `validate-governance-pin.py` | **none — new code, first written here** | implements the Gate 1 caution; provenance stated in its header |

## 2. What the validators check

**`validate-claims.py`** (over `canon/claims/*.yaml`): claim format v1 — `SF-<area>-<nn>`
identifiers, legal kind and status, statement/region/changed present, evidence entry conditions
per status, **falsifier presence at every live status** (error; CG-rule-03's extracted wording,
with `test` standing in for the kinds the format exempts), retirement provenance
(`retired_from`, error), duplicate ids (error), single-limb statements (warning — a drafting
prompt, never promotable without adjudication). In `--decisions` mode: no escaped decisions — a
principal, basedOn edges, a resolution and a made context on every decision (CG-rule-04's bite
point, wired into CI when a decisions directory first exists).

**`validate-core-order.py`** (over `canon/`): dependency-ordered numbered docs with `sf:contract`
blocks — no forward edges, single establishment per term, embeds byte-matching the graph in their
one canonical home, refs resolving (E1–E11); and the **projection** pins in
`canon/graph/upstream.yaml` against `actor-indexed-determination` — pinned ids exist at the pinned
ref (E12), embeds of pinned ids match upstream byte-for-byte (E13), status movement (W5), content
movement under a held status (W6), undeclared shadowing of upstream ids (W7).

**E14 — the relation guard, the one addition.** `upstream.yaml` must declare
`relation: projects-from`; anything else — including absence — is refused with an error naming
why. The guard sits exactly at the point where reuse would be tempting: the pin machinery looks
like a generic cross-repository dependency checker, and it is not — every check in it encodes
that upstream cannot legitimately be diverged from, which is true of projection and false of
conformance. The module header carries the full notice; the demonstration runs show the refusal
firing on an `upstream.yaml` declaring `conforms-to`.

**`validate-governance-pin.py`**: the README cites exactly the ref recorded in
`meta/canon-governance-ref.yaml`, and every 40-hex hash in the README is that ref or explicitly
allowlisted — so the pin cannot advance silently in either document alone (CG-R-10, mechanised as
far as it can be).

**CI** (`validate.yml`): all three run on every push and pull request; each **fails the build on
violation** — errors are exit 1, never demoted to warnings. Warnings print and do not gate.

## 3. What they do not check — stated, not implied

- **Correctness of anything.** A green run means **well formed, not correct**: every reference
  can resolve and every determination be wrong. The README says this where the reader lands.
- **The conformance relation.** No validator here evaluates it, E14 actively refuses it, and the
  gap is recorded rather than closed.
- **The canon boundary as content.** CG-R-11's placement test (determination vs. evidential) is
  applied by people at filing; nothing mechanical distinguishes a determination from evidence by
  reading it. The paths make misfiling *visible*, not impossible.
- **Prose canon.** `evidence/`, `meta/` and unnumbered prose under `canon/` are never scanned.
  The arrived canon artefacts, filed at Gate 4, will not be validated by anything here unless
  Gate 3 files them as numbered docs with contracts — a Gate 3 decision, not a default.
- **Behaviour.** Per CG-R-7 the checks verify artefacts; a rule can be honoured or breached with
  no artefact moving.
- **Check-class fitness for this corpus.** The error/warning classes are inherited from the
  source's hit lists against 89 claims; this corpus has zero. The validator's header states that
  the first local claim legitimately failing an inherited error class is a ruling request, not a
  formatting chore.

## 4. Runs — an empty canon set, and both directions of failure

Nine demonstration runs, outputs verbatim in the session shell log, summarised:

| # | Run | Result |
|---|---|---|
| 1 | claims over an empty directory | **pass**, `valid: 0 claims` — the denominator printed |
| 2 | claims over a missing directory | **fail** — a mistyped path cannot pass as an empty set |
| 3 | claims over a valid `SF-` fixture | pass, with a single-limb **warning** demonstrating warning-not-fatal |
| 4 | claims over an invalid fixture | **fail**, 6 violations including the `DDD-` prefix rejection — the `SF-` adaptation demonstrably took |
| 5 | core-order over the current `canon/` | **pass** — upstream-only mode, `0 pins`, 0 errors |
| 6 | core-order over a missing directory | **fail** |
| 7 | core-order over an `upstream.yaml` declaring `conforms-to` | **fail — E14 refusal**, the guard firing |
| 8 | governance-pin over the real README and record | **pass** — 1 hash, accounted for |
| 9 | governance-pin with record and README moved apart | **fail in both directions** — missing recorded ref, unaccounted hash |

One defect found by the runs and recorded: an all-digit ref in the pin record would be parsed by
YAML as an integer and rejected with a misleading message. Noted as a comment in the record file
(quote such a ref); not code-patched, since the current ref cannot trigger it and the failure is
loud, not silent.

**The empty-set passes (runs 1 and 5) are the required state before any content is filed.** Both
pass against the tree as it stands.

## 5. Verdicts, and what a false adverse one looks like

These validators issue **verdicts** — exit 1 fails CI — not measurements. The `canon-governance`
seed chose measurement over judgement because an instrument issuing no verdicts cannot produce a
false one; that choice was available here and is **not** taken, because these checks gate future
filings rather than evaluating existing repositories, and a gate that only measures gates
nothing. The prompt's price for that choice is stating what a false adverse verdict looks like:

- **claims**: a legitimate claim shape the format does not know — the designed example is a
  future format v2 record, refused until `SUPPORTED_FORMATS` learns it; the undesigned example is
  an inherited error class misfitting this corpus (§3). Both surface as loud CI failures naming
  the check, which is the correction path working; the risk accepted is friction, not silent
  wrongness.
- **core-order**: an upstream clone failure — network, a moved ref — reads as E12 and turns CI
  red with nothing wrong in the repository. `SF_UPSTREAM_DIR` is the offline path; the failure
  message says so.
- **governance-pin**: a legitimate second canon-governance hash in the README (quoting a
  historical ref in prose) fails until allowlisted in `also_cited`. That friction is the design:
  the allowlisting is the deliberate act CG-R-10 requires.

The worst case common to all three: a false red invites repairing something that was never wrong.
Every failure message therefore names the rule or ruling behind the check, so the repair starts
from the right question.

## 6. Weakest point

**The relation guard protects one door and the building has others.** E14 binds
`validate-core-order.py`'s own entry point; nothing stops a future session copying the pin
machinery into a new script without the guard, or pointing a generic tool at the conformance
relation. The header notice and this record are the only defence at those doors — prose, exactly
what CG-R-7 warns a text search will miss reading and a determined session can ignore. The guard
is real where it is, and it is not a property of the repository.

Second: the claims validator's `--decisions` mode is wired into nothing until a decisions
directory exists, so CG-rule-04's bite point is present in code and absent from CI. Recorded here
rather than discovered when the first decision files.

## 7. `[OPEN]` at this gate

- G-1 — input 8 outstanding; blocks Gate 3.
- Whether Gate 3 files any canon artefact as a numbered, contract-carrying doc (bringing it under
  E1–E11) or as prose the ordering validator never reads. Either is coherent; the choice is
  placement, so it is Gate 3's.
- When a decisions directory first exists, wiring `--decisions` into CI should land in the same
  commit — recorded so it is not rediscovered.

---

**Hold.** Awaiting explicit ratification of Gate 2. On ratification: scripts land in `scripts/`,
the workflow in `.github/workflows/`, the pin record in `meta/`, `canon/claims/` is established
with its README, the root README's validator section moves to present tense, and the validators
are re-run at their landed paths with results recorded before Gate 3 opens.
