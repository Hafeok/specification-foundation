# Gate 0 report — orientation

**Status of this report: session output, proposing nothing for ratification except that Gate 0
is complete.** Everything it finds is held, not resolved. Register discipline per `CG-rule-01`:
rulings in force are cited by identifier; everything this session produces is `[PROPOSED]` at
most; open items are marked `[OPEN]`.

**On this report being a file.** The prompt's Gate 0 reads "without writing to the repository".
It is read here as the seed session read the same words: no proposal artefact lands, no
repository structure is produced. The session records — arrived inputs with hashes (a standing
rule that requires writing), and this report — are committed under `meta/sessions/`. The prior
falsifier session read the words literally, and the consequence is on this repository's record
as a defect: its Gate 0 report was never a repository object and is unrecoverable
(`meta/sessions/2026-09-01-seed-specification-foundation/carried-items.md`, CI-1). This session
does not repeat that. If Emil rules the literal reading, this file is the thing to strike.

---

## 1. Governing repository, read and recorded

`Hafeok/canon-governance` read at **`c5383be06e5b181dc79307554a35cddeacbcd3e8`**, the head of its
default branch, because the invocation's `<REF>` arrived unfilled. Details in `bootstrap.md`:

- `rules/` holds ten rules, read in full; **`CG-rule-08` and `CG-rule-10` are provisional** in
  their own records and are cited as in force, never as established, anywhere in this session.
- Between the README's pin (`ad6d1b0b…`) and the ref read, only `registry/rulings.yaml` differs
  (CG-R-10 … CG-R-16 appended). The rules complied with are the rules the pin records. The pin is
  not advanced (`CG-R-10`).
- The register at the ref read **ends at `CG-R-16`**. This matters below (I-1).
- Enforcement was searched, not only prose: the rules held in this repository's validators were
  read (`scripts/`), and the binding's rules held in its schema were read from the schema, not
  the README (§3).

## 2. The claim and the measure, restated

**The claim.** Take one act and one fixed set of determinations addressed to it. Render the set
twice: as records valid against the binding's schema (arm R), and as a prose specification
written as clearly as a competent engineer can write it for a colleague (arm P). Nothing differs
between the two but form. Give each to the same actor under the same settings with the same
task: perform the act. Before any run, fix the frame — the consequential properties of this act
type — and mark each category as one the set settles or one the set explicitly declares it does
not. After each run, a reader who does not know which arm produced the output classifies each
category by how the output disposed of it. **Determined:** the disposition is the set's — the
actor retrieved it. **Inferred:** the actor supplied a disposition the set did not give, from
convention, training or guesswork, and it does not matter whether it was a good one. **Asked:**
the output raises the category as unsettled instead of disposing of it. The measure per run is
inferred over frame size. The claim predicts R's rate is below P's by more than a threshold fixed
before execution. If the gap is inside the threshold, or P is lower, or the arms turn out not to
carry the same content, the claim fails.

**What "form" means here, read from the schema.** A record's content — what is settled — is a
prose string (`statement`). What the notation adds is typed structure around it: where it
applies and where it stops, who carries it, how acceptability is decided and what the check does
not reach, what the act reads and writes and where the boundary is, who settled it and when. So
the claim, sharpened: *typed structure around prose statements leaves less to inference than
prose carrying both the statements and the structure.* That is what arm P has to carry for the
comparison to be of form.

**The floor, as written.** The categories the set declares unsettled are the residual partition.
§1 says the inference rate cannot legitimately fall below residual over frame; a run below it
means the actor invented over declared gaps; such runs are reported separately and excluded from
the effect. **Its purpose can be restated: a guard so that no run looks good by treating declared
gaps as settled. Its mechanism cannot be restated soundly**, because as written it is inverted —
U-1 below.

## 3. The binding: what a conforming record contains, from the schema

Read from `schema/determination.schema.json`, not the README. `additionalProperties: false` at
every object except `boundary`, so nothing beyond this can be carried.

