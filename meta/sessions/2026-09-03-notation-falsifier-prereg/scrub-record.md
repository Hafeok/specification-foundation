# Scrub record — category derivation bundle

**Filed 2026-09-07 in the session directory, outside the bundle**, because it enumerates the
leaking terms. Records every change Gate B made to the bundle, every audited hit it did not
change and why, both manifests, and the old folder name. Read with `gateA-leak-audit.md`
(the hits) and `rulings-gateA.md` (the rulings).

## 1. The rename

`blind-rederivation/` → `command-slice-categories/`, by `git mv` in its own commit, so the old
path stays in history. Nothing inside changed in that commit.

## 2. Substitutions in the brief (`README.md`), before and after

Thirteen, applied by a script that required each *before* text to occur exactly once. Each is
neutral wording preserving the instruction; none touches the grid, the four admission
conditions, the naming rule's vocabulary, or the output form. Two are consequences of other
rulings rather than audit hits and are marked so: the §3 and §4.2 references to the schema
(dropped under `CG-R-42`) and the §7 table (extract, schema, invocation).

### 1. R-1

**Before**

```
# Blind re-derivation brief — consequential-property categories for a command slice
```

**After**

```
# Brief — consequential-property categories for a command slice
```

### 2. R-2/R-3/R-6 (+S-1 consistency)

**Before**

```
**Read this file first. It is the whole of your instruction set.** You are performing the
re-derivation ruled at `CG-R-35`. You derive a category list by a stated method and stop. You
are not told, and must not try to learn, what any other session derived, what act instance is
under test, or what determinations it carries. If anything you are given or find seems to tell
you, stop and report it rather than reading on.
```

**After**

```
**Read this file first. It is your instruction set; where the invocation and this brief
differ, this brief wins.** You are producing a category list by a stated method and stopping.
Work from this bundle only; it is complete. If anything you are given or find goes beyond it,
stop and report it rather than reading on.
```

### 3. R-4/R-5/R-6

**Before**

```
**You propose; Emil ratifies. Produce one file and stop.** Commit identity, if you commit at
all, is `Claude <noreply@anthropic.com>`. If this bundle is all you were given, work from it
alone; if you have repository access, use nothing outside this directory.
```

**After**

```
**You propose; the principal who issued this brief ratifies. Produce one file and stop.**
```

### 4. R-7

**Before**

```
Your output is a single markdown file, `rederived-category-list.md`, containing:
```

**After**

```
Your output is a single markdown file, `category-list.md`, containing:
```

### 5. R-8

**Before**

```
Nothing else. No experiment design, no measure, no discussion of what the list is for beyond
what §2 says.
```

**After**

```
Nothing else. No discussion of what the list is for beyond what §2 says.
```

### 6. SC-3 (§3 reference; schema dropped under CG-R-42)

**Before**

```
declarations, provenance — whose record shape is `determination.schema.json`, enclosed.
```

**After**

```
declarations, provenance — recorded in a typed record whose field vocabulary is listed at
§4.3.
```

### 7. SC-3 (§4.2 corroboration paragraph; schema dropped under CG-R-42)

**Before**

```
**The schema is consulted as enforcement only.** Where it requires a field, that marks a
decision point the binding's authors judged consequential — corroboration for a category, never
its source. Do not derive categories from schema fields.
```

**After**

```
**The record vocabulary is not a source.** §4.3 lists the binding's record fields so that names
avoid them. Do not derive categories from record fields.
```

### 8. R-10

**Before**

```
  A category may be a *kind* of decision point that an instance exhibits more than once; that
  is acceptable and is handled after your work, not by you.
```

**After**

```
  A category may be a *kind* of decision point that a given act exhibits more than once; that
  is acceptable — do not split a kind into instances.
```

### 9. R-11

**Before**

```
- Do not look for, ask about, or reason from any act instance, event model, example
  determination, or other session's list. The enclosed schema's one example name is not an
  instance under test and tells you nothing.
```

**After**

```
- Do not reason from any particular act, event model or example determination; the list is
  for the act type.
```

### 10. R-6 (§6 repository line)

**Before**

```
- Do not read anything outside this directory. The bundle is complete.
```

**After**

```
- Do not read anything outside this bundle. It is complete.
```

### 11. R-12

**Before**

```
- Do not design the experiment, the measure, thresholds, or a rubric.
```

**After**

```
- Do not produce anything beyond §1's four items.
```

### 12. §7 enclosed table (extract, schema dropped, invocation added)

**Before**

```
| `supersession-foundation-construct-list.md` | S-1 and S-2, the superseding state |
| `resolution-condition.md` | C-1, C-2, C-3 |
| `boundary-declarations.md` | B-1, B-2 |
| `determination.schema.json` | the binding's record shape, for §4.2's corroboration and §4.3's naming rule |
| `MANIFEST.md` | sha256 of every file above — check them before starting |
```

