# [PROPOSED] Hypothesis: actor-proximate accrual and seam clustering

**Status:** `[PROPOSED]`. Not ratified. ID to be assigned at ratification (next in the empirical hypothesis series).

**Origin:** session discussion, derived from the observation that developers begin at code because determination is actor-indexed and code is the store nearest a developer's repeated acts.

**Related-work status:** unchecked. Adjacent literature almost certainly exists (Conway's law, boundary-spanning coordination costs, knowledge-boundary research). Must be checked before this leaves `projected`.

---

## Statement

The hypothesis has two separable parts. Both are stated so that the second can fail while the first survives.

### H-a (mechanism)

An actor population accrues determinations into a store whose shape is determined by that population's own recurring acts. Determinations that the store cannot express are not thereby prevented; they are made at act time and left unrecorded.

Instances: developers accrue into code and code-shaped artefacts (abstractions, frameworks, DSLs, generators). Architects accrue into diagrams and models. Product roles accrue into tickets, roadmaps and backlogs. Each store is well fitted to its population's act vocabulary and drops what falls outside it.

### H-b (distribution)

If H-a holds, then escaped decisions are not uniformly distributed across a system. They cluster where the store shape changes — that is, at seams between actor populations — because a determination expressible in one population's store and not in the adjacent one has no carrier across the boundary.

---

## Falsifier

**H-b is false if**, on a corpus where escaped decisions can be detected and actor populations can be labelled, the rate of escaped decisions per unit of traffic across actor-population boundaries is not materially higher than the rate within a single actor population.

**H-a is false if** determinations that a population's store cannot express are found to be recorded at comparable rates by that population through some other carrier — that is, if the store shape does not predict what goes unrecorded.

Note that H-a can hold while H-b fails: populations may drop the same determinations, but divergence may still be distributed by traffic rather than by boundary.

---

## Measurement requirements

None of these exist yet. This hypothesis is not testable until they do.

1. **An escaped-decision detector.** Currently the uncovered-remainder column of the act index. Requires an operating decision store to produce a signal at all.
2. **Actor-population labelling** over the corpus, at a granularity that distinguishes population from team.
3. **A traffic denominator.** Raw counts are meaningless; the seam is visited more often by construction in most systems.
4. **A within-population control.** Divergence occurring inside one population, detected by the same instrument, or the comparison is between a measured rate and an assumed one.

---

## Confounders

Listed in descending order of threat.

**Detection asymmetry — the strongest threat.** Cross-population divergence is noticed because two parties meet and disagree. Within-population divergence is frequently invisible: one actor quietly does the same thing two different ways and nobody convenes. If the detector inherits this asymmetry, it will produce seam clustering whether or not the effect is real. Any instrument must detect within-population divergence by the same mechanism it uses across, or the result is unusable.

**Conway's law.** Seams between actor populations often coincide with organisational and architectural boundaries, which independently predict integration defects. The predictions overlap; distinguishing them requires cases where the actor-population boundary and the architectural boundary come apart.

**Team boundary is not actor-population boundary.** Two teams of developers share a store shape. A developer and a product owner do not. The hypothesis is about store shape, and labelling by team will test something else.

**Traffic concentration.** Seams carry more crossings, so more opportunities for divergence per unit time. Handled by the denominator, but only if the denominator is right.

---

## Relation to existing claims

- Depends on determination being actor-indexed. If the index had no actor position this hypothesis is unstatable.
- Supplies a mechanism for the existing observation that value density is highest at recurrent, multi-actor addresses. If true, it explains *why* rather than merely predicting where.
- Bears on the machine-actor case directly: a model is an actor population whose store shape is whatever it is handed, and the seam between it and any human population is new, unqualified, and by this hypothesis the place divergence should concentrate.

---

## Why it is worth filing now

It is measurable in principle, it falsifies cleanly, and it makes a prediction that the framework does not otherwise make. It also carries a real risk of being an artefact of detection, which is stated above rather than discovered later.

It should not be built on until measured. Nothing downstream may cite it as support while it remains `projected`.
