# Rulings CG-R-20 … CG-R-28 — notation falsifier Gate 0

**Issued by Emil, 2026-09-03.** Gate 0 is ratified. Gate 1 proceeds. Register rows owed to `canon-governance`, together with CG-R-17…19, which were ruled but never drafted as rows — that debt is mine and is the reason the layer pre-registration cites identifiers the register does not hold.

---

## CG-R-20 — The floor is removed. U-1 is a design defect, not an ambiguity.

The report is right and the error is mine. Under the classification as written, inventing over a declared gap scores **inferred** and *raises* the rate; surfacing it scores **asked** and does not. So a run that retrieves every determination and asks about every residual scores zero — the best run the design can produce — and the floor would exclude it.

**Ruled: the floor is struck from §1.** No lower bound. The measure already catches invention over gaps, because invention *is* inference; the floor was guarding against something the primary measure handles.

**Replaced with the guard that actually discriminates.** The failure mode worth watching is the opposite one: an actor that asks about everything, including matters the specification settles. That is cheap to produce and would depress inference rate without the notation doing anything.

> **Asked-over-determined rate**, reported per arm: questions raised about frame categories the specification settles, over the size of the determined partition. A ceiling is fixed at Gate 3, above which the run is invalidated for delivery failure — the artefact failed to deliver what it contains, which is a different defect from the notation being illegible.

**Secondary, reported not tested.** Asked-over-residual is the disposition the layer claim predicts. Report it; it is an observation about one arm's behaviour, not a test, because nothing here varies whether the residual is declared.

---

## CG-R-21 — The determination set closes against the frame. Gate 1 is provisional.

U-4 accepted. A category list drawn for the act type will contain categories the set neither settles nor declares residual, and a three-way partition would dilute the denominator equally in both arms — a power cost rather than a bias, but an avoidable one.

**Ruled:** every frame category is either **determined by the specification** or **declared residual**. The set closes against the frame after Gate 2.

**Consequence for the gate order:** Gate 1's determination set is ratified as **provisional**. Gate 2 draws the frame; the set is then closed against it and the closure is ratified before Gate 3 fixes quantities. Gate 1 is not reopened — closure adds, it does not revise.

---

## CG-R-22 — Counter-conventional determinations are required, and are the primary subset.

U-3 is the design's weakest point and the report is right that no ruling eliminates it. Retrieval and lucky inference are indistinguishable in the determined partition whenever a determination matches what a competent actor would default to.

It can, however, be **measured** rather than merely conceded.

**Ruled:** the determination set must contain determinations that **depart from convention** — resolutions a competent actor would not default to. Matching a counter-conventional determination is strong evidence of retrieval; matching a conventional one is not.

- The primary measure is computed **on the whole frame and on the counter-conventional subset separately**, both pre-registered.
- Gate 1 states, per determination, whether it is conventional or counter-conventional, with the basis.
- The minimum size of the counter-conventional subset is fixed at Gate 3.

If the effect appears on the whole frame and not on the counter-conventional subset, the result is consistent with the actor defaulting correctly rather than reading, and must be reported that way.

---

## CG-R-23 — Two-stage classification, as in the layer pre-registration.

U-2 accepted; §5 contradicts itself and single-stage blinding does not work here for the same reason it did not there.

- **Stage 1** — a reader sees the **output and the frame only**, never the specification, and marks each category **resolved** or **raised**.
- **Stage 2** — a second reader, seeing the **specification and the frame only**, never the output, records what each category's determination is.
- **determined / inferred** is computed by comparing the two, not judged by either reader.

Neither reader sees both sides, so neither can classify toward expectation.

---

## CG-R-24 — "Asked" for a single-turn actor

U-5. **Ruled:** a category is **asked** when the output explicitly identifies it as unsettled and either declines to resolve it or resolves it while stating that it did so and on what basis. Silent resolution is never asked, however reasonable.

A conversational turn is not required. What is required is that the actor's output makes the unsettledness visible to a reader who did not see the specification — which is exactly what Stage 1 can determine.

---

## CG-R-25 — No human control arm

**Ruled: none.** The confound it would address — that a model parses YAML more readily than prose for reasons unrelated to the determinations carried — is addressed more cheaply by the structured-prose arm, which is already in the design.

**Consequently that arm is promoted from descriptive-only to a pre-registered secondary comparison**, with its prediction fixed now, before any result:

> If structured prose performs comparably to records, the effect is **structure**, not schema. If records outperform structured prose, the schema is doing work beyond organising the text.

Pre-registering it now is legitimate; promoting it after seeing results would not be.

**The limit is permanent and stated wherever the result is cited:** this measures how one actor class reads two notations. It is not a claim about notations in general.

---

## CG-R-26 — Structured-prose arm authorship

U-8. **Ruled:** authored by arm P's author, from the same determination set, **after** arm P is complete. It is arm P reorganised — headed sections, one determination per section — not a third independent composition. The comparison is structure versus schema, and a differently-authored third arm would vary content quality as well as form.

---

## CG-R-27 — The worked example is not reusable

U-9 accepted. `PlaceOrder` and its determination set ship in the binding, in arm R form, and are in the training-adjacent context of anyone reading the repository. Gate 1 selects a different act, and states that it did.

---

## CG-R-28 — The Gate 0 report commit stands

The judgement call was correct. My prompt's instruction was the CI-1 defect: Gate 0 output that is not a repository object cannot be retrieved later, and the falsifier session that followed that instruction literally produced its most substantive artefact as chat text that now exists nowhere.

**Ruled:** Gate 0 output is filed. The prompt's wording is the defect and is recorded as such; the file is not struck. This is prior art for the CI-1 proposal against `canon-governance`, which remains unwritten.

---

## Carried

- **Runner defects** in the binding: `run_all.sh` exits green when a schema check crashes, and its record counts are hardcoded labels. Both are real; neither blocks this session. An instrument that reports success when it did not run is the same defect class as a proxy without its divergence.
- **Register debt.** CG-R-17…19 and this batch are owed rows in `canon-governance`. Mine.
