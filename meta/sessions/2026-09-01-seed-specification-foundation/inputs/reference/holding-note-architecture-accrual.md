# Holding note: why architecture determines whether decisions accrue

**Status: [PROPOSED].** Nothing here has been through a gate. No falsifiers pre-registered. Related-work check has run against six sources on the closure claim only; the accrual claims below are unchecked against prior art.

**Purpose.** Capture the composition and architecture argument before it decays, in a shape that can become a deck for a leadership group containing technical people.

**Audience assumption.** A group that can be moved by a mechanism rather than a testimonial, that has personally watched a documentation initiative fail, and that will ask what it costs and what breaks. If the actual audience is a client's leadership rather than ours, the ask slide changes but nothing else does.

---

## The argument in one line

Decisions only pay back if a later piece of work arrives at the same address to collect them — and architecture is what determines whether work arrives at the same address twice.

---

## Slide skeleton

### 1. The cost that moved
Transcription collapsed. The number of decisions in the work did not. Whatever fraction of the day was typing is now available; the decisions are the whole job.

*Speaker note: this is the only slide that needs no evidence. Everyone in the room has felt it this quarter.*

### 2. The failure everyone has already paid for
Two parts of the system resolve the same question differently. Nobody disagreed. The second team never knew the first decision existed. The bill arrives at the seam, months later, as "inconsistent handling of X."

*Have one real example ready, pseudonymised. This slide fails without it.*

### 3. Why our docs didn't prevent it
They are addressed by subject. Work is addressed by task. To find something in a subject index you must already know it exists — which is precisely what the person who needs it does not know.

*This is the slide where technical people stop being sceptical and start agreeing, because it explains a failure they have blamed themselves for.*

### 3b. A task that feels completely settled
Take one endpoint. Return a list of customers by subscription type. The data is already in the database. Nothing to design; just write the code.

Now list what that sentence does not settle:

- who may call it, and whether a caller may query subscription types other than their own
- whether deleted, soft-deleted, and lapsed customers are in the result — and whether a lapsed subscription is the type they hold or held
- paginated, capped, or unbounded; ordering, and whether ordering is stable
- what an unknown subscription type returns, and what zero matches returns
- which fields of a customer record the caller sees
- whether a replica read is acceptable, and what staleness is tolerable
- what surfaces on failure, and whether customer identifiers may be logged

Seven decisions. All will be made. Most will be made sensibly. None of them is written anywhere, and nobody will know which way they went.

*This is the strongest slide in the deck and it needs no client example, so it cannot be argued with on the grounds that the example was unrepresentative. Ask the room to add to the list before showing the rest — they will, and that is the point landing.*

### 4. Everyone else already solved the addressing problem
Checklists, protocols, work instructions, runbooks. Aviation, medicine, manufacturing, and our own incident response all index by the act being performed. Software is the outlier.

*Moves the burden of proof. We are not proposing something novel; we are asking why software should be exceptional.*

### 5. Accrual needs recurrence
A decision recorded at an address that is never visited again is a diary entry. Value requires that the same act shape recurs.

**So the precondition is not volume. It is that work has repeated, nameable shapes at all.**

### 6. That is what architecture supplies
An architecture constrains work into a small set of named, recurring act shapes. Add a command. Add a projection. Handle a policy.

Architectures that name *components* — `UserService`, `OrderManager` — name topics, not acts. They put us back at slide 3, one abstraction up.

**Consequence: architecture choice determines whether a decision store can accrue at all.** This is the claim the deck exists to make.

### 7. The familiar proof: every CMS
Pages and components. A closed vocabulary of component types, each carrying decisions settled once — accessibility, responsive behaviour, brand, semantics — composed into an unbounded space of pages. Nobody re-decides heading contrast on page 4,000.

And every CMS ships a custom HTML block, where every one of those guarantees is void. That is the residual, with a UI. Use it; it makes the limit concrete without argument.

