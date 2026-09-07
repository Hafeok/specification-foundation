# Reconciliation rule for the blind re-derivation

**Status: `[PROPOSED]`, fixed before either list is compared.** `CG-R-35` sets the three
outcomes per row; this file fixes how rows are matched and how each outcome is worked, so that
the reconciliation cannot be shaped by what the re-derivation turns out to contain. Filed
2026-09-04, before the re-derivation exists.

## 1. Inputs

- the proposed list, `gate2-proposal.md` §2, nineteen rows `F-01` … `F-19`, as committed;
- the re-derived list, filed byte-identical under `inputs/` with its hash on arrival, rows
  `R-nn`, together with its rejection register.

## 2. Matching

Two rows **match** when the same feature of an actor's output would answer both questions. The
test is on the questions and answer forms, not the names. Three cases:

- **one-to-one** — matched; counted *in both*;
- **one-to-many** — one row's question spans two or more of the other's; recorded as a split;
  counted *in both* if the finer rows together cover exactly the coarser row's decision points,
  and the finer partition is taken forward, since the frame wants the finer grain (U-11);
- **no match** — the row is *only in* its list.

Matching is done by this session, shown row by row with the reason, and ratified by Emil. The
session cannot be blind to its own list; the mitigation is that every match is written down and
arguable.

## 3. Working the three outcomes

- **In both.** Reproducible; the row stands as proposed, in whichever wording is plainer.
- **Only in the proposed list.** A set-fitting candidate. Defended in writing on the derivation
  alone — cell and the four conditions. **The defence may not cite the determination set,
  the Gate 1 act, or the closure preview.** If the defence does not stand on the grid, the row
  is struck. A struck row is recorded, not deleted.
- **Only in the re-derivation.** An omission candidate. Admitted or refused on the four
  conditions, in writing; refusals are checked against the proposed list's own rejection
  register — a candidate the proposed list already rejected for a stated reason is refused for
  that reason unless the re-derivation's derivation defeats it.

The re-derivation's rejection register is also read against the proposed list: a row the
re-derivation considered and rejected that the proposed list admits is reported as a
disagreement about the conditions, and ruled.

## 4. The overlap, reported

Counts: rows in both, only-proposed, only-rederived, struck, admitted. The reproduction rate is
*in both* over the proposed list's row count. **No threshold is fixed here**, because none is
principled; one is offered for ruling: if fewer than two-thirds of the proposed rows are
reproduced, the method section of the Gate 2 proposal is revised before any list is ratified,
per `CG-R-35`'s reading that a small overlap is a finding about the grid.

## 5. Order

Reconciliation → ratification of the reconciled list → closure of the determination set
against it (`CG-R-21`, `CG-R-29`) → ratification of the closure → Gate 3. The closure preview in
`gate2-proposal.md` §6 is redone against the reconciled list, not carried forward.

---

## Note appended 2026-09-04 — §4's offered threshold refused; provenance grade substituted (`CG-R-40`)

§4 above offered a two-thirds threshold for ruling. **Refused**: an arbitrary ceiling of the
kind already refused for the boundary ratio, and the aggregate is the wrong place to look. §4
stays as written; this note governs.

**Per row.** A proposed-only row is retained only if defended on the grid alone. §3 already
forbids citing the determination set, the Gate 1 act, or the closure preview in the defence;
the consequence is now explicit: a row defensible only by pointing at the set is set-fitted and
struck, and **one such row is a finding regardless of overlap**.

**In aggregate.** The overlap sets the list's provenance grade, recorded on the reconciled list
and carried into every citation of the result:

| Grade | Condition |
|---|---|
| **derived** | every retained row is defended on the grid alone |
| **authored** | some retained rows survive on author judgement the grid does not reach |

An authored list is usable and weakly warranted; the frame is then an artefact of this
author's reading of the act type, not of a reproducible method, and downstream reuse of the
method inherits that. The reconciliation states the grade and, for an authored grade, names
every row that carries it.

**Revision trigger.** Not a percentage. If a derived grade is unachievable — the grid cannot
defend rows the author believes belong — the grid underdetermines the list, and that is
reported as a finding about the method before any list is ratified.

---

## Note appended 2026-09-07 — the aggregated independence limit (`CG-R-47`)

Three residuals on the re-derivation's independence were filed separately as they arose:
`CG-R-39` (the brief is this session's phrasing of a grid that is itself under test), `CG-R-43`
(the receiving session can infer that a falsification programme exists and that a
pre-registration tests a closure claim), and the scrub record's weakest point (the care in the
brief's prohibitions discloses that its output matters to something). **Ruled: they are read as
one limit, not three.** Aggregated they describe a single channel — *the receiving session can
tell it is doing careful work for a programme that will scrutinise the result, without knowing
what the scrutiny is.*

**How the reconciliation uses it.** One input to the provenance grade under `CG-R-40`, weighed
once. It does not by itself make the list *authored*; it bounds how much a *derived* grade can
claim, and the grade statement names it. What keeps it tolerable is recorded with it: the audit
found no frame vocabulary in the bundle, so the inference reaches *this matters* and stops
short of *this is a denominator*.
