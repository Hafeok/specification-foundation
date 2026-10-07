RULING — specification-foundation, session 2026-10-06-post-move-repair, GATE 1

Gate 1 is ratified. The survey's classification stands as filed
(gate1-survey.md, sha256 1250be5145add3902608f8a6a43e1c7e519038d7c926daa918f92388b6df435d).

O-1. canon-governance is private by design. This is intended and is not a defect. No README
     text about visibility changes in this session. Carry it in the closing record as a stated
     fact, so the next session does not rediscover it as a finding.
O-2. A-1 (scripts/validate-core-order.py:15): repair the owner prefix only. Line 4 untouched.
     Record in the closing record that the text as ratified survives at
     meta/sessions/2026-09-01-seed-specification-foundation/gate2-draft/validate-core-order.py:15.
O-3. Closed session records: no edits. The closing record carries the central note. Add one new
     file, meta/sessions/README.md, stating that records dated before this session name
     Hafeok/… as read, that the repositories were found at mindovermachine-dev on 2026-10-06,
     and that the transfer date is not recorded. No transfer date is to be inferred.
O-4. Read-only access to mindovermachine-dev/canon-governance will be granted at G-3.
     G-3 does not open before it is.
O-5. Closed by observation, not by assumption. Re-run it yourself at G-2: resolve
     claude/closure-falsifier-prereg-w1mm7d at mindovermachine-dev/product-cli, and hash
     meta/sessions/2026-08-28-closure-falsifier-prereg/{prereg-closure-falsifier.md,bootstrap.md}
     at that commit against the two evidence sidecars. Record the output verbatim.

R-1. Ratified: README.md:9, :35, :51, link targets only, no other word changed.
R-2. Ratified: CITATION.cff:16 repaired, with the appended comment recording the old value and
     the date of the change.
R-3. Ratified as repair, per O-2.
R-4. Ratified: appended location note in evidence/falsifier/README.md, including the O-5 result.
     No edit to line 19, the arrival record, or either sidecar.
R-5. Superseded by O-3 above.

G-a and G-b (README.md:72, meta/canon-governance-ref.yaml:8) are untouched at G-2. They are G-3's.
Commit identity: set GIT_AUTHOR_NAME, GIT_AUTHOR_EMAIL, GIT_COMMITTER_NAME and
GIT_COMMITTER_EMAIL to Claude <noreply@anthropic.com> on every commit, and check before committing.

Proceed to G-2. Report the diff grouped by class before committing. Hold at GATE 2.
