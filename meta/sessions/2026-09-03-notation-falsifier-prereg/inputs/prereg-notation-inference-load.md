# [PROPOSED] Pre-registration: notation and inference load

**Status:** `[PROPOSED]`. Committed before execution. The items under §6 are fixed at commit; there is no re-roll.

**Relation to the other falsifier.** `prereg-residual-declaration-mechanism.md` tests the **layer** claim — whether declaring the residual changes what an actor does with what is not settled. This tests the **notation** claim. They are separate propositions and can come apart in both directions: records could reduce inference while residual declaration does nothing, and residual declaration could work while the format makes no difference against well-written prose. Neither result licenses the other.

---

## 1. Claim under test

**Holding the determinations constant, a conforming notation leaves less to inference than prose carrying the same content.**

The comparison is **not** specification versus none, which is trivially true and tests nothing. It is the same determinations in two formats.

**Primary measure.** Per decision point in a fixed frame, the actor's resolution is classified:

| | Means |
|---|---|
| **determined** | resolved from the artefact — the actor retrieved it |
| **inferred** | supplied from elsewhere — convention, training, guess |
| **asked** | raised rather than resolved |

`inference rate = inferred / frame size`

**Prediction.** Inference rate is lower in the records arm than in the prose arm by more than the threshold fixed at §6.3.

**Floor.** Inference rate cannot legitimately fall below the declared residual — the frame categories nothing in the specification determines. A run below the floor means the actor is inventing over declared gaps rather than surfacing them, which is a failure presenting as a good result. Runs below the floor are reported separately and do not count toward the effect.

---

## 2. What a pass licenses, and what it does not

**Licenses:** that a typed record carries determinations more legibly to an actor than prose carrying the same content, at the act type and scale stated.

**Does not license:** that declaring the residual changes behaviour — that is the layer claim and this experiment does not test it; that the determinations are correct; that fewer decisions escape over time, which is the accrual claim and needs a corpus; that the notation is adequate.

**Stated before results are visible**, because a pass will be tempting to present as validating the framework. It validates one thing.

---

## 3. Arms

Both arms carry **the same determinations**. Nothing is added, removed, or reworded in content — only the form differs.

| Arm | Form |
|---|---|
| **R** | Conforming records: YAML against `determination.schema.json` — address, extent, allocation, acceptance with coverage, positions, provenance |
| **P** | Prose: the same determinations written as a well-formed specification document, in the style a competent engineer would write for a colleague |

**Arm P is authored at full strength.** A poorly written prose arm proves nothing. It is written by someone instructed to make the specification as clear as they can, given the same determination set, and it is not seen by whoever authors arm R. A weak P that loses is the easiest way to fake a pass, and this design's credibility rests on P being good.

**Derivation.** Arm R is authored first from the determination set. Arm P is produced from the same set by a different author who does not see arm R. Both are checked against the set for content parity before either is used: every determination present in one is present in the other, and no arm carries a determination the other lacks.

---

## 4. The frame

Enumerated in advance from the ratified category list for the act type, never discovered from output. The denominator is identical across arms and independent of what any run produced.

The frame is partitioned before execution into:

- **determined by the specification** — categories some determination settles
- **declared residual** — categories the specification explicitly states it does not settle

The second partition is the floor in §1.

---

## 5. Classification

**Blinded.** The reader sees the actor's output and the frame; the reader does not see which arm produced it, and does not see the specification during classification.

Per frame category: was the resolution visible in the output traceable to the specification, supplied by the actor, or raised as a question?

**Correctness is irrelevant.** An actor can infer correctly. A right answer arrived at by invention is still an inference, and it is the one that fails on the next act where the convention does not hold. Reviewers drift toward scoring only wrong resolutions; the rubric states this and inter-reader agreement is reported.

**Citation is not the measure.** Records carry identifiers and prose does not, so an actor citing a record id would score determined by construction. Classification is against the frame and the specification's content, never against whether the actor cited anything.

---

## 6. Fixed before execution

1. **The act.** One act instance, at act scale, in the software projection. The act and its determination set are fixed.
2. **The category list** for that act type. A separate ratified artefact, not authored in the executing session. If it can be adjusted after results are visible, the measure is unfalsifiable.
3. **Runs per arm and the effect threshold** governing §1, plus the floor computed from the frame partition.
4. **The classification rubric**, with worked examples and disagreement resolution.
5. **Actor settings.** Model identifier and parameters, recorded per run, identical across arms.

---

## 7. Failure conditions

The claim fails if any holds:

- inference rate does not differ by more than the threshold
- **the prose arm matches or beats the records arm.** Expected if the format's contribution is smaller than good writing, in which case the determination discipline could have been written in markdown — a genuinely useful finding that would change what a binding needs to be
- content parity fails — an arm carried determinations the other did not, so the comparison was never of format

---

## 8. Threats

**Prose arm quality.** The single largest threat, and the design's credibility rests on it. Mitigated by separate authorship at full strength and by content-parity checking. Reported: who wrote each arm, and whether they saw the other.

**Actor familiarity with the notation.** A model may handle YAML more readily than prose for reasons unrelated to the determinations it carries. This runs *for* the hypothesis and is a validity threat, not a power one. Partially addressed by running one arm as structured prose — headed sections, one determination per section — as a secondary comparison. Reported as descriptive only.

**Frame leakage.** If the frame's category names appear verbatim in one arm and not the other, the actor is being cued. Both arms are checked for this before execution.

**Actor settings drift.** Verified per run.

---

## 9. Open

**Human control arm undecided.** With it, a human performing the same act under both arms discriminates a notation effect from a model-specific one. Without it, a result is contestable as an artefact of how one model reads YAML. The choice changes the quantities and must be made before §6.3 is fixed.

**Single act.** One act instance establishes nothing about generalisation across act types. Stated wherever the result is cited.

---

## 10. Execution

Sessions propose; they do not ratify their own pre-registration. The four items at §6.1–§6.4 are produced by a session that stops, are ratified, and are committed before any run. Classification is outside the executing session and is not performed by the actor under test.

**Byproduct.** The category list produced at §6.2 is the frame the layer-claim pre-registration currently defers to a separate session. Running this first means that claim inherits a frame that has been exercised rather than one authored and never used.
