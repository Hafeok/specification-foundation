# Gate 1 — survey, before any edit

**Session:** `2026-10-06-post-move-repair` · **Base:** `main` at `9b6c4d0` · **State:** held. No
repair has been made. The only files this session has written are its own records in this
directory.

Method: case-insensitive search for `hafeok` across every tracked file (65 lines in 37 files,
excluding this session's directory), plus the members of the one archive in the tree
(`command-slice-categories.zip`, 7 members, scanned decompressed: **0 hits**), plus a search for
`github.com`, `upstream`, `mindovermachine` and the former branch name, for location references
that do not carry the old owner string. **`canon/` and `terms/`: 0 hits. Licence files: 0 hits.**

---

## Rulings in force that this gate applies

- `CG-R-10` — a citation records what was read and complied with, not what is current; it
  advances only by a deliberate act; going stale is its correct behaviour.
- The prompt's rule for hard cases: a reference saying where to find something **now** is
  repaired; one saying **what was read, when** is left exactly as it is, and, if now ambiguous,
  receives an appended note, never an edit to the original line.
- Supersession never rewrites; errors are corrected by appended note.

## 0. Location facts as found (2026-10-06)

From the account's repository listing (the session's GitHub scope covers only this repository,
so the siblings were **listed, not read**):

| Repository | Present location | Visibility | Moved? |
|---|---|---|---|
| `specification-foundation` | `mindovermachine-dev/specification-foundation` | public | yes |
| `actor-indexed-determination` | `mindovermachine-dev/actor-indexed-determination` | public | yes |
| `decision-driven-design` | `mindovermachine-dev/decision-driven-design` | public | yes |
| `canon-governance` | `mindovermachine-dev/canon-governance` | **private** | **yes** — the prompt's "presumably" is confirmed |
| `product-cli` | `mindovermachine-dev/product-cli` | public | yes (not named in the prompt) |
| `ai-development-foundations` | `Hafeok/ai-development-foundations` | public | **no** |
| `specification-languages` | — | — | does not exist under either owner |

So the programme is **not** split across two accounts in the governing sense: all four programme
repositories are under `mindovermachine-dev`. The one repository still under `Hafeok` that this
repository mentions (`ai-development-foundations`) appears only inside a filed provenance record.

**Untested:** whether the old `github.com/Hafeok/…` URLs still redirect. GitHub normally
redirects after a transfer until the old name is reused, but the container's proxy refuses
unauthenticated GitHub HTTP (403), so this was not observed. The survey does not rely on
redirects either way.

---

## 1. Every `Hafeok` reference, classified

### 1a. The live surface — files outside `meta/sessions/`

| # | Location | Text (abridged) | Class | Note |
|---|---|---|---|---|
| L-1 | `README.md:9` | link `https://github.com/Hafeok/actor-indexed-determination` | **live pointer** | |
| L-2 | `README.md:35` | link `https://github.com/Hafeok/decision-driven-design` | **live pointer** | |
| L-3 | `README.md:51` | link `https://github.com/Hafeok/canon-governance` | **live pointer** | target is now **private** — see §5, F-3 |
| L-4 | `CITATION.cff:16` | `repository-code: "https://github.com/Hafeok/specification-foundation"` | **live pointer** | see §4 |
| G-a | `README.md:72` | "The rules … are held in **`Hafeok/canon-governance`**, read at commit **`ad6d1b0…`**" | **mixed: false statement of location + provenance** | reserved to G-3 |
| G-b | `meta/canon-governance-ref.yaml:8` | `repo: Hafeok/canon-governance` | **provenance-shaped recorded value** | reserved to G-3 |
| A-1 | `scripts/validate-core-order.py:15` | "the forward-only, never-contradicted derivation of this repository from Hafeok/actor-indexed-determination" | **ambiguous** — see below | |
| P-1 | `scripts/validate-claims.py:4` | "Adapted at Gate 2 … from Hafeok/decision-driven-design … at commit d89ed557…" | **provenance** | |
| P-2 | `scripts/validate-core-order.py:4` | same | **provenance** | |
| P-3 | `scripts/README.md:8` | "adapted from `Hafeok/decision-driven-design` at `d89ed557…`" | **provenance** | |
| P-4 | `evidence/falsifier/README.md:19` | "(`Hafeok/product-cli`, branch `claude/closure-falsifier-prereg-w1mm7d` …)" | **provenance** | describes where a filed record came from |
| P-5 | `evidence/falsifier/closure-falsifier-session-arrival-record.md:17,19,40,41,42,53` (6) | `Hafeok/product-cli`, `Hafeok/decision-driven-design`, `Hafeok/ai-development-foundations`, `Hafeok/specification-language`, merge subject | **provenance** — and **hash-pinned** | sha256 `662c7eb3…` in its sidecar; verified matching. Any edit breaks the pin |
| P-6 | `evidence/falsifier/closure-falsifier-session-arrival-record.filing.yaml:8` | `original_identity: … at Hafeok/product-cli, branch …, commit a1232bf2…` | **provenance** (an identity statement) | |
| P-7 | `evidence/falsifier/prereg-closure-falsifier.filing.yaml:14` | "Verified at an independent source: byte-identical to … at Hafeok/product-cli … commit a1232bf2…" | **provenance** | |