| Field | Required | Content |
|---|---|---|
| `id` | yes | `DSC-` + four digits |
| `address` | yes | `act_type` ∈ {command, read-model, automation, translation}; `act_instance` (a name; checked against the event model by a tool, not the schema); `scale` ∈ {act, slice, context, system}, default act |
| `statement` | yes | **free prose**, non-empty — the determination's content |
| `extent.axes` | yes, ≥1 axis, axis names open | per axis: `state` ∈ {bound-here, travels-to, does-not-travel, silent}; `region` required for travels-to and does-not-travel, **forbidden** for silent; optional `reason` |
| `allocation` | yes, closed union | **pinned** + `settled_by`; **checked** + `acceptance`; **residual** + `carried_by` ∈ {human, machine, team, external-party} + `principal` {`kind` ∈ {human, team, external-party} — machine absent by construction; `identifier`} |
| `acceptance` (checked only) | all five | `predicate` (prose); `closure.kind` ∈ {operational, logical-only, unestablished}, operational requiring `runnable_by` and `terminates`, optional `tolerance`; `ranges_over` ≥1 fact; `covers` ≥1 **free-text property name**; `does_not_cover` ≥1 free-text name **or** the literal `asserted-none`; optional `proxy` {`stands_in_for`, `known_divergence`, both required together} |
| `positions` | **no** | list of {`fact_type`; `role` ∈ {read, write}; optional `boundary.kind` ∈ {internal, external, terminal}; external requires `source`, `read_provenance`, `tick_rate` ∈ {static, slow, fast, unknown}; terminal requires `consumer`, `consumption_observable`} |
| `provenance` | yes | `made_at` ∈ {build-time, act-time}; `made_by`; `recorded` (date-time); optional `supersedes` |

Three things the README does not say that the schema does:

- **`positions` is optional.** A record with no ground and no verdict declared is valid. The
  foundation's ground requirement (§2.2, provenance mandatory) is enforced per position when a
  position is declared external, and not at all when no position is declared.
- **`covers` and `does_not_cover` name consequential properties in free text.** These are the
  same kind of thing the frame enumerates. Consequence for Gate 2 at §5, U-11 and for the
  leakage check: coverage vocabulary in the set will appear in both arms, by parity, so the
  leakage check is "in one arm and not the other", exactly as §8 words it.
- **The content of every determination is prose.** See §2.

**The checks were run.** With `jsonschema` installed: 6/6 ordering records valid, 2/2
fulfilment, 7/7 forbidden shapes rejected, resolution and composition resolved on the positive
fixtures, both negative fixtures caught, criterion 11/11. The schema does what the README claims.
Two defects in the runner, reported and not fixed (arrived input, not modified):

- **D-1 — `run_all.sh` reports green with checks unrun.** In an environment without
  `jsonschema`, `validate.py` and `prove_prohibitions.py` crash; the runner's `cmd && echo`
  pattern under `set -e` does not abort on the left side of `&&`, so the three schema lines are
  silently absent and the script exits 0. The first run here did exactly that. A runner whose
  green can mean "did not run" is the failure its own header names — an instrument that has never
  returned an adverse result.
- **D-2 — "5/5 ordering records valid" is a hardcoded label.** The file holds six records
  (`DSC-0006`, the terminal declaration the composition check needs); the example's header still
  says "Five determinations". `CG-rule-10` in miniature: prose describing a state that no longer
  holds.

## 4. The two partitions: how derived, and from what

**From the determination set as content — never from either arm.** Arm R does not exist when the
partition is fixed, and the partition must be arm-independent; the set is the only object that is
both fixed and arm-neutral.

**Determined by the specification:** category *c* is determined iff some determination in the set
disposes of *c* — a pinned determination whose statement resolves *c*, or a checked determination
whose acceptance names *c* in `covers` (the actor retrieves the predicate; that is the retrieval
the measure counts). **Declared residual:** *c* is residual iff a residual determination names *c*
as not settled, or *c* appears in some `does_not_cover` and no other determination disposes of it.

