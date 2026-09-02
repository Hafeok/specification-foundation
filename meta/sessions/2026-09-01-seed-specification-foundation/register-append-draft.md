# Draft rows for `registry/rulings.yaml` — CG-R-10 … CG-R-16

**Supplied by Emil, 2026-09-01, filed verbatim below.** Drafted for the session record; **the
append is a ruling authority act and is not performed by this session.** OD-2 stays open until
the rows land in `canon-governance` — a draft is not an append.

The stated check — each subject against the verbatim filings in this repository — is run in the
verification section at the end, which is this session's output, not part of the draft.

---

> Draft rows for registry/rulings.yaml — CG-R-10 … CG-R-16
>
> Clears OD-2. Seven rulings currently recorded only in downstream verbatim filings.
>
> Drafted by session; the append is a ruling authority act. Subjects are one-line summaries
> written by the party the rulings were ruling on — the verbatim filings in
> `specification-foundation` are the check.
>
> All seven issued 2026-09-01 during the `specification-foundation` seed. Note that identifier
> order does not reconstruct chronology in the pre-assignment range; within `CG-R-` it does, and
> these were issued sequentially.

```yaml
- id: CG-R-10
  issued: 2026-09-01
  status: assigned
  subject: >-
    A pinned citation to canon-governance records what was read and complied
    with, not what is current. It does not advance on head movement. Advancing
    requires a deliberate act stating what changed between refs; if nothing
    changed, the ref stays put. Going stale is correct behaviour.
  bears_on: [specification-foundation]
  recorded_verbatim: specification-foundation meta/sessions/2026-09-01-seed-specification-foundation/rulings-gate1.md

- id: CG-R-11
  issued: 2026-09-01
  status: assigned
  subject: >-
    Placement test for the canon/evidence split — what the artefact is for,
    not what it is about. canon/ holds determinations only. Provenance about
    canon, and material load-bearing for a derivation, are both evidential.
    The supersession record files under evidence/.
  bears_on: [specification-foundation]
  recorded_verbatim: specification-foundation meta/sessions/2026-09-01-seed-specification-foundation/rulings-gate1.md

- id: CG-R-12
  issued: 2026-09-01
  status: assigned
  subject: >-
    The peer term-registry drift check stays a dated gap with no build
    commitment. Drift between two peer registries is a two-party problem that
    neither peer owns; it belongs where cross-repository checks belong. An
    unowned gap is more honest than either peer building half a check.
  bears_on: [specification-foundation, decision-driven-design, canon-governance]
  recorded_verbatim: specification-foundation meta/sessions/2026-09-01-seed-specification-foundation/rulings-gate1.md

- id: CG-R-13
  issued: 2026-09-01
  status: assigned
  subject: >-
    Verdict-issuing validators are accepted in specification-foundation. The
    discriminator: an instrument pointing backward at a corpus predating the
    rules measures; one pointing forward at filings under rules in force may
    issue verdicts. The two repositories differ on this by design and the
    distinction is recorded where the instruments live.
  bears_on: [specification-foundation]
  note: >-
    Issued naming "checks/", which is canon-governance's instrument directory.
    specification-foundation's ratified structure names it scripts/. The
    session's reading was correct; the path in the ruling as issued was a
    drafting error by the issuing authority, corrected on the record, not by
    amending the ruling.
  recorded_verbatim: specification-foundation meta/sessions/2026-09-01-seed-specification-foundation/rulings-gate2.md

- id: CG-R-14
  issued: 2026-09-01
  status: assigned
  subject: >-
    Canon artefacts file as prose at the seed, because none carries a
    falsifier and the reason is ruled rather than lazy. Each records at filing
    which falsifier it awaits and a dated commitment to convert to a numbered
    claim when that falsifier lands. canon/README.md states the risk: prose the
    ordering validator never reads is where an unfalsified proposition sits
    indefinitely looking settled.
  bears_on: [specification-foundation]
  recorded_verbatim: specification-foundation meta/sessions/2026-09-01-seed-specification-foundation/rulings-gate2.md

- id: CG-R-15
  issued: 2026-09-01
  status: assigned
  subject: >-
    E14's coverage limit is recorded, not fixed. Nothing stops a future session
    copying pin machinery without the guard, and a header notice is prose,
    which CG-R-7 names as the blind spot. E14 guards the one door that exists
    today. Fifth recorded instance of nothing checking the governing acts.
  bears_on: [specification-foundation]
  recorded_verbatim: specification-foundation meta/sessions/2026-09-01-seed-specification-foundation/rulings-gate2.md

- id: CG-R-16
  issued: 2026-09-01
  status: assigned
  subject: >-
    The sidecar-presence check lands in the same change as the first artefact
    conversion, not before. A presence-only check passes a drifted sidecar as
    readily as an accurate one; the sidecar's real content is the conversion
    commitment, which has nothing to assert against until a conversion has a
    target. Recorded as a dated commitment against a named trigger, not as a
    general gap awaiting an unnamed future act.
  bears_on: [specification-foundation]
  recorded_verbatim: specification-foundation meta/sessions/2026-09-01-seed-specification-foundation/rulings-gate3.md
```

> Carried
>
> Six instances now of the scope question — nothing checks the governing acts, and every one was
> caught by a person reading a document rather than by an instrument. CG-R-15 records the fifth;
> the sidecars are the sixth.
>
> It is the best-evidenced open question in the framework and it is not approaching closure by
> accumulating instances. It warrants a decision outside a gate: an instrument, or an explicit
> ruling that there will never be one.

---

## Session verification — subjects against the verbatim filings

Run 2026-09-01, row by row against `rulings-gate1.md`, `rulings-gate2.md` and
`rulings-gate3.md`. This section is the session's check, not part of the draft.

**Substance: all seven subjects are faithful summaries of their verbatim filings.** Each
`recorded_verbatim` path resolves to the file carrying the ruling's full text; every issue date
matches; the sequential-issue note is correct (10–12 at the Gate 1 ratification, 13–15 at
Gate 2's, 16 at Gate 3's, in that order, same day). CG-R-13's `note` matches the correction as
owned in the Gate 3 message. One addition worth making there: the correction itself is recorded
in `rulings-gate3.md` ("scripts/ is right, no rename… the correction is mine"), so the note's
own basis lives in a file the row does not cite — citing both files would make the note
self-checking.

**Two schema observations against the register as it exists at `ad6d1b0b…`, for the appending
authority to resolve — the register's shape is not this session's to settle:**

1. **`status: assigned` collides with the register's existing field semantics.** In
   `registry/rulings.yaml` today, the assignment case is carried by `case:`
   (`pre_assignment | post_assignment_in_error | assigned`), and `status:` carries force
   (`in force` / `superseded by R-7`). Appending these rows as drafted would give one register
   two meanings for `status`. The existing-schema form would be `case: assigned` plus
   `status: in force`.
2. **`bears_on`, `recorded_verbatim` and per-row `note` are new fields**, and the register's
   top-level `sources:` list currently names only canon-governance session files. Consistent
   options: add the three `specification-foundation` filings to `sources:`, or let the per-row
   `recorded_verbatim` carry it — either works, but the register README describes `sources` as
   where the subject lines are checkable, so leaving the new filings out of it would make these
   seven rows the only ones whose check lives off-list.

Neither observation touches the substance of any ruling; both are about the append staying
consistent with the file it appends to.

**OD-2 state after this filing: still open.** The draft exists and is checked; the entry clears
when the rows land in `canon-governance`, per the dependency table's own rule.
