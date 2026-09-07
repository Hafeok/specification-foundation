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
