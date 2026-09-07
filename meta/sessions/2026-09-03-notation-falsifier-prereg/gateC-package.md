# Gate C — package and provenance

**Filed 2026-09-07.** The handover artefact and its identity.

## The archive

| | |
|---|---|
| File | `command-slice-categories.zip`, in this session directory |
| sha256 | `8b53e98805bd5cab63b62c4ff13a4a88fee399c2495b19bbc448eb1713de59f9` |
| Size | 15824 bytes |
| Contents | `command-slice-categories/` — `README.md`, `INVOCATION.md`, `foundation.md`, `supersession-extract.md`, `resolution-condition.md`, `boundary-declarations.md`, `MANIFEST.md` |
| Built | from the committed directory, files in sorted order, extra attributes stripped, modification times normalised to 2026-09-07T00:00:00Z, so a rebuild from the same commit yields the same bytes |
| Verified | unpacked and every file's sha256 checked against the enclosed `MANIFEST.md` |

**This is what gets handed over.** The receiving session works from the archive: no clone, no
branch, no repository access (`CG-R-39`). Its invocation is inside it; the manifest is what it
checks first.

## The PR

Opened from this branch against the repository's default branch as **the provenance record,
not the delivery mechanism.** Anyone reading the PR sees the whole design — the set, the
proposed list, the reconciliation rule, the audit and the scrub record. The receiving session
sees only the archive. The PR's URL is appended below when it exists.

## PR opened

<https://github.com/Hafeok/specification-foundation/pull/1>, from
`claude/notation-falsifier-prereg-b590ym` against `claude/seed-specification-foundation-g6a2y0`,
2026-09-07. Its description states what the bundle is for, where the audit and scrub record are,
both manifests, that the bundle is handed over as an archive and not cloned, and that the PR is
the provenance record while the receiving session sees only the archive. The archive was also
delivered to Emil directly in the session conversation.

**Correction, appended (`CG-rule-09`).** The PR description as first posted carried the dropped
schema's sha256 in the *before* manifest with one digit wrong (`…cba53fc67c6` for
`…cba52fc67c6`) — a transcription error by this session, caught by re-reading the posted body
against the committed manifests. The PR body is corrected in place, since a PR description is
not a repository record; this note is the record of the slip and the catch. The committed
manifests and the scrub record were never wrong.

---

**Task complete. Back to the `CG-R-35` hold**: awaiting the re-derived list.
