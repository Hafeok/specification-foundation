# Seed bundle — checklist and index

Everything needed to run the `specification-foundation` seed session, in the order it is needed.

---

## 1. Before the session — decisions to fix

| Item | State | Note |
|---|---|---|
| Claim ID prefix | **`SF-`** | Ruled. Fixed before any claim record. |
| `meta/sessions/` | **native** | R-6. Upstream proposal filed separately, non-blocking. |
| Attribution | **Emil personally** | Not a future custodial body. Transfer sentence included. |
| Terminology | **layer / scale** | R-2. Independent coordinates, seeded into the term registry at Gate 1. |
| Family name, ORCID, seed date | **outstanding** | Required for `CITATION.cff`. The citation string is fixed at seed. |
| Repository created and empty | **outstanding** | Gate 0 stops if it contains anything else. |

---

## 2. The session prompt

`session-seed-specification-foundation.md` — commit to `meta/sessions/` as the first act of the session.

Four gates: governance, validators, filing plan, execute. The session authors governance and tooling; it files canon rather than writing it.

---

## 3. Arrived inputs to attach

| # | File | Kind | Load-bearing at |
|---|---|---|---|
| 1 | `specification-language-foundation.md` | canon, original state | Gate 3 |
| 2 | `supersession-foundation-construct-list.md` | provenance | Gate 3 |
| 3 | `resolution-condition.md` | canon | Gate 3 |
| 4 | `boundary-declarations.md` | canon | Gate 3 |
| 5 | `rulings-session-close.md` | rulings | Gates 1, 3 |
| 6 | `prereg-closure-falsifier.md` | evidence, not canon | Gate 3 |
| 7 | `rulings-gate0-closure-falsifier.md` | rulings | Gate 3 |
| 8 | prior falsifier Gate 0 output | arrived input | Gate 3 |

**Item 8 is the only one not in this bundle.** It is the output of the earlier `claude/closure-falsifier-prereg-w1mm7d` session and must be supplied from there. Do not let the session reconstruct it.

**Item 1 must be supplied in its original state.** Not resolved against item 2. The falsifier's category list derives from the construct list and the derivation needs both states; a tidied version defeats it.

---

## 4. Seed artefacts

`CITATION.cff` — three fields marked `SUPPLY`. The citation string is fixed at seed and cited by everything downstream, so it is worth getting right before the first commit rather than after.

---

## 5. Filed separately, not part of the seed

`proposal-meta-sessions-upstream.md` — against `actor-indexed-determination`. Non-blocking. It carries an open question that should be settled before acceptance: whether Layer 1 should hold procedural conventions at all, or whether a fourth place for shared governance is the right answer. Accepting the proposal decides the general case by precedent either way.

---

## 6. Order of operations

1. Fix the three outstanding `CITATION.cff` fields.
2. Create the repository, empty.
3. Attach the eight arrived inputs and the prompt.
4. Run the session. Ratify at each of the four gates.
5. File the upstream `meta/sessions/` proposal separately.

---

## 7. What this session does not produce

- the conformance criterion and discrimination pairs
- any binding — event modelling, SPETLR, authorisation
- the engineering process, which stays in `specification-languages` per R-5
- a validator for the conformance relation; that gap is recorded, not closed
- any falsifier for the resolution condition; per R-1 the current pre-registration tests a different claim, and nothing filed here may present it otherwise

---

## 8. Known state of what is being filed

All canon in this bundle is `[PROPOSED]`. None of it has a falsifier attached except by reference. The seed establishes a repository with governance, validators and provenance intact — it does not establish that anything in it is true.

Worth stating in the session log, because a well-organised repository reads as more settled than its contents are.
