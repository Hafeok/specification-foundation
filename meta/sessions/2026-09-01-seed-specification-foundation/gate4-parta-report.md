# Gate 4 report — Part A executed

**Executed as ratified at Gate 3, Part A. No new content; nothing not ratified.** Part B remains
unexecuted and unratified, holding on OD-1.

---

## 1. Filed

| File | sha256 at landing | Verified against arrival |
|---|---|---|
| `canon/specification-language-foundation.md` | `3d9a5254…` | **byte-identical** — the original, pre-supersession state |
| `canon/resolution-condition.md` | `802fc286…` | **byte-identical** |
| `canon/boundary-declarations.md` | `0690cb55…` | **byte-identical**; adjacent to the condition it makes sound |
| `evidence/supersession-foundation-construct-list.md` | `0c2c17cc…` | **byte-identical**; under `evidence/` per CG-R-11 |

Each carries its `filing/v1` sidecar with the CG-R-14 apparatus: arrival provenance and hash,
state, the falsifier it awaits, the dated conversion commitment, and adjacency pointers — the
foundation's names the supersession record and vice versa, so both construct-list states are
visible from either side without either text being touched. The foundation's sidecar carries the
permanent provenance fact in full. `inputs/README.md` landed beside the session-record copies,
doing the I-4 pointing (R-6 → register) without annotating any copy.

**No SF- identifier was assigned. Nothing is numbered.** The SF- space is empty, as ratified.

## 2. The canon-governance ref, re-checked at execution

Re-fetched at Gate 4: the head of `claude/seed-canon-governance-ntf524` is still
**`ad6d1b0b861306561364cc8d3a3e554cfb92d90c`** — the ref this session read at Gate 0. Read ref
and cited ref coincide; nothing changed between refs, so under CG-R-10 the citation stays put.
The invocation's `<REF>` is discharged by the records that carry the resolved value — the
bootstrap parameters, the README citation, and `meta/canon-governance-ref.yaml` — while the
verbatim invocation quote keeps its placeholder, as arrived.

## 3. Validator runs after filing

All three green at the landed tree (`gate4-parta-runs.txt`, verbatim): 0 claims valid; 0 pins,
0 errors; pin accounted for.

## 4. What passes for the wrong reason — or for less than a reader will assume

Reported per the gate's instruction; none is a defect in a validator, each is a green light that
covers less than the tree now suggests:

1. **The ordering validator's green says nothing about the four filed artefacts.** They are
   prose, unnumbered, invisible to every one of its passes — by CG-R-14's ruling, not by
   accident — but a reader seeing filed canon and green CI will assume the canon was validated.
   It was hash-verified at filing by this session, once; nothing re-checks it on any future
   push. The green means: no numbered docs violate ordering (there are none), no pins drift
   (there are none).
2. **The claims validator's green is about an empty directory.** `valid: 0 claims` states its
   denominator; the filed canon is not claim records and was not read.
3. **The governance-pin check covers `README.md` only.** `scripts/README.md` cites the
   `decision-driven-design` adaptation source at `d89ed557…`, and nothing checks that citation —
   it can silently rot in a way the canon-governance pin now cannot. A smaller instance of the
   same staleness class, uncovered, recorded here.
4. **The sidecars are unread** until the CG-R-16 trigger — the first conversion — lands the
   check that can actually fail.

## 5. Carried risks, stated for the session log (the prompt's closing list)

1. **The construct list has moved twice.** Filed with the supersession record visible from the
   artefact's own sidecar; a session deriving from the foundation and skipping the sidecar still
   gets a stale list — the sidecar is the guard, and it is prose.
2. **The conformance relation has no validator** and ends this session without one. Recorded in
   the README, at `scripts/README.md`, and refused mechanically at E14; the gap is for
   `specification-languages`' creation to confront, on the record rather than by discovery.
3. **The resolution condition has no falsifier.** Per R-1 the current pre-registration tests a
   different claim, and the bar on presenting its result as a test of the condition is stated at
   `evidence/README.md` and in the artefacts' sidecars.
4. **Licence, attribution and editor role** were fixed in the first root commit (CC BY 4.0,
   Apache-2.0, `CITATION.cff` with the transfer sentence), not retrofitted.
5. **`canon-governance` governs nothing operationally.** Stated in the README exactly at that
   strength: rules in force as rules, no registry coverage, no verdicts. This repository
   declares nowhere that it is governed.
6. **CG-rule-08 and CG-rule-10 are provisional** and were exercised here (pre-registration
   discipline respected in filing; unbuilt apparatus marked and dated throughout). Nothing in
   this session discharges either: a session's own exercise is not independent evidence, and the
   over-claim corrections this session recorded (Gate 3 §8's framing, corrected by CG-R-16)
   were caught by Emil, not by the session before commit — so no discharge is claimed.

## 6. Session state

- Gates 0–3: ratified. Gate 4: **Part A executed.**
- **Part B holds** on OD-1 (input 8, Emil's): arrival record filed with hash verification →
  addendum to the Gate 3 plan → ratification → execution. Nothing else remains.
- OD-2 (the register append, seven rulings) is Emil's, acknowledged.
- Per the prompt's stop line: the conformance criterion, the discrimination pairs, and the
  bindings are later sessions. Nothing of them was touched.
