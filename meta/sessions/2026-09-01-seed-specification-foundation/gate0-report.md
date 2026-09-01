# Gate 0 report — arrival and orientation

**Status of this report: session output, proposing nothing for ratification except that Gate 0 is
complete.** Everything it reports is held, not resolved. Register discipline per CG-rule-01:
rulings in force are cited by identifier; everything this session produces is `[PROPOSED]` at most;
open items are marked `[OPEN]`.

No repository structure has been produced. The only commits are the arrival commit (prompt,
invocation, bootstrap) and this one (arrived inputs and this report), both session records under
`meta/sessions/`.

---

## 1. Repository state

**Empty, confirmed.** No commits on the remote, no branches, no files. The working branch
`claude/seed-specification-foundation-g6a2y0` was created from nothing; the arrival commit is the
root commit.

## 2. Governing repository, read and recorded

`Hafeok/canon-governance` read at **`ad6d1b0b861306561364cc8d3a3e554cfb92d90c`** — the head of
`claude/seed-canon-governance-ntf524`, which is the repository's default branch; no `main` exists.
This is the seeding branch head the invocation message directs the session to read.

- `rules/` holds ten rules, `CG-rule-01` … `CG-rule-10`, read in full. Eight carry
  `grade: established`; **`CG-rule-08` and `CG-rule-10` carry `grade: provisional`** in their own
  records, matching the invocation message. They are applied in this session as in force and are
  not cited as established anywhere in this session's output.
- `registry/rulings.yaml` — the programme ruling register, 35 rulings; used below to read R-6's
  status.
- The rules are **not restated** in this repository, at this gate or any later one. They are cited
  at the commit above.

**One wording discrepancy between the invocation message and the repository read (D-4 below):** the
invocation says "registry/governed.yaml is empty pending a ruling"; at the commit read, no
`governed.yaml` exists — `registry/README.md` records it as *not created*, a documented standing
state pending CG-R-9. Operationally identical: nothing is governed, `pending` is unimplementable,
CG-R-2 bars every instrument from issuing a verdict. Reported for exactness, since this session
must not describe the repository as governed in any stronger sense.

## 3. Arrived inputs

Filed with sha256 in `arrived-inputs.md`, byte-identical to the delivered bundle, before use.
Verification against independent copies at `canon-governance`: two byte-identical matches
(`rulings-session-close.md`, `holding-note-structure-and-languages.md`); the prompt differs from
the copy filed there and the diff corresponds point-for-point to the amendments Emil's handover
directed (recorded in `bootstrap.md`).

`specification-language-foundation.md` presents as its original state — its §1 design driver is
still the per-act layer-completeness quantification, with no trace of S-1 or S-2 resolved into the
text — which is what filing requires. *Presents as* is the honest strength: nothing reachable from
this session verifies originality. See the weakest point.

## 4. Gap G-1 — the input that did not arrive

**Input 8, the prior falsifier session's Gate 0 output, from
`claude/closure-falsifier-prereg-w1mm7d`, is not in the bundle.** Emil announced it would be
supplied separately. It has not been reconstructed and will not be; it carries the arrival record
and hashes that filing rules exist to preserve, and a reconstruction would be a substitute artefact
of exactly the kind the prompt prohibits.

**It blocks Gate 3.** The checklist marks it load-bearing there, and the dependency is concrete:

- Gate 3 must propose placement for the falsifier material. Input 7 is a set of rulings *on* the
  missing document; filing rulings on a document that is not itself filed would place an answer
  whose question is absent.
- Input 6 (the pre-registration) arrived in its pre-amendment state (I-1). The missing output is
  the record of the Gate 0 that generated the amendment directions, and it is the likeliest
  independent anchor for the hashes of the foundation and the pre-registration as that session read
  them.

Gates 1 and 2 are not blocked: governance and validators take nothing from input 8. If it has not
arrived by the close of Gate 2, Gate 3 holds on this gap alone regardless of ratification state
elsewhere.