**After**

```
| `supersession-extract.md` | S-1 and S-2, the superseding state — an extract of the supersession record's construct content, with its provenance line |
| `resolution-condition.md` | C-1, C-2, C-3 |
| `boundary-declarations.md` | B-1, B-2 |
| `INVOCATION.md` | the invocation you were given, filed beside this brief so the two can be checked against each other |
| `MANIFEST.md` | sha256 of every file above — check them before starting |
```

### 13. §4.2 table row wording (extract)

**Before**

```
**original** state (`foundation.md`) together with the **supersession record** that retired
two of its positions (`supersession-foundation-construct-list.md`). Use both: where the
```

**After**

```
**original** state (`foundation.md`) together with an **extract of the supersession record**
that retired two of its positions (`supersession-extract.md`). Use both: where the
```

**One substitution not in the audit, S-1.** The brief's opening sentence said it was *the whole
of your instruction set*; with `INVOCATION.md` filed beside it that was no longer true, and the
invocation itself says the brief wins on conflict. The replacement states that rule from the
brief's side. Made for consistency under step B.5; flagged here for ratification with the rest.

## 3. The supersession record: extracted, not substituted (`CG-R-41`)

`supersession-foundation-construct-list.md` (sha256 `0c2c17cce8e9abe01b7a1dbc27a5e8148ce0bb31cfcacc9436e01a215940b700`,
75 lines) is removed from the bundle and replaced by `supersession-extract.md`: the S-1 and S-2
sections' retired position, superseding position, basis and consequence — source lines 11–33 and
38–70 — verbatim, under a provenance line naming the source, its hash and the ranges. Not
extracted: the header and status lines (1–9, which held SS-1 and SS-2), the two *Open*
subsections (34–37 and 71–75, which held SS-3), and the rules between sections. A script
verified every extracted line byte-identical to the source. SS-1, SS-2 and SS-3 are gone
without a word altered.

## 4. The schema: dropped (`CG-R-42`, preference 1)

**The grid does not cite the schema.** Axis B of the grid names the foundation (both states),
the resolution condition and the boundary declarations; the schema's only roles in the brief
were optional corroboration ("never its source") and the naming rule's vocabulary, which the
brief enumerates in full at §4.3. No row of the proposed list cites it as a cell. So the file
(`determination.schema.json`, sha256 `4df4db09cf11d9a0cc02b4fee762fb9b71c3194dd1cb59691ccb6cba52fc67c6`)
is removed, and the two references in the brief are reworded (substitutions 6 and 7 above).

**This is a method-adjacent change, reported under the task's rule 3 rather than refused.**
What the receiving session loses is a corroboration source it was told not to derive from.
What it keeps is everything the grid consists of. The reconciliation reads rows against the
grid, and the grid is unchanged. SC-1, SC-2, SC-3 and SC-4 are gone with the file.

## 5. Hits not substituted, with the reason

| Hit | Where | Why it stays |
|---|---|---|
| R-9 | brief §2 | the foundation's own concept of a category; removing it changes the question. Ratified leave |
| R-13 | brief §6, *any expectation* | protective instruction; residual inference is only that the list will be read. Ratified leave |
| R-14 | brief, *rejection register*, *invented*, *weakest point* | the method; must be given. Ratified leave |
| R-15 | brief §4.2, *S-1*, *S-2* | identifiers internal to the enclosed extract. Ratified leave |
| R-16 | brief §1, *the domain-state-change binding* | the act type cannot be stated without it. Ratified leave; its discoverability path (SC-3) is closed by dropping the schema, not by removing the name |
| M-3 | manifest date | harmless; updated to the filing date |
| F-1, F-2, F-3, F-4, F-5 | `foundation.md` | canon, handed over whole; `CG-R-41` forbids modification and `CG-R-43` accepts the residual |
| RC-1, RC-2, RC-3, RC-4 | `resolution-condition.md` | same |
| BD-1, BD-2, BD-3 | `boundary-declarations.md` | same |
| — | `INVOCATION.md` line 33, *by inference about intent* | the word in its ordinary sense; the invocation is filed as arrived and unscrubbed (`CG-R-44`); leaks nothing about any measure in context |

## 6. Residual inference after the scrub (`CG-R-43`)

From the three untouched canon copies a reader can still infer that the framework attaches
falsifiers to claims, and that a pre-registration tests a closure claim (`foundation.md` §5.1,
`resolution-condition.md` line 3, `boundary-declarations.md` line 79). **Accepted, recorded, not
relied upon.** It mis-points at the layer claim, and that is not protection: a session that
infers some falsification programme may still reason about what makes a defensible list rather
than a derived one. Carried to the reconciliation as a stated limit on the re-derivation's
independence, beside `CG-R-39`'s framing residual.

