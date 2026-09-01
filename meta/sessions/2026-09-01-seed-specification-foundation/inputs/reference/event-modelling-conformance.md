# [PROPOSED] Event modelling assessed against the specification language foundation

**Status:** `[PROPOSED]`. Assessment, not ratification. Reads against `specification-language-foundation.md`, which is itself unratified.

**Question.** The foundation states what must be expressible for layer completeness to be decidable. Event modelling is claimed as the method that supplies the act vocabulary. Does it meet the foundation, and where does it not?

**Summary.** Event modelling supplies the address space, a partial ground discipline, the mechanical-placement property, and — significantly — an existence proof that an operationally closed completeness predicate is achievable in practice. It supplies nothing for extent, coverage, residual, provenance or write-back. On one point it actively conflicts with the foundation, and that conflict has to be resolved rather than absorbed.

---

## 1. Conformance against section 2

| Construct | Status | Basis |
|---|---|---|
| 2.1 Act | **Supplied** | Slices: command, view, automation, translation |
| 2.2 Ground requirement | **Partial, strong** | Information completeness rule, data only |
| 2.3 Determination | **Not supplied** | Method produces addresses, not determinations |
| 2.4 Extent | **Not supplied** | No notion of travel across slices |
| 2.5 Allocation | **Partial, weak** | Swimlanes allocate acts, not determinations |
| 2.6 Acceptance relation | **Partial, conflicting** | Given-when-then; extension form |
| 2.7 Coverage and residual | **Not supplied** | Scenarios never declare what they omit |
| 2.8 Provenance, supersession | **Not supplied** | Design-time artefact |

### Where it is strong

**2.1 Act.** This is the reason for the claim and it holds without qualification. The method's atomic unit is a slice, and a slice has the shape of an act: something initiates it, it consumes declared information, it produces a defined outcome. The vocabulary is finite and enumerable for a bounded scope, which is the property completeness quantifies over.

The grammar of the method resists nouns. It is difficult to name a slice with a thing rather than a happening, and that resistance is what keeps the address space from degrading into topics. No other mainstream method has this property; domain-driven design, layered architecture and C4 all produce nouns.

Recurrence exists at two levels — every command slice shares a shape with every other, and each has its own specifics — so determinations can attach either to the pattern or to the instance. That two-tier structure is the amortisation the accrual argument depends on.

**2.2 Ground requirement.** The information completeness rule requires that every piece of information appearing on a view trace back to an event that put it there. That is a per-act declaration of required inputs with provenance, enforced at design time, and it is the closest thing in mainstream practice to the foundation's requirement.

It is bounded to data. It says nothing about which conventions, prior determinations or rules an act requires, which is the other half of what an act needs to be performable. So the discipline exists and its scope is narrower than the foundation needs.

### Where it is absent

**2.4 Extent** is the largest structural gap. Cross-cutting concerns — authorisation, observability, error handling, audit — are not slices, and the method has nowhere to put them. In practice they escape to a document, which is the failure the whole scheme exists to prevent. The gap is not incidental: it is the direct consequence of having an address space and no travel relation over it.

**2.7 Coverage and residual** is the gap that matters most for assurance. Given-when-then scenarios assert what must hold; they never state which consequential properties they leave unreached. This is the same defect found in the invariants-plus-evidence line: the conjunction of stated criteria is treated as defining acceptability by fiat.

**2.8 Provenance and write-back.** The model is produced in a workshop, drawn, photographed, and then drifts. Event sourcing rescues the act *names* at runtime, because acts acquire durable identity in the running system and drift breaks things. It does not rescue determinations. Nothing in an event store holds what was decided about how a slice should be built.

---

## 2. The conflict

**Given-when-then is extension, and the foundation requires predicate.**

Scenarios enumerate cases. The foundation requires acceptance relations stated as predicates — what admits, rather than a list of what was admitted — on the grounds that enumerations are silently incomplete and their incompleteness is invisible. There is independent evidence that predicates are both more reliably authored and more reliably checkable than the sets they induce.

This is not a gap to be filled. It is a disagreement, and one of the two positions is wrong.

The foundation's position is the defensible one, and it means event modelling's acceptance criteria must be **promoted** rather than adopted. A scenario set is evidence about a predicate and a useful starting point for writing one. It is not itself the acceptance relation, and treating it as such imports exactly the silent incompleteness the foundation was constructed to avoid.

Practical consequence: wherever a slice arrives with scenarios, the specification work is to state the predicate the scenarios were sampling, record its operational closure status, and keep the scenarios as tests rather than as the specification.

---

## 3. Conformance against section 3

| Property | Status |
|---|---|
| Closed under its own completeness predicate | **Partial — see below** |
| Symmetric across build and act time | Not met |
| Filing requires no judgement about location | Met, inherited from the act index |
| Silence is expressible | Not met |
| Generality expensive, specificity free | Met, structurally |
| Quantitative constructs declare measurement | Not met |

Two of these deserve comment.

**The completeness predicate — the strongest finding in this assessment.** The information completeness rule is an operationally closed completeness predicate. It is mechanical, it terminates, it runs against the model itself, and a model either passes it or does not. Its scope is narrow — data appearing on views — but within that scope it does precisely what the foundation demands and it was arrived at independently, for unrelated reasons, years before anyone was arguing about specification closure.

That is an existence proof. The foundation's central requirement is not speculative; it has been implemented once, at small scope, by practitioners who were not trying to satisfy it.

**Generality is expensive, and the same property produces the defect.** Slices are specific by construction and there is nowhere to record a general rule. That is exactly the incentive shape the foundation asks for, and it is also why cross-cutting determinations escape. One property, one benefit, one defect. Adding a travel relation must not invert the incentive while closing the gap.

---

## 4. Where the actor position already sits

Swimlanes separate human-initiated slices from automation-initiated ones. The method drew the distinction into its notation long before delegation to machine actors was a concern, and treats it as a diagram convention.

Reading a swimlane as an index position rather than a lane is a reinterpretation of an existing artefact, not a new demand on practitioners. That matters considerably for adoption.

What it does not supply: a swimlane is a role, not an accountable principal. Nothing in the method names who answers for an outcome, and nothing distinguishes pinned, checked and residual allocation. The accountability leg comes entirely from outside.

---

## 5. Verdict

Event modelling meets the foundation on the one requirement that cannot be retrofitted — a closed, verb-shaped, countable act set — and supplies a partial ground discipline and a working example of an operationally closed completeness predicate.

It does not meet the foundation on extent, coverage, residual, allocation classes, provenance, or write-back. Its acceptance mechanism is in the wrong form and needs promoting.

**The correct claim is therefore narrow.** Event modelling supplies the address space and the placement property. Event sourcing makes the addresses durable at runtime. Everything the foundation adds is genuinely absent from both, which is what makes the position defensible: it is not a repackaging, and the gaps are nameable one by one.

---

## 6. Open

1. Whether the information completeness rule can be generalised beyond data to determination ground, or whether the two need separate predicates.
2. Whether adding a travel relation over slices can be done without inverting the specificity incentive identified in section 3.
3. Related-work check on the scenario-to-predicate promotion. Property-based testing and specification-animation literature occupy adjacent ground and may have settled it already.
