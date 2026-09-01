# Holding note: repository chain, engineering process, CLI scope, and language criterion

**Status: [PROPOSED] throughout.** Nothing here has been through a gate. Where a position supersedes an earlier one, that is marked. This is a capture note, not canon.

**Purpose.** The structural ground moved substantially in one session. This records it before it decays, and separates what is settled enough to seed a repository from what is still argument.

---

## 1. The repository chain

Four positions, three different relations. The relations matter more than the names.

| Repository | Relation | Holds |
|---|---|---|
| `actor-indexed-determination` | root | actor, capability, accountability, the index |
| `decision-driven-design` | projects from root | software projection |
| `specification-foundation` | projects from root, **peer** of DDD | the criterion, resolution condition, boundary declarations |
| `specification-languages` | **conforms to** foundation | bindings, each with conformance evidence |
| engineering process | **client of** the languages | the method |
| `product-cli` | downstream of the process | tooling |

**Conformance is not projection.** A conforming instance may fail the criterion; a projection may not fail its upstream. Different rules, different validators. This is the relation most likely to be got wrong, because "downstream" reads as projection by default.

**Stable dependency, corrected in session.** Languages first, process second. A language can be stated with no process; a process cannot be stated without a language. The earlier ordering had the process in the same repository as the bindings and was wrong.

Consequences worth keeping: the process is where engagement-specific opinion accumulates — event modelling, event sourcing, the Microsoft stack, analyser sets — and none of it is language material. That keeps the language transferable to a foundation while the process stays commercial. And the process is the first real client of the language, which is a genuine test; the temptation when the language proves inexpressive will be to add a construct rather than restate the process, and that is the direction the dependency must never run.

**Scope of the foundation.** Acts whose verdicts are inspectable. Not scoped to LLM automation: nothing in the constructs mentions models, and binding a general layer to a fast-moving actor kind would need repairing when the actor population changes again. The physical world is excluded not for lack of expertise but because a physical act's verdict is not fully readable back — a weld cannot be diffed against its specification.

---

## 2. The engineering process

1. Identify the recurring act. Not by recurrence alone: **recurrence × cost of divergence × number of actors touching the address.** The most-repeated acts are often the cheapest.
2. Specify it in a specification language. If none exists, build one — and that clause is most of the cost, and where the transferable asset is.
3. Build the architecture for execution. Schema before architecture, content after.
4. Define the actor set. Not "add the LLM": classify determinations as pinned, checked or residual; allocate the residual; name the accountable principal.
5. Write back. Acting produces determinations the specification did not contain, and they return to the same address.

Step 5 has been dropped from this list three times in one session. That is evidence it needs to be inside the sequence rather than appended to it. Without it the first four steps are a waterfall in a new vocabulary.

**Brownfield first move.** Most engagements have an implicit act vocabulary nobody wrote down. Extraction and scoring comes before proposing change, and it is the qualification instrument.

**Extraction is bounded by the forward-only rule.** Reading acts out of existing code is reading backwards. The extractor produces *evidence about* an act vocabulary — a candidate for ratification by people holding the intent — not the vocabulary itself. Scope it to the seam, not the interior.

---

## 3. CLI scope

**Retrieval and placement at the transcription act. Nothing else.** No elicitation, no decision authoring, no analysis, no advice. Every feature request should have to survive that.

Transcription is not chosen because it matters most. It is chosen because it is where the address is unambiguous and delivery is therefore mechanically possible. Upstream acts have fuzzier addresses.

**Composition.** CLI serves an LSP through MCP; Roslyn analysers carry determinations in executable form, delivered at the moment of the act. An analyser is an operationally closed acceptance relation — mechanical, terminating, inspectable, versioned.

**Four constraints.**

- Analysers close structural properties, not semantic ones. A green run must report coverage alongside verdict, or it manufactures false assurance.
- Rejection payload richness is a first-class design surface. It moves effective capability more than model choice usually does.
- No "give me everything relevant" mode. That is the rules file with a command line, and it will be requested.
- Write-back must run through the same server. Read-only first would harden the read path around assumptions that make writes awkward.

**Address layering.** Act type (`implement a command`) → act instance (type with parameter bound: `implement PlaceOrder command`) → ground (what that instance reads) → symbols (where it manifests, by declared correspondence, never derived).

What makes an act concrete is **binding a parameter, not adding ground.** Ground ticks; act identity must not, or accrual breaks whenever the domain model changes. The binding parameter comes from the act vocabulary, which makes the instance set the type set crossed with the vocabulary — computable rather than authored. Determinations bind at both tiers.

