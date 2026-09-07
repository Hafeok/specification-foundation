# [PROPOSED] Consequential-property categories — command slice

**Status:** `[PROPOSED]`. Derived by the method in the bundle brief (`command-slice-categories/README.md`)
and not ratified. The principal who issued the brief ratifies; nothing here is settled by having been
produced. Every row and every rejection below is `[PROPOSED]` unless marked otherwise.

**How the three registers are marked in this file.** Plain text under *Settled* in §0 records what was
checked and what was done; those are facts about this session. Everything derived is `[PROPOSED]`.
Questions the derivation could not close are marked `[OPEN]` and gathered at §0.4.

---

## 0. Record of the session

### 0.1 Settled — what was checked

- Bundle located at `meta/sessions/2026-09-03-notation-falsifier-prereg/command-slice-categories/`,
  with `command-slice-categories.zip` beside it. The zip's table of contents (seven names, seven sizes)
  matches the directory. Only the directory was read.
- sha256 of all six manifested files recomputed and **matched** `MANIFEST.md`:
  `README.md` 41aa1448…, `INVOCATION.md` 424e5396…, `foundation.md` 3d9a5254…,
  `supersession-extract.md` ffd2b368…, `resolution-condition.md` 802fc286…,
  `boundary-declarations.md` 0690cb55…. Line counts (147, 35, 142, 69, 58, 79) matched.
  `MANIFEST.md` carries no hash of itself; recomputed as 3281a407… for the record.
- The invocation received in the session was compared by reading against `INVOCATION.md` lines 9–35
  and found identical. Compared by reading, not by hash. The pre-flight note that `INVOCATION.md`
  line 5 refers to is not in the bundle and was not read.
- Nothing outside the bundle was read. To find the bundle, the repository's file tree was listed by
  name; no file outside the bundle was opened. No web search.

### 0.2 Settled — which state of each construct was used (brief §4.2)

- **Ground requirement (foundation §2.2)** is the one construct on Axis B that supersession S-2
  retired. For every ground cell the **superseding state** was used: read position is ground. The
  original §2.2 text supplied the content of the cell — performability, and the read path — because
  S-2 relocates the construct without restating that content. Each such row cites both.
- Supersession **S-1** (specification as peer projection) touches no cell on the grid; it contributed
  no candidate. Recorded so that its absence is visible rather than an oversight.
- The grid's Axis B omits foundation §2.4 (extent) and §2.8 (provenance and supersession). This is
  consistent with admission condition 2, which does not list them. They were **not** added as
  constructs. Considered and not done.

### 0.3 Settled — where the invocation and the brief differ

- The invocation reads as asking for the category list and "alongside it" a rejection register. The
  brief (§1) asks for **one file** containing both. The brief wins: everything is in this file.
- The invocation asks that the weakest point be stated; the brief (§1 item 4) places it in the file.
  It is in §4 below and is also stated in the reply. No conflict.
- The invocation's standing rules (three registers, appended-note corrections, British spelling) are
  not in the brief. They are conventions of presentation, not additional content, and are followed.
- Brief §6 says "nothing beyond §1's four items". This §0 is not a fifth item: the manifest requires
  the receiving session to record what it checked, brief §4.2 requires the construct state to be
  stated, and the invocation requires conflicts to be said. It is `[OPEN]` whether the ratifier
  accepts that reading; if not, §0 can be struck without touching §§1–4.
- The **cell index** at §2.1 is an addition to the register form of brief §5, included because the
  invocation makes exhaustive application of the grid a requirement and empty cells cannot otherwise
  appear on the record. Marked as an addition; strikeable.

### 0.4 `[OPEN]` — questions this derivation could not close

- **O-1.** Brief §3 lists "reports an outcome to the caller" separately from "writes the facts the
  model declares it writes". Under S-2 the report is a produced object and so in write position, and
  C-2 requires every written object to resolve to a fact-vocabulary type. Whether an event model types
  the report is the model's business; where it does not, the resolution condition is silent on the
  report. R-09 and R-10 are drawn on the S-2 reading. See c69.
