# Supersession record — extract

**Extract, not the whole document.** Source: `supersession-foundation-construct-list.md`, sha256
`0c2c17cce8e9abe01b7a1dbc27a5e8148ce0bb31cfcacc9436e01a215940b700`, 75 lines. Extracted: §S-1 lines 11–33 and §S-2 lines 38–70 — each supersession's retired
position, superseding position, basis and consequence, verbatim. Not extracted: the document's
header and status lines (1–9), the two *Open* subsections (34–37, 71–75), and the horizontal rules
between sections. Every extracted line is byte-identical to the source.

---

## S-1 — Specification is a peer projection, not a child

### Retired position

The foundation was drafted with specification-driven development treated as a layer above the software projection, in an ordering of actor → specification → decision. The construct list was written without ruling on where the specification projection sits relative to `decision-driven-design`.

### Superseding position

Specification is a **peer projection** of the decision layer, alongside the software projection. Both project from `actor-indexed-determination`. Neither depends on the other.

### Basis

The retired ordering contains a forward reference. A specification is a set of decisions taken in advance; closure is a property of decisions declared with their extent; slices, acceptance relations and the pinned/checked/residual partition are all decision vocabulary. A layer cannot sit above the layer supplying its primitives.

The peer reading is admitted on the structural test rather than on preference: the specification projection has vocabulary the software projection does not need — specification, closure, releasable increment — so it is not a naming variant.

### Consequence

- Two projections, therefore two completeness predicates and two term registries, with a drift check between them. This is a real cost of the peer ruling and is accepted knowingly.
- The conformance relation to `specification-languages` is **not** projection and requires separate rules. A conforming instance may fail the criterion; a projection may not fail its upstream.

### Open


---

## S-2 — Ground and verdict are positions, not ontologies

### Retired position

The construct list treated ground requirement (§2.2) and the objects an acceptance relation ranges over as separate constructs, and a later session framing proposed three ontologies per specification: verdict, ground, and act.

### Superseding position

Ground and verdict are **roles an object occupies relative to an act**, not separate vocabularies.

A specification carries:

- **act vocabulary** — what can be done
- **fact vocabulary** — the type space of objects acts read and write; the domain model
- **position** — whether a given object is read or written by a given act

Read position is ground. Written position is verdict.

### Basis

The reduction was reached by way of a rejected argument and a sound one. Both are recorded, because the rejected one will be re-proposed otherwise.

**Rejected.** *A verdict's outcome varies with the actor, therefore verdicts are ground.* Actor-variance cannot be the criterion. Under actor-indexed determination everything varies with the actor; that is what the index is for. What varies is the determination — the mapping from what an act reads to what it produces — and variance is a property of the mapping, not evidence about position.

**Sound.** The verdicts of prior acts are what later acts read. This is why event sourcing functions as an outcome record: the log of past outcomes is the ground for future acts. Ground and verdict are therefore the same objects in different positions, and modelling them as separate ontologies duplicates the type space and loses the relation between them.

### Consequence

- Position must remain marked. Merging without it makes acceptance relations unstatable, because an acceptance relation ranges over what an act **produces**.
- The completeness predicate becomes a **resolution condition** across act, fact and position: every ground requirement an act declares resolves in the fact vocabulary; every acceptance relation ranges over objects some act produces; every produced object has a producing act. Incompleteness is a dangling reference.
- This generalises the information-completeness rule from data to the whole triple.
- Two sets do not fully overlap, and the resolution condition is unsound without declarations on both sides: not every verdict becomes ground, and not all ground is a prior verdict. See the boundary declarations.

