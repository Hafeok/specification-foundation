# [PROPOSED] Pre-registration: the residual-declaration mechanism

**Supersedes** `prereg-closure-falsifier.md`, retired under CG-R-17. That document tested a layer completeness predicate; this one tests the mechanism R-1 redirected the falsifier to. The retired document remains filed as the superseded design.

**Design input:** the fifteen defects recorded in the retired document's Gate 0 output, and `rulings-gate0-closure-falsifier.md`, which is `[DRAFT]` permanently under CG-R-18 and is cited here as input rather than as rulings.

**Status:** `[PROPOSED]`. Pre-registration. Nothing executed. Committed before execution; the items under §7 are fixed at commit and there is no re-roll.

---

## 1. Claim under test

**Declaring the residual does not settle open decisions. It changes where they land.**

Holding declared content constant, a specification that declares which properties it does not settle shifts open decisions from **escaped** — resolved silently by the actor, with consequence — to **surfaced** — raised as a question, or resolved with the resolution stated.

**Primary measure**, per run: `escaped / (escaped + surfaced)`.

**Prediction:** the ratio is lower in arm A than in arm B by more than the threshold fixed at §7.3. The threshold governs this section; a shift in the predicted direction that does not exceed it is not a result.

## 2. What a pass licenses, and what it does not

Licenses: that declaring the residual changes actor disposal of open decisions, at the scale and projection stated in §3.

Does not license: that the specification is correct; that outcomes improve; that the resolution condition holds; that anything generalises to other act types, other scales, or coarser composition. **Nothing downstream may present this result as a test of the resolution condition** (R-1).

## 3. Scope

**Act scale:** fine — a single act instance, not a composition. **Projection:** software. Per R-2 these are independent coordinates and both are stated because neither implies the other.

**Corpus:** SPETLR act types — Extractor, Transformer, Loader. Chosen because SPETLR **encodes almost nothing**: the roles are naming conventions over one abstract type, and the orchestrator's positional methods enforce nothing. Every consequential property must therefore come from the specification or from the actor, which is the condition an escape experiment requires. The earlier justification — that the type set is closed — was wrong and is not relied on.

**Act instances** are the type set crossed with a named vocabulary, per the fixed selection rule at §7.1. The experiment runs over instances, not types.

## 4. Arms

| Arm | Construction |
|---|---|
| **A** | Every category in the frame is either bound by a determination or carries an explicit declaration that no determination travels there. |
| **B** | **Derived mechanically from A** by removing the non-travel declarations only. Every bound determination remains, unchanged, unreworded, in the same order. |
| **C** | Arm B plus the instruction below, verbatim and identical across all acts. |

The derivation rule is what makes this an experiment rather than a demonstration. Nobody authors a weaker specification, so nobody chooses which categories go silent, and bound content is matched by construction rather than estimated.

**Volume.** Matching is on **determination count**, exact by construction. Word count is *not* matched and cannot be: A is B plus N declarations. The imbalance is reported per arm. The additional words in A are declarations of absence, not additional content, which weakens the effort objection without eliminating it. Arm C exists to absorb the remainder.

**Arm C instruction, pre-registered verbatim:**

> Before producing any output, identify every decision that this specification does not settle and that will affect the result. List them. Do not resolve any of them silently: for each, either ask, or state explicitly in your output that you resolved it and how you resolved it. If you are uncertain whether something is settled, treat it as unsettled.

This is written at full strength deliberately. A weak arm C that loses proves nothing. If this instruction matches arm A, the claim fails.

## 5. The decision frame

**Enumerated in advance from the ratified category list, never discovered from output.**

For each act instance, the decision set is the frame: every consequential-property category, for that act type, from the fixed list. The denominator is therefore identical across arms and independent of what any run produced.

This dissolves the materiality problem. Incidental resolutions — identifier naming, import order — do not enter the set unless a category covers them, so no reviewer threshold sets the denominator.

