# [PROPOSED] The resolution condition

**Status:** `[PROPOSED]`. Depends on supersession S-2, unratified. Falsifier deferred per R-1: this condition is not what the current closure pre-registration tests.

**What it is.** The completeness predicate for a specification. It replaces the per-act category check the foundation was originally drafted around, and it generalises event modelling's information-completeness rule from data to the whole triple.

---

## Statement

A specification is complete when it contains no dangling references across act vocabulary, fact vocabulary and position.

**C-1 — Ground resolves.** Every object an act reads resolves to a type in the fact vocabulary, and is either produced by some act in scope or declared external.

**C-2 — Verdict resolves.** Every object an act writes resolves to a type in the fact vocabulary, and is either read by some act in scope or declared terminal.

**C-3 — Acceptance relations range over produced objects.** Every acceptance relation ranges over objects that some act in scope writes. A check over something no act produces is not a check.

Incompleteness is a dangling reference. Nothing else is.

---

## Scope of a single evaluation

The condition is evaluated at **one scale, within one projection, over one declared scope.**

- **Scale**, per R-2: acts compose, and the condition holds over the act set at a given granularity. It does not automatically hold at a coarser or finer one.
- **Projection**, per R-2: independent of scale. A specification at sector depth is evaluated against its own act and fact vocabularies.
- **Scope**: the boundary declarations are relative to it. An object external to one specification is produced within another.

**Consequence, stated rather than hidden.** The condition is **not composable by default**. Two specifications each internally complete may leave a dangling reference between them. That gap is addressed by the boundary composition check committed at R-4, and until that exists, closure is claimed within a scope only and must be stated that way wherever it is claimed.

---

## What passing does not establish

- **Not coverage of the act.** The condition closes over what the specification declares. It says nothing about whether the acceptance relations reach the consequential properties, which is the separate coverage measure and is reported separately.
- **Not correctness.** Every reference can resolve and every determination be wrong.
- **Not that the act vocabulary is right.** A specification over a badly drawn act set can resolve perfectly.
- **Not assurance.** A green run means well formed.

The condition makes incompleteness *statable*. It does not make specifications complete, and a specification that passes it may still leave most of the work to the actor — declared, rather than silently.

---

## Why declaration is not free

If external and terminal declarations cost nothing, the cheapest way to pass is to declare everything at the boundary, and a specification resolving nothing would pass.

The boundary declarations therefore carry mandatory fields, and the ratio of declared-boundary objects to internally resolved objects is reported per specification. No ceiling is imposed: a ceiling is arbitrary and invites tuning to it. Reporting with the exception rate is the discipline.

---

## Open

1. No falsifier. The candidate is stated in the boundary declarations and requires two conforming specifications to exist.
2. Whether C-3 should also require the converse — that every written object is ranged over by some acceptance relation. As stated it does not, which permits verdicts nobody checks. That may be correct, since not everything warrants a check, but it means the condition is silent on a real gap and the coverage measure carries it instead.
3. Whether the condition holds across scales when acts compose, or whether composition requires its own check. Currently unaddressed.
