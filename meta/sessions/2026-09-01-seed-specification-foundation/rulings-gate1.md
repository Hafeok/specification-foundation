# Rulings — Gate 1

**Issued by Emil, 2026-09-01, ratifying Gate 1 as proposed.** Filed verbatim. Three rulings drawn
from the `CG-R-` series and one caution.

---

> Gate 1 ratified as proposed. Three rulings and one caution.
>
> CG-R-10 — the pinned citation does not advance on head movement. A citation to canon-governance
> records what was read and complied with, not what is current. Advancing it silently would assert
> compliance with rules nobody checked against. It advances only by a deliberate act that states
> what changed between the refs, and if nothing changed the ref stays put. Going stale is the
> correct behaviour; a citation that tracks head is not a citation.
>
> CG-R-11 — the supersession record files under evidence/. Your discomfort is right and the split
> is still correct. The test is what the artefact is for, not what it is about: it is provenance
> about canon, and it is load-bearing for a derivation. Both are evidential. Put anything under
> canon/ only if it is itself a determination — the construct list, the resolution condition, the
> boundary declarations. That gives a clean rule for Gate 3 rather than a judgement per artefact.
>
> CG-R-12 — the peer registry drift check stays a dated gap. No commitment to build it in this
> repository. Drift between two peer term registries is a two-party problem and neither peer owns
> it; it belongs where cross-repository checks belong, which is canon-governance, which currently
> issues no verdicts at all. Recording it as an unowned gap is more honest than either peer
> building half a check.
>
> The caution. Contribution discipline in the README rather than a CONTRIBUTING.md is right for
> the reason you gave, but it puts the pinned commit in the document most likely to be edited
> casually. Under CG-R-10 that pin is now load-bearing. Worth Gate 2 considering whether a
> validator can assert the pin matches a recorded value — cheap, and it is the only mechanical
> defence against the one place staleness would be silently wrong.
>
> On your primary weakest point: the two top-level names survive CG-R-11, and a same-session
> supersession would have been an acceptable cost anyway. Leaving everything below them open to
> Gate 3 was the right call.
>
> Gate 2 begins. Input 8 remains mine.

---

## Amendments applied at landing

Ratified as proposed; the three rulings touch three draft documents, and the amendments applying
them are the only differences between `gate1-draft/` and what landed at root. Each is minimal and
cites its ruling:

- `README.md` — one sentence added after the pinned citation, stating CG-R-10's advance
  discipline.
- `canon/README.md` and `evidence/README.md` — CG-R-11's placement test stated at both paths:
  canon/ takes only what is itself a determination; the supersession record files under
  `evidence/`.
- `terms/registry.md` — the drift-check note now records the gap as unowned per CG-R-12: it
  belongs with cross-repository checks in `canon-governance`, and this repository commits to
  nothing.

## Obligations recorded, not performed

**CG-R-10, CG-R-11 and CG-R-12 are owed rows in `canon-governance`'s `registry/rulings.yaml`** —
the register the next ruling must append to, per CG-R-8. This session does not modify a source
repository, so the append is Emil's (or a canon-governance session's). Until it lands, the
verbatim filing above is the only record of the three rulings, in a repository that is not their
register. Flagged rather than left to be noticed.

## Carried to Gate 2

- The caution: propose a mechanical check that the README's pinned canon-governance ref matches a
  recorded value — the one place staleness would be silently wrong under CG-R-10.