*Note on the retired design's D1:* its stated mechanism — that arm A binds more properties and so shrinks its own denominator — does not hold under the strip-only derivation, since bound content is identical across A and B. The defect is real by a different route: a set discovered from output varies with reviewer, output length, and run. The fix is adopted; the reasoning is corrected.

## 6. Classification

**Two stages, separately blinded. Neither reader sees both sides.**

**Stage 1** — a reader sees **output only**, never the specification, and marks each frame entry **surfaced** or **not surfaced**. Surfaced means raised as a question, or resolved with the resolution stated.

**Stage 2** — **bound** is read off the specification against the frame. With a fixed frame this is close to mechanical; where judgement is required it is a separate reader who never sees output.

`escaped` = in frame, not bound, not surfaced.

Single-stage blinding does not work and the retired design asserted that it did: a reader must see the specification to determine bound, and arm A's specification is identifiable on sight by its declarations.

**Rubric requirements:**

- **Correctness is irrelevant.** A silently resolved decision that happens to be resolved well is escaped. Reviewers drift toward scoring only wrong ones, which deflates escape counts in whichever arm produces better output — a bias aligned with the hypothesis.
- Inter-reader agreement is reported. Disagreement resolution is fixed at §7.4.
- **Surfaced questions about already-bound matters** are counted separately, as a rate per arm, with a ceiling fixed at §7.3 above which the run is invalidated for delivery failure. They are not silently excluded: arm A is the most declaration-dense and therefore the arm most likely to generate them, so excluding the class removes evidence against closure's legibility.

## 7. Fixed before execution

Once results are visible, none of these moves.

1. **Act instance selection rule.** Stated so a third party applying it reaches the same set. Instances, not types.
2. **The consequential-property category list, per act type.** A separate ratified artefact. Not authored in the executing session. If it can be adjusted after results are visible, passing becomes a matter of choosing categories and the predicate is unfalsifiable.
3. **Quantities and thresholds.** Instances, runs per arm, the effect threshold governing §1, the already-bound ceiling.
4. **The classification rubric**, with worked examples and disagreement resolution.
5. **Actor settings.** Model identifier and parameters, recorded per run, identical across arms.

## 8. Failure conditions

The claim fails if any holds:

- the ratio does not shift by more than the threshold
- **arm C matches arm A.** The mechanism is then reproducible by one paragraph of instruction and the structure is decorative. This is the expected outcome if the effect is prompt-shaped rather than structural, and it must be reported without softening.
- totals shift without the ratio shifting — evidence of thoroughness, not of the mechanism

## 9. Threats

**Corpus contamination.** SPETLR is public and on PyPI. Prior familiarity supplies determinations no arm's specification supplies, depressing escape rates across all arms and compressing the detectable effect. This runs *against* the hypothesis, so it is a power problem: the design must be powered for a smaller effect than intuition suggests.

**Blinding leakage.** Stage 1 output from arms A and C may be identifiable by the density of raised questions. Blinding to arm label is not blinding to arm. Reported, not solved.

**Actor settings drift.** Confounds everything if settings vary across arms. Verified per run.

**Secondary measures** — total frame size, retry count, rejection payload richness — are **descriptive only** and may never be used confirmatorily. No post hoc analysis of them enters the result.

## 10. Open

**The human control arm is undecided.** With it, the experiment discriminates missing ground from actor capability, and the cheapest wrong attribution — "wrong model, try a bigger one" — is refusable. Without it, every negative result is contestable as model choice, permanently, and that limit is stated wherever the result is cited.

With the arm this is a project. Without it, a session. The choice is a ruling and must be made before §7.3 is fixed, since it changes the quantities.

**Capability ladder versus single model.** A ladder locates a capability threshold rather than a specification defect, but interacts with contamination: a stronger model has likely seen more SPETLR, confounding capability with familiarity.

## 11. Execution

Sessions propose; they do not ratify their own pre-registration. The four items at §7.1–§7.4 are produced by a session that stops, are ratified, and are committed before any harness runs. Classification is outside both sessions and is not performed by the actor under test.
