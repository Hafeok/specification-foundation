# Session: seed `specification-foundation`

**Session kind:** repository seeding. Governance and tooling are built in-session; canon content is filed, not authored.

**Commit this prompt to `meta/sessions/` as the first act of the session, before anything else, per `DDD-dec-20`. Session-neutral commit identity: `Claude <noreply@anthropic.com>`.**

---

## Standing rules

`canon-governance` is seeded and holds ten ratified rules. **They are in force here and are not restated.** Read `rules/` at the recorded commit and comply. Restating them in this repository would create the two-sources-one-rule state that `canon-governance` exists to end, and which already exists unrecorded between the two source repositories.

The rules bearing most directly on this session:

- three-register discipline, supersession never rewrites, a named principal on every record
- falsifier presence at every live status
- session records under `meta/sessions/`
- **CG-rule-10** — prose describes what is in force and implemented; anything designed but not built carries a date and an explicit marker

Beyond them:

- You propose; Emil ratifies. Gates hold until an explicit ratification message.
- Report defects honestly, including in your own earlier gate output in this session.
- Name the weakest point in each proposal rather than leaving it for a reader to find.
- File arrived inputs with their sha256 before using them.
- **Search enforcement, not only prose** (CG-R-7). A rule or determination can be in force while stated nowhere — held in a validator, a schema, a required field. A text search for governance misses it.

## Explicit prohibitions

You must not, in this session:

- **author canon content.** The foundation, the resolution condition, the supersession record and the boundary declarations are ratified artefacts. You file them, propose their placement, and check them against the validators. You do not write them, and you do not edit them to resolve inconsistencies you find — you report the inconsistency and hold.
- write the conformance criterion or any discrimination pairs
- write anything about event modelling, SPETLR, or any binding
- create any claim record before the validators are in place and passing
- substitute a plausible artefact for one that did not arrive. Report the gap and hold.
- proceed past a gate on your own assessment that the output looks right

---

## Context

This repository holds the foundation of the specification language: what must be expressible for a specification's completeness to be decidable.

**Relations. These must be declared explicitly in the README and not left implicit.**

- **Projects from** `Hafeok/actor-indexed-determination`.
- **Peer of** `Hafeok/decision-driven-design`. Neither depends on the other; both project from the same root.
- **Conformed to by** `specification-languages` (not yet created), which also holds the engineering process for now, per R-5.
- **Governed by** `Hafeok/canon-governance` — asserted from there, not declared here.

| Relation | Requirement | Violation |
|---|---|---|
| projects from | must not contradict upstream; derivation forward only | defect; requires a supersession record |
| conforms to | must satisfy the criterion, with evidence published | admissible outcome; the instance is non-conforming |
| governed by | must comply | defect; not a variant |

Conformance is the relation most likely to be got wrong, because "downstream" reads as projection by default. If the ordering validator is pointed at it, it will govern a relation it does not understand.

Governance is **orthogonal** — a third axis. Not up, not sideways. Nothing is projected from `canon-governance`; everything complies with it.

**Canon boundary.** Canon: the foundation, the resolution condition, the boundary declarations, the conformance criterion when it lands. Not canon: bindings, tooling, the falsifier material, session records.

---

## Settled before this session

Rulings, not open questions. Apply them; do not re-litigate.

- **Claim ID prefix: `SF-`.** A prefix names a **programme**, not a repository (§Q, verified at 132 identifiers with no collision). `SF-` names this programme.
- **`meta/sessions/` is inherited from `canon-governance`** (CG-rule-06), superseding the earlier native declaration. It is not borrowed from `decision-driven-design`, and it is not native here.
- **Compliance is asserted downward, not declared upward** (§B). `canon-governance` holds the registry of repositories it governs. **This repository does not declare that it is governed.** Do not add such a declaration; it would be a reference to a governing repository of exactly the kind §B was ruled to avoid.
- **This repository is not yet in the registry.** `registry/governed.yaml` is empty pending a ruling on governance start points (CG-R-9), so `canon-governance` governs nothing operationally yet. The rules are in force as rules; no instrument evaluates this repository. State this where relevant rather than implying coverage.
- **Rulings are issued by one authority in the `CG-R-` series, held in `canon-governance`** (§O). Sessions propose; they do not issue rulings and do not draw identifiers from that space.
- **Attribution is to Emil personally**, with one sentence stating the editorial role is intended to transfer.
- **Terminology, per R-2.** *Layer* denotes projection depth only. *Scale* denotes granularity of act composition within a projection. **Independent coordinates, not a hierarchy.**

---

## Arrived inputs

Emil attaches these. If any is missing, Gate 0 reports the gap, names the gate it is load-bearing for, and holds. Do not proceed on a substitute.