## 5. The three relations, restated

In this session's own words, per the prompt's instruction:

1. **Projects from `actor-indexed-determination`.** A derivation relation, forward only. This
   repository may add determinations to what the root supplies; it may never contradict the root,
   and nothing here may be derived by reading backwards out of anything downstream. A projection
   that conflicts with its upstream is defective, and the defect is repaired by a supersession
   record, not an edit. A projection *cannot legitimately fail* its upstream — failure is always a
   defect.

2. **Peer of `decision-driven-design`.** No dependency in either direction; both project from the
   same root. Nothing is borrowed sideways. The accepted cost (S-1): two projections mean two
   completeness predicates and two term registries, with drift between them a real risk that a
   check must eventually watch.

3. **Conformed to by `specification-languages`** (not yet created). A conformance relation, and
   categorically different from projection: the criterion must be satisfied *with evidence
   published*, and **a conforming instance may fail** — non-conformance is an admissible outcome,
   recorded as such, not a defect. This is the relation most likely to be mistaken for projection
   because "downstream" reads as projection by default; the ordering validator must never be
   pointed at it (Gate 2 carries this as a requirement). No validator for conformance exists, and
   none will exist at the end of this session — a recorded gap, not a closed one.

Orthogonal to all three: **governed by `canon-governance`**, asserted downward from its registry,
never declared here. Compliance, not derivation; non-compliance is a defect, not a variant. Nothing
operational evaluates this repository yet (CG-R-9, CG-R-2).

**Flags:** none of the three relations is believed to be stated wrongly in the prompt. One
formulation in the *orientation note* is superseded — see D-1.

## 6. Disagreements: prompt vs orientation material

The prompt wins in each case, per the precedence rule. Reported, not resolved; no delivered file is
edited.

- **D-1 — "sideways" vs "orthogonal."** `invocation.md` §1: "`governed by` points sideways, not
  up." The prompt: governance is "**orthogonal** — a third axis. Not up, not sideways." Ruling A
  (register: "orthogonal replaces sideways") settles it; the orientation note carries the
  superseded formulation. Prompt applied.
- **D-2 — checklist row on `meta/sessions/`.** `seed-bundle-checklist.md` §1: "native — R-6." The
  prompt: inherited from `canon-governance` via CG-rule-06, R-6 having been superseded by R-7. The
  checklist row is stale — written before the `canon-governance` seed's outcome. Prompt applied;
  this session's records are made under the inherited convention.
- **D-3 — checklist and orientation rows on `CITATION.cff`.** Both list family name, ORCID and
  seed date as outstanding (`SUPPLY`). The delivered `CITATION.cff` arrives with all three filled.
  The delivered artefact is taken as the current state; the rows are stale. (The date it carries
  raises I-6.)
- **D-4 — `governed.yaml` "empty" vs "not created."** Invocation message vs the repository read;
  detail in §2. Operationally identical; recorded for exactness.

## 7. Inconsistencies between arrived documents

Reported and held, per the prompt. None is resolved, and none of the texts has been altered.

- **I-1 — the pre-registration arrived pre-amendment.** `rulings-session-close.md` closes with
  "R-1 and R-2 amendments pending"; `rulings-gate0-closure-falsifier.md` directs further specific
  amendments (D1 frame enumeration, D3 two-stage blinding, D4 strip-only arm B derivation, D5 §1
  threshold reference, D12 act-completeness narrowing, D14 §4/§2 reconciliation, D15 §8 feasibility
  qualifier). **None of these is visible in the arrived `prereg-closure-falsifier.md`.** Whether an
  amended pre-registration exists elsewhere or the amendments have not been made is not
  determinable from the bundle. Filing at Gate 3 must preserve the arrived state either way.
