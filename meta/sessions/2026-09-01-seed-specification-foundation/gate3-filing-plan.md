# Gate 3 — filing plan for the arrived canon

**`[PROPOSED]` in full. Placement only: no artefact text is altered, nothing is executed until
Gate 4, and nothing lands that is not ratified here.**

**The plan is in two parts.** Part A (the canon artefacts and the supersession record) is
complete and ratifiable now. Part B (the falsifier material) is **blocked on OD-1** — input 8 has
not arrived — and is stated as far as it can be, with its completion an addendum to this plan
when the input lands. Whether to ratify Part A ahead of Part B or hold for both is Emil's;
nothing in Part A depends on Part B's contents.

Register discipline: rulings applied are CG-R-11 (the placement test), CG-R-14 (prose with dated
conversion commitments), R-1 (what the pre-registration tests), the Gate 0 rulings (the prereg
files unamended; the draft rulings stay `[DRAFT]`; the foundation's provenance is a permanent
fact), and CG-rule-02 (nothing is annotated in place). `[OPEN]` in §7.

---

## Part A — canon artefacts and the supersession record

### A-1. Placement, by the CG-R-11 test

Only what is itself a determination files under `canon/`; everything evidential under
`evidence/`. Applying it artefact by artefact:

| Arrived input | Is it a determination? | Files as |
|---|---|---|
| `specification-language-foundation.md` | yes — the construct list | `canon/specification-language-foundation.md` |
| `resolution-condition.md` | yes — the completeness predicate | `canon/resolution-condition.md` |
| `boundary-declarations.md` | yes — what makes the predicate sound | `canon/boundary-declarations.md` |
| `supersession-foundation-construct-list.md` | no — provenance about canon, load-bearing for a derivation; both evidential (CG-R-11's own worked example) | `evidence/supersession-foundation-construct-list.md` |

Arrived filenames are kept, so every citation of an input resolves to the same name at its filed
location. The resolution condition and the boundary declarations sit **adjacent in the same
directory** — the declarations make the condition sound and are not separated from it; each
one's filing record names the other.

### A-2. State: byte-identical, original, both states visible

Every file lands **byte-identical to its arrived copy** (hashes in `arrived-inputs.md`; Gate 4
re-verifies at landing). In particular:

- **The foundation files in its original state.** S-1 and S-2 are *not* resolved into the text.
  The falsifier's category list derives from the construct list and the derivation needs both
  states; a tidied text would destroy exactly what the supersession record exists to preserve.
- **Both states stay visible** as: the original under `canon/`, the superseding positions in the
  record under `evidence/`, each side's filing record naming the other. No marker is added to
  either text (CG-rule-02: the copies are not annotated; adjacency does the pointing).

### A-3. Filing records — the CG-R-14 apparatus

Each filed artefact gets an adjacent sidecar, `<name>.filing.yaml`, at its filed location. The
sidecar is a filing record, not canon: it carries what CG-R-14 requires *at filing* without
touching the arrived text.

Fields, per artefact under `canon/`:

```yaml
format: filing/v1
artefact: <filename>            # the adjacent file, byte-identical to arrival
filed: 2026-09-01               # Gate 4's actual date at landing
filed_by: 2026-09-01-seed-specification-foundation
arrived_as: <path under meta/sessions/.../inputs/>
sha256: <hash of the arrived copy>
state: <original | arrived>     # foundation: original, with the supersession record named
provenance: <the permanent fact, where ruled>   # foundation: authored in conversation,
                                # first filed in the seed bundle; presents as original,
                                # not verified — no independent anchor exists or will
status: as the artefact's own header — [PROPOSED]; filing does not promote
awaits_falsifier: <which falsifier this artefact awaits, and why it is deferred>
converts: to numbered claim records under canon/claims/ when that falsifier lands
          (CG-R-14, dated 2026-09-01)
related: <adjacency pointers — e.g. the boundary declarations for the condition>
```

The `awaits_falsifier` values, stated now so ratification covers them:

- **foundation** — the closure claim's own falsifier (its §5, open item 1); the current
  pre-registration tests the mechanism claim instead, per R-1, and nothing may present its
  result as this artefact's test.
- **resolution condition** — its own falsifier, requiring two conforming specifications and a
  boundary between them (R-1's deferral; R-4 commits the composition check the candidate needs).
- **boundary declarations** — the candidate its own §Dependencies states (fewer escaped
  decisions at declared seams), untested, and a different claim from the current
  pre-registration's.

The supersession record's sidecar under `evidence/` carries the provenance fields only — it is
evidence, awaits no falsifier and converts to nothing; its `related` names the foundation.

### A-4. Claim IDs: none

**No SF- identifier is assigned at this seed, and nothing is numbered.** Per CG-R-14 the
artefacts are prose until their falsifiers land; the conversion commitments in the sidecars are
where numbering enters, later, as claim records under `canon/claims/`. The SF- space stays
empty, which is what `canon/claims/README.md` already says.

### A-5. The arrived rulings document points at the register without being touched

`rulings-session-close.md` (R-1…R-6) stays where it is filed, in the session record — rulings
live in `canon-governance` and this copy is arrival provenance, not a placement. Per the Gate 0
ruling on I-4, the pointing is done beside the copy, never in it: an `inputs/README.md` lands in
the session record stating that R-6 in that file is superseded by R-7 per
`registry/rulings.yaml` in `canon-governance` at the pinned ref, and that the file is a
pre-supersession record kept byte-identical under CG-rule-02.

### A-6. What is deliberately not placed

The four `reference/` notes and the two future falsifier session prompts stay session-record
inputs with no root placement. None is a determination (CG-R-11), none is evidence *about a
proposition filed here* in the way the falsifier material is — they are working notes and
charters for sessions that have not run. Placing them would grant standing nothing has ratified.
A later session can place any of them by its own gate. Recorded so the non-placement reads as
decided, not overlooked.

---

## Part B — falsifier material *(blocked on OD-1; stated as far as it can be)*

What can be proposed without input 8, so the addendum is small when it arrives:

- The falsifier material files under **`evidence/falsifier/`**: the pre-registration
  (`prereg-closure-falsifier.md`) **unamended — the correct state, not merely the faithful one**
  (Gate 0 ruling on I-1/I-2), and the never-issued draft
  (`rulings-gate0-closure-falsifier.md`) **as `[DRAFT]`**, filed in its arrived state, not
  treated as issued, not put forward for ratification (Gate 0 ruling on I-3). Each gets a
  sidecar recording provenance and, for the prereg, R-1's bar: it tests the mechanism claim,
  and nothing in this repository may present its result as a test of the resolution condition.
- **Input 8, when it arrives**, is filed first as an arrived input with its sha256 in
  `arrived-inputs.md` (its recorded `145ed0a2…` for the prereg is the one available cross-check
  of the five unanchored inputs — verified at arrival), and its placement beside the material it
  is the arrival record of is proposed **in the addendum**, not presumed here.

Part B cannot be ratified before the addendum exists: ratifying placement for an arrival record
nobody has seen would be ratifying a blank.

---

## §7 — `[OPEN]` at this gate

- OD-1 — input 8 (Emil). Blocks Part B's completion and therefore Gate 4's execution of it.
- OD-2 — the ruling-register append (Emil). Blocks nothing here mechanically.
- Whether Part A is ratified ahead of Part B or the plan is ratified whole — Emil's call, stated
  in §preamble.

## §8 — weakest point

**The sidecars are load-bearing and nothing validates them.** The whole CG-R-14 apparatus — the
conversion commitments, the awaited falsifiers, the provenance facts, the both-states-visible
pointing — lives in `filing/v1` YAML files that no validator reads: a sidecar could be deleted,
or drift from the artefact beside it, and CI would stay green. The canon boundary was given a
path so a validator *could* check it; the filing records have a format so a validator *could*
check them — and none does, and this plan does not propose one, because Gate 3 is placement and
a new check is Gate 2 work this session already closed. Recorded here so the gap is a known
state at ratification, not a discovery after it; wiring a sidecar-presence check into
`validate-claims.py` or a fourth script is a cheap later act, and under CG-R-15's honesty
standard the true statement today is: the commitments are prose, exactly the category CG-R-7
warns about.

---

**Hold.** Awaiting ratification of Part A (or of the plan whole, once the Part B addendum
exists), and input 8 for Part B.
