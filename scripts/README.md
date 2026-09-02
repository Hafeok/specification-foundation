# scripts/

The repository's validators. Three, all run by CI on every push and pull request, each failing
the build on violation.

| Script | Governs | Provenance |
|---|---|---|
| `validate-claims.py` | claim records under `canon/claims/` — `SF-` space, format v1, falsifier presence at every live status; `--decisions` mode for escaped-decision checks when a decisions directory exists | adapted from `Hafeok/decision-driven-design` at `d89ed55724c55f26a995b067907add2bcb580290` |
| `validate-core-order.py` | the **projection** relation only — canon doc ordering, graph transclusion, upstream pins against `actor-indexed-determination` | adapted from the same source; E14 added here |
| `validate-governance-pin.py` | the README's `canon-governance` citation matches `meta/canon-governance-ref.yaml` (CG-R-10) | new code, first written here |

A green run means **well formed, not correct**.

---

## These validators issue verdicts — and canon-governance's instrument does not

The two repositories differ here **by ruling, and neither is wrong**. Recorded because the next
reader will assume one of them is.

- **`canon-governance`'s instrument measures and may not judge** (`CG-R-2`). It evaluates
  existing repositories, and until governance start points exist a verdict could score a
  repository non-compliant against a rule not in force where it was written — the false-red
  defect ruling §H was issued about. An instrument issuing no verdicts cannot produce a false
  one.
- **This repository's validators issue verdicts** (`CG-R-13`). They gate **future filings**,
  never evaluate an existing corpus, so there is nothing to be scored against a rule not in
  force where it was written — the §H defect cannot arise. A gate that only measures gates
  nothing.

The distinction that decides which posture an instrument takes: **what the instrument points
at.** Backward at a corpus that predates the rules — measure. Forward at filings made under
rules already in force — verdict. An instrument here that ever starts evaluating existing
external content has crossed that line and needs re-ruling, not a bigger allowlist.

What a false adverse verdict looks like here, per check, is recorded in the Gate 2 proposal
(`meta/sessions/2026-09-01-seed-specification-foundation/gate2-proposal.md`, §5). Every failure
message names the rule or ruling behind the check so a false red is repaired from the right
question.

## The relation guard's coverage limit — recorded, not fixed (`CG-R-15`)

## Committed, not built: the sidecar check lands with the first conversion (`CG-R-16`)

**Dated commitment, 2026-09-01, against a named trigger.** The `filing/v1` sidecars under
`canon/` and `evidence/` carry the CG-R-14 conversion commitments, and no validator reads them.
Ruled at `CG-R-16` that the check **lands in the same change as the first artefact converting to
a numbered claim** — not before: a presence-only check passes a drifted sidecar as readily as an
accurate one, a green light over an unread file. The first conversion gives the check something
that could fail — that the committed conversion actually happened, at the committed target.
Until that trigger, the commitments are prose, stated as such.

## The relation guard's coverage limit — recorded, not fixed (`CG-R-15`)

`validate-core-order.py` refuses to evaluate any relation other than `projects-from` (E14),
because every check in its pin machinery encodes that upstream cannot legitimately be diverged
from — true of projection, false of conformance. **E14 guards the one door that exists today.**
Nothing stops a future session copying the pin machinery into a new script without the guard,
and the header notice is prose — the blind spot `CG-R-7` names. Ruled at `CG-R-15`: the limit is
recorded here rather than closed by a scanner nobody costed. It is the fifth instance of the
standing scope question that *nothing checks the governing acts*.
