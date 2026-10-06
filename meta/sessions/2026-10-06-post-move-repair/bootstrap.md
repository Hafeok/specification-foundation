# Bootstrap — post-move repair

**Session:** `2026-10-06-post-move-repair`
**Session kind:** repair. No canon is authored, no claim is filed, no criterion is written.
**Principal:** Emil. The session proposes; Emil ratifies. Every gate holds until an explicit
ratification message.
**Commit identity:** `Claude <noreply@anthropic.com>` — session-neutral, per the prompt.

---

## Charter document

The session prompt is filed verbatim as `prompt.md`, the session's first commit (`df5b8b3`), per
`CG-rule-06`. It arrived as the body of the invocation message, not as a file; the filed copy is a
transcription of that body, and its hash is of the filed copy.

| File | sha256 | Lines |
|---|---|---|
| `prompt.md` | `b4036b3ee29db2edc231542da4b85e0101406d4833b8b172d0c5d88acda86911` | 73 |

No other input arrived. Nothing else is filed as an arrived input.

## Parameters

| Parameter | Value |
|---|---|
| Repository | `mindovermachine-dev/specification-foundation` (moved from `Hafeok/specification-foundation`) |
| Branch | `claude/ecstatic-mccarthy-ns00bh` |
| Base commit | `9b6c4d0b85081d8087d7397d2eee5b18c126870b` — head of `main`, the default branch (formerly `claude/seed-specification-foundation-g6a2y0`) |
| Gates | G-1 survey · G-2 repairs · G-3 the governance citation · G-4 close |
| Register discipline | Rulings in force · `[PROPOSED]` · `[OPEN]`, kept distinct in every gate output (`CG-rule-01`) |

## Governing repository

`canon-governance` was **not read** at Gate 1. The citation in force remains
`ad6d1b0b861306561364cc8d3a3e554cfb92d90c` and is not advanced by this session (prompt
prohibition; `CG-R-10`). Whether the commit resolves at the repository's present location is a
G-3 question.

---

## Appended note — D-1, commit identity of the first commit (2026-10-06)

The first commit of this session, `df5b8b3cc0d1e9baa2c37e3e6f2310fbe513259a` ("File the post-move
repair session prompt…"), carries author and committer `Claude (Emil)
<claude+emil@okkels-klein.dk>`, **not** the session-neutral identity the prompt requires. Cause:
the container sets `GIT_AUTHOR_NAME`, `GIT_AUTHOR_EMAIL`, `GIT_COMMITTER_NAME` and
`GIT_COMMITTER_EMAIL`, which take precedence over the `-c user.name=… -c user.email=…` the commit
was made with. The defect was the session's: the identity was not checked before committing.

Not corrected by amendment or force-push, per the standing rule. The commit stays as made; this
note records the error beside it. Every later commit in this session sets the four environment
variables explicitly to `Claude <noreply@anthropic.com>`.
