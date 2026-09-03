# Bootstrap — notation falsifier pre-registration

**Session:** `2026-09-03-notation-falsifier-prereg`
**Session kind:** proposal only. Four pre-registration artefacts are proposed for ratification —
the act and its determination set, the category list, quantities and thresholds, the
classification rubric. **No arm is authored, no harness is built, nothing is run.**
**Principal:** Emil. The session proposes; Emil ratifies. Every gate holds until an explicit
ratification message.
**Commit identity:** `Claude <noreply@anthropic.com>` — session-neutral, per the prompt and the
invocation.

---

## Charter documents

The session prompt is filed verbatim as `prompt.md`
(`session-notation-falsifier-prereg.md` in the delivered bundle, and separately attached to the
invocation; both copies sha256
`1dd3cee41275a7c608d92628858136c60ec990267457da8d82a87c0269553f72`, 140 lines).

The invocation message is filed verbatim as `invocation.md`.

The design this session works from is `prereg-notation-inference-load.md`
(sha256 `9d29b2fdaa3c740d8975e86910fd865fd674d03d4862f6ed20df66b83c221a34`, 125 lines), filed with
the other arrived inputs in the next commit, with hashes in `arrived-inputs.md`.

## Parameters

| Parameter | Value |
|---|---|
| Repository | `Hafeok/specification-foundation` |
| Branch | `claude/notation-falsifier-prereg-b590ym` |
| Base commit | `ecd4974ab8b33e38475420ae393ee1ec9ebd7c3b` — head of `claude/seed-specification-foundation-g6a2y0`, the repository's default branch ("Gate 4: execute Part B — file the falsifier material; close the session"); no `main` exists |
| Gates | Gate 0 orientation · Gate 1 act and determination set · Gate 2 category list · Gate 3 quantities, thresholds, floor · Gate 4 classification rubric · Gate 5 assembly |
| Gate discipline | Hold at every gate. No gate is passed on the session's own assessment; each requires an explicit ratification message from the principal |
| Register discipline | Rulings in force · `[PROPOSED]` · `[OPEN]`, kept distinct in every gate output (`CG-rule-01`) |
| Claim under test | The **notation** claim only. Not the layer claim (`prereg-residual-declaration-mechanism.md`, included for contrast), not the accrual claim |
| Delivered bundle | `notation-falsifier-bundle.zip`, sha256 `64c70ab5b698da8b2f7d1e8bfb8ba124dcfbfa69177ecc8fd84b75b787979985`, upload path `/root/.claude/uploads/bbf511ec-785e-5336-8780-ce1fc035428c/d6efba8f-notationfalsifierbundle.zip` |

## Governing repository read (not modified)

| Repository | Ref read | Role |
|---|---|---|
| `Hafeok/canon-governance` | **`c5383be06e5b181dc79307554a35cddeacbcd3e8`** — head of `claude/seed-canon-governance-ntf524`, the repository's default branch, dated 2026-09-02 ("registry: append CG-R-10..16, issued during the specification-foundation seed") | holds the ten rules in force here; `rules/` read in full |

**Why this ref.** The invocation's `<REF>` placeholder arrived unfilled. The session read the
default-branch head and records it here as the ref actually read, per the invocation's own
instruction to record what was read.

**Relation to the pin this repository carries.** `README.md` and `meta/canon-governance-ref.yaml`
pin `ad6d1b0b861306561364cc8d3a3e554cfb92d90c`. Diffed: between that ref and the one read, **the
only change is `registry/rulings.yaml`** (the seven rows CG-R-10 … CG-R-16 appended, 106 lines);
`rules/` is byte-identical. The ten rules complied with here are therefore the ten the pin records.
Per `CG-R-10` the pin is not advanced by this session: advancing it is a deliberate act stating
what changed, and what changed does not touch the rules. This record cites the ref read; the
governance-pin validator scans `README.md` only, so the citation here is outside its scope by
design and is stated so nobody wonders.

**The ten rules.** `CG-rule-01` … `CG-rule-10`, read at the ref above. Eight carry
`grade: established`. **`CG-rule-08` and `CG-rule-10` carry `grade: provisional`** in their own
records, matching the invocation: applied here as in force, not cited as established anywhere in
this session's output. Both bear directly on this session — `CG-rule-08` (pre-registration
precedes execution; categories and thresholds fixed at commit, no re-roll) is the discipline the
four artefacts exist to satisfy, and this session is a candidate independent instance of it only
if the falsifier later executes without a re-roll; `CG-rule-10` (prose describes what is in force
and implemented; anything designed but not built carries a date and a marker) governs how every
artefact here describes the harness and arms that do not yet exist.

**The register.** `registry/rulings.yaml` at the ref read ends at `CG-R-16`. This is checked
against the arrived inputs at Gate 0.

## Session-record convention

This record is made under `CG-rule-06`, inherited from `canon-governance` at the ref above. Its
first-commit requirement is met by this commit: prompt, invocation and bootstrap, ahead of any
other act. Arrived inputs are filed with their hashes in the next commit, before use.
