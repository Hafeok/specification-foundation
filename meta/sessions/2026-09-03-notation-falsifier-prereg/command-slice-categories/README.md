# Brief — consequential-property categories for a command slice

**Read this file first. It is your instruction set; where the invocation and this brief
differ, this brief wins.** You are producing a category list by a stated method and stopping.
Work from this bundle only; it is complete. If anything you are given or find goes beyond it,
stop and report it rather than reading on.

**You propose; the principal who issued this brief ratifies. Produce one file and stop.**

---

## 1. The task

Produce the list of **consequential-property categories** for one act type: a **command slice**
in the domain-state-change binding, in the software projection, at act scale. The list is drawn
for the act type — any command slice, in any domain — never for an instance.

Your output is a single markdown file, `category-list.md`, containing:

1. the list, in the form fixed at §5;
2. a **rejection register** — every candidate the method produced that you did not admit, with
   the admission condition it failed and why;
3. any point at which you had to invent a category the grid did not produce, marked as
   invented at the point of invention;
4. the weakest point of your list, named.

Nothing else. No discussion of what the list is for beyond what §2 says.

## 2. What a category is

A **consequential-property category** is a decision point that performing an act of this type
entails: something an actor implementing the slice must resolve, explicitly or by default,
whose resolution has consequence for what the act does. A specification written in the binding
either settles such a point by a determination, or declares it unsettled. The list is the set of
such points for the act type.

## 3. The act type

The binding sits on an **event model**, which supplies the act vocabulary (slices, by type and
name) and the fact vocabulary (the types of things acts read and write). Slice types are
*command*, *read-model*, *automation* and *translation*. Position is relative to the act: each
slice declares which facts it reads and which it writes. The determination layer adds, at each
slice's address, determinations — extent, allocation, acceptance with coverage, boundary
declarations, provenance — recorded in a typed record whose field vocabulary is listed at
§4.3.

A **command slice** receives a command from a caller, reads the facts the event model declares
it reads, decides, writes the facts the model declares it writes, and reports an outcome to the
caller. That gives the stages of the grid below.

## 4. The method

### 4.1 Admission conditions — apply all four to every candidate

1. **Entailed by the act type.** An actor performing any command slice meets this decision
   point, whatever the domain. A point that arises only in one domain or one instance fails.
2. **Within a construct the foundation names.** A determination in the layer can settle it: it
   lies inside ground, position, allocation, acceptance, coverage, or a boundary declaration
   (the enclosed `foundation.md`, `resolution-condition.md`, `boundary-declarations.md`). A
   point the layer has no form for is out of the list, however consequential.
3. **Outside what the act vocabulary fixes.** The foundation §4: the language is *not a
   replacement for the act vocabulary's own artefacts*. Which act this is, and which facts it
   reads and writes by name, are the event model's and are not categories. What the act does
   with them is.
4. **Recognisable from output.** A reader who sees only an actor's output and your list can say
   whether the output addresses the point, without first reconstructing what the points should
   have been. Each category is therefore one question with a stated answer form.

### 4.2 The grid

**Axis A — stages of a command slice:** *receive* (the command arrives), *read* (the declared
ground is obtained), *decide*, *write* (the verdict is produced), *report* (the caller learns
the outcome). A sixth row, *act as a whole*, holds cross-cutting points.

**Axis B — the foundation's constructs, in both states.** The foundation is enclosed in its
**original** state (`foundation.md`) together with an **extract of the supersession record**
that retired two of its positions (`supersession-extract.md`). Use both: where the
original names a construct the supersession replaced, the cell is the same and the name
differs, and you say which state you used.

| Construct | Where |
|---|---|
| ground requirement | foundation §2.2 — retired by S-2 into position |
| position: read is ground, write is verdict | supersession S-2; resolution condition |
| determination addressed to the act | foundation §2.3 |
| allocation: pinned, checked, residual | foundation §2.5 |
| acceptance relation; operational closure | foundation §2.6 |
| coverage and residual | foundation §2.7 |
| C-1, C-2, C-3 | resolution condition |
| B-1 external ground; B-2 terminal verdict | boundary declarations |

A category is the intersection of a stage and a construct at which all four conditions hold.
Work the grid cell by cell; a cell may yield nothing, one category, or several.

**The record vocabulary is not a source.** §4.3 lists the binding's record fields so that names
avoid them. Do not derive categories from record fields.

### 4.3 Rules on the rows

- **One question per category.** Each row is one question with one recognisable answer form.
  A category may be a *kind* of decision point that a given act exhibits more than once; that
  is acceptable — do not split a kind into instances.
- **Names in plain words, avoiding the schema's vocabulary.** No category name may be a schema
  key or enum value: *address, act_type, act_instance, scale, statement, extent, axes, state,
  region, reason, allocation, class, settled_by, acceptance, predicate, closure, kind,
  runnable_by, terminates, tolerance, ranges_over, covers, does_not_cover, proxy, stands_in_for,
  known_divergence, positions, fact_type, role, boundary, source, consumer, read_provenance,
  tick_rate, consumption_observable, provenance, made_at, made_by, recorded, supersedes*, nor
  *bound-here, travels-to, does-not-travel, silent, pinned, checked, residual, external,
  terminal, internal, operational, logical-only, unestablished, asserted-none, build-time,
  act-time, static, slow, fast, unknown, human, machine, team, external-party*. Avoid also the
  words *external, terminal, residual, coverage, closure, provenance* in names.
- **Cite the cell.** Every row states its stage and its construct, with the section or clause.
- **Record what you reject.** Every candidate the grid produced and you did not admit goes in
  the rejection register with the failing condition. A list without a rejection register is
  incomplete.

## 5. Output form

For each stage, a table:

| Id | Name | Question | An answer looks like | Cell |
|---|---|---|---|---|

Ids `R-01`, `R-02`, … in order. Then the rejection register as a table: candidate, cell,
condition failed, why. Then invented categories, if any. Then the weakest point.

## 6. What you must not do

- Do not reason from any particular act, event model or example determination; the list is
  for the act type.
- Do not read anything outside this bundle. It is complete.
- Do not produce anything beyond §1's four items.
- Do not tune the list to be long, short, or to any expectation. The number of rows is an
  outcome of the method.

## 7. Enclosed

| File | Role |
|---|---|
| `README.md` | this brief |
| `foundation.md` | the foundation, original state |
| `supersession-extract.md` | S-1 and S-2, the superseding state — an extract of the supersession record's construct content, with its provenance line |
| `resolution-condition.md` | C-1, C-2, C-3 |
| `boundary-declarations.md` | B-1, B-2 |
| `INVOCATION.md` | the invocation you were given, filed beside this brief so the two can be checked against each other |
| `MANIFEST.md` | sha256 of every file above — check them before starting |