- **O-2.** Whether the command a slice receives is ground in the S-2 sense. This file treats it so
  (it is read by the act), which is what collapses the receive-stage ground cells into the read-stage
  ones (R-01, R-02, R-03). If the ratifier holds the command apart from ground, those rows split.
- **O-3.** Granularity. Brief §4.3 admits a category as a *kind* of decision point and forbids
  splitting a kind into instances. Read as here, the structural properties of a verdict (no second
  verdict for a repeated command; all declared writes together or none; verdicts in receipt order)
  are instances of R-07 and are not rows. See c50, c55 and §4.
- **O-4.** The four admission conditions do not by themselves stop a point being factored by its
  allocation (who carries it) or by its tolerance. Those factorings are refused here under §4.3's
  one-question rule, not under conditions 1–4. Every such refusal is in the register with "none of
  1–4" in the condition column so it can be reversed.
- **O-5.** File location. Placed beside the bundle directory. Chosen without reading repository
  conventions, which the invocation forbids.

---

## 1. The list

Ids run `R-01` … `R-11` in stage order. **Cell** names the stage and the construct with its clause;
where a row was produced at more than one cell the further cells are listed and the row appears under
the first stage named. "S-2 state" marks a ground cell read in the superseding state.

### 1.1 Receive — the command arrives

| Id | Name | Question | An answer looks like | Cell |
|---|---|---|---|---|
| R-01 | What must be in hand | For each thing the act reads — the command included — what must hold of it for the act to be performable at all, and may the act proceed without it? | Per read object: a condition it must meet before the act proceeds, and whether the act may proceed if it is absent or fails the condition. | receive × ground requirement (§2.2, S-2 state: read position); also read × §2.2; decide × §2.2 |
| R-02 | How each thing read is obtained | By what path does the act obtain each thing it reads, the command included? | Per read object: a named path from where it is held or issued to the act. Two actors with the same reads and different paths give different answers. | receive × ground requirement (§2.2 "with provenance", S-2 state); also read × §2.2; read × B-1 "read provenance"; whole act × §2.2 substitutability |
| R-03 | Who supplies what no act in scope produces | For each thing the act reads that no act in scope produces — a command from outside included — which party outside the scope produces it? | Per such read object: a named producing party, sufficient to identify it. | receive × C-1 with B-1 "where it comes from"; also read × C-1; read × B-1 |

### 1.2 Read — the declared ground is obtained

| Id | Name | Question | An answer looks like | Cell |
|---|---|---|---|---|
| R-04 | How current the ground must be | For each thing the act reads, as of what moment is it taken, and must it still hold at the moment the verdict is written? | Per read object: taken at the moment of acting, and whether re-confirmed before writing; or taken from a copy fixed earlier, with the rate at which the original changes; or that rate not known. | read × B-1 "tick rate … encoded or read at act time"; also read × §2.2 "available … to be performable" (S-2 state); write × §2.2 |

### 1.3 Decide

| Id | Name | Question | An answer looks like | Cell |
|---|---|---|---|---|
| R-05 | How much of the verdict is fixed in advance | Given what it reads, is what the act writes fixed in advance, admitted by a stated condition with the choice within it left to the act, or left to the act's judgement? | One of: fixed in advance by a stated rule, the act having no discretion (the rule is stated); the act has discretion and a stated condition admits or refuses what it produces regardless of who produced it (the condition is R-07); the act has discretion and no condition reaches it (the carrier is R-11). | decide × allocation (§2.5, three classes); also decide × S-2 "variance is a property of the mapping"; write × §2.5 |
| R-06 | Whether the admitting condition can be run while acting | Where a condition admits what the act writes, can this act — with the ground and tools this arrangement actually has — run it before the verdict is committed? | One of: runnable by this arrangement before committing; decidable in principle but not runnable here; which of the two holds has not been established. | decide × acceptance relation (§2.6 "operational closure, not logical closure"); also write × §2.6; whole act × §2.6 |

### 1.4 Write — the verdict is produced