1. `specification-language-foundation.md` — the construct list, **in its original state**
2. `supersession-foundation-construct-list.md` — two supersessions against it
3. `resolution-condition.md` — the completeness predicate
4. `boundary-declarations.md` — what makes the resolution condition sound
5. `rulings-session-close.md` — six rulings, including R-2 terminology and R-3 actor instances
6. `prereg-closure-falsifier.md` — falsifier material, evidence rather than canon
7. `rulings-gate0-closure-falsifier.md` — rulings on the prior session's Gate 0
8. the prior falsifier session's Gate 0 output, as an arrived input

---

## Gate 0 — arrival and orientation

1. Confirm the repository is empty or contains only an initial commit. If it contains anything else, stop and report.
2. File this prompt and a bootstrap record under `meta/sessions/`, with base commit hash and gate list.
3. File every arrived input with its sha256 in an arrived-inputs table.
4. Report any input that did not arrive and name the gate it blocks.
5. Restate the three relations in your own words and flag any you believe are stated wrongly.
6. Report any inconsistency you find **between** arrived documents. Do not resolve it.

Produce no repository structure yet.

**Hold.**

---

## Gate 1 — governance

Propose and, on ratification, commit governance only. No claims, no canon content.

Contents:

- `README.md` stating: what this repository is the foundation *of* — the name is locally scoped, `actor-indexed-determination` is the actual root, and a reader must not infer otherwise; the three relations with conformance explicitly distinguished from projection; the canon boundary
- `LICENSE` — CC BY 4.0 for canon
- `LICENSE-code` — Apache-2.0 for scripts
- `CITATION.cff` — so the attribution string is fixed at seed and downstream reuse cites consistently rather than inventing forms
- contribution discipline: **cite `canon-governance` at its commit; do not restate its rules.** What is stated here is only what is local — the `SF-` prefix, and anything this repository decides for itself. Duplicating governance text is the defect `canon-governance` was created to end.
- **a term registry seeded with `layer` and `scale`**, each carrying R-2's statement that the axes are independent coordinates. The natural reading of two ordered axes is that they nest; the registry entry must say they do not.
- directory structure, proposed with reasons

**CG-rule-10 applies to every document produced at this gate**, not only the root README. Anything describing an apparatus that does not exist says so in its first line, with a date and a marker.

State the weakest point in the structure you propose.

**Hold.**

---

## Gate 2 — validators

Adapt `validate-core-order.py` and `validate-claims.py` from `Hafeok/decision-driven-design`, and wire them into CI.

Requirements:

- adapted to the `SF-` prefix
- the ordering validator governs **projection** only. It must not be applied to the conformance relation, and the code should say so at the point where reuse would be tempting.
- CI fails on violation rather than warning
- validators run and pass on an empty canon set before any content is filed

Report what the validators check and, explicitly, what they do not. A green run means well formed, not correct, and the README should say so where a reader will see it.

If a validator issues verdicts rather than measurements, state what a false adverse verdict would look like before shipping it. The `canon-governance` seed found that an instrument issuing no verdicts cannot produce a false one, and chose measurement over judgement for that reason. That choice is available here and is not mandatory.

**Hold.**

---

## Gate 3 — filing plan for the arrived canon

Propose placement. Do not execute, and do not alter content.

- where the foundation is filed, and in what state
- how the supersession record is filed such that **both** the original construct list and the superseding position remain visible. The falsifier's category list derives from this document and the derivation needs both states; resolving the supersessions into the text would defeat that.
- where the resolution condition sits, and the boundary declarations adjacent to it — the declarations make the condition sound and should not be separated from it
- where the falsifier material goes, given it is evidence about a proposition in the foundation and not canon itself
- what claim IDs, if any, are assigned at this stage, and what stays unnumbered

**Hold.** You are proposing placement, not content.

---

## Gate 4 — execute the ratified filing plan

File as ratified at Gate 3. No new content. Nothing not ratified.

Run the validators. Report results, including anything that passes for the wrong reason.

**Stop.** The conformance criterion, the discrimination pairs, and the bindings are later sessions.

---

## Carried risks to state in the session log

1. The foundation's construct list has moved twice since it was written. Filing it without the supersession record visible would hand a stale list to any session deriving from it.
2. The conformance relation has no validator and will not have one at the end of this session. Record the gap rather than leaving it to be discovered when `specification-languages` is created.
3. The resolution condition has no falsifier. The current pre-registration tests a different claim, per R-1, and nothing in this repository may present the falsifier result as a test of the resolution condition.
4. Licence, attribution and editor role are cheaper to get right in the first commit than to retrofit across a history.
5. `canon-governance` governs nothing operationally yet — no start points ruled, no verdicts permitted. Its rules bind this session as rules, not as checks. Do not describe this repository as governed in any sense stronger than that.
6. Two of the ten governance rules are **provisional** (CG-rule-08, CG-rule-10), resting on the seeding session's account of its own practice. They are in force and may not be cited as established. This session exercising them is not independent evidence.