**Mechanism.** A mapping table, category → determination(s) → partition, drawn by this session
from the Gate 1 set and the Gate 2 list, fixed at Gate 3 with the quantities, ratified with them.
The table is part of the frame and never moves after commit (`CG-rule-08`, provisional).

**The gap in this derivation is U-4:** a category the set neither disposes of nor declares
residual has no partition, and the pre-registration's two-way partition is stated as exhaustive.

## 5. Unsound, ambiguous, or unfalsifiable as written

Reported and held. Nothing is adjusted; the prompt forbids adjusting the claim, and every fix
below is Emil's to rule. Each item names the gate it blocks.

- **U-1 — The floor is inverted.** Inventing over a declared gap scores *inferred*, which raises
  the rate; surfacing it scores *asked*, which does not. A run that asks about every residual
  category and retrieves every determined one has rate zero — below any non-zero floor, and the
  best run the design could hope for. The floor as written excludes it. Invention over a gap can
  present as a good result only by scoring *determined*, which is a classification error, not an
  actor behaviour. **Proposed reading, for ruling:** (i) *determined* is available only in the
  determined partition, applied mechanically at classification, so determined ≤ |determined
  partition| by construction; (ii) the guard the floor was for becomes a separately reported
  per-arm quantity — residual categories scored inferred, over residual size — descriptive only,
  since it is the layer claim's measure restricted to the residual partition; (iii) no run is
  excluded on it. This neither eases nor hardens the claim: inferred over frame is untouched.
  **Blocks Gate 3**, whose deliverables include the floor computation and below-floor reporting.
- **U-2 — §5 contradicts itself.** The reader "does not see the specification" and classifies
  "against the specification's content". A reader who cannot see the set cannot say whether a
  disposition is traceable to it. The layer pre-registration met the same problem with two stages
  (its §6). **Proposed for Gate 4:** stage 1, a reader sees output and frame only, marks each
  category *disposed* (the output commits), *raised* (the output names it unsettled and does not
  commit), or *untouched*; stage 2, a different reader — or a mechanical step — sees the frame,
  the partition, the set as content, and the disposed resolutions, never an arm: disposed in the
  determined partition and agreeing with the set is *determined*; disagreeing is *inferred*;
  disposed in the residual partition is *inferred*; raised is *asked*. *Untouched* needs a ruling
  (a determined category the output never reaches is a delivery failure, not an inference; a
  residual one untouched is neither surfaced nor invented). **Blocks Gate 4.**
- **U-3 — "Correctness is irrelevant" names two correctnesses and only one is irrelevant.**
  Correctness against the world — would the principal have decided this — is irrelevant, and
  Gate 4's worked example lives there: a residual category the actor disposes of well is
  inferred. Correctness against the set is the measure in the determined partition, unavoidably:
  from output alone a retrieval and a coincidentally agreeing inference cannot be told apart.
  Stated limit: where P is read badly and convention happens to agree with the set, P's inferred
  count is deflated — a bias against the hypothesis, so conservative. **Mitigation for Gate 1:**
  prefer determinations whose content departs from convention where the act allows, so agreement
  is evidence of retrieval rather than of convention. The rubric must say which correctness it
  means. **Shapes Gate 1 and Gate 4; blocks neither.**
- **U-4 — The partition is two-way and stated as exhaustive, and will not be.** A list drawn for
  the act type — as the prompt directs — will hold categories this set neither disposes of nor
  declares. Two resolutions: (a) close the set against the frame after Gate 2 by adding a
  residual declaration for each such category — a declaration of absence, the layer
  pre-registration's arm A construction — so the partition is exhaustive by construction; (b)
  admit a third partition, *silent*, kept in the denominator (excluding it would be frame-tuning),
  where inference is expected in both arms alike. **Recommendation: (a)**, because it makes §4
  true as stated and uses the list the way the layer claim will. Consequence: Gate 1's set is not
  final; it is closed against the frame after Gate 2 and fixed at Gate 3. **Blocks Gate 3.**