**A-1, the ambiguous one.** It is a docstring saying what the validator governs: a present-tense
description, not a record of a reading. That argues for repair. Against: it was written at Gate 2
of the seed as part of an adaptation whose provenance the same docstring carries (line 4). The
owner prefix serves to name the upstream; the relation itself is unchanged by the move.
Following the standing note, it is **treated as ambiguous and reported here, not decided**. See
§6 for the proposal.

### 1b. Session records — `meta/sessions/` (closed sessions)

All of these record what a session was given, read, proposed, ran or opened, at a moment. **All
are classed provenance**, and many are also hash-pinned as arrived inputs:

| Location | Lines | What it records | Class |
|---|---|---|---|
| `2026-09-01-seed-…/prompt.md` | 47, 48, 50, 134 | the seed prompt as received | provenance (arrived; hashed) |
| `2026-09-01-seed-…/bootstrap.md` | 44, 50, 80, 91 | invocation quoted; repository parameter; ref read | provenance |
| `2026-09-01-seed-…/gate0-report.md` | 22 | `canon-governance` read at `ad6d1b0…` | provenance |
| `2026-09-01-seed-…/gate2-proposal.md` | 17 | validator source | provenance |
| `2026-09-01-seed-…/gate3-partb-addendum.md` | 10, 42 | `product-cli` identity | provenance |
| `2026-09-01-seed-…/rulings-close.md` | 44 | where the falsifier branch was located | provenance |
| `2026-09-01-seed-…/arrived-inputs.md` | 53, 86 | sources of arrived inputs | provenance |
| `2026-09-01-seed-…/outstanding-dependencies.md` | 9 | OD-1 cleared: "retrieved from `Hafeok/product-cli@a1232bf2…`" | provenance |
| `2026-09-01-seed-…/gate2-landing-runs.txt`, `gate4-parta-runs.txt`, `gate4-partb-runs.txt` | 16, 16, 15 | **verbatim validator output**: `README cites Hafeok/canon-governance@ad6d1b0…` | provenance (verbatim output) |
| `2026-09-01-seed-…/gate1-draft/README.md`, `gate1-draft/CITATION.cff` | 9, 35, 51, 72; 16 | the drafts as proposed at Gate 1 | provenance (draft as proposed) |
| `2026-09-01-seed-…/gate2-draft/*` | `canon-governance-ref.yaml:8`, `validate-claims.py:4`, `validate-core-order.py:4,15` | the drafts as proposed at Gate 2 | provenance (draft as proposed) |
| `2026-09-01-seed-…/inputs/*` | `CITATION.cff.arrived:16`, `README.md:13`, `closure-falsifier-prereg-w1mm7d/bootstrap.md:17,19,40,41,42,53` | arrived inputs | provenance (arrived; hashed) |
| `2026-09-03-notation-…/prompt.md` (none), `invocation.md` | 17 | the invocation as received | provenance |
| `2026-09-03-notation-…/bootstrap.md` | 31, 44 | repository parameter; ref read (`c5383be0…`) | provenance |
| `2026-09-03-notation-…/gate0-report.md` | 21, 207 | ref read; the schema `$id` quoted | provenance |
| `2026-09-03-notation-…/arrived-inputs.md` | 52 | the schema `$id` quoted | provenance |
| `2026-09-03-notation-…/gateA-leak-audit.md` | 106 | the `$id` audited as a leak | provenance |
| `2026-09-03-notation-…/gateC-package.md` | 29 | "PR opened: `<https://github.com/Hafeok/specification-foundation/pull/1>`" | **provenance**, but a link a reader may follow — see §6 |
| `2026-09-03-notation-…/inputs/domain-state-change-binding/README.md` | 5 | link `[conformance criterion](https://github.com/Hafeok/specification-foundation)` | provenance (arrived; sha256 `86079e9c…`, verified) |

### 1c. Identifiers — strings that are names, not addresses

