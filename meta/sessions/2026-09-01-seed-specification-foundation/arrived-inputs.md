# Arrived inputs — seed `specification-foundation`

Every input is filed with its sha256 before use. Hashes are of the filed copy, which is
byte-identical to the delivered bundle.

**Filing an input is not placement.** These copies are session records — provenance for what this
session was given. They are not canon, and filing them here creates no claim ID and no canonical
location. Placement is Gate 3's to propose and Gate 4's to execute.

---

## 1. The eight arrived inputs named in the prompt

| # | File | sha256 | Lines | Status |
|---|---|---|---|---|
| 1 | `inputs/specification-language-foundation.md` | `3d9a52546fc35b05fffb2b0de2a97faa656b813e61c3c893ab2a093571219510` | 142 | canon, `[PROPOSED]` by its own header; **required in original state** — see verification note below |
| 2 | `inputs/supersession-foundation-construct-list.md` | `0c2c17cce8e9abe01b7a1dbc27a5e8148ce0bb31cfcacc9436e01a215940b700` | 75 | provenance; S-1 and S-2, `[PROPOSED]` |
| 3 | `inputs/resolution-condition.md` | `802fc286cfcbb308b178066386bc1da6bceb4d006d33dbdc62fb2b40264b0055` | 58 | canon, `[PROPOSED]`; depends on S-2 |
| 4 | `inputs/boundary-declarations.md` | `0690cb5577d24e7b27077141c06f4572451797de406c41bfb8d6cdf05fcb131e` | 79 | canon, `[PROPOSED]`; depends on S-2 |
| 5 | `inputs/rulings-session-close.md` | `c7fa1c035687876227c3c26b548e04c0632de0b32f63dc6587fe6a36c5553035` | 48 | **rulings** R-1…R-6; byte-identical to the copy filed at `canon-governance` (same sha256). R-6 is superseded by R-7 per the `canon-governance` ruling register; the text arrives unmarked and is filed as arrived |
| 6 | `inputs/prereg-closure-falsifier.md` | `145ed0a2204d1a698cb0d4d6ff2b33ba431d20a152d52b86cc91986df3fd632b` | 113 | evidence, not canon; `[PROPOSED]`. **Arrived in its pre-amendment state** — see Gate 0 report, I-1 |
| 7 | `inputs/rulings-gate0-closure-falsifier.md` | `1b568178938463754f5d6de292316c86be6596d5ef8cc83b7436ab6fd1323004` | 86 | self-declared `[DRAFT]` — "for Emil to issue, amend or reject". Issued status not stated in the bundle; see Gate 0 report, I-3 |
| 8 | prior falsifier session's Gate 0 output, from `claude/closure-falsifier-prereg-w1mm7d` | — | — | **DID NOT ARRIVE.** Announced by Emil as to be supplied. Reported as gap G-1; blocks Gate 3. Not reconstructed |

## 2. Charter documents (filed in the arrival commit)

| File | sha256 | Lines |
|---|---|---|
| `prompt.md` (`session-seed-specification-foundation.md`) | `9a2c20adef4c093c85d6ce85df1dc3942385b542b90ed64d374fb30f979f0c85` | 182 |
| `invocation.md` (`BOOTSTRAP.md`) | `96313ce102934ad3fbdab245bbd8fc58f61e63f4ca41357a3dc791f26a6a8e85` | 130 |

## 3. Also delivered with the bundle

| File | sha256 | Lines | Status |
|---|---|---|---|
| `inputs/CITATION.cff.arrived` | `cd4467af5b16abda913d824813c6dc4021c34b06c5d4868743747c47f67330b7` | 32 | **complete** — the three `SUPPLY` fields the checklist lists as outstanding arrive filled (family name, ORCID, `date-released: 2026-08-31`). Filed with the `.arrived` suffix: placing a `CITATION.cff` at root is a Gate 1 act. See Gate 0 report, I-6 on the date |
| `inputs/seed-bundle-checklist.md` | `c101d578aa54b637496fe47b86012838dd24895d98afda9da8ffe010e1744f60` | 83 | orientation; two rows stale — see Gate 0 report, D-2 and D-3 |
| `inputs/falsifier/session-closure-falsifier-prereg.md` | `4b5296634f648957b56563922d37b5103610795a8c17797e4b0e884ac40a3be0` | 134 | a future session's prompt; not this session's instruction set |
| `inputs/falsifier/session-closure-falsifier-harness.md` | `9f27f2fe4e913176d6fbd54d046b26e4f4aa652d45bd2cb951d7e7e0944be664` | 124 | a future session's prompt; not this session's instruction set |
| `inputs/reference/event-modelling-conformance.md` | `bf852a1d0df69ae45fd3e6dfc3f869ed9cd192f5dcd335aecd26ba11710d23a2` | 105 | `[PROPOSED]` assessment; reference |
| `inputs/reference/holding-note-architecture-accrual.md` | `b083b56627335b293c374c84a8517dbe2a04d25e9c79b9632b4e3c970a3ebf47` | 128 | `[PROPOSED]` holding note; reference |
| `inputs/reference/holding-note-structure-and-languages.md` | `ff987768a62dbc06c862ae3c757000a7c836040b06ebd54c4e0f2fe3a763286f` | 134 | `[PROPOSED]` holding note; byte-identical to the copy filed at `canon-governance` (same sha256) |
| `inputs/reference/hypothesis-actor-proximate-accrual.md` | `3ee6f2ef0c51cf557287e76ba754913450b6b1023cff7876962b2bbab5d8562f` | 74 | `[PROPOSED]` hypothesis; reference; unratified, ID unassigned |

---

## Verification against independent copies

Three of the delivered files have copies filed at `Hafeok/canon-governance`
(`ad6d1b0b861306561364cc8d3a3e554cfb92d90c`,
`meta/sessions/2026-08-30-seed-canon-governance/inputs/`), giving an anchor outside this bundle:

- `rulings-session-close.md` — **byte-identical** (sha256 match)
- `holding-note-structure-and-languages.md` — **byte-identical** (sha256 match)
- `session-seed-specification-foundation.md` — **differs**; the arrived copy is the amended state.
  Diffed in full; every difference corresponds to an amendment named in that repository's
  `handover-specification-foundation.md`. Recorded in `bootstrap.md`.

The remaining arrived inputs (items 1, 2, 3, 4, 6, 7) have no independent copy reachable from this
session. Their hashes are recorded here so that later cross-checks — including against input 8 when
it arrives, which as the falsifier session's arrival record may carry hashes of the foundation and
the pre-registration — can establish what this session cannot: that these are the states earlier
sessions read. In particular, item 1's "original state" is taken on the bundle's word; nothing
reachable here verifies it. See Gate 0 report, weakest point.