- **U-5 — "Asked" is not operational for a single-turn actor.** An actor performing the act end
  to end cannot wait for an answer; every ask is ask-and-stop or ask-and-proceed with a labelled
  provisional choice, and the scheme has no cell for a disclosed provisional choice. **Proposed
  for Gate 4** as a borderline case with the ruling stated: *asked* if the output marks the
  category as not settled by the artefact and flags it for a decision, whether or not it proceeds
  provisionally; *inferred* if it commits without marking. The harness must not suppress
  questions — a requirement on the executing session, recorded here. **Blocks Gate 4.**
- **U-6 — Parity is stated per "determination" and a record carries more than a statement.**
  Extent states (silence included), allocation class, principal, predicate with coverage and
  uncovered set, positions with boundary fields, provenance. Unless the set enumerates its content
  at field granularity and P carries every item, either R carries content P lacks — §7's third
  failure condition, before any run — or P drops the structure and the comparison is of content,
  not form. **Proposed for Gate 1:** the set is a content inventory, per determination and per
  field, in the foundation's construct vocabulary (§2.1–2.8) rather than the schema's field
  names; Gate 3's parity check is item-by-item against it; the P author receives the inventory,
  never the records. **Shapes Gate 1 and Gate 3.**
- **U-7 — The set cannot be notation-neutral.** A field-granular table is record-shaped; prose is
  P-shaped. The inventory of U-6 in the foundation's vocabulary is the least-bad form, since both
  arms derive from it. Threat, not defect: the form the P author received is reported at
  execution.
- **U-8 — The structured-prose secondary comparison (§8) is a third arm in all but name**, and
  nothing says who authors it or how. Authored freely, it is a third quality variable; derived
  mechanically from P — restructuring only, no rewording — it is a controlled variant.
  **Recommendation:** mechanical derivation by the P author after P is fixed; same runs per arm;
  descriptive only, per Carried 3. **Affects Gate 3 quantities; needs a ruling before Gate 3.**
- **U-9 — The worked example pre-empts Gate 1.** `examples/place-order.determinations.yaml` is a
  complete determination set for `PlaceOrder` in arm R form, and the binding README paraphrases
  three of its determinations in prose. Selecting that act with that set would mean arm R exists
  before ratification, visible to whoever writes P. **Constraint carried into Gate 1:** the set is
  not the example's; any act from this event model is a contamination threat to the degree the
  example touches it. Selection rule to address it explicitly.
- **U-10 — Whether the binding is public is not determinable from the bundle.** The schema's
  `$id` names `Hafeok/specification-languages`, which this repository's README records as not
  created. If it is public, the actor may have seen the schema and the example. Reported at
  execution per §6.5; nothing here settles it.
- **U-11 — One decision point per category.** §1 counts per decision point; §4 enumerates
  categories. A category holding several decision points reintroduces a reader threshold into
  the denominator, which §4 exists to remove. Requirement on Gate 2: each category is written as
  one question with a recognisable answer.
- **U-12 — "Conforming" is anchored to a criterion that is not canon.** The binding self-certifies
  11/11 against a criterion that exists as its own checker and manifest (PR-1..3, SR-1, DP-1..7);
  this repository's canon holds no conformance criterion yet. The experiment is unaffected — arm R
  is written against the schema regardless — but a pass licenses a claim about *this binding*,
  not about "a conforming notation" in a sense the canon does not yet have. Stated wherever the
  result is cited.

**Not unsound.** The unfixed threshold and run count are Gate 3's deliverables, not defects.
Single actor on a single act is Carried 4, stated where cited. The prediction is falsifiable once
Gate 3 fixes its quantities and U-1 is ruled; without U-1 ruled, the exclusion rule as written
could remove the runs most favourable to the hypothesis, which is a defect of the wrong shape to
be a bias but is not a falsifiable design either.

