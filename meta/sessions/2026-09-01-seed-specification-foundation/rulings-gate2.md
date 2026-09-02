# Rulings — Gate 2

**Issued by Emil, 2026-09-01, ratifying Gate 2.** Filed verbatim: three rulings and one
acknowledgement.

---

> Gate 2 ratified. Three rulings, and one acknowledgement.
>
> The registry/rulings.yaml append is mine and I have not done it. CG-R-10 through -12 sit
> outside their register, and now -13 through -15 will too. That is six rulings recorded only in
> a downstream repository's verbatim filing. Flagging it rather than performing it was correct;
> the debt is on me, and it should be visible in your Gate 2 record as an outstanding dependency,
> not just as a note.
>
> CG-R-13 — verdicts accepted here, with the distinction recorded. Your reasoning holds: these
> gate future filings rather than evaluate existing repositories, so there is no corpus to be
> scored non-compliant against a rule not in force where it was written. The defect §H was issued
> about cannot arise. Record the distinction explicitly in checks/, because the two repositories
> now differ on this and the next reader will assume one of them is wrong.
>
> CG-R-14 — canon artefacts file as prose at this seed, with a dated conversion commitment per
> artefact. Not because prose is easier. Because none of them carries a falsifier, and the reason
> is ruled rather than lazy: the resolution condition's falsifier requires two conforming
> specifications, and R-1 already defers it.
>
> Each artefact records, at filing, which falsifier it awaits and the fact that it converts to a
> numbered claim when that falsifier lands. canon/README.md states the risk plainly: prose the
> ordering validator never reads is exactly where an unfalsified proposition sits indefinitely
> looking settled. The commitment is what stops the category becoming permanent, and it is dated
> per CG-rule-10.
>
> CG-R-15 — E14's coverage limit is recorded, not fixed. Nothing stops a future session copying
> pin machinery without the guard, and a header notice is prose, which CG-R-7 names as the blind
> spot. This is the fifth instance of the scope question: nothing checks the governing acts.
> Record it there rather than building a scanner nobody costed. The honest statement is that E14
> guards the one door that exists today.
>
> The all-digit ref finding is right to record rather than patch — a loud failure with a quoting
> note beats a silent coercion someone later trusts.
>
> Gate 3 begins, blocked only on input 8, which remains mine.

---

## Consequences applied at landing

- **The register debt is promoted** from a note to an entry in `outstanding-dependencies.md`,
  beside G-1: six rulings (CG-R-10…15) recorded only in this repository's verbatim filings,
  awaiting Emil's append to `canon-governance`'s `registry/rulings.yaml`.
- **CG-R-13**: the verdict/measurement distinction is recorded where this repository's
  instruments live — `scripts/README.md`. One reading applied and stated rather than assumed:
  the ruling says "in checks/", which is `canon-governance`'s name for its instrument directory;
  this repository's ratified structure names it `scripts/`, and the record lands there. If the
  ruling meant a directory literally named `checks/`, that is a cheap rename to order.
- **CG-R-14**: shapes the Gate 3 plan — canon artefacts file as prose, each with an adjacent
  filing record naming the falsifier it awaits and a dated commitment to convert to numbered
  claims when it lands. `canon/README.md` now states the risk plainly, dated per CG-rule-10.
- **CG-R-15**: recorded in `scripts/README.md` beside the distinction — E14 guards the one door
  that exists today; the fifth instance of *nothing checks the governing acts*, held as a
  recorded limit, not fixed by an uncosted scanner.
- The all-digit ref finding stays a recorded quoting note; no code patch.
- Landing executed: the three validators to `scripts/`, CI to `.github/workflows/validate.yml`,
  the pin record to `meta/canon-governance-ref.yaml`, `canon/claims/` established, the root
  README's validator section moved to present tense. Landed-path runs recorded in
  `gate2-landing-runs.txt`.
