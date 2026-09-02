# Gate 3 addendum — Part B, completed for ratification

**`[PROPOSED]`.** Completes the filing plan's Part B now that input 8 is retrieved
(arrived-inputs addendum, 2026-09-02). Placement only; nothing executes before ratification.

---

## B-1. What input 8 turned out to be

The branch (`Hafeok/product-cli` `claude/closure-falsifier-prereg-w1mm7d`, head `a1232bf2…`)
holds the falsifier session's **arrival record** — not its Gate 0 report. That session's own
Gate 0 instructed "produce, without writing anything to the repository", and its two commits are
the inauguration and one appended correction. So:

- **The arrival record exists and is filed** (`inputs/closure-falsifier-prereg-w1mm7d/bootstrap.md`,
  sha256 `662c7eb3…`). It carries the identity anchors: the prereg at `145ed0a2…` (byte-identical
  to arrived input 6 — the cross-check Emil named, now verified at source) and the session prompt
  at `4b529663…` (byte-identical to the bundle's copy). It also records that the foundation could
  not be found anywhere on 2026-08-28 — corroborating the ruled permanent provenance fact.
- **The Gate 0 report (restatement, D1–D15 defect list, SPETLR confirmation) was never a
  repository object** and is not on the branch. It is **not reconstructed**. Its content survives
  only refracted through the never-issued draft rulings, which respond to it finding by finding.
  The set filed below is therefore complete with respect to what exists, and the absence is
  recorded where the material lives rather than discovered later.

## B-2. Placement

All under **`evidence/falsifier/`**, each byte-identical to its filed input, each with a
`filing/v1` sidecar (provenance-only, like the supersession record's — evidence awaits no
falsifier and converts to nothing):

| Files as | From | State recorded in the sidecar |
|---|---|---|
| `evidence/falsifier/prereg-closure-falsifier.md` | arrived input 6 | **unamended — the correct state, not merely the faithful one** (Gate 0 ruling on I-1/I-2); carries R-1's bar: tests the mechanism claim, never presentable as a test of the resolution condition |
| `evidence/falsifier/rulings-gate0-closure-falsifier.md` | arrived input 7 | **`[DRAFT]`, never issued** (Gate 0 ruling on I-3); not to be treated as issued; reconsidered when the falsifier work restarts |
| `evidence/falsifier/closure-falsifier-session-arrival-record.md` | input 8 (`bootstrap.md` on the branch) | the arrival record, renamed at filing — content byte-identical, original name and path recorded in the sidecar; carries the anchors and the arrival gap |
| `evidence/falsifier/README.md` | written at filing (governance, not canon) | names the set, the three states above, the never-committed Gate 0 report, and R-1's bar at the directory a reader enters |

The rename of the third file is placement metadata, not amendment: a file named `bootstrap.md`
loose in `evidence/falsifier/` would read as this repository's own apparatus. The sidecar records
`meta/sessions/2026-08-28-closure-falsifier-prereg/bootstrap.md` at
`Hafeok/product-cli@a1232bf2…` as the identity, precedent being the seed's own
`CITATION.cff.arrived`.

Not placed, unchanged from Part A's reasoning: the two falsifier session prompts (future
charters, session-record inputs only — the branch's own `prompt.md` is byte-identical to one of
them and equally stays unplaced).

## B-3. Claim IDs

None, as ratified for Part A. Nothing in the falsifier set is numbered.

## B-4. Weakest point

**The set inherits an absence it cannot cure.** The draft rulings respond to a Gate 0 report that
exists nowhere; filing both the draft and the arrival record makes the absence visible and
navigable, but a future reader of the draft can still mistake its fifteen findings for a summary
of the report rather than a response to it — the README and sidecars say otherwise, and they are
prose (the scope question's territory, instance-counting left to Emil). The alternative —
declining to file the draft until the report is reconstructed — was ruled out at Gate 0:
reconstruction is the substitute-artefact defect, and this absence is a true fact about the
programme's record.

---

**Hold.** Awaiting Part B ratification. On it: the four files land, the sidecars land, validators
re-run, and the session's Gate 4 closes whole.