| # | Location | String | Note |
|---|---|---|---|
| I-1 | `meta/sessions/2026-09-03-notation-…/inputs/domain-state-change-binding/schema/determination.schema.json:3` | `"$id": "https://github.com/Hafeok/specification-languages/…"` | A JSON Schema `$id` is a name; it never resolved (the repository does not exist). It is also inside an arrived, hash-pinned input (`4df4db09…`, verified). **Not repairable here, not to be repaired.** |
| I-2 | git history: commit `9b6c4d0` (and the PR-1 head label) | "Merge pull request #1 from Hafeok/claude/notation-falsifier-prereg-b590ym" | Immutable history; GitHub's PR head label. Not a file. Quoted in no live file. |
| I-3 | `…/closure-falsifier-prereg-w1mm7d/bootstrap.md:19` and its evidence copy (`…arrival-record.md:19`) | merge subject "from Hafeok/claude/prd-tick-rate-validity-re7ofs" | an identifier inside a provenance record; doubly untouchable |

**Count.** 65 lines: 4 live pointers (L-1…L-4), 2 reserved to G-3 (G-a, G-b), 1 ambiguous (A-1),
the rest provenance or identifiers. No `Hafeok` string anywhere in `canon/`, `terms/`, the
licences, or the workflow.

---

## 2. Branch and default state as found

- **Default branch:** `main` (`git ls-remote --symref origin HEAD` → `ref: refs/heads/main`), at
  `9b6c4d0b85081d8087d7397d2eee5b18c126870b`. It is the renamed seed branch: CI run #18 records
  the same commit on `claude/seed-specification-foundation-g6a2y0`, run #20 on `main`.
- **Other branches on the remote:**
  - `claude/notation-falsifier-prereg-b590ym` at `08d5561` — the head of PR 1, already merged.
  - `claude/consequential-property-categories-3dwjpu` at `04f61c0`, 2026-09-07, "Derive
    consequential-property categories for a command slice". It is not merged into `main`, and
    this session does not touch it. (By its message it is presumably the receiving session of
    the category derivation bundle. That is inferred, not verified.)
  - `claude/ecstatic-mccarthy-ns00bh` — this session's branch.
- **The former name does not resolve:** `git ls-remote origin
  claude/seed-specification-foundation-g6a2y0` returns nothing; the contents API returns 404 for
  `refs/heads/claude/seed-specification-foundation-g6a2y0`. (GitHub's web UI redirect for renamed
  branches was not tested; the proxy blocks it.)
