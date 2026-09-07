# Gate A — leak audit of the category derivation bundle

**Enumerates; fixes nothing.** Every hit carries the file, the location, the term, what a
reader could infer from it, and a proposed disposition for Gate B. Hits that leak nothing in
context are listed and marked so. Dispositions are proposals; Emil ratifies each.

**Searched:** 7 files (`README.md`, `MANIFEST.md`, `foundation.md`,
`supersession-foundation-construct-list.md`, `resolution-condition.md`,
`boundary-declarations.md`, `determination.schema.json`) plus 1 path name — every object in the
bundle. Method: the task's five term classes expanded to 40 case-insensitive patterns run over
every file, then a full read of the brief and the manifest for prose-level leaks the patterns
cannot see. The four canon documents were read for context around each pattern hit, not
re-read in full; their §1–§3 construct sections are the derivation source and carry no hit.

**Hits: 38.** By disposition: substitute 14 · delete, ratification required 2 · leave and
report 19 · **rule needed 3** (SS-1, SS-3, SC-3 — the three that matter most).

---

## 1. Path

| Id | Location | Term | What a reader could infer | Disposition |
|---|---|---|---|---|
| P-1 | directory `blind-rederivation/` | *blind*, *re-derivation* | a prior derivation exists and this one is kept from seeing it; therefore a comparison; therefore the list will be judged against another | **rename** to `command-slice-categories/` — names the deliverable, not the process. Alternatives considered: `category-derivation/` (names the method, harmless, but *derivation* is the brief's own word and gains nothing), `act-type-categories/` (drops the act type, which the receiving session needs anyway). The task's suggestion is the best of the three |

## 2. `README.md` — the brief

The brief is where the leaks are, because it was written knowing the design. Line numbers are
the filed copy's.

| Id | Line | Term | What a reader could infer | Disposition |
|---|---|---|---|---|
| R-1 | 1 | *Blind re-derivation brief* | as P-1 | substitute: *Brief — consequential-property categories for a command slice* |
| R-2 | 3–4 | *performing the re-derivation ruled at `CG-R-35`* | a re-derivation; a ruling series with a numbered authority; thirty-five rulings means a mature programme; the identifier is searchable | substitute: *You are producing a category list by a stated method and stopping.* |
| R-3 | 4–7 | *must not try to learn what any other session derived, what act instance is under test, or what determinations it carries* | **the largest leak in the brief**: another session derived a list; an act instance is under test; a determination set exists for it. Names all three hidden objects in one sentence | substitute, preserving the stop-and-report behaviour without naming what is hidden: *Work from this bundle only; it is complete. If anything you are given or find goes beyond it, stop and report it rather than reading on.* |
| R-4 | 9 | *Emil ratifies* | a named principal; a reader who knows the programme identifies it | substitute: *the principal who issued this brief ratifies*. Leaks little on its own and the invocation will carry the name anyway; listed for the ruling |
| R-5 | 9–10 | *Commit identity, if you commit at all, is `Claude <noreply@anthropic.com>`* | the programme's convention; the actor kind | **delete, ratification required**: under Gate C the receiving session has no repository and never commits, so the sentence is moot; neutral wording has nothing to preserve |
| R-6 | 10–11 | *if you have repository access, use nothing outside this directory* | a repository exists holding more | substitute, merged into R-3's replacement (*work from this bundle only*) |
| R-7 | 21 | output filename `rederived-category-list.md` | as P-1 | substitute: `category-list.md` |
| R-8 | 30 | *No experiment design, no measure* | an experiment exists and has a measure; the list is an input to it | substitute: *Nothing else. No discussion of what the list is for beyond what §2 says.* — the prohibition's work is done by *nothing else* |
| R-9 | 35–39 | §2: *a specification either settles such a point by a determination, or declares it unsettled* | that category lists are held against specifications for what they settle — the foundation's own stated purpose (§1, §2.7), not this experiment's; does not say counted, frame, or measure | **leave and report.** This is the concept of a category as the source states it; removing it changes the question. Frame-class, searched hardest, found not to leak the measure |
| R-10 | 105–106 | *that is acceptable and is handled after your work, not by you* | the list is processed downstream against an instance — an instantiated, measured object. Frame-class | substitute: *that is acceptable — do not split a kind into instances.* Preserves the rule, removes the downstream hint |
| R-11 | 134–136 | *any act instance, event model, example determination, or other session's list. The enclosed schema's one example name is not an instance under test* | as R-3: an instance under test; another session's list. The second sentence draws attention to the schema's example name and thereby to the existence of a real instance | substitute: *Do not reason from any particular act, event model or example determination; the list is for the act type. The enclosed schema's one example name is illustrative and says nothing about any domain.* |
| R-12 | 138 | *Do not design the experiment, the measure, thresholds, or a rubric* | the whole design shape in one line: experiment, measure, thresholds, rubric | substitute: *Do not produce anything beyond §1's four items.* (or **delete**, ratification required; the substitution is preferred because the constraint survives) |
| R-13 | 139–140 | *Do not tune the list … to any expectation* | an expectation exists somewhere. Mild; the instruction is protective | leave and report; the residual inference is only that someone will read the list, which the brief cannot hide |
| R-14 | 24–28, 118–120 | *rejection register*, *invented … at the point of invention*, *weakest point* | the programme's idiom; a reader who knows it recognises it. Method content, not design content | leave and report — these are the method, and the method is what the receiving session must be given |
| R-15 | 79–87, 148 | *S-1*, *S-2*, *supersession* | identifiers internal to the enclosed canon; they name what the enclosed document names | leave and report — leaks nothing beyond the enclosure |
| R-16 | 18 | *the domain-state-change binding* | the binding's name; the binding may be discoverable | leave — the act type cannot be stated without it; see SC-3 for the discoverability path |

## 3. `MANIFEST.md`

| Id | Line | Term | Inference | Disposition |
|---|---|---|---|---|
| M-1 | 1 | *blind re-derivation bundle* | as P-1 | substitute: *Manifest — command-slice categories bundle* |
| M-2 | 3 | *The re-deriving session* | as P-1 | substitute: *The receiving session* |
| M-3 | 3 | *as filed on 2026-09-04* | a date; provenance, harmless | leave and report |
| M-4 | 6–12 | hashes | will be stale after Gate B | regenerate over the scrubbed files (task step B.4); old and new manifests go in the scrub record |

## 4. `foundation.md` — canon, original state

**Required in its original state**: the derivation needs it as written, and every substitution
here produces a copy that is not the canon. Dispositions weigh that.

| Id | Line | Term | Inference | Disposition |
|---|---|---|---|---|
| F-1 | 3 | *No falsifiers attached to the design constraints below* | the framework attaches falsifiers to claims — a falsification programme exists. Nothing about this list's use | leave and report: the framework's vocabulary, in a status header; does not reach the comparison, the measure, or the proposed list |
| F-2 | 139 | §5.1 *Falsifier for the closure requirement … measurably fewer escaped decisions* | a falsifier of the closure claim is planned, measuring escaped decisions — the **layer** claim's shape, not this experiment's. With SS-1 a reader could connect the category list to a falsifier | leave and report, **or** withhold the bullet with a visible marker — ruling. Recommendation: leave; the inference is to the wrong experiment, and a withheld bullet in an *Open* section signals that something is hidden without hiding it |
| F-3 | 34, 85, 140 | *independent* | none — used in the mathematical or evidential sense | listed as hits; leak nothing |
| F-4 | 121 | *measurement* | none — a property of quantitative constructs | leak nothing |
| F-5 | §1 | *universal quantification over acts, evaluated against declared extent* | that a per-act completeness check is the foundation's design driver — which is why the original state is enclosed | leave; this is the source, not a leak |

## 5. `supersession-foundation-construct-list.md` — canon, superseding state

| Id | Line | Term | Inference | Disposition |
|---|---|---|---|---|
| **SS-1** | 5 | *The construct list is the derivation source for **the falsifier's category list**. Any session deriving from it must see both … states* | **the highest-value leak in the bundle.** The reader learns that a category list derived from these documents is a falsifier's instrument, and that a session deriving one is anticipated — so their list has a role in a test. It does not reveal a prior list or a comparison. Frame-class by implication: a falsifier's category list is something counted against | **rule needed.** Two options. (a) Substitute the four words: *the derivation source for **category lists drawn from it***, keeping the both-states instruction intact — a minimal rewording of a canon copy. (b) Withhold line 5 with a visible marker. Recommendation: (a), with the scrub record carrying before-and-after, and the manifest noting that enclosed canon copies are for derivation and may differ from the filed originals in their headers. Whether a canon copy may be reworded at all is the principal's call, not the session's |
| SS-2 | 3 | *neither has a falsifier attached* | as F-1 | leave and report |
| **SS-3** | 75 | *The **falsifier's** completeness predicate is per-act category coverage, not the resolution condition … blocks the amended **pre-registration*** | the falsifier's predicate is *per-act category coverage*: the list is a coverage denominator. A pre-registration exists and is being amended. Frame-class, direct | **rule needed.** (a) Substitute: *A per-act category-coverage predicate is not the resolution condition. These are not the same predicate, and which one a given test should use is unresolved.* — rewords an *Open* bullet of a canon copy and drops the pre-registration clause. (b) Withhold the bullet with a marker. (c) Leave: the original foundation §1 already states per-act coverage as the design driver, so the concept is not new to the reader; what is new is *the falsifier's* and *pre-registration*. Recommendation: (a) |
| SS-4 | 42 | *a later session framing proposed* | sessions exist; harmless | leave and report |
| SS-5 | 69 | *overlap* | none — set-theoretic sense | leaks nothing |
| SS-6 | 73 | *Closed by R-3*, *Layer 1* | a ruling series exists; the programme has layers | leave and report — canon's own cross-references; same for RC-4 and BD-2 |

## 6. `resolution-condition.md` — canon

| Id | Line | Term | Inference | Disposition |
|---|---|---|---|---|
| RC-1 | 3 | *Falsifier deferred per R-1: this condition is not what the current closure **pre-registration** tests* | a closure pre-registration exists and tests something other than this condition — the layer claim again | leave and report; recommendation as F-2. If SS-1 and SS-3 are substituted, this is the strongest remaining pointer to a pre-registration programme, and it points at the other one |
| RC-2 | 56 | *No falsifier. The candidate … requires two conforming specifications* | as F-1 | leave and report |
| RC-3 | 37 | *consequential properties* | the term the brief uses — this is its source | leave; needed |
| RC-4 | 27–28 | *per R-2* | as SS-6 | leave and report |

## 7. `boundary-declarations.md` — canon

| Id | Line | Term | Inference | Disposition |
|---|---|---|---|---|
| BD-1 | 79 | *No falsifier attached … a different claim from the one the current **pre-registration** tests* | as RC-1 | leave and report; same recommendation |
| BD-2 | 56 | *Closed by R-4* | as SS-6 | leave and report |
| BD-3 | 69, 71 | *measure*, *a measure into a target* | none — about the boundary ratio, and the ceiling refused for it | leaks nothing |

## 8. `determination.schema.json`

| Id | Line | Term | Inference | Disposition |
|---|---|---|---|---|
| SC-1 | 24 | *e.g. PlaceOrder* | the binding's worked example name. Not the act under test; a reader who finds the binding recognises it | leave and report. The leak was the brief's sentence pointing at it (R-11), not the schema |
| SC-2 | 140 | *the notation records which was established* | the binding is called a notation; no inference toward the notation claim | leaks nothing |
| **SC-3** | 3 | `$id` = `https://github.com/Hafeok/specification-languages/domain-state-change/…` | **a pointer out of the bundle**: the GitHub owner. If that owner's repositories are public, one click reaches `specification-foundation`, this branch, the set, the list, and the whole design. The brief's *read nothing outside this directory* is then a constraint held in prose — `CG-R-39`'s point exactly | **rule needed**, on a fact the session cannot check: the repositories' visibility. If public, substitute the `$id` with a neutral URN (`urn:domain-state-change:determination-schema`) — metadata only, enforcement unchanged, hash changes and is recorded. If private, leave and report. Recommendation: substitute regardless; the pointer does no work in the derivation |
| SC-4 | 6, 11, 78, 129, 229 | *PR-1 … DP-5*, *SR-1* | the conformance criterion's requirement identifiers; a reader learns a criterion exists | leave and report — the schema's own comments, and the corroboration rule in §4.2 reads them |

## 9. What the audit did not find

No hit for *frame*, *denominator*, *arm*, *inference*, *counted*, *compare*, *grade*,
*set-fitted*, *proposed list*, any `AC-` or `F-` identifier, the Gate 1 act, or any
determination of the set. The bundle was built to exclude the set and the list and does; what
it failed to exclude is the design around them, in the brief, the path, and the canon's own
status lines.

## 10. Two things Gate B needs that the session does not have

- **Task step B.5, `INVOCATION.md` "from the arrived invocation file".** No invocation for the
  receiving session has arrived. It is Emil's to write; the session files it when it arrives
  and checks it against the scrubbed brief for consistency, per the step's purpose.
- **SC-3 needs the repositories' visibility**, or the ruling to substitute regardless.

## 11. Weakest point

**The canon copies.** Three of the strongest hits (SS-1, SS-3, RC-1) are in canon documents the
derivation needs in their filed state. Every substitution there hands the receiving session a
text that is not the canon, and every withholding tells it something is hidden. The audit
recommends minimal substitution at SS-1 and SS-3 and leaving the rest, which means the
receiving session will still be able to infer that a falsification programme exists and that a
pre-registration tests the closure claim. That is the layer claim, not this one; it is a real
inference and it is reported here as the residual the scrub cannot remove without changing the
source.

---

**Hold.** Gate B is not entered. Awaiting ratification of the audit, the folder name, and
rulings on SS-1, SS-3 and SC-3.
