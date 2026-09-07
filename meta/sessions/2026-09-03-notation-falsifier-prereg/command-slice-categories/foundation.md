# [PROPOSED] Foundation of the specification language

**Status:** `[PROPOSED]`. Not ratified. No falsifiers attached to the design constraints below; several are stated as requirements derived from the closure claim, and inherit its unratified status.

**Method.** Nothing here is designed forward from taste. Every requirement is derived backwards from one question: what must be expressible for layer completeness to be decidable? A construct that is not needed for that, or for the write side, is not in the foundation.

**Naming.** `protocol` is unavailable — He and Yu used it in May 2026 for an adjacent construct. See the closing section; the artefact may already be named in canon.

---

## 1. The design driver

A layer is complete when every determination that could bind acts in that layer either binds there or is declared not to travel there.

This is a universal quantification over acts, evaluated against declared extent. Everything the language must express follows from making that sentence decidable:

- quantification requires a **closed, countable act set**
- *binds there* requires **determinations addressed to acts**
- *declared not to travel* requires **extent as a positive statement**
- *decidable* requires every predicate involved to be **operationally closed**, not merely well formed

A language that expresses less than this cannot state its own completeness. A language that expresses more is carrying constructs the predicate does not need, and each one is a place where filing becomes a judgement call.

---

## 2. What must be expressible

Presented in dependency order. No construct refers forward.

### 2.1 Act

The unit of address. Named, countable, and closed for a bounded scope.

Closure of the act set is not a nicety. Without it there is nothing to quantify over and completeness is unstatable. This is also the property that most architectures fail to supply, which is why the language cannot be defined independently of an architecture that names acts.

An act is a happening, not a thing. If a name in the act set can be read as a noun denoting a component, it is a topic and the address space has been compromised.

### 2.2 Ground requirement

What an act must have available to be performable, with provenance.

Provenance is not optional and cannot be deferred. Two actors with nominally identical ground and different read paths are not substitutable, and a record that omits the read path cannot support the substitution question later.

### 2.3 Determination

Something settled, addressed to an act.

A determination floating free of an address is a prose rule, and prose rules are the failure mode the whole scheme exists to avoid. The language should have no way to express one.

### 2.4 Extent

The axes a determination travels on, and where it stops.

Four states must be distinguishable, and the fourth is the one that is usually lost:

| State | Meaning |
|---|---|
| bound here | applies at this address only |
| travels to X | applies across the named region |
| does not travel to X | stated boundary; a positive fact |
| silent on axis A | the axis was not considered |

*Silent* is not the same as *does not travel*. A determination filed before an axis existed is silent on it; one filed after and deliberately bounded is not. Collapsing these makes the revisit computation unsound the first time a new axis is added, and the loss is unrecoverable after the fact.

**Default extent is the narrowest.** Travel is the deliberate act that costs something. Any other default reintroduces judgement at write time and placement stops happening.

### 2.5 Allocation

Who carries the determination. Mandatory; a determination without an allocation is not well formed.

Three classes, exhaustive:

- **pinned** — settled in advance; the act has no discretion
- **checked** — discretion exists, and a predicate settles acceptability regardless of producer
- **residual** — discretion exists and no predicate reaches it

For residual, the language must record which actor carries it and which principal answers for the outcome. The principal is a role a machine actor cannot occupy.

### 2.6 Acceptance relation

For checked determinations: the predicate, and its closure status against the ground and tools the arrangement actually has, at the stated tolerance.

Two requirements distinguish this from an assertion of quality.

**Predicate form, not extension.** State what admits, do not enumerate what is admitted. Enumerations are silently incomplete and their incompleteness is invisible. There is independent evidence that predicates are more reliably authored than the sets they induce.

**Operational closure, not logical closure.** A predicate that is decidable in principle and unrunnable by this arrangement at act time is not a specification. The language must record which of the two has been established, because they are routinely conflated.

### 2.7 Coverage and residual

For each acceptance relation: which consequential properties of the act it reaches, and which it does not.

This is the construct that distinguishes the language from every adjacent approach. Elsewhere the conjunction of constraints is treated as defining the admissible space by fiat, and the uncovered remainder is invisible. Here it is named.

The residual is not a defect to be minimised to zero. It is the part that must be allocated to an actor competent to carry it, and it cannot be allocated if it cannot be seen.

Where a predicate stands in for another, three fields are required: the proxy, the original predicate, and the known divergence. A proxy recorded without its divergence is a coverage claim that overstates itself.

### 2.8 Provenance and supersession

Who settled it, when, and what it supersedes.

Correction files a superseding record; it does not rewrite. A determination whose extent has been narrowed twice is evidence about the original extent claim, and that evidence is destroyed by editing in place.

---

## 3. Properties the language must have

Stated as properties, not mechanisms.

**It is closed under its own completeness predicate.** The language can express the check that decides whether a layer is complete. If it cannot, the closure claim is decorative.

**It is symmetric across build and act time.** The same schema expresses a determination taken in advance and one produced while acting. Any asymmetry bifurcates the store and the second half rots. This is the property no existing specification language has, and it is the one that stops the method being a waterfall.

**Filing requires no judgement about location.** The act supplies the address. If an author must understand a taxonomy before recording something, recording will not happen.

**Silence is expressible.** *This layer does not settle X* is a statement the language can make. Absence must never be the only way to say it.

**Generality is expensive and specificity is free.** The inverse of a prose rules file, where generality costs nothing and rots the artefact.

**Every quantitative construct declares its measurement.** Tolerance, assurance and coverage are unusable without stated units and a stated instrument.

---

## 4. Non-goals

Naming these prevents the language absorbing work it should not carry.

- **Not executable code, and not a generator input.** It allocates determinations; it does not produce implementations.
- **Not a domain ontology.** It carries decisions about acts, not a model of the world the acts operate on.
- **Not a replacement for the act vocabulary's own artefacts.** The architecture produces the act names; the language addresses them.
- **Not complete over outcomes.** It closes over its own declared scope. Completeness of the specification is not coverage of the act, and conflating the two would sell closure as assurance.
- **Not an elicitation method.** How determinations are arrived at, prioritised, or disagreed over is untouched.

---

## 5. Open

1. **Falsifier for the closure requirement.** A specification passing the layer completeness predicate should show measurably fewer escaped decisions than one failing it. Until measured, section 1 is an assertion.
2. **Whether the axis set is a clean product.** Sectors carry act vocabularies and impose acceptance relations, so sector and act interact. If the axes are not independent, extent is not a Cartesian region and the completeness predicate must close over the actual shape.
3. **Related-work check.** Design-by-contract, Z and B, ADLs, policy languages, and the invariants-plus-evidence line all occupy adjacent ground. Only the closure claim has been checked, against six sources.
4. **Name.** The artefact written in this language may already exist in canon as the What — a store allocation declaring which determinations a built actor carries over run acts. If so, the language is the language in which a What is written, and no new name is required. Deciding this is cheap now and expensive after adoption.