- **References to the former branch name:** **none in any live file or in the workflow**. The
  workflow triggers on `push` and `pull_request` with no branch filter, so the rename cannot have
  disarmed it. The only mentions are in closed session records, all provenance:
  `meta/sessions/2026-09-01-seed-…/bootstrap.md:81` (the seed's branch parameter),
  `meta/sessions/2026-09-03-notation-…/bootstrap.md:33` (base commit "head of
  `claude/seed-…-g6a2y0`, the repository's default branch; no `main` exists"),
  `meta/sessions/2026-09-03-notation-…/gateC-package.md:30` (the PR's base). The notation
  bootstrap's "no `main` exists" was true when written and is left as provenance.

## 3. CI at `main`

**CI:** run #20, workflow `validate`, `push` on `main` at `9b6c4d0`, 2026-10-06 09:22:16Z —
**success** (after the move;
<https://github.com/mindovermachine-dev/specification-foundation/actions/runs/37442476847>).

**Validators, run locally on a clean detached worktree at `9b6c4d0`, PyYAML 6.0.1, verbatim:**

```
$ python3 scripts/validate-claims.py canon/claims/
valid: 0 claims, ids unique, format rules satisfied
exit=0
$ python3 scripts/validate-core-order.py canon
  upstream  no canon/graph/upstream.yaml — nothing pinned yet (0 pins)

upstream-only mode (0 numbered canon docs): 0 errors, 0 warnings
canon: OK — every pin resolves at the pinned ref; no drift
exit=0
$ python3 scripts/validate-governance-pin.py
governance pin: OK — README cites Hafeok/canon-governance@ad6d1b0b861306561364cc8d3a3e554cfb92d90c; 1 hash(es) in README, all accounted for
exit=0
```

The move broke no path. This is partly structural: no `canon/graph/upstream.yaml` exists, so the
ordering validator clones nothing. **The first `upstream.yaml` written will name an upstream repo
to clone, and must use the present location.** Recorded so it is not rediscovered as a CI
failure.

## 4. `CITATION.cff`

- `repository-code` (line 16) points at the old location. It is an address, and a **live
  pointer**.
- **The citation string itself is not affected.** Title, authors (name, ORCID, affiliation),
  licence, keywords and `date-released: "2026-09-01"` carry no location. The comment block
  (lines 27–38) names an in-repository path, which is unchanged.
- **What is required is a URL repair, not a change of citation.** The citation form fixed at seed
  (who, what, when) is untouched by correcting the field.
- **Weakest point:** citation renderers (GitHub's "Cite this repository", Zotero) may emit
  `repository-code` as the `url` of the rendered entry, so the *rendered* string would change in
  its URL. Downstream citations already made with the old URL stay as they are, and they are not
  ours to change. A reader following one depends on GitHub's redirect, which was not tested
  (§0).

## 5. False statements of location, not only links

| # | Location | Statement | Finding |
|---|---|---|---|
| F-1 | `README.md:71–72` | "The rules … **are held in `Hafeok/canon-governance`**, read at commit `ad6d1b0…`" | **False in the present tense.** The repository is held in `mindovermachine-dev`. The sentence fuses a present-tense location claim with a provenance claim, which is exactly the G-3 hard case. Reserved to G-3, not repaired in G-2. |
| F-2 | `meta/canon-governance-ref.yaml:8`, echoed in every validator run | `repo: Hafeok/canon-governance` | Not prose. A recorded value: G-3. Note that the validator **prints** it, so every future CI log will assert `README cites Hafeok/canon-governance@…` until G-3 rules. |
| F-3 | `README.md:51` (and L-3) | link to `canon-governance` presented to a public reader | Not a false *location* once repaired, but the target is **private**: a public reader of this public repository cannot follow it under either owner. The README's claim that whether this repository is governed is "asserted from that repository's registry" is then unverifiable by the public. **Not a repair**: visibility is Emil's decision. Raised as `[OPEN]` O-1. |
| F-4 | `scripts/validate-core-order.py:15` | "derivation of this repository from Hafeok/actor-indexed-determination" | Present-tense; false as to owner. This is A-1, held as ambiguous. |
| F-5 | Statements without the `Hafeok` string | `README.md:39` "`specification-languages` (not yet created)"; `README.md:87` "held in `canon-governance`" | **True as stated.** The name-only references carry no owner and need nothing. |

No live file asserts anything about the branch name.

---

## 6. `[PROPOSED]` — what G-2 would do, if Gate 1 is ratified as classified

| # | Act | Class |
|---|---|---|
| R-1 | `README.md:9, 35, 51`: `https://github.com/Hafeok/…` → `https://github.com/mindovermachine-dev/…`, link targets only, no other word changed | live pointer |
| R-2 | `CITATION.cff:16`: `repository-code` → `https://github.com/mindovermachine-dev/specification-foundation`; plus an appended comment at the foot of the comment block recording the old value and the date of the change, so the wrong value stays visible beside the correction | live pointer |
| R-3 | A-1 (`validate-core-order.py:15`): **recommend repair** of the owner prefix, as a present-tense description of what the validator governs, with line 4 (provenance) untouched. Alternative: leave it, with an appended docstring note. Recommendation weakly held; this is the judgement the standing note warns about, so it is put to Emil rather than taken | ambiguous |
| R-4 | `evidence/falsifier/README.md`: **append** one dated "location note" stating that `product-cli`, `decision-driven-design` and this repository moved to `mindovermachine-dev`, that `ai-development-foundations` did not, and that the records above it are left as read. No edit to line 19, to the hash-pinned arrival record, or to either sidecar | provenance — appended note |
| R-5 | Closed session records: **no edits**. This session's closing record serves as the note for all of them, including the `gateC-package.md:29` PR link | provenance |
| — | G-a, G-b: nothing in G-2; G-3's question | — |

**Weakest point of this proposal:** R-5. The rule says an ambiguous provenance reference gets an
appended note *beside* it. A note held only in a later session's record is not beside anything.
A reader of `gateC-package.md` following the PR link will not see it unless redirects hold. The
alternative is a one-line dated appended note at the foot of each closed session's
`bootstrap.md` (two files). That is more faithful to "beside", at the cost of touching closed
records at all. I lean to the central record and name it as the place this proposal is most
likely wrong.

## `[OPEN]` — for Emil

- **O-1.** `canon-governance` is private, while this repository is public and links to it as the
  source of its governing rules. Is that intended?
- **O-2.** R-3 (A-1): repair, or leave with a note?
- **O-3.** R-5: central note only, or also one appended line per closed session bootstrap?
- **O-4.** For G-3, confirming that `ad6d1b0…` resolves at `mindovermachine-dev/canon-governance`
  needs read access to that repository. It is outside this session's GitHub scope. Adding it
  (read-only) at G-3 is proposed. Without it, G-3 can state the location but not that the
  commit is there.
- **O-5.** Not checked, and outside scope: whether `claude/closure-falsifier-prereg-w1mm7d` at
  `a1232bf2…` still resolves in `mindovermachine-dev/product-cli`. The evidence records' identity
  claims depend on it. R-4's note would say "moved" without asserting the commit is reachable.

## Defects in this session's own output

- **D-1.** The first commit (`df5b8b3`) carries the wrong commit identity. Recorded by appended
  note in `bootstrap.md`; not amended.

---

**GATE 1 — held.** No edits before ratification.