### 7b. The second proof: OData, and the endpoint from slide 3b
Four of those seven decisions — pagination, ordering, filtering, projection — are settled once by a protocol and collected by every endpoint afterwards. Nobody re-decides pagination on the fortieth endpoint. That is the accrual claim with a well-known instance, and the room will already know it works.

The other three — who may call it, which customers count, what may be logged — are not protocol-settleable. They are settled at the architecture and at the domain model, and they have to be *retrievable at the act*, not merely true of the codebase. "The architecture handles authorisation" is true of most systems that have authorisation bugs.

*This is where the ask on slide 13 becomes concrete. The protocol half already exists and proves the mechanism. The other half is what we are proposing to build.*

### 8. Two different value mechanisms
- **Amortisation** scales with how often an address recurs. Decide once, collect many times.
- **Divergence prevention** scales with how many *actors* visit the address. A decision only one person ever touches cannot diverge.

**These point at different work.** Ranking by frequency alone overweights private, single-actor tasks and underweights the shared ones — which are the architectural seams, and where the slide 2 incidents come from.

### 9. Where the value is densest
Recurrent **and** multi-actor. Seams, boundaries, contracts, shared conventions.

Weight by frequency times cost of divergence, not frequency alone. The high-density acts are often the cheap ones — add a field, add an endpoint. The expensive decisions live in rare acts: identity semantics, deletion, what a correction means.

### 10. Why event modelling, specifically
It produces a named act vocabulary as its primary output. Most methods produce nouns; this one produces happenings, and the acts come with acceptance criteria already attached.

Event sourcing then makes those names load-bearing at runtime. In most architectures act names are a convention that quietly drifts. Under event sourcing they have durable identity — drift breaks things — so the address space maintains itself instead of needing maintenance.

### 11. The compounding bit
Two stores, one vocabulary. The event log records what happened. The decision store records what was settled about how it should happen.

So the run log tells us which acts actually recur and which seams carry the most traffic across teams. **Prioritisation of specification effort becomes measured rather than intuited.** That is unusual and worth saying slowly.

### 12. Where it stops
Amortisation applies to decisions that were pinned in advance or are settled by a check. It does not apply to genuine judgement, which is paid per person per act and does not compound.

So the curve flattens, and the better it works the higher the proportion of remaining work that is irreducible judgement.

**Say this out loud.** It is our own thesis arriving on schedule: transcription cost falls, judgement cost does not. A pitch promising unbounded returns would be contradicting its own foundation, and the technical people in the room will find the flat part anyway.

### 13. What we are asking for
- Event modelling as the method that produces the act vocabulary
- Event sourcing where the domain is state change over time
- A decision store addressed by act, taking reads and writes at the same address
- Filing that is mechanical, or the whole thing reverts to a tidier wiki

### 14. What it costs, honestly
- **Mechanical placement is the load-bearing risk.** If filing requires judgement about where things go, adoption dies in a fortnight, exactly like every prior attempt.
- **Architectural churn orphans the store.** Decisions accrue at architecture-shaped addresses; a migration is not free. Supersession handles it without rewriting history, but the cost is real.
- **Scope condition.** Architectures with no act vocabulary get no benefit. If a client's system has none, producing one is the first engagement — a service, not an obstacle.
- **Not everything is state change over time.** Compilers, solvers, renderers, training pipelines have acts that are not transitions. The claim is bounded and should be stated bounded.

---

## Open items before this becomes a deck

1. Falsifier for the accrual claim. Candidate: act-indexed retrieval and placement produces no measurable reduction in re-made decisions against a subject-indexed baseline on a matched corpus.
2. Related-work check on the accrual and architecture claims. Only the closure claim has been checked.
3. Decide the audience. Internal adoption and client-facing qualification need different slides 13 and 14.
4. Two real pseudonymised examples: one divergence-at-a-seam incident, one decision that would have been collected.
5. Decide whether slide 6 is a claim or a scope condition. It is currently stated as a claim and is not yet earned.