**Two risks.** A CLI version is a determination version, so an upgrade changes settled decisions across every client system — fleet migration arriving through tooling and less visible for it. And symbol identity is derived while determinations must survive renaming; storing the mapping by symbol identity orphans determinations silently.

---

## 4. Language criterion

**Expressiveness alone certifies nothing.** English can express everything on the construct list. The criterion needs prohibitions: the language must be *unable* to express a determination with no address, a determination with no allocation, or a coverage claim with no stated uncovered set.

**Discrimination pairs** make the positive half operational. Each is a pass/fail test with published encodings:

- silent on an axis vs. deliberately bounded at it
- decidable in principle vs. runnable at act time by this arrangement
- covered by a check vs. outside its reach
- settled in advance vs. discretion carried by an actor
- proxy standing in for another predicate vs. direct

**One sameness test.** Build-time and act-time determinations expressible in the same schema. Most candidates fail this, and it is the property that stops the method being a waterfall.

**Self-certification with published evidence**, not an authority. Conformance claims carry their suite results; disputes are settled by re-running them.

**Test of the criterion itself:** if the language built for SPETLR differs from the one built for event modelling, it is a notation for one architecture, not a specification language.

---

## 5. Design principle, and its exception

**When determinations are actor-relative, you need a language. When they are protocol-settleable, you need an architecture.** Both bind at act addresses; only one requires something new to be built.

Worked on a single endpoint returning customers by subscription type: pagination, ordering, filtering and projection are protocol-settleable and OData proves the mechanism. Authorisation, which customers count, and logging policy are not.

### The exception: extent inverts for authorisation

Everywhere else, a determination failing to reach an act leaves it **undetermined** — a visible gap. In authorisation, failing to reach an act leaves it **unprotected**, which is functionally a grant. Extent failure produces a wrong outcome rather than a missing one.

Consequences:

- **Deny-by-default is resolution behaviour, not a rule.** Modelled as a maximally-travelling rule, it becomes editable, reorderable and narrowable, and the safety property came precisely from it not being. The language should have no way to express permit-if-unmatched.
- **Grants take the standard narrow default.** Inverted at the base, standard above it. Grants are what authors write to unblock people, and each one stops the fallback for the acts it reaches.
- **Explicit deny is not the fallback** and must not be collapsed into it. It carries the information that someone decided specifically, which is what gets audited.
- **Two completeness predicates, running opposite directions.** No act unreachable by any actor kind; no grant broader than declared. The usual check — every act bound or declared non-travel — passes vacuously here because the fallback resolves everything.

That shape is different enough from the foundation's single resolution condition to be evidence that authorisation is a peer language rather than a construct in the main one.

**Related work to check before building:** Cedar, Rego/OPA, XACML, ReBAC systems. All have settled fallback semantics. The open question is whether any can express reachability coverage over a declared act set.

---

## 6. Coverage is not assurance

Computable: the fraction of an act's category frame bound or checked. Not computable: whether the frame names the properties that matter — which for novel acts is exactly what is uncertain.

- **Do not emit 100%.** Report "all N categories bound" so the denominator stays visible. A full-marks reading suppresses the scrutiny novel work most needs.
- **Coverage does not compose upward.** A composite act built from well-covered parts can have low coverage at the composition, and the interactions are where the interesting escapes live.
- **The valuable output is the uncovered list, not the score.** A number invites comparison and gaming; a list of gaps routes the residual to a competent actor before work starts.
- **Generation does not close the gap.** A generator is a predictable producer, not an independent check on itself. It moves determinations from residual to pinned for what the template settles, makes them auditable in one place, and says nothing about what the template does not reach. A wrong template determination is now wrong identically everywhere, which is worse than divergence because divergence at least surfaces at a seam.

**Keep settled categories in the frame.** The failure mode is that a category with a stable architectural answer stops being asked about, becomes invisible rather than bound, and then one act genuinely differs and nobody notices. Pagination is the obvious candidate.

---

## 7. Open, carried

1. The falsifier tests per-act category coverage; the foundation's predicate is now the resolution condition. Not the same predicate. Blocks the amended pre-registration.
2. Whether act composition and projection give the same ordering. If they do, one relation does both jobs. If not, two orderings need distinguishing before either is called a layer.
3. Actor instances are absent from the act/fact/position triple. Either a further vocabulary or a ruling that instances are declared per specification.
4. Whether a composition check across two specifications' boundary declarations can be mechanically run. If it can, it is the highest-value check in the scheme.
5. Whether the engineering process warrants its own repository. Test: does it have its own act vocabulary and completeness predicate? Probably yes. The bindings almost certainly do not.
6. `meta/sessions/` is a Layer 1 concern, not a DDD one. Declare native in the seed, propose lifting upstream.
