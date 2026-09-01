# BOOTSTRAP — seeding programme

Orientation for a session picking this up cold. Read this before the session prompt.

**Precedence.** This document is orientation; the session prompt is the instruction set. Where they disagree, the prompt wins, and the disagreement is reported at Gate 0.

**Scope.** This copy is for the `specification-foundation` seed. `canon-governance` was seeded first and is complete.

**Status of everything here: `[PROPOSED]`.** The bundle establishes repositories with governance, validators and provenance intact. It does not establish that anything in them is true. A well-organised repository reads as more settled than its contents are, and this note exists partly to counteract that.

---

## 1. What is being built

A specification language foundation: what must be expressible for a specification's completeness to be decidable, and the criterion by which someone else's language can be checked against it.

It sits in a chain of repositories with **three distinct relations**. Getting these wrong is the most likely structural error, because "downstream" reads as projection by default.

| Repository | Relation | Holds |
|---|---|---|
| `canon-governance` | governs all others | rules for producing and ratifying canon |
| `actor-indexed-determination` | root | actor, capability, accountability, the index |
| `decision-driven-design` | projects from root | software projection |
| `specification-foundation` | projects from root, peer of DDD | construct list, resolution condition, boundary declarations, conformance criterion |
| `specification-languages` | conforms to foundation | bindings; also holds the engineering process for now (R-5) |
| `product-cli` | downstream of the process | tooling |

| Relation | Rule | Failure mode |
|---|---|---|
| **projects from** | determinations added, never contradicted, forward only | a projection cannot fail its upstream |
| **conforms to** | criterion satisfied, evidence published | a conforming instance *may* fail |
| **governed by** | compliance, no derivation | non-compliance is a defect, not a variant |

`governed by` points sideways, not up. Nothing derives from `canon-governance`; everything complies with it. It is not a root above the root.

---

## 2. Order of work

1. ~~Seed `canon-governance`~~ — **done.** Ten rules filed, four refused, two markers and a half, no CI, no verdicts permitted.
2. **Seed `specification-foundation`** — `session-seed-specification-foundation.md` ← **this session**
3. Falsifier work — separate, and blocked on decisions noted below

Governance first was deliberate, and it means the session-record convention is **inherited** here rather than declared native. Note what `canon-governance` did *not* settle: `registry/governed.yaml` is empty pending a ruling on governance start points, so its rules are in force as rules and no instrument evaluates anything.

---

## 3. Settled — apply, do not re-litigate

- **ID prefixes.** `SF-` for `specification-foundation`. `CG-` for `canon-governance`. `DDD-` is taken.
- **Terminology (R-2).** *Layer* = projection depth. *Scale* = granularity of act composition within a projection. **Independent coordinates, not a hierarchy.** Nothing about a position on one implies anything about the other.
- **Actor instances (R-3)** are declared per specification, not held in a vocabulary. Kinds come from Layer 1 and are stable; instances are deployment facts and tick fast.
- **Attribution** is to Emil personally, not to a future custodial body, with a sentence stating the editorial role is intended to transfer.
- **`meta/sessions/`** is held in `canon-governance` as CG-rule-06 and inherited here. The earlier proposal targeting Layer 1 is superseded in full and retained showing why.
- **Compliance is asserted downward.** `canon-governance` holds the registry; no repository declares that it is governed. Do not add such a declaration.
- **Governance is orthogonal** — a third axis, neither up nor sideways. Nothing is projected from it; everything complies with it.
- **Rulings live in `canon-governance`**, series `CG-R-`, one authority. Sessions propose and never issue.
- **Governance rules are not restated downstream.** Cite `canon-governance` at its commit. Duplicating them recreates the state that repository exists to end.
- **Extraction is supersession, not copy.** Rules moving into `canon-governance` leave superseding records behind. No source repository is modified by a seeding session.

---

## 4. Core positions a session needs to hold