| Id | Name | Question | An answer looks like | Cell |
|---|---|---|---|---|
| R-07 | What admits what is written | Where the act has discretion, what condition must the objects it writes — the report to the caller included — satisfy to be admitted? | A condition stated as what admits, not as a list of admitted outcomes, over objects the act writes; with units and tolerance where it is quantitative. A kind: an act may carry several. | write × acceptance relation (§2.6 "predicate form, not extension"; C-3 ranges over produced objects); also decide × §2.6; report × §2.6 |
| R-08 | Whether the check runs on the thing itself or a substitute | Is each admitting condition evaluated on the written object itself, or on something standing in for it? | Per condition: on the object itself; or on a named substitute, together with the condition it stands in for and how the substitute is known to differ from it. | write × coverage and residual (§2.7 "where a predicate stands in for another"); also decide × §2.7; report × §2.7 |

### 1.5 Report — the caller learns the outcome

| Id | Name | Question | An answer looks like | Cell |
|---|---|---|---|---|
| R-09 | What the caller is told | For each way the act can end — it proceeded; it decided against the command; it could not proceed for want of what it needed — what does the caller learn? | Per ending: what is reported to the caller, and whether that report is the same object as a fact the act writes or a distinct produced object. | report × position (S-2: the report is produced, so in write position; C-2); also receive × §2.2 (what becomes of a command the act does not act on) |
| R-10 | Who takes what leaves the scope, and whether that is seen | For each object the act produces that no act in scope reads — the report to the caller included — who or what takes it outside the scope, and can any act in scope observe that it was taken? | Per such object: the outside party or system that consumes it, and yes or no on whether its consumption is observable to any act in scope. | report × B-2 (terminal verdicts: consumer; consumption observable); also write × B-2; write × C-2; report × C-2 |

### 1.6 Act as a whole

| Id | Name | Question | An answer looks like | Cell |
|---|---|---|---|---|
| R-11 | Who carries what is left to judgement | For every point on this list that is neither fixed in advance nor admitted by a condition runnable while acting, which actor decides at the moment of acting, and which principal answers for the outcome? | An actor, and a principal. The principal is a role no machine actor can occupy (§2.5). Where the verdict turned on ground from outside the scope, the answer does not shift to the outside party (B-1). | whole act × allocation (§2.5 "for residual … which actor carries it and which principal answers"); also whole act × §2.7 "allocated to an actor competent to carry it"; decide × §2.5; decide × B-1 accountability; whole act × B-1 |

**Finding on the receive stage.** Under S-2 the command is a read object, so every candidate the
receive-stage ground cells produced is the same kind as a read-stage candidate with the command as its
instance. The receive row of the grid therefore yields no category that is not also yielded at read.
The three rows above are placed under receive because it is the first stage they cite, not because
they belong to it alone. See O-2.

**Finding on the whole-act row.** Every cross-cutting candidate other than R-11 was either a property
of the specification rather than of the act (resolution, scope, boundary ratio, which points are
declared reached) or the per-object kind already admitted at a stage. The whole-act row yields one
category.

---

## 2. Rejection register