## 7. The invocation (`CG-R-44`)

Filed byte-identical as `INVOCATION.md` (sha256 `424e53963e2fce9eb55e7b6b5858a3d3480ef3ae34f53b48c8fbdf1084af977d`,
35 lines), unscrubbed. Checked against the scrubbed brief:

- **Consistent:** the deliverable (list with cells, rejection register), the act type, work from
  the bundle only, the brief wins on conflict, the *about anything* test (the brief's condition
  1), exhaustive grid before pruning (the brief's *work the grid cell by cell*).
- **One minor difference, not fixed:** the invocation says the rejection register comes
  *alongside* the list; the brief says one file containing both. The brief wins by the
  invocation's own rule; a session producing two files has not erred materially.
- **Two things the invocation adds that the brief does not:** British spelling, and the three
  registers. Neither conflicts.
- **The pre-flight lines (1–7)** are in the bundled copy, as arrived. A reader sees an
  instruction addressed to the issuer about what to paste. Unremarkable; disclosed as filed.
- **Its no-clone, no-search and do-not-ask instructions are prose** and do not enforce. The
  enforcement is that the receiving session gets an archive and no repository access. If it
  asks what the task is for, that is reported in the reconciliation as an observation about
  what the bundle disclosed, and not answered.

## 8. Manifests

### Old (as filed 2026-09-04, under the old folder name)


```
# Manifest — blind re-derivation bundle

sha256 of every file in this directory as filed on 2026-09-04. The re-deriving session checks
these before starting and records what it checked; a bundle that does not match was not this one.

| File | sha256 | Lines |
|---|---|---|
| `README.md` | `224bf88670ad85ee7871f7b2c6c841171f8145c3c0bb1f2b750a44e78791fb44` | 152 |
| `foundation.md` | `3d9a52546fc35b05fffb2b0de2a97faa656b813e61c3c893ab2a093571219510` | 142 |
| `supersession-foundation-construct-list.md` | `0c2c17cce8e9abe01b7a1dbc27a5e8148ce0bb31cfcacc9436e01a215940b700` | 75 |
| `resolution-condition.md` | `802fc286cfcbb308b178066386bc1da6bceb4d006d33dbdc62fb2b40264b0055` | 58 |
| `boundary-declarations.md` | `0690cb5577d24e7b27077141c06f4572451797de406c41bfb8d6cdf05fcb131e` | 79 |
| `determination.schema.json` | `4df4db09cf11d9a0cc02b4fee762fb9b71c3194dd1cb59691ccb6cba52fc67c6` | 255 |
```

### New (as filed 2026-09-07)

```
# Manifest — command-slice categories bundle

sha256 of every file in this bundle as filed on 2026-09-07. The receiving session checks these
before starting and records what it checked; a bundle that does not match was not this one.

| File | sha256 | Lines |
|---|---|---|
| `README.md` | `41aa14480d5d65be31395f66f4606650149fddb3eeeedf1084eb93c16c2989b9` | 147 |
| `INVOCATION.md` | `424e53963e2fce9eb55e7b6b5858a3d3480ef3ae34f53b48c8fbdf1084af977d` | 35 |
| `foundation.md` | `3d9a52546fc35b05fffb2b0de2a97faa656b813e61c3c893ab2a093571219510` | 142 |
| `supersession-extract.md` | `ffd2b368ee5c4c5c867f97855f1d70edf0a1fab0091717ebdf58b1f5c8c68a7f` | 69 |
| `resolution-condition.md` | `802fc286cfcbb308b178066386bc1da6bceb4d006d33dbdc62fb2b40264b0055` | 58 |
| `boundary-declarations.md` | `0690cb5577d24e7b27077141c06f4572451797de406c41bfb8d6cdf05fcb131e` | 79 |
```


## 9. Bundle after Gate B

Seven files: `README.md`, `INVOCATION.md`, `foundation.md`, `supersession-extract.md`,
`resolution-condition.md`, `boundary-declarations.md`, `MANIFEST.md`. A bundle-wide search for
the audit's term classes after the scrub returns only the canon status lines listed in §5 and
the invocation's *inference*.

## 10. Weakest point

**The brief still reads as written by someone who knows what the list is for.** Every
substitution removed a term; none removed the shape of a document that carefully tells its
reader what not to do. A receiving session that notices how much care went into the
prohibitions can infer that the output matters to something, which is `CG-R-43`'s residual by
another route. That is not removable by scrubbing words, and it is recorded here rather than
claimed away.

---

**Hold.** Gate C is not entered. Awaiting ratification of the applied scrub, including S-1 and
the schema drop.