- **I-2 — the human control arm.** The arrived pre-registration §5 mandates it ("Each arm is run
  with … A human control") and its §8 feasibility claim is stated unqualified. The rulings document
  records the arm as **undecided** (carried open item F.1, "Decide before Gate 3" of that
  programme) and accepts at D15 that §8 holds only *without* the arm. The arrived design mandates
  an arm whose inclusion is ruled undecided.
- **I-3 — the rulings document self-declares `[DRAFT]`.** Input 7's own header: "Draft rulings for
  Emil to issue, amend or reject. Not ratified by having been drafted." The prompt and checklist
  list it as *rulings*. Nothing in the bundle states whether issue happened. Gate 3 needs Emil's
  statement of its status before proposing to file it as anything; filing a draft as rulings would
  assert a ratification the record does not contain.
- **I-4 — R-6 arrives unmarked.** `rulings-session-close.md` presents R-6 as in force; the
  `canon-governance` ruling register records it "superseded by R-7," text unaltered at its recorded
  sha256, which the byte-identical arrival confirms. Correct behaviour under CG-rule-02 — the
  superseded record stays in place — but any reader of the filed copy must reach the register to
  learn R-6's status. Gate 3 should propose how the filed copy points to the register without
  amending the arrived text.
- **I-5 — identifier count: 132 vs 122.** The prompt's settled list says the programme-scoped
  prefix reading was "verified at 132 identifiers with no collision" (§Q). CG-rule-07's notes and
  the `canon-governance` handover record the verification at **122** identifiers (CG-R-4, at commit
  `bf9dde9`). One number is wrong, or they measure different sets at different times; not
  determinable here. Nothing in this session depends on the figure.
- **I-6 — `date-released: 2026-08-31`.** The arrived `CITATION.cff` carries a release date one day
  before this seed session runs (2026-09-01), and the repository was empty until today. If the
  citation string is fixed at seed, the date precedes the seed. Whether to keep or amend is Emil's,
  at Gate 1, where placing `CITATION.cff` at root is proposed.
- **I-7 — holdings tables differ on what this repository holds.** The orientation note and prompt:
  construct list, resolution condition, boundary declarations, conformance criterion.
  `holding-note-structure-and-languages.md` §1: "the criterion, resolution condition, boundary
  declarations" — no construct list. The holding note is `[PROPOSED]` orientation and predates the
  bundle; noted only because Gate 3 places the construct list and should not be read against the
  older table.

## 8. Registers

**Rulings in force, applied at this gate:** CG-rule-01 … CG-rule-10 (08 and 10 as provisional);
R-1 … R-5 and R-7 from the programme register; rulings A, B, N, O, Q as recorded there. Ruling O
observed: this session draws no identifier from the `CG-R-` space and issues nothing.

**`[PROPOSED]` by this session so far:** nothing beyond this report's own completeness. The
arrival records are acts performed under the prompt's direct instruction, not proposals.

**`[OPEN]`, held at this gate:**

- G-1 — input 8 outstanding; blocks Gate 3 (§4)
- I-1 … I-7 (§7) — held for Emil; none blocks Gate 1 or Gate 2. I-3 and I-6 need answers before
  the gate named in each
- Carried from the prompt for the session log at close: the five carried risks of its closing
  section, and the six known-open items of the orientation note, none of which this gate advances

## 9. Weakest point

**Five of the seven arrived canon-and-evidence inputs have no anchor outside the bundle that
delivered them.** The foundation, the supersession record, the resolution condition, the boundary
declarations and the pre-registration exist, as far as this session can see, only as this bundle's
copies. The foundation's required "original state" is therefore taken on the bundle's word — the
one property Gate 3's filing design depends on (both states visible, derivation intact) is the one
this session cannot independently verify. The hashes are now on the record, and input 8, when it
arrives, is the likeliest independent cross-check; until then, "verified original" would be an
overclaim and is not made.

---

**Hold.** Gate 1 is not entered. Awaiting explicit ratification of Gate 0, and Emil's word on I-3
(status of the draft rulings) and I-6 (the release date) at his convenience — neither blocks
Gate 1.
