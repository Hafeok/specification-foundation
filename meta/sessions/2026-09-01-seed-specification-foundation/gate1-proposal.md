# Gate 1 proposal — governance

**`[PROPOSED]` in full.** Nothing in this proposal is committed to the repository root until
ratified. The draft files are under `gate1-draft/`, verbatim as they would land. No claims, no
canon content, no validators — governance only.

Register discipline: rulings in force applied here are R-2, R-5, ruling Q (`SF-` as programme
naming), rulings A and B (orthogonality; no upward declaration), the Gate 0 rulings of 2026-09-01,
and CG-rule-01…10 as cited (08 and 10 as provisional). Open items are in §6.

---

## 1. Proposed contents

| File | What it is |
|---|---|
| `README.md` | scope of the name, the three relations, canon boundary, governance-by-citation, local conventions, validator commitment marked unbuilt |
| `LICENSE` | CC BY 4.0, verbatim standard text (sha256 `9ba9550a…`, byte-identical to `canon-governance`'s) — canon and prose |
| `LICENSE-code` | Apache-2.0, verbatim standard text (sha256 `cfc7749b…`, byte-identical to `canon-governance`'s) — scripts |
| `CITATION.cff` | the arrived draft with one amendment: `date-released: 2026-09-01`, per the Gate 0 ruling on I-6; the arrived value and the arrived copy's hash recorded in a comment in the file itself |
| `terms/registry.md` | the term registry, seeded with `layer` and `scale`, each entry carrying R-2's independence statement, plus a joint statement that the axes do not nest |
| `canon/README.md` | the canon boundary at the path that enforces it; explicitly empty, filing deferred to Gates 3–4 |
| `evidence/README.md` | evidence-not-canon at its path; explicitly empty; R-1's bar on presenting the closure result as a test of the resolution condition, stated where the material will live |

## 2. Directory structure, with reasons

```
README.md  LICENSE  LICENSE-code  CITATION.cff
canon/            canonical artefacts (empty until Gate 4)
evidence/         evidence about canon (empty until Gate 4)
terms/            term registry (seeded now)
meta/sessions/    session records (exists; CG-rule-06, inherited)
scripts/          validators — created at Gate 2, not now
.github/          CI — created at Gate 2, not now
```

- **`canon/` and `evidence/` as separate top-level paths.** The canon boundary is the prompt's own
  line (foundation, resolution condition, boundary declarations, criterion vs. bindings, tooling,
  falsifier material, session records). Making it a path rather than a header convention means a
  Gate 2 validator can check it mechanically, and a reader browsing the tree gets the boundary
  before reading a single file.
- **`terms/` at top level, not inside `canon/`.** The registry is the repository's vocabulary
  about its own structure — governance-adjacent, not a determination about acts. Filing it as
  canon would give it a claim status it has not earned.
- **`scripts/` deferred to Gate 2** so the directory arrives with working content rather than as a
  promise; same for CI. Their names are stated here only so the structure is proposed once.
- **No claims directory yet.** Creating any claim record before the validators are in place and
  passing is prohibited by the prompt. The shape a claim record takes here follows the validator
  adaptation, so proposing the directory now would prejudge Gate 2's outcome.
- **Contribution discipline lives in the README**, not a separate `CONTRIBUTING.md`. It is four
  local points plus one citation at a pinned commit; a second file would be a second place for the
  pinned commit to go stale.

## 3. The canon-governance citation

Cited in the README at **`ad6d1b0b861306561364cc8d3a3e554cfb92d90c`** — the ref this session
actually read (head of the seeding branch, which is the default branch; no `main` exists). To be
re-verified at Gate 4 per the invocation message: if that repository's head has moved by then, the
session records what it read regardless, and whether the README citation advances is Emil's call
at that gate.

## 4. CG-rule-10 pass over every document in this proposal

Performed before proposing, not left to review:

- `README.md` — the validators are the only apparatus described that does not exist; the section
  is headed *(commitment — not built, as at 2026-09-01)*.
- `terms/registry.md` — the drift check against the peer registry does not exist and is marked as
  a gap with a date, with an explicit statement that nothing is committed to build it.
- `canon/README.md`, `evidence/README.md` — both state they are empty and dated; both describe
  filing discipline in the future tense tied to Gates 3–4 rather than as operating apparatus.
- `CITATION.cff`, licences — describe nothing unbuilt.

## 5. Weakest point

**The structure is asserted one gate before the filing plan that has to live inside it.** The
`canon/` / `evidence/` split is clean for five of the arrived artefacts, but the supersession
record is neither comfortably: it is provenance *about* canon, canonically load-bearing (the
falsifier derivation needs it) yet not itself a determination. If Gate 3 concludes it needs a
distinct placement — say `canon/provenance/` or adjacency to the construct list under a different
convention — the structure ratified here either absorbs that without change (a subdirectory is not
a new top-level path) or has to be superseded within the same session. The proposal deliberately
leaves everything below the two top-level names open to Gate 3 for that reason; the residual risk
is that the two names themselves prove wrong, and that would cost a recorded supersession of a
one-gate-old ratification.

Second, smaller: the README states what the validators will and will not do before Gate 2 has
adapted them. The marker discipline contains the over-claim, but if Gate 2's outcome differs
(e.g. the measurement-over-judgement choice changes what "green" means), the README section is
amended at Gate 2 and the amendment is on the record as a same-session correction.

## 6. `[OPEN]` at this gate

- G-1 — input 8 outstanding (Emil chasing); blocks Gate 3 only.
- Whether the README's canon-governance citation advances at Gate 4 if that repository's head
  moves (§3) — Emil's call then; recorded now so it is not decided by default.

---

**Hold.** Awaiting explicit ratification of Gate 1. On ratification, the draft files land at the
repository root verbatim (any amendments ruled at ratification applied and recorded), and Gate 2
begins.
