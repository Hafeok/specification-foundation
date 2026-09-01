# Bootstrap — seed `specification-foundation`

**Session:** `2026-09-01-seed-specification-foundation`
**Session kind:** repository seeding. Governance and tooling are built in-session; canon content is
filed, not authored.
**Principal:** Emil. The session proposes; Emil ratifies. Gates hold until an explicit ratification
message.
**Commit identity:** `Claude <noreply@anthropic.com>` — session-neutral, per the prompt and the
invocation message.

---

## Charter documents

The session prompt is filed verbatim as `prompt.md`
(`session-seed-specification-foundation.md` in the delivered bundle,
sha256 `9a2c20adef4c093c85d6ce85df1dc3942385b542b90ed64d374fb30f979f0c85`, 182 lines).

The seeding-programme orientation note is filed verbatim as `invocation.md`
(`BOOTSTRAP.md` in the delivered bundle,
sha256 `96313ce102934ad3fbdab245bbd8fc58f61e63f4ca41357a3dc791f26a6a8e85`, 130 lines).

Where the two disagree, the prompt governs and the disagreement is reported at Gate 0. That
precedence rule comes from the invocation message and from the orientation note itself; it is a
parameter of this session, not an inherited convention.

**The prompt arrived amended.** The copy of this prompt filed at `canon-governance`
(`meta/sessions/2026-08-30-seed-canon-governance/inputs/session-seed-specification-foundation.md`,
sha256 `0844244f46188a4fd1be5c04d2ee65bbb112af4a2003bb020f643bd0468c7d1f`, 155 lines) is an earlier
state. The differences match, point for point, the amendments named in that repository's
`handover-specification-foundation.md`: `meta/sessions/` inherited via `CG-rule-06` rather than
native per R-6; contribution discipline replaced by cite-at-commit; British spelling removed from
Gate 1 governance; the `SF-` prefix restated as a programme-scoped naming convention. The amendment
is Emil's, per the handover's closing line. Verified by diff at Gate 0, not taken on the handover's
word.

## Invocation message

Delivered by Emil with the bundle
(`specification-foundation-seed.zip`, upload path
`/root/.claude/uploads/ca6fc40b-b6eb-5f87-957b-026f658140fc/8a051a03-specificationfoundationseed.zip`).
Verbatim:

> Seed Hafeok/specification-foundation. The repository is created and empty.
>
> Attached: specification-foundation-seed.zip. Read BOOTSTRAP.md first, then
> session-seed-specification-foundation.md, which is the instruction set. Where they disagree, the
> prompt wins and you report the disagreement at Gate 0.
>
> Before Gate 0, read Hafeok/canon-governance at \<REF\> and record the ref you read. Its rules/
> directory holds ten ratified rules that are in force here. They are not reproduced in the bundle
> and must not be restated in this repository — cite them at the commit. Two of the ten are
> provisional (CG-rule-08, CG-rule-10): in force, not citable as established.
>
> canon-governance governs nothing operationally yet — registry/governed.yaml is empty pending a
> ruling on governance start points, and no instrument may issue verdicts. Its rules bind this
> session as rules, not as checks. Do not describe this repository as governed in any sense
> stronger than that. Do not add a declaration that this repository is governed; compliance is
> asserted downward from the registry.
>
> Work on a branch claude/seed-specification-foundation-\<suffix\>. Session-neutral commit identity
> Claude \<noreply@anthropic.com\>. Commit the prompt and a bootstrap record under meta/sessions/ as
> the first act.
>
> One arrived input is missing from the bundle and I will supply it: the prior falsifier session's
> Gate 0 output from claude/closure-falsifier-prereg-w1mm7d. Report it as a gap at Gate 0 and name
> the gate it blocks; do not reconstruct it.
>
> Four gates: governance, validators, filing plan, execute. Hold at each for explicit ratification.
> Propose; do not ratify your own output.
>
> Fill \<REF\> with the canon-governance commit after Gate 4 — the seeding branch head, not main,
> unless you've merged it. Worth pinning the exact hash rather than a branch name, so the session
> records what it actually read.

## Parameters

| Parameter | Value |
|---|---|
| Repository | `Hafeok/specification-foundation` |
| Branch | `claude/seed-specification-foundation-g6a2y0` |
| Base commit | **none — the repository is empty.** No commits, no branches on the remote |
| Gates | Gate 0 arrival · Gate 1 governance · Gate 2 validators · Gate 3 filing plan · Gate 4 execute |
| Register discipline | Rulings in force · `[PROPOSED]` · `[OPEN]`, kept distinct in every gate output (CG-rule-01) |
| Attribution | Emil personally; the editorial role is intended to transfer |

## Governing repository read (not modified)

| Repository | Ref read | Role |
|---|---|---|
| `Hafeok/canon-governance` | `ad6d1b0b861306561364cc8d3a3e554cfb92d90c` — head of `claude/seed-canon-governance-ntf524`, the repository's default branch; `main` does not exist | holds the ten rules in force here; `rules/` read in full |

The ten rules were read at that commit. `CG-rule-08` and `CG-rule-10` carry `grade: provisional` in
their own records and are applied here as in force and not citable as established, consistent with
the invocation message. No source repository is modified by this session.

## Session-record convention

This record is made under `CG-rule-06`, **inherited** from `canon-governance` at the ref above —
not native here, not borrowed from `decision-driven-design`. The prompt's citation of `DDD-dec-20`
is the rule's extraction source; the in-force holding is `CG-rule-06`.