## 6. Inconsistencies between arrived documents

- **I-1 — The layer pre-registration cites `CG-R-17` and `CG-R-18`; neither exists at the ref
  read.** It says `prereg-closure-falsifier.md` is "retired under CG-R-17" and the draft rulings
  are "`[DRAFT]` permanently under CG-R-18". The register ends at `CG-R-16`, and nothing in this
  repository carries either identifier — this repository's evidence README still files the
  closure pre-registration as `[PROPOSED]`, not retired. Either two rulings were issued and not
  yet registered (the state OD-2 of the seed session existed to end), or the layer
  pre-registration cites rulings not yet issued. Not determinable here; not this session's
  document. Nothing in this session depends on it, since the layer pre-registration is contrast
  only.
- **I-2 — Binding README and runner vs the example file:** "five determinations" and "5/5" against
  six records (D-2 above).
- **I-3 — Prompt vs invocation:** no disagreement found. The invocation adds two things the prompt
  does not state — the `<REF>` instruction and the branch — and both are followed.

## 7. Carried items, state at Gate 0

1. **Human control arm — undecided; recorded as a block on Gate 3.** With it, runs per arm, the
   actor populations and the output forms Gate 4 must handle all change. Emil's ruling is needed
   before Gate 3 is proposed. The layer pre-registration records the same block for its own §7.3.
2. **Arm P quality.** Gate 3 will propose: the P author's instruction pre-registered verbatim at
   full strength (as the layer pre-registration does for its arm C); item-by-item parity against
   the inventory of U-6; a report of who wrote each arm and whether they saw the other. Gate 0
   adds: the P author receives the inventory, not the records.
3. **YAML familiarity.** U-8 — the secondary comparison needs an authorship rule.
4. **Single act.** Stated wherever the result is cited; Gate 5's assembly carries the sentence.

## 8. Registers

**Rulings in force, applied at this gate:** `CG-rule-01` … `CG-rule-10` (08 and 10 as
provisional); `CG-R-10` (pin not advanced); `CG-R-11` (this session's artefacts, when assembled,
are evidence, not canon); R-1 and R-2 as recorded in the register. No identifier is drawn from
the `CG-R-` space; nothing is issued.

**`[PROPOSED]` by this session so far:** nothing beyond this report's own completeness. The
readings offered under U-1, U-2, U-4, U-5, U-6 and U-8 are candidate rulings for Emil, not
proposals of this session's artefacts.

**`[OPEN]`, held at this gate:** U-1, U-4, U-8 and Carried 1 — **each blocks Gate 3**; U-2 and
U-5 — **each blocks Gate 4**; I-1 — held, blocks nothing here; U-3, U-6, U-7, U-9, U-10, U-11,
U-12 — shape later gates, block none; D-1 and D-2 — the binding's, reported to its author.

**Gates 1 and 2 are not blocked by anything above.** Gate 1 proceeds under the constraints of U-3,
U-6 and U-9 on ratification of this gate.

## 9. Weakest point

**U-3.** In the determined partition, *determined* can only be operationalised as agreement with
the set, because output does not show whether a disposition was retrieved or arrived at. So the
primary measure is, in that partition, a fidelity measure — how faithfully the actor reproduced
the determinations — and the design assumes fidelity and inference load are the same quantity.
The bias argument (coincident convention deflates P, so the error is conservative) softens this
and does not remove it. The Gate 1 mitigation — determinations that depart from convention —
narrows the overlap without closing it, and costs realism in the act. U-1 is the most
consequential defect; U-3 is the one no ruling fixes.

---

**Hold.** Gate 1 is not entered. Awaiting explicit ratification of Gate 0, and Emil's rulings on
U-1, U-4, U-8 and the human control arm before Gate 3, and on U-2 and U-5 before Gate 4. None of
those blocks Gate 1.
