# Gate 2 — the repairs, as proposed

**Session:** `2026-10-06-post-move-repair` · **State when reported:** held, repairs uncommitted.

The proposal is `gate2.patch` in this directory: the complete diff of the working tree as reported
at Gate 2, sha256 **`bc71d37ba12eef61cbb81e611d9e8b1c4d72f950265fe26e16b0e70e3ccc6524`**. It is
filed as a session record, not as the repairs. What was committed as the repairs is the patch
with the amendment ruled at Gate 2 (`rulings-gate2.md`, item 2) applied to
`meta/sessions/README.md`.

## The diff, by class

**Live pointers**
- **R-1, `README.md:9`, `:35`, `:51`:** link targets `https://github.com/Hafeok/` →
  `https://github.com/mindovermachine-dev/`. No other word changed; not rewrapped, so the three
  lines run past the file's ~100-column width. Line 72 untouched (G-3).
- **R-2, `CITATION.cff:16`:** `repository-code` → `mindovermachine-dev/specification-foundation`;
  an appended comment at the foot records the old value, the date found (2026-10-06), the date of
  the repair (2026-10-07), the ruling, and that title, authors and date-released are unchanged.
  The file parses.

**Ambiguous, ruled as repair**
- **R-3, `scripts/validate-core-order.py:15`:** owner prefix only. Line 4 untouched; the file
  compiles. The text as ratified survives at
  `meta/sessions/2026-09-01-seed-specification-foundation/gate2-draft/validate-core-order.py:15`.

**Provenance — appended note**
- **R-4, `evidence/falsifier/README.md`:** dated location note appended at the foot, including the
  O-5 result. Line 19, the arrival record and both sidecars untouched; all seven sidecar pins
  still match.
- **O-3:** new `meta/sessions/README.md`. No closed record edited.

**Session record**
- **O-5:** `gate2-o5-runs.txt`, verbatim. `claude/closure-falsifier-prereg-w1mm7d` at
  `mindovermachine-dev/product-cli` resolves to `a1232bf2b60107136115cdc620a2f3df19f2875d`; at that
  commit `prereg-closure-falsifier.md` hashes to `145ed0a2…` and `bootstrap.md` to `662c7eb3…`,
  matching the two sidecars. Read by anonymous git only (the repository is public); nothing was
  attached to the session.

**Untouched (G-3):** `README.md:72`, `meta/canon-governance-ref.yaml:8`. The governance
validator still prints `Hafeok/canon-governance@ad6d1b0…`.

## Validators on the working tree, verbatim

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

Every `Hafeok` string remaining outside `meta/sessions/` is provenance, reserved to G-3, or inside
one of the two appended notes.

## Weakest points, as reported

- `meta/sessions/README.md` went beyond O-3: an opening paragraph on what session records are,
  and a paragraph on the branch rename. Neither was ruled. *(Ruled at Gate 2: the first cut, the
  second kept as a fourth statement.)*
- The edits carry 2026-10-07, when they were made; the session name and the "found" date are
  2026-10-06. Left visible, not smoothed. *(Ruled at Gate 2: both stay.)*
- The working tree was uncommitted in an ephemeral container while the gate held. *(Ruled at
  Gate 2: this patch filed first.)*
