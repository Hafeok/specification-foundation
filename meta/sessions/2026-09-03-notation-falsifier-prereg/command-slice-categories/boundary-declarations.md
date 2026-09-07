# [PROPOSED] Boundary declarations

**Status:** `[PROPOSED]`. Not ratified. Depends on supersession S-2, which is itself unratified.

**Why this exists.** The resolution condition treats a dangling reference as incompleteness: every ground requirement resolves in the fact vocabulary, every acceptance relation ranges over produced objects, every produced object has a producing act.

Applied without boundaries, this is false of every real specification. Some ground arrives from outside and no act in scope produces it. Some verdicts are delivered outward and no act in scope reads them. Both would register as dangling references, so the condition would fail every specification that touches anything, and a predicate that nothing passes is as useless as one everything passes.

Boundaries make the condition sound by converting *unresolved* into *declared unresolved*. This is the same move as declared extent: absence becomes a positive fact rather than an unexplained gap.

---

## B-1 — External ground

**Declaration.** An object may be declared **external**: required by an act in scope, and produced by no act in scope.

**Requirements on the declaration.** Each declared external object states:

- what it is, in fact vocabulary terms
- where it comes from, sufficient to identify the producing party
- its read provenance — the path by which the act obtains it
- its tick rate, or a statement that the tick rate is unknown

Tick rate is not decoration. It determines whether the object may be encoded or must be read at act time, and an external object with unknown tick rate is a staleness hazard that should be visible.

**What the declaration does not license.** Declaring an object external settles that the specification does not produce it. It does not settle its correctness, availability, or stability, and it does not transfer accountability for acts that depend on it.

**Candidates.** Regulation and standards; customer data; third-party service responses; environment and infrastructure facts; human intent arriving through channels the specification does not model.

---

## B-2 — Terminal verdicts

**Declaration.** An object may be declared **terminal**: produced by an act in scope, and read by no act in scope.

**Requirements on the declaration.** Each declared terminal object states:

- what it is, in fact vocabulary terms
- who or what consumes it outside the scope
- whether consumption is observable to any act in scope

That last field is the one that matters. A terminal verdict whose consumption is unobservable is a place where consequence leaves the system with no return path, which is where undetected divergence accumulates.

**Candidates.** Outputs delivered to users; notifications; exports to systems not in scope; audit records written and never read back by any modelled act.

---

## B-3 — Scope, and the honest consequence

Both declarations are relative to a declared scope. An object external to one specification is produced within another; a verdict terminal in one is ground in another.

This means the resolution condition is **scope-relative and not composable by default**. Two specifications each internally complete may leave a dangling reference between them: A declares an object terminal, B declares the same object external, and nobody has checked that what A produces is what B expects.

That gap is exactly the seam where divergence is predicted to concentrate. It is not a defect in the boundary mechanism — it is the mechanism making the seam visible instead of leaving it implicit.

**Closed by R-4.** The composition check is committed as a design constraint: where A declares an object terminal and B declares the same object external, the fact-vocabulary types must agree. It is mechanically stateable and is the highest-value check in the scheme, since it addresses the case the accrual argument identifies as most costly.

The build is deferred — it requires two conforming specifications to exist. The declaration fields below must not be designed in any way that forecloses it. Until it exists, the resolution condition holds within a scope only, and that limit is stated wherever closure is claimed.

---

## B-4 — Constraints on declaration

**Declaring is not free.** If external and terminal declarations cost nothing, the cheapest way to pass the resolution condition is to declare everything at the boundary. The condition would then be satisfied by a specification that resolves nothing.

Two constraints follow:

- the declaration fields above are mandatory, not optional; an external object without provenance or a terminal object without a stated consumer is not a declaration
- the ratio of declared-boundary objects to internally resolved objects is a reported measure, not a hidden one

**Ruled: reporting, no ceiling.** A ceiling is arbitrary and invites tuning to it, which converts a measure into a target. The ratio is reported per specification alongside the exception rate, and a specification whose boundary ratio is high is visibly one that resolves little — which is the information a reader needs, without a threshold anyone can argue with.

---

## Dependencies

- Requires S-2. Without the position reduction, ground and verdict are separate ontologies and these declarations have no shared object to attach to.
- The resolution condition itself is not yet written as canon. These declarations make it sound; they do not state it.
- No falsifier attached. The nearest candidate: a specification passing the resolution condition with boundaries declared should show fewer escaped decisions at the seams it declares than one without declared boundaries. Untested, and it is a different claim from the one the current pre-registration tests.
