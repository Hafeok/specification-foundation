# Gate 2 proposal — the category list

**Status: `[PROPOSED]`.** The frame's denominator. Once ratified and committed it is fixed for
execution and never adjusted after results are visible (`CG-rule-08`, provisional, applied as in
force). It is drawn for the **act type** — a command slice in the domain-state-change binding,
software projection, act scale — not for the Gate 1 instance, and §7 says what that means for
the reuse the prompt anticipates.

**The warning, taken.** A plausible list of this shape can be written in a minute, and the
session that wrote the determination set a gate ago is the least independent author this list
could have. Three things are done about that, and none removes it. The derivation runs from a
fixed grid — the stages a command slice passes through, crossed with the constructs the
foundation names — and every category cites its cell, so each can be checked against the source
rather than accepted on presentation. Candidates the grid produced and the list rejects are
recorded with the reason (§4), so the pruning is visible. And the check against the Gate 1 set
(§6) was done **after** the list was fixed and is reported as a check, not used as a source.
The session cannot prove the order in which it thought; it can only show its working.

---

## 1. Derivation

### 1.1 What a category is

A **consequential-property category** is a decision point that performing an act of this type
entails: something an actor implementing the slice must resolve, explicitly or by default,
whose resolution has consequence for what the act does. The frame is the set of such points.
The specification either settles a point, declares it unsettled, or — after closure under
`CG-R-21` — cannot fail to do one or the other.

Four admission conditions, each applied to every candidate:

1. **Entailed by the act type.** An actor performing any command slice meets this decision
   point, whatever the domain. A point that arises only for carts, or only for this instance,
   fails here.
2. **Within a construct the foundation names.** A determination in the layer can settle it: it
   lies inside ground, position, allocation, acceptance, coverage, or a boundary declaration.
   A point the layer has no form for is out of the frame, however consequential.
3. **Outside what the act vocabulary fixes.** The foundation §4: the language is *not a
   replacement for the act vocabulary's own artefacts*. Which act this is, and which facts it
   reads and writes by name, are the base's — delivered identically to both arms per `CG-R-30`
   and not in the frame. What the act does with them is.
4. **Recognisable from output.** A stage-1 reader (`CG-R-23`), seeing output and frame only,
   can say whether the output addresses the point without reconstructing what the points should
   have been. Each category is therefore one question with a stated answer form.

### 1.2 The grid

**Axis A — the stages of a command slice.** From event modelling as the binding's base: a
command slice receives a command, reads its declared ground, decides, writes its verdict, and
reports an outcome. Five stages: *receive*, *read*, *decide*, *write*, *report*. Cross-cutting
points that attach to the act as a whole are a sixth row.

**Axis B — the constructs, in both states of the foundation.**

| Construct | Source | State |
|---|---|---|
| ground requirement — what the act must have available, with provenance | foundation §2.2 | original; **retired by S-2** into position |
| position — read is ground, write is verdict | S-2; resolution condition | superseding |
| determination addressed to the act | foundation §2.3 | both |
| allocation — pinned, checked, residual | foundation §2.5 | both |
| acceptance relation — predicate, operational closure | foundation §2.6 | both |
| coverage and residual — what a check reaches and does not | foundation §2.7 | both |
| C-1, C-2, C-3 — ground resolves, verdict resolves, checks range over produced objects | resolution condition | superseding |
| B-1 external ground — source, read provenance, tick rate | boundary declarations | superseding; made necessary by S-2 |
| B-2 terminal verdict — consumer, observability | boundary declarations | superseding |

Both states are used deliberately. The original §2.2 supplies the *receive* and *read* rows
directly — the command payload is ground the act requires and no act in scope produces, which
under S-2 is external ground from the caller, so the two states agree on the cell and differ
only in name. Where the derivation uses the retired construct it says so.

