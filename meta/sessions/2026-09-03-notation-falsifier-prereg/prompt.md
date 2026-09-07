# Session: notation falsifier — pre-registration artefacts

**Session kind:** proposal only. No harness, no execution, no arms authored.

**Commit this prompt and a bootstrap record to `meta/sessions/` as the first act. Session-neutral commit identity: `Claude <noreply@anthropic.com>`.**

---

## Standing rules

`canon-governance` holds the in-force rules; read them at the pinned commit and comply. **They are not restated here.** The ones bearing most directly on this session: three-register discipline, supersession never rewrites, a named principal on every record, session records, and prose describes what is in force and implemented — anything designed but not built carries a date and a marker.

Beyond them:

- You propose; Emil ratifies. Gates hold until an explicit ratification message.
- Report defects honestly, including in your own earlier gate output.
- Name the weakest point in each proposal.
- File arrived inputs with their sha256 before using them.
- Search enforcement, not only prose: a rule can be in force while stated nowhere, held in a schema or a required field.

## Explicit prohibitions

- **Do not author either arm.** Arm R and arm P are written after this pre-registration is ratified and committed, by separate authors, neither seeing the other.
- **Do not write the harness or run anything.**
- **Do not adjust the claim** to make it easier to satisfy.
- Do not proceed past a gate without explicit ratification.

---

## Context

The claim: *holding the determinations constant, a conforming notation leaves less to inference than prose carrying the same content.*

This is the **notation** claim. It is not the layer claim (whether declaring the residual changes behaviour) and not the accrual claim (whether decisions escape less over time). Those are separate propositions with separate falsifiers, and a result here licenses neither.

Read `prereg-notation-inference-load.md` before starting. It is the design; this session produces the four artefacts §6 leaves open, because those four determine what the measure means and drafting them in the executing session would be self-ratification.

The binding under test is in `domain-state-change-binding/`. Its schema, worked example and checks run — that is the notation arm R will use.

---

## Gate 0 — orientation

Without writing to the repository:

1. Restate the claim and the primary measure in your own words, including the floor.
2. List anything in the pre-registration you believe is unsound, ambiguous, or unfalsifiable as written.
3. Confirm from the binding what a conforming record actually contains, from the schema rather than the README.
4. State how the frame's two partitions — determined by the specification, declared residual — will be derived, and from what.

**Hold.**

---

## Gate 1 — the act and its determination set

Propose:

- **one act instance**, at act scale, in the software projection, with the rule by which it was selected stated so a third party would reach the same choice
- **its determination set** — the determinations both arms will carry, as content, not yet in either notation

Requirements:

- the act must be one a model can plausibly attempt end to end
- the determination set must include at least one of each allocation class: pinned, checked, residual
- the set must include at least one declared residual, or the floor in §1 is zero and the design loses its guard against invention over gaps

State the weakest point in the selection.

**Hold.**

---

## Gate 2 — the category list

The critical artefact. Take it slowly.

Propose the consequential-property categories for this act type. The frame is the denominator of the primary measure, and it partitions into *determined by the specification* and *declared residual*.

Requirements:

- **recognition, not recall.** A reader should be able to say whether a category is addressed without first reconstructing what the categories should have been.
- **fixed before execution, never adjusted after.** If it can be tuned once results are visible, the measure is unfalsifiable.
- **no frame leakage.** Category names must not appear verbatim in one arm and not the other. State how this will be verified before execution.
- state explicitly what the list omits, and why.

**Warn yourself here.** You can generate a plausible, well-organised category list in a minute. Plausible is not pre-registered, and fluency is not warrant. Present the list with its derivation so the basis of each category can be checked rather than accepted on presentation.

Note: this artefact is reused by the layer-claim pre-registration, which currently defers it. Draw it for this act type, not for this experiment.

**Hold.**

---

## Gate 3 — quantities, thresholds, and the floor

Propose:

- runs per arm, and why that number
- the effect threshold governing the claim
- how the floor is computed from the frame partition, and how a below-floor run is reported
- how content parity between arms will be verified before execution, and what failure invalidates
- how variance across runs is reported

State the smallest effect this design could detect, and say plainly whether that is smaller than the effect worth caring about.

**Hold.**

---

## Gate 4 — the classification rubric

Propose the rubric a blinded reader applies. Per frame category: **determined**, **inferred**, or **asked**.

Requirements:

- usable by a reader who has not read this session
- **states that correctness is irrelevant**, with a worked example of a correct inference scored as inference. Reviewers drift toward scoring only wrong resolutions, and unstated this deflates the inference count in whichever arm produces better output.
- **states that citation is not the measure.** Records carry identifiers and prose does not; an actor citing a record id would score determined by construction. Classification is against the frame and the specification's content.
- at least two borderline cases with the ruling stated
- how two readers disagreeing is resolved

**Hold.**

---

## Gate 5 — assembly

Assemble the four ratified artefacts into a single file for commit. No new content; nothing not ratified at Gates 1–4.

Then stop. Authoring the arms, building the harness, and execution are separate sessions.

---

## Carried

1. **The human control arm is undecided.** It changes the quantities, so it must be ruled before Gate 3 is fixed. Record the decision or the block.
2. **Arm P quality is the design's largest threat.** This session does not author it, but Gate 3 should state how parity and quality will be evidenced.
3. **Actor familiarity with YAML** runs for the hypothesis and is a validity threat, not a power one. The structured-prose secondary comparison is descriptive only.
4. One act instance establishes nothing about generalisation. State it wherever the result is cited.
