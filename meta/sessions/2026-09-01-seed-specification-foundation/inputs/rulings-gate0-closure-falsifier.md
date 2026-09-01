# [DRAFT] Rulings on Gate 0 — closure falsifier pre-registration

**Nature.** Draft rulings for Emil to issue, amend or reject. Not ratified by having been drafted.

**Overall.** Gate 0 is accepted. The defect list is substantially correct and four of its findings are structural. The pre-registration is amended before commit rather than carried forward with known defects. One correction runs the other way, and one finding corrects an earlier assessment of SPETLR rather than the pre-registration.

---

## A. Correction to Gate 0

**D1's fix is accepted; D1's stated mechanism is rejected.**

D1 argues the denominator shrinks in arm A because more properties are bound under A. Under the strip-only derivation rule that the same session endorses in its `[OPEN]` list, arms A and B carry identical bound determinations — A is B plus declarations of absence. Bound is therefore constant across arms and the asymmetry as described does not arise.

The defect is nonetheless real by a different route: a decision set discovered post hoc from output varies with reviewer, with output length, and with what each arm happened to produce. That is sufficient to require the fix.

Record this correction rather than carrying a wrong justification for a right amendment.

---

## B. Structural rulings

**D1 — accepted with the correction above.** The decision frame is enumerated from the pre-registered category list per act, not discovered from output. Consequence for Gate 2: the category list is a **measurement frame** as well as a completeness predicate. Gate 2's brief is amended accordingly.

**D3 — accepted.** Blinding as written does not discharge the expectancy threat. Adopt the two-stage split:

- Stage 1: a reviewer sees output only, never the specification, and classifies each frame entry as **surfaced** or **escaped**.
- Stage 2: **bound** is read off the specification against the frame. With D1's fixed frame this is close to mechanical and may not require independent judgement; if it does, it is a separate reviewer who never sees output.

**D4 — accepted, and promoted from open item to ruling.** Arm B is derived mechanically from arm A by removing non-travel declarations only. All bound determinations remain, unchanged, in the same order, unreworded. No discretionary construction of arm B. This is pre-registered.

**D12 — ruled, not simply accepted.** The claim under test is narrowed to **act completeness**: for a given act, every category in the frame is either bound or declared non-travelling. Layer completeness is the quantification of act completeness over the acts in a layer. This experiment tests the atom and does not test the quantification.

§7 is amended to state this. Any downstream use of the result must not silently promote act completeness to layer completeness.

---

## C. Substantive rulings

**D2 — ruled.** Volume matching is on **determination count**, which the strip-only rule makes exact by construction. Word count is not matched and cannot be: arm A is arm B plus N declarations. The asymmetry is reported per arm and acknowledged as a limitation.

Note for the record that the additional words in arm A are declarations of *absence*, not additional content, which weakens but does not eliminate the effort objection. §1, §2 and §6 are reconciled to this single quantity.

**D5 — accepted.** §1's falsification condition is governed by the threshold fixed at Gate 3. §1 is amended to say so.

**D6 — accepted, including the stronger reading.** Arm C's instruction is pre-registered verbatim, identical across all acts, and is to be **the strongest generic instruction the authors can write**, not a representative or weak one. A weak arm C that loses proves nothing. If arm C written at full strength matches arm A, the claim fails and that outcome is reported without softening.

**D7 — largely dissolved by D1, residually accepted.** With the frame enumerated from categories, incidental resolutions (identifier naming, import order) do not enter the decision set unless a category covers them. What remains is the materiality of categories themselves, which is Gate 2's business and is now explicit.

**D8 — accepted.** The rubric states that correctness is irrelevant to classification: a silently resolved decision resolved well is escaped. The bias direction identified is correct and the statement is mandatory, not advisory.

**D9 — accepted.** Surfaced questions concerning already-bound matters are reported as a rate per arm, with a ceiling fixed at Gate 3 above which the run is invalidated for delivery failure. They are not silently excluded.

**D10 — accepted as a power problem, with a trade-off named.** Corpus familiarity depresses escape rates across all arms and compresses the detectable effect. Drawing acts away from the published surface would reduce contamination but also reduce the realism of the acts, and the acts are the point. Recommendation: accept the contamination, name it in §6, and treat it as a reason the design must be powered for a smaller effect than intuition suggests.

**D11 — accepted, Gate 1.** The act set is a set of instances. The rule for deriving instances from role types is Gate 1's to propose and is a fixed-before-execution item; §4 is amended to list it.

**D13 — accepted.** Secondary measures are marked descriptive-only and may not be used confirmatorily. No post hoc analysis of them enters the result.

**D14 — acknowledged as an authoring defect.** §4 does predate arm C and was not reconciled with §2. Corrected. Noted rather than silently fixed.

**D15 — accepted.** §8's feasibility claim holds only without the human control arm, and is amended to say so explicitly. See open item below.

---

## D. Direction on the two items Gate 0 asked about

**D1/D3 — the frame becomes the pre-registered category list.** Yes. Gate 2 produces a measurement frame and a completeness predicate in one artefact, and its brief is amended before it starts.

**Item 4 — the foundation is supplied before Gate 2.** `specification-language-foundation.md` exists and is to be provided. Gate 2 derives the category list from the foundation's construct list and states the derivation, rather than reconstructing one from the pre-registration alone. If any category cannot be derived and must be invented, that is stated at the point of invention.

---

## E. Correction to the earlier SPETLR assessment

Gate 0's reading of the source corrects a prior assessment made from documentation. The three ETL roles are a naming convention over a single abstract type; the orchestrator's positional methods are aliases and enforce nothing about role position.

The earlier claim that SPETLR supplies a closed act-type set is withdrawn. Gate 0's replacement justification is adopted: SPETLR is suitable because it **encodes almost nothing**, so every consequential property must come from the specification or from the actor, which is the condition an escape experiment requires.

---

## F. Carried open

1. **Human control arm.** Undecided. Without it, a negative result is permanently contestable as model choice. With it, §8's feasibility claim fails and this becomes a project. Decide before Gate 3, since it changes the quantities.
2. **Single model or ladder.** Interacts with D10: a stronger model has likely seen more SPETLR, confounding capability with familiarity.
3. Whether act completeness generalises to layer completeness at all, which this design cannot address and which the foundation's warrant depends on.