A category is the intersection of a stage and a construct at which the four conditions hold.
The schema is consulted only as enforcement (`CG-R-7`'s search obligation): where it requires a
field, the field marks a decision point the binding's authors already judged consequential, and
the derivation notes that as corroboration, never as the source.

## 2. The list

Nineteen categories, `F-01` … `F-19`. Each carries: the question a reader answers; what an
answer looks like in output; its grid cell. Names are in plain words and avoid the schema's
vocabulary entirely (§5).

### Receive — the command as ground from the caller

| Id | Name | Question | An answer looks like | Cell |
|---|---|---|---|---|
| F-01 | command fields | Which values does the command carry? | the handler's input definition | receive × ground requirement (§2.2); B-1 under S-2 |
| F-02 | acceptable values | What makes a supplied value unacceptable, and what happens then? | validation of format, type or range, and the response to a failure | receive × acceptance relation (§2.6) — the check the act runs on its own input |
| F-03 | target identity | How does the act find the thing it changes? | the key by which existing state is looked up | receive × C-1 — the ground the act resolves to |
| F-04 | caller binding | Does the act check who is calling, and against what? | an authorisation step, or its stated absence | receive × allocation (§2.5) — the residual the foundation says a machine actor cannot carry; B-1 for the identity source |
| F-05 | repeat delivery | When the same command arrives twice, what happens the second time? | absorbed, rejected, applied again | receive × coverage (§2.7) — the canonical uncovered property of any message-driven act |

### Read — the act's ground

| Id | Name | Question | An answer looks like | Cell |
|---|---|---|---|---|
| F-06 | outside sources | What does the act read beyond what the slice declares, and does it decide on it? | a lookup against something the base does not name, or its stated absence | read × B-1, C-1 |
| F-07 | freshness | Is the state read guaranteed to reflect earlier writes, and what if it does not? | a consistency assumption about the projection, stated or embodied | read × B-1 tick rate; §2.2 provenance of the read path |
| F-08 | absent state | What happens when the state the act reads does not exist yet? | creation, rejection, or a default | read × C-1 — absent is not dangling, and the act must say which it is |
| F-09 | unreadable state | What happens when the state cannot be read at all? | an error path, a retry, or silence | read × §2.2 — an act is performable only with its ground available |

### Decide

| Id | Name | Question | An answer looks like | Cell |
|---|---|---|---|---|
| F-10 | what current state forbids | Which conditions of the existing state cause rejection? | invariant checks against what was read | decide × allocation pinned/checked (§2.5); acceptance (§2.6) |
| F-11 | concurrent commands | When two commands on the same target race, what happens? | locking, versioning, last-writer-wins, or nothing | decide × coverage (§2.7) — the example's own uncovered sets name it twice |

### Write — the verdict

| Id | Name | Question | An answer looks like | Cell |
|---|---|---|---|---|
| F-12 | outcome content | What does the written fact carry? | the event's fields | write × position (S-2) — verdict resolves in the fact vocabulary, C-2 |
| F-13 | effect on existing state | Does the act create, change, or leave untouched what already exists? | a new record, a mutation, a no-op | write × position — what the verdict does to the ground it will become |
| F-14 | identity of created things | Who assigns the identifier of anything the act creates, and in what form? | generated in the handler, supplied by the caller, derived | write × C-2 — a produced object must be nameable to be read later |
| F-15 | partial outcomes | Can the act report one thing and have written another? | atomicity of write and response, or its absence | write × C-2 — a partial verdict is a fact the vocabulary cannot name |
| F-16 | outcome leaving the scope | Is the written fact consumed outside the scope, by whom, and observably? | a declared receiver beyond the scope, or its absence | write × B-2 |

### Report

| Id | Name | Question | An answer looks like | Cell |
|---|---|---|---|---|
| F-17 | reporting rejection | What does the caller learn when the command is rejected? | a named cause, a code, silence | report × acceptance (§2.6) — a check whose verdict is not delivered is not operationally closed |
| F-18 | reporting success | What does the caller learn when the command succeeds? | an acknowledgement, the created identifier, nothing | report × position — the verdict as the caller sees it |

### Cross-cutting

| Id | Name | Question | An answer looks like | Cell |
|---|---|---|---|---|
| F-19 | stated versus tested | Which of the act's rules are made runnable in the arrangement, and which are only stated? | tests or analysers present for some rules and not others | act × acceptance closure (§2.6) — operational versus logical closure is the distinction the foundation insists on |

## 3. One decision point per category

Each category is one question (U-11). At the act-type level a category is a **kind** of decision
point; an instance may exhibit it more than once — `F-02` for an act with several fields, `F-19`
for an act with several checked rules. The rule for that is fixed now, before the mapping exists:

**At closure, each category is instantiated into the decision points the determination set
exhibits for it.** Each instance names the determination or determinations that jointly settle
it, or is declared residual. The instance list is the frame for the run, identical across arms,
fixed and ratified with the closure. An instance settled jointly by several determinations —
`F-01` will be, since no single determination states a command's whole shape — agrees only if
the output matches all of them.

Resolutions in the output that no instance covers are **out of frame**: not counted, reported
as a descriptive tally so the frame's reach is visible.

## 4. Candidates rejected, with the reason

The grid produced these; the list does not carry them.

| Candidate | Cell | Rejected because |
|---|---|---|
| where a shared rule is implemented — local code or a shared mechanism | act × extent (§2.4) | fails condition 4 and, on reflection, 1: extent is a property of a determination's reach, not of the act's performance; where the actor places code is implementation structure, and the consequential content is already in `F-17` |
| the act's own record — who performed it, when | act × provenance (§2.8) | fails condition 2 as a property of the *act*: provenance attaches to determinations, and whether the actor records its act-time determinations is the accrual claim's object, not a property of this act's outcome |
| which rejection is reported when several apply | report × acceptance | a sub-question of `F-17`; folded into its answer form rather than counted twice |
| business rules on supplied values beyond format and type | receive × acceptance | folded into `F-02`: the question asks what makes a value unacceptable, and a range is one answer |
| the act's latency, throughput, resource use | — | fails condition 2: the foundation names no construct for it; a determination could carry one as a checked predicate with a tolerance, but no stage entails it as a decision point |
| logging and observability of the act's execution | — | fails condition 2, same reason; `F-16`'s observability is of the verdict's consumption, a different thing |
| retry on failure | — | the caller's decision, not the act's; the act's side is `F-05` |
| security beyond who may call — injection, sanitisation | — | folded into `F-02` where it is a property of acceptable values; otherwise fails condition 2 |
| what the act settles that it did not before — the act-time write form | act × provenance `made_at` | the notation's write side is a property of the *store*, not of the act's performance; out of frame, and it is what the layer and accrual claims are about |

## 5. Leakage: names, and how the check runs

**Names avoid the schema's vocabulary.** Every schema key and enum value appears in arm R by
construction and in arm P only where content requires it, so a category named after one would
leak structurally. The avoided set, read from the schema: *address, act_type, act_instance,
scale, statement, extent, axes, state, region, reason, allocation, class, settled_by,
acceptance, predicate, closure, kind, runnable_by, terminates, tolerance, ranges_over, covers,
does_not_cover, proxy, stands_in_for, known_divergence, positions, fact_type, role, boundary,
source, consumer, read_provenance, tick_rate, consumption_observable, provenance, made_at,
made_by, recorded, supersedes*; and *bound-here, travels-to, does-not-travel, silent, pinned,
checked, residual, external, terminal, internal, operational, logical-only, unestablished,
asserted-none, build-time, act-time, static, slow, fast, unknown, human, machine, team,
external-party*. No name in §2 is on that list, and none uses the words *external*, *terminal*,
*residual*, *coverage*, *closure* or *provenance*, which the foundation's prose would otherwise
make natural.

**The check, run before execution, by the executing session, recorded with the run:**

1. The term list is every category name in §2, every content word of every question in §2
   (stop words excluded), and the schema vocabulary above.
2. Each term is searched, case-insensitive and whole-word, in arm R, arm P, the structured-prose
   arm, and the base statement (`CG-R-30`).
3. A category term present in one arm and absent from another **fails**; the arm carrying it is
   revised by its own author to remove the term without altering content, and the check reruns.
   A schema term present in P and absent from R is reported, not failed — it means P's author
   reached for the notation's word, which is worth knowing.
4. The base statement must contain no category term at all.
5. The full term table, with counts per arm, is filed with the run.

**Limit, stated.** The check is verbatim. A paraphrase — *idempotent* for `F-05`, *optimistic
concurrency* for `F-11` — leaks the same cue and is not mechanically detectable. The arms'
authors are instructed not to name categories; the instruction is pre-registered with the
authorship instructions at Gate 3; and residual semantic leakage is a reported limit, not a
checked one.

## 6. Check against the Gate 1 set — done after the list was fixed

Reported so the closure can be seen coming. This is not the closure, which is a separate step
after ratification (`CG-R-21`), and it is not a source for the list.

| Category | What the eleven do | Expected at closure |
|---|---|---|
| F-01 command fields | no single determination; AC-02, AC-03, AC-08, AC-10 jointly imply customer, product, quantity, line identifier | one instance, settled jointly |
| F-02 acceptable values | AC-02 (quantity), AC-10 (line identifier) | two determined instances; product identifier and customer identifier formats unsettled → **two residuals to declare** |
| F-03 target identity | AC-08 | determined |
| F-04 caller binding | AC-07 | residual, already declared |
| F-05 repeat delivery | AC-05 | determined |
| F-06 outside sources | AC-03 | determined (none consulted) |
| F-07 freshness | nothing; AC-05's uncovered set names the case | **residual to declare** |
| F-08 absent state | AC-08 | determined |
| F-09 unreadable state | nothing | **residual to declare** |
| F-10 what current state forbids | AC-04 | determined |
| F-11 concurrent commands | nothing; AC-04's uncovered set names the case | **residual to declare** |
| F-12 outcome content | AC-11 (fields), AC-06 (price) | one determined instance, one residual already declared |
| F-13 effect on existing state | AC-01 | determined |
| F-14 identity of created things | AC-10 | determined |
| F-15 partial outcomes | AC-09 (never partially succeed) | determined |
| F-16 outcome leaving the scope | the base: `Cart` reads it | **settled by the base**, in both arms identically — `CG-R-34`'s limit made visible |
| F-17 reporting rejection | AC-09 | determined |
| F-18 reporting success | AC-05 says "reports success" for one case only | **residual to declare** |
| F-19 stated versus tested | AC-04 (stated), AC-05 (tested) | two determined instances |

Expected frame after closure: **about 23 instances** — 16 determined by determinations, 1 by
the base, 2 residual already, 6 residual to declare at closure. Every closure candidate is
declarable as residual without a new determination, so no `CG-R-29` finding is expected; if one
arises at closure it is reported there.

Two things this check shows that the list did not set out to show. `F-16` is settled by the
base and not by any determination, which is exactly `CG-R-34`: the boundary category exists in
the frame for the act type and does no work in this instance. And six of nineteen close as
residual — the actor will meet a specification that declares a third of the frame open, which
is realistic for a first-cut specification and is stated so the size of the residual partition
does not surprise anyone at Gate 3.

## 7. Reuse by the layer pre-registration — a finding

The prompt says this artefact is reused by the layer-claim pre-registration and should be drawn
for the act type. It is. **But the layer pre-registration's corpus is SPETLR — Extractor,
Transformer, Loader — not command slices in an event model.** A list derived from the stages of
a command slice does not transfer to an ETL role type; `F-03`, `F-12`, `F-13` and `F-17` have no
obvious counterpart for a Transformer, and a Transformer has decision points a command slice
lacks. What transfers is the **method** — the stage grid crossed with the constructs, the four
admission conditions, the rejection register — not the nineteen rows. Reported, not resolved:
either the layer pre-registration re-derives its list for its act types by this method, or its
corpus changes. Nothing here depends on which.

## 8. What the list omits, and why

Beyond §4: everything condition 3 excludes — the act's name, which facts it reads and writes —
because the base carries it; everything the notation says *about* a determination rather than
about the act — its reach, who settled it, when, what it supersedes — because those are
properties of the record, not of the performance, and the actor is not asked to resolve them;
and correctness against the world, because the frame is a set of questions, not answers, and
whether the specification's answers are right is nobody's measure here.

## 9. Weakest point

**The list and the set have the same author, a gate apart.** `CG-rule-08` fixes the list before
results; nothing fixes it before the set, and the prompt's instruction to draw for the act type
is a discipline the session applied to itself, unverifiably. The derivation, the rejection
register and the after-the-fact check are what a reader has instead of independence. The
specific way this would bite: a category shaped to what the set happens to settle inflates the
determined partition with easy matches. The reader's test is §1.2 — does each row survive as a
decision point for a command slice about *anything*, with the eleven determinations forgotten?
If any row does not, it should be struck before ratification, and the session would rather lose
a row now than carry one that was fitted.

---

**Hold.** Closure and Gate 3 are not entered. Awaiting explicit ratification of the list, after
which the closure step maps the set onto it and is itself ratified before Gate 3.