**The addressing claim.** Decisions must be retrievable by the act being performed, because the person who needs a decision is the one who does not know it exists. Topic-indexed documentation fails structurally, not through neglect.

**Read address equals write address.** Acting produces determinations the specification did not contain. If they do not return to the address they were read from, the store is stale from first use. This has dropped out of the design repeatedly and is the property nothing else in the field has.

**Position, not ontology (S-2).** Ground and verdict are roles relative to an act, not separate vocabularies. A specification carries an act vocabulary, a fact vocabulary, and position. Read position is ground; written position is verdict.

**The resolution condition** is the completeness predicate: no dangling references across act, fact and position. Evaluated at one scale, within one projection, over one declared scope. Not composable across scopes by default.

**Coverage is not assurance.** Coverage is computable against a frame; whether the frame names the properties that matter is not. Do not emit 100%. The valuable output is the uncovered list, not the score.

**Derivation runs forward only.** Reading acts backwards out of existing code is prohibited. An extractor produces *evidence about* an act vocabulary for ratification, never the vocabulary itself.

---

## 5. Known open, carried

1. **The falsifier tests a different claim from the resolution condition** (R-1). It tests whether declaring the residual shifts open decisions from escaped to surfaced. Nothing may present its result as a test of the resolution condition.
2. **The conformance relation has no validator** and will not have one after these seeds. Recorded, not closed.
3. **C-3's converse is unresolved** — the resolution condition permits a written object no acceptance relation ranges over. Probably correct; means the condition is silent on a real gap that coverage must carry.
4. **Composition across scales** is unaddressed. Whether the condition holds when acts compose, or needs its own check.
5. **Boundary composition check** (R-4) is committed as a design constraint, build deferred. Requires two conforming specifications.
6. **Related-work checks are thin.** Only the closure claim has been checked, against six sources. The accrual claims, the extent-declaration claim and the authorisation findings are unchecked.
7. **Governance start points are unruled** (CG-R-9), so `canon-governance` governs nothing operationally. Its rules bind as rules, not as checks.
8. **Two of the ten governance rules are provisional** — CG-rule-08 and CG-rule-10 — resting on the seeding session's account of its own practice. In force; not citable as established.
9. **Nothing checks the governing acts.** Every instrument points outward at governed repositories; the `CG-R-` series was breached by its own issuing authority within a day and was caught by a person reading a register. Four such instances now, no instrument, no rule — an absence is not a practice.

---

## 6. What a seeding session must not do

- author canon content; it files what arrives and proposes placement
- resolve inconsistencies between arrived documents — report and hold
- substitute a plausible artefact for one that did not arrive
- modify a source repository
- proceed past a gate on its own assessment that the output looks right

---

## 7. Bundle contents

```
BOOTSTRAP.md                                    this file
session-seed-specification-foundation.md        the instruction set
seed-bundle-checklist.md                        decisions, inputs, order
CITATION.cff                                    date-released outstanding
inputs/
  specification-language-foundation.md            canon, ORIGINAL STATE
  supersession-foundation-construct-list.md       provenance, two supersessions
  resolution-condition.md                         canon
  boundary-declarations.md                        canon
  rulings-session-close.md                        R-1..R-6
  rulings-gate0-closure-falsifier.md              falsifier rulings
  prereg-closure-falsifier.md                     evidence, not canon
falsifier/                                      two session prompts
reference/                                      holding notes, hypothesis, assessments
```

**Read `canon-governance` at its recorded commit.** `rules/` holds the ten in-force rules; they are not reproduced in this bundle by design.

**One arrived input is not in this bundle and must be supplied from its repository:**

- the prior falsifier session's Gate 0 output, from `claude/closure-falsifier-prereg-w1mm7d`

Reconstruction is not acceptable. It carries the arrival record and hashes that filing rules exist to preserve.

**`specification-language-foundation.md` must be filed in its original state**, not resolved against the supersession record. The falsifier's category list derives from it and the derivation needs both states.
