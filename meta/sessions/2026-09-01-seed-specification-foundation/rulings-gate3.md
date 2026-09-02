# Rulings — Gate 3

**Issued by Emil, 2026-09-01, ratifying Part A of the filing plan.** Filed verbatim: one ruling,
one correction owned, one standing observation.

---

> Part A ratified. Nothing in it depends on Part B, and holding a complete plan behind a blocked
> one would be deferral without a reason. Part B stays unratified until the addendum exists —
> ratifying placement for an arrival record nobody has seen would be ratifying a blank, correctly
> stated.
>
> scripts/ is right, no rename. CG-R-13 named checks/ because I was writing from the governance
> repository's structure and did not check yours. The ruling's substance is the discriminator,
> not the path. Your reading was correct and the correction is mine.
>
> CG-R-16 — the sidecar-presence check lands with the first conversion, not before. A validator
> that only asserts presence, when a drifted sidecar passes it just as well as an accurate one,
> buys less than it appears to. The sidecar's real content is the conversion commitment, and the
> moment that has a target — the first artefact converting to a numbered claim — the check can
> assert something that could fail. Until then it would be a green light over an unread file.
>
> Record it as a dated commitment against the first conversion, not as a general gap. The
> distinction matters: a gap awaiting an unnamed future act is what CG-rule-10 exists to stop.
>
> On the sidecars being prose: that is now the sixth instance of the scope question. Six
> instances, five caught by a person reading a document after changing the state it described,
> and still no rule — because an absence remains not a practice. It has become the best-evidenced
> open question in the framework and it is not getting closer to closure by accumulating
> instances. Worth deciding, at some point outside a gate, whether it warrants an instrument or
> an explicit ruling that it never will.
>
> OD-2 is mine and I will clear it. Six rulings held only in downstream verbatim filings is a
> real provenance defect, and CG-R-16 makes seven.
>
> Gate 4 executes Part A.

---

## Consequences applied at execution

- **CG-R-16** is recorded in `scripts/README.md` as a **dated commitment against a named
  trigger** — the first artefact converting to a numbered claim — not as a general gap. The
  Gate 3 plan's §8 framed it as a gap with an unnamed future act; the ruling supersedes that
  framing, and the plan text stays as written per CG-rule-02, with this record beside it.
- **OD-2 is amended to seven rulings** (CG-R-10 … CG-R-16), per the acknowledgement.
- The sixth-instance observation on the scope question — whether *nothing checks the governing
  acts* warrants an instrument or an explicit ruling that it never will — is Emil's to take up
  outside a gate. Recorded verbatim above; no action here.
- The `checks/` naming in CG-R-13 is confirmed as a path slip, correction Emil's; `scripts/`
  stands.
- Gate 4 executes Part A only. Part B holds for input 8, the addendum, and its own ratification.
