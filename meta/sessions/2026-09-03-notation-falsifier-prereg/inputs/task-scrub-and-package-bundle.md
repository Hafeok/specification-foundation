# Session task: scrub and package the category derivation bundle

**For the held notation falsifier session on `claude/notation-falsifier-prereg-b590ym`.** A bounded task inside the existing hold, not a new gate. Gate 2 remains held pending CG-R-35.

**Record this task and its ruling basis in the session log before the first act.**

---

## Why

The bundle prepared for CG-R-35 is filed as `blind-rederivation/`. That folder name discloses the design: *re-derivation* implies a prior derivation, and one step gets a competent reader to what it is being compared against. CG-R-39 named the framing channel; this is that channel left open in a path.

The receiving session must be able to derive a category list without learning that its list will be compared, or that a proposed list exists. If it knows, it will produce what it infers is wanted, which is the fitting CG-R-35 exists to detect arriving from the other side.

## Standing rules

As in force for this session. In particular: supersession never rewrites, errors are corrected by appended note, you propose and Emil ratifies, and each output names its weakest point.

**The rename is a change, not a rewrite.** Use `git mv` so the old path stays in history. Do not force-push and do not rewrite the commits that filed the bundle.

## Prohibitions

- **Do not modify the proposed category list, the Gate 1 determination set, or the reconciliation rule.** This task touches the bundle only.
- **Do not weaken the brief while scrubbing.** A scrub that would change what the derivation is asked to do is reported, not performed. See Gate B.
- **The scrub record does not go in the bundle.** It enumerates the leaking terms, so filing it inside would reintroduce every leak it documents. It goes in the session directory.
- Do not hand the receiving session repository access. See Gate C.

---

## Gate A — leak audit

Enumerate, do not fix.

Search the bundle — every file, plus path names, the manifest, and any header or provenance line — for anything that would let a reader infer the purpose. At minimum:

| Class | Terms |
|---|---|
| the comparison | blind, re-deriv, reconcil, independent, compare, overlap, proposed list, set-fitted, grade |
| the experiment | falsifier, arm, inference, notation, experiment, measure, denominator |
| **the frame** | frame, category list as a measured object, anything implying the list is counted against something |
| the act | the Gate 1 act instance, every determination identifier, the eleven determinations |
| provenance | session names, gate numbers, ruling identifiers, branch names |

**The frame row is the one to search hardest.** If the brief describes the output as a frame, the receiving session knows there is a measure and will reason about what makes a good denominator rather than what makes a category.

For each hit: the file, the location, the term, and **what a reader could infer from it**. A term that leaks nothing in context is reported as a hit and marked as such rather than silently passed over.

Report the count of files searched as well as the count of hits, so a search that missed a file is visible.

**Hold.**

---

## Gate B — apply

On ratification of the audit:

1. `git mv blind-rederivation/ command-slice-categories/` — or a better neutral name, proposed at Gate A.
2. Apply each ratified substitution. **Neutral wording that preserves meaning, never deletion**, unless deletion is ratified for a specific hit.
3. Where a substitution would change what the derivation is asked to do — the grid, the four admission conditions, the naming rules, the output form — **do not perform it**. Report it, and state what the receiving session will therefore be able to infer. A brief scrubbed into something that asks a different question is worse than a brief that leaks, because the leak is visible and the change is not.
4. Regenerate the manifest with fresh hashes over the scrubbed files.
5. Add `INVOCATION.md` to the bundle, from the arrived invocation file, so the receiving session's instruction set and its brief are filed together and their consistency is checkable.
6. File the **scrub record in the session directory, outside the bundle**: every substitution as before-and-after, every hit not substituted with its reason, the old and new manifests, and the old folder name.

**Hold.**

---

## Gate C — package and open the PR

1. Produce a distributable copy of `command-slice-categories/` — an archive — with its sha256 recorded in the session log. **This is what gets handed over.** The receiving session works from the archive: no clone, no branch, no repository access, per CG-R-39.
2. Open a PR from this branch. Its description states: what the bundle is for in terms safe to read publicly, the scrub record's location, both manifests, and that the bundle is handed over as an archive rather than cloned.
3. State plainly in the PR that **the PR is the provenance record, not the delivery mechanism**. Anyone reading the PR can see the whole design; the receiving session sees only the archive.

**Hold.** Then return to the CG-R-35 hold.

---

## Carried

- The rename does not discharge CG-R-39's framing observation. The brief remains this session's phrasing of a grid that is itself under test, and the reconciliation reads the re-derived rows against the grid rather than against the brief's wording of it.
- If Gate B reports a substitution refused under rule 3, that inference is a stated limit on the re-derivation's independence and belongs in the reconciliation, not only in the scrub record.
- Register debt CG-R-17 … CG-R-40 is unaffected and remains outstanding.
