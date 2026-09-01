# Session: closure falsifier — harness and execution

**Session kind:** build and execute. Runs only against a committed, ratified pre-registration.

**Commit this prompt to `meta/sessions/` before any canonical act, per `DDD-dec-20`. Session-neutral commit identity.**

---

## Standing rules

- You propose; Emil ratifies. Execution gates hold until ratified.
- `[PROPOSED]` on all proposals; three-register discipline in every gate output.
- British spelling.
- **Honest defect reporting.** If a run fails, is misconfigured, or produces something you did not expect, record it and correct going forward. Do not re-run to get a cleaner result. Do not amend and re-record. A discarded run is a recorded discarded run.
- No force-push. Supersession never rewrites.
- Name the weakest link in each gate output.

## Explicit prohibitions

- **Do not modify the pre-registration.** Not the category list, not the thresholds, not the act set, not the rubric. If you believe one is wrong, stop and say so; do not adjust and continue.
- **Do not classify outputs.** Classification is blinded and happens outside this session. Producing classifications here destroys the primary measure.
- **Do not act as the machine actor under test.** The actor is invoked by the harness at fixed settings and is a separate instance. You orchestrate; you do not perform the acts being measured.
- No re-roll. The act set is what the committed selection rule produced.
- No customer-identifying material anywhere in this session's outputs.

---

## Gate 0 — verify the pre-registration

Before anything else:

1. Confirm the pre-registration file exists in the repository and is committed.
2. Record its commit hash in the session log.
3. Confirm it contains all four artefacts: act set selection rule, consequential-property category list, quantities and thresholds, classification rubric.
4. Confirm whether the arm B derivation rule was ratified (see below).

If any of these fail, **stop**. Do not proceed and do not fill the gap yourself.

**Hold.**

---

## Gate 1 — harness skeleton

Build the harness with no specification content in it.

Requirements:

- Invokes the machine actor at fixed, recorded settings. Model identifier, temperature, and any other parameter are recorded per run.
- Captures full output per run, plus retry count and any rejection payloads.
- Records run metadata: arm, act, run index, timestamp, settings hash.
- Outputs are stored such that arm identity can be stripped for blinded classification. This is a hard requirement — if the storage format leaks the arm into the artefact a reviewer sees, blinding fails.
- Deterministic where it can be. Seeded, logged, reproducible.

**Hold.**

---

## Gate 2 — arm construction

Construct the three arms from the ratified category list.

**Arm A.** For each act, a specification in which every category is either bound by a determination or carries an explicit declaration that no determination travels there.

**Arm B.** Derived mechanically from arm A by removing the non-travel declarations only. All bound determinations remain, unchanged and in the same order. Nothing is reworded.

This derivation rule matters. It means arm B cannot be an unintentional straw man, and volume matching over bound content is automatic rather than estimated. If it was not ratified in the pre-registration, stop and raise it rather than adopting it here.

**Arm C.** Arm B plus a single fixed instruction to raise questions rather than resolve silently when uncertain. The instruction text is fixed once, recorded, and identical across all acts.

Report the volume measures per arm before running anything. If arms A and B differ materially on bound content, the derivation went wrong.

**Hold.**

---

## Gate 3 — dry run

Execute one act, all three arms, one run each.

Present:

- the raw outputs
- run metadata and settings
- retry counts
- any harness defects observed

Do not interpret the outputs. Do not classify them. Do not comment on which arm appears better.

**Hold.** This is the last gate before results exist and the design becomes unamendable.

---

## Gate 4 — execution

Run the full matrix at the committed quantities.

Record every run, including failures. If the harness breaks partway, record where, fix forward, and note in the log which runs preceded the fix.

**Hold.**

---

## Gate 5 — tabulation

Produce, without classification:

- run inventory, complete, including discarded runs and the reason for each
- volume measures per arm
- retry counts per arm
- an anonymised output bundle for blinded classification, arm identity stripped, with a sealed mapping held outside the bundle

State plainly what the tabulation does not establish. In particular it establishes nothing about the claim until classification is complete.

**Stop.** Classification and analysis are outside this session.

---

## Carried risks to restate in the session log

1. If arm C matches arm A after classification, the closure claim fails. This is the expected outcome if the effect is prompt-shaped rather than structural, and it must not be softened in reporting.
2. The machine actor's settings are a confounder if they vary across arms. Verify they did not.
3. Surfaced questions concerning matters already bound in the specification indicate a delivery defect, not evidence about closure, and are tabulated separately per the rubric.
4. This experiment is itself a governed act performed by a machine actor. Anything learned about specifying it well is evidence bearing on the claim, and should be recorded as observation rather than absorbed silently.