Every candidate the grid produced that is not a row above. Candidates are numbered `c01` … `c89` in
the order the cells were worked (receive, read, decide, write, report, whole act; constructs in the
order of the brief's Axis B table). Three dispositions appear:

- **Rejected** — failed one of admission conditions 1–4; the column says which.
- **Merged into R-nn** — the same kind as an admitted row (an instance of it, or the same question
  at another stage); admitted as part of that row, not as a row of its own. Condition column reads
  "none of 1–4 — §4.3 one-question rule", because no admission condition failed.
- **Absorbed into R-nn** — a field of the answer to an admitted row (its allocation, its tolerance),
  not a separate question about the act. Same condition column. See O-4.

Merged and absorbed candidates are listed although they were not strictly rejected, so that the
pruning can be checked rather than trusted. Register rows marked ✱ are the ones whose disposition
rests on §4.3 rather than on conditions 1–4.

### 2.1 Cell index (addition to the §5 form; strikeable)

Stage × construct → candidates produced → outcome. "—" means the cell was worked and produced nothing.

| Stage | §2.2 ground (S-2 state) | S-2 position / resolution | §2.3 determination | §2.5 allocation | §2.6 acceptance | §2.7 coverage | C-1, C-2, C-3 | B-1, B-2 |
|---|---|---|---|---|---|---|---|---|
| receive | c01→R-01, c02→R-02, c03→R-09 | c04 rejected | c05 rejected | c06 absorbed | c07, c08 rejected | c09 rejected | c10 rejected, c11a rejected, c11b→R-03; C-2, C-3 — | c12→R-03, c13→R-02, c14 rejected; B-2 — (c15) |
| read | c16→R-01, c17→R-02, c18→R-04 | c19 rejected, c20 rejected | c21 rejected | c22 absorbed | c23 rejected | c24 rejected | c25 rejected, c26a rejected, c26b→R-03; C-2, C-3 — (c27) | c28→R-03, c29→R-02, c30→R-04, c31 merged; B-2 — (c32) |
| decide | c33 merged→R-01 | c34 merged→R-05 | c35 rejected | c36→R-05, c37→R-11 | c38→R-07, c39→R-06, c40 rejected, c41 absorbed | c42 rejected, c43→R-08, c44→R-11 | c45 absorbed | c46→R-11; B-2 — (c47) |
| write | c48 merged→R-04 | c49 rejected, c50 merged, c51 merged | c52 rejected | c53 merged→R-05 | c54→R-07, c55 merged (three instances), c56 merged→R-06, c57 absorbed | c58 rejected, c59→R-08, c60→R-11 | c61 rejected, c62a rejected, c62b→R-10, c63 absorbed | c64, c65→R-10; B-1 — (c66) |
| report | c67 rejected | c68→R-09, c69 rejected (O-1) | c70 rejected | c71 absorbed | c72 merged→R-07 | c73 rejected, c74 merged→R-08 | c75→R-10 | c76, c77→R-10; B-1 — |
| whole act | c78 merged | c79 rejected | c80 rejected, c81 not a candidate | c82→R-11 | c83 merged→R-06 | c84 rejected, c85→R-11 | c86 rejected, c87 rejected | c88 rejected, c89→R-11 |

Empty cells on the record: receive × C-2, receive × C-3, receive × B-2, read × C-2, read × C-3,
read × B-2, decide × B-2, write × B-1, report × B-1. Each was worked; each construct has no object
to attach to at that stage (nothing is written at receive or read; B-1 attaches to read objects only;
B-2 attaches to written objects only).

### 2.2 The register

| # | Candidate | Cell | Condition failed | Why |
|---|---|---|---|---|
| c03 ✱ | What the act does with a command it will not act on (refuse, drop, hold) | receive × §2.2 | none of 1–4 — §4.3 | The endings "decided against" and "could not proceed" are two of the three endings R-09 asks about; what the caller then learns is R-09's answer. Merged into R-09. |
| c04 | Whether the received command is ground | receive × S-2 | 3 | The slice type fixes that a command slice receives a command (brief §3); S-2 fixes that what is read is ground. No discretion remains to the act. |
| c05 | Whether receipt is the subject of any determination addressed to this act | receive × §2.3 | 4 | This is the question the list as a whole answers. It has no answer form other than the list itself; a reader would have to reconstruct the points to check it, which condition 4 forbids relying on. |
| c06 ✱ | Who carries the admission of the command — fixed, by condition, or judgement | receive × §2.5 | none of 1–4 — §4.3 | Passes all four conditions. It is the allocation carried by whatever determination settles R-01, not a second question about the act. Admitting it would factor every row by allocation. Absorbed into R-01. See O-4. |
| c07 | A condition admitting the command | receive × §2.6 | 2 | Acceptance relations range over what the act produces (S-2 consequence; C-3). A condition on what is received is a ground requirement, and that is R-01. The acceptance construct has no form for it. |
| c08 | Whether a condition on the command is runnable while acting | receive × §2.6 | 2 | As c07: no acceptance relation ranges over the command, so there is no closure status to establish here. |
| c09 | What a check on the command reaches and does not reach | receive × §2.7 | 2 | Coverage is per acceptance relation (§2.7). None ranges over the command (c07), so there is nothing here for coverage to attach to. |
| c10 | The command resolves to a type in the fact vocabulary | receive × C-1 | 3 | The fact vocabulary is the event model's (brief §4.1 condition 3; foundation §4). |
| c11a | Whether the command is produced by an act in scope | receive × C-1 | 3 | Whether some slice in scope writes the command is read off the event model, which declares each slice's writes. |
| c14 | The tick rate of a command from outside | receive × B-1 | 3 | The slice type fixes that a command is taken at the moment it arrives (brief §3). Encoding it in advance is not an option the act has, so the B-1 field records nothing the act decides. Recorded as a finding: B-1's tick-rate field is idle for commands. |
| c15 | B-2 at receive | receive × B-2 | — (no candidate) | B-2 attaches to written objects; nothing is written at receive. Cell empty. |
| c19 | Each declared read is ground | read × S-2 | 3 | Fixed by the event model's declaration of reads together with S-2. |
| c20 | Whether the act's own prior verdicts are among what it reads (S-2 "the verdicts of prior acts are what later acts read") | read × S-2 | 3 | Which facts a slice reads is declared by the event model. If its prior verdicts are not declared read, it does not read them. (Whether a repeated command yields a second verdict is a property of what is written; see c55.) |
| c21 | Whether the read stage is the subject of a determination addressed to this act | read × §2.3 | 4 | As c05. |
| c22 ✱ | Who carries each ground requirement | read × §2.5 | none of 1–4 — §4.3 | As c06. Absorbed into R-01. |
| c23 | A condition admitting the ground | read × §2.6 | 2 | As c07. |
| c24 | What a check on the ground reaches | read × §2.7 | 2 | As c09. |
| c25 | Each read resolves to a type in the fact vocabulary | read × C-1 | 3 | As c10. |
| c26a | Whether each read is produced by an act in scope | read × C-1 | 3 | As c11a. |
| c27 | C-2 and C-3 at read | read × C-2, C-3 | — (no candidate) | Nothing is written at the read stage; nothing for C-2 or C-3 to attach to. Cell empty. |
| c31 ✱ | What the act does when ground from outside is unavailable, has moved, or is wrong (B-1 "does not license correctness, availability, or stability") | read × B-1 | none of 1–4 — §4.3 | Distributed, not lost: unavailable is R-01 (may the act proceed without it); moved is R-04 (must it still hold when writing); wrong is undetectable by the act, and who answers is R-11. No question remains that one of those rows does not ask. |
| c32 | B-2 at read | read × B-2 | — (no candidate) | B-2 attaches to written objects; nothing is written at read. Cell empty. |
| c33 ✱ | What must be in hand to decide | decide × §2.2 | none of 1–4 — §4.3 | The same question as R-01 at the stage where performability bites. Cell cited on R-01. |
| c34 ✱ | Whether the verdict varies with which actor performs the act | decide × S-2 | none of 1–4 — §4.3 | S-2 rules that variance is a property of the mapping. Whether the mapping is fixed or leaves discretion is exactly R-05's three-way answer. Merged into R-05; cell cited. |
| c35 | Whether deciding is the subject of a determination addressed to this act | decide × §2.3 | 4 | As c05. |
| c40 | Whether what admits is written as a condition or as a list of admitted outcomes | decide × §2.6 | 1 | A rule on how the determination is authored (§2.6 "predicate form, not extension"), met by whoever writes it, not a point an actor performing the act meets. It survives as a constraint on R-07's answer form. |
| c41 ✱ | The tolerance at which the admitting condition holds | decide × §2.6 | none of 1–4 — §4.3 | Passes 1–4 in kind (an exact condition has tolerance "exact"). It is part of stating the condition (§2.6 "at the stated tolerance"; §3 "every quantitative construct declares its measurement"), not a second question. Absorbed into R-07's answer form. See O-4. |
| c42 | Which properties of the act the admitting condition reaches and which it does not | decide × §2.7 | 4 | Its only answer form is a selection from this list. It is the measure §2.7 takes over the list, not a point in it; a row for it would have the list range over itself. Recorded as a judgement conditions 1–4 do not make cleanly. |
| c45 ✱ | The condition must range over objects some act writes (C-3) | decide × C-3 | none of 1–4 — §4.3 | A well-formedness rule on the relation, not a decision of the act. Survives as a constraint on R-07's answer form. |
| c47 | B-2 at decide | decide × B-2 | — (no candidate) | B-2 attaches to written objects; nothing is written at decide. Cell empty. |
| c48 ✱ | What must still hold at the moment of writing for the verdict to stand | write × §2.2 | none of 1–4 — §4.3 | The same kind as R-04: the moment the ground is taken as of, relative to the write. Merged into R-04; cell cited. Whether the write itself can land, and what follows if not, is the ending "could not proceed" in R-09. Flagged in §4 as a merge the ratifier may reverse. |
| c49 | Each written object is verdict | write × S-2 | 3 | Fixed by the model's declaration of writes together with S-2. |
| c50 ✱ | Whether the written objects stand as one verdict or may land in part | write × S-2 | none of 1–4 — §4.3 | Passes 1–4 in kind. It is one condition over the objects the act writes ("all declared writes together or none"), so an instance of R-07, and §4.3 forbids splitting a kind into instances. Merged into R-07. See O-3. |
| c51 ✱ | Which declared writes are produced on each way the act can end | write × S-2 | none of 1–4 — §4.3 | Content of the rule or condition that settles the verdict: R-05 when fixed in advance, R-07 when admitted by condition. The report side of each ending is R-09. Merged. |
| c52 | Whether writing is the subject of a determination addressed to this act | write × §2.3 | 4 | As c05. |
| c53 ✱ | Who carries the verdict | write × §2.5 | none of 1–4 — §4.3 | The same question as c36 (R-05) asked at the write stage. Merged; cell cited on R-05. |
| c55 ✱ | Three structural conditions on what is written: no second verdict for a repeated command; all declared writes together or none (c50); verdicts respect the order commands were received in | write × §2.6 ("several") | none of 1–4 — §4.3 | Each passes 1–4: universal to command slices, statable as a condition over produced objects, not fixed by the model, recognisable. Each is one condition of the kind R-07 names, and §4.3 forbids splitting a kind into instances. Merged into R-07. Recorded individually so that they can be promoted to rows if the ratifier reads §4.3 otherwise. See O-3 and §4. |
| c56 ✱ | Whether the condition on what is written is runnable while acting | write × §2.6 | none of 1–4 — §4.3 | The same question as R-06 at the write stage. Cell cited. |
| c57 ✱ | Tolerance of the condition on what is written | write × §2.6 | none of 1–4 — §4.3 | As c41. |
| c58 | What the condition on what is written reaches and does not | write × §2.7 | 4 | As c42. |
| c61 | Each written object resolves to a type in the fact vocabulary | write × C-2 | 3 | As c10. |
| c62a | Whether each written object is read by some act in scope | write × C-2 | 3 | Read off the event model's declared reads. |
| c63 ✱ | C-3 at write | write × C-3 | none of 1–4 — §4.3 | As c45. |
| c66 | B-1 at write | write × B-1 | — (no candidate) | B-1 attaches to read objects; the write stage reads nothing. Cell empty. |
| c67 | What must be in hand to report | report × §2.2 | 3 | What the act must have in order to report is the outcome it produced; the slice type fixes that an outcome is reported (brief §3). Nothing is left to decide that R-09 does not ask. |
| c69 | Whether the report resolves to a type in the fact vocabulary | report × S-2 / C-2 | 3 | The fact vocabulary is the model's. Finding recorded at O-1: brief §3 lists the report separately from the declared writes, while S-2 makes it a produced object to which C-2 applies; where a model does not type the report, the resolution condition is silent on it. |
| c70 | Whether reporting is the subject of a determination addressed to this act | report × §2.3 | 4 | As c05. |
| c71 ✱ | Who carries what the caller is told | report × §2.5 | none of 1–4 — §4.3 | As c06; absorbed into R-09. |
| c72 ✱ | A condition on the report | report × §2.6 | none of 1–4 — §4.3 | The report is a produced object; R-07 already ranges over it. Merged; cell cited on R-07. |
| c73 | What the condition on the report reaches | report × §2.7 | 4 | As c42. |
| c74 ✱ | Whether the report is checked on itself or a substitute | report × §2.7 | none of 1–4 — §4.3 | The same question as R-08 for the report. Cell cited on R-08. |
| c78 ✱ | Which actors may perform the act, given that actors with different read paths are not substitutable (§2.2) | whole act × §2.2 | none of 1–4 — §4.3 | Two questions already on the list: the read path per read object is R-02 (cell cited); which actor exercises judgement is R-11. For points fixed in advance or admitted by condition the producer is immaterial (§2.5 "regardless of producer"). |
| c79 | Position is marked for each object the act touches | whole act × S-2 | 3 | Fixed by the event model's declared reads and writes. |
| c80 | Which determinations are addressed to this act | whole act × §2.3 | 3 | The act supplies the address (foundation §3 "the act supplies the address"); which determinations are filed there is the specification's, not a decision the act makes. |
| c81 | Whether each determination is taken in advance or produced while acting (foundation §3, build-act symmetry) | whole act × §2.3 | — (not a candidate) | Foundation §3 is not a construct on Axis B and condition 2 does not name it. Not generated by the grid; recorded so the omission is visible. Considered and not done. |
| c83 ✱ | Whether all the act's admitting conditions are runnable while acting | whole act × §2.6 | none of 1–4 — §4.3 | The per-condition kind R-06, summed. Cell cited on R-06. |
| c84 | Which points on this list the act's conditions reach, and which are declared unreached | whole act × §2.7 | 4 | As c42. This is the specification's coverage declaration over the list; the "declares it unsettled" of brief §2 is made by the specification, not decided by the act. |
| c86 | Every read and every write of the act resolves (C-1, C-2) | whole act × C | 1 | A property of the specification, met by writing it; an actor performing the act does not meet it as a decision point. |
| c87 | Which declared scope the act sits within (B-3) | whole act × C / B-3 | 3 | The scope is the specification's, declared with its act vocabulary; not a decision of the act. |
| c88 | The ratio of declared-boundary objects to internally resolved objects (B-4) | whole act × B-4 | 1 | A reported measure of the specification, not a decision point of the act. |

Candidates not in the register because they became rows: c01, c02, c11b, c12, c13, c16, c17, c18,
c26b, c28, c29, c30, c36, c37, c38, c39, c43, c44, c46, c54, c59, c60, c62b, c64, c65, c68, c75, c76,
c77, c82, c85, c89. Each appears in the **Cell** column of its row.

---

## 3. Invented categories

None. Every row was produced at a grid cell and cites it. The rows whose derivation from the
construct text is thinnest, and which a reader should test first, are:

- **R-04's write-time clause** (c48): §2.2 says only "available … to be performable"; reading that at
  the write stage as "must the ground still hold when the verdict is written" is the longest step in
  the file.
- **R-09** rests on the S-2 reading that the report is a produced object (O-1).
- **R-03** rests on B-1's "where it comes from" being a decision of the act rather than a field of a
  declaration the specification makes about it.

If the ratifier finds any of these to be invention rather than derivation, the row should be struck
and this section amended by appended note, not edited.

---

## 4. Weakest point

**Granularity.** The list sits at the level of kinds, because brief §4.3 admits a kind and forbids
splitting it into instances. The consequence is that the properties a coverage declaration most needs
to discriminate between — whether a repeated command yields a second verdict, whether the declared
writes land together or in part, whether verdicts keep receipt order, what is written when the act
refuses — all fall inside two rows (R-05, R-07) as instances, and a coverage declaration over this
list can only say "reaches what admits what is written" or "does not". Coverage over the list is
therefore coarse exactly where §2.7 says the residual must be made visible. This is not a defect I
have fixed; it follows from the method as written, and the register (c50, c51, c55) keeps the
instances recoverable if the ratifier reads §4.3 as admitting them. Two further points, in order:
the collapse of the receive stage into read (O-2), and the merge of write-time ground currency into
R-04 (c48), both of which rest on my reading of S-2 rather than on its text.

---

## Notes appended

Corrections to anything above are made here, beside the original, never by amendment.

- **N-1 (before filing).** A completeness check over the candidate numbering found c15 and c32 — the empty B-2 cells at receive and at read — present in the working numbering but absent from the cell index and register. Both were added as empty-cell entries before the file was filed. No other candidate was affected; the count of admitted rows and of register entries is unchanged apart from these two.
