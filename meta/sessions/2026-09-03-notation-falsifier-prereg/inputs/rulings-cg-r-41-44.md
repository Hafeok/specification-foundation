# Rulings CG-R-41 … CG-R-44 — Gate A leak audit

**Issued by Emil, 2026-09-03.** The audit is ratified. The fourteen substitutions, the two deletions and the nineteen leave-and-report dispositions are accepted as proposed. `command-slice-categories/` is accepted.

---

## CG-R-41 — Canon copies are extracted, never substituted

SS-1 and SS-3 sit in a canon copy the derivation needs. The two options offered were substitute or withhold, and both are wrong for the same reason.

**Substituting inside a canon copy produces a document that looks like canon and is not.** In a programme whose discipline is byte-identical filing and supersession-never-rewrites, a doctored canon text in circulation is a worse artefact than the leak it repairs. Withholding signals concealment and removes something the derivation needs.

**Ruled: extract.** The bundle carries an **extract** of the supersession record, not a copy — the construct content the derivation requires, with a provenance line naming the source document, its sha256, and the section range extracted.

This drops SS-1 and SS-3 without altering a word: both are purpose and open-item lines, which are metadata about why the record exists rather than construct content. If the derivation needs both construct-list states, the extract carries both.

What the receiving session sees is that it was given an extract. That is ordinary and uninformative — being handed the relevant part of a document is unremarkable, and it discloses far less than either a modified text or a missing one.

**This generalises.** No canon document is modified for a bundle, ever. Extract with provenance, or hand it over whole and accept the leak.

---

## CG-R-42 — SC-3: prefer dropping the schema; substitute only if the grid cites it

**The visibility fact you asked for: the organisation is public.** Two of its repositories were confirmed publicly readable during the governance seed, and a third was fetched over the open web during this programme. Treat the pointer as reaching a public org, and the brief's do-not-read as a constraint held in prose, which does not enforce.

**Ruled, in preference order:**

1. **If the grid does not cite the schema, drop it.** No substitution, no leak, no modified artefact. Check whether the derivation actually needs it before doing anything else — the categories are drawn from the constructs, and the schema may be redundant.
2. **If the grid cites it**, substitute the `$id` with a neutral URN, and add a header line in the bundled copy stating that it is a modified copy with a URL neutralised, carrying the original's sha256. Record both hashes in the scrub record.

The header is not optional. A silently altered schema is the same defect as a doctored canon copy, one register down. "A URL was neutralised" is routine and discloses nothing worth having.

---

## CG-R-43 — The residual inference is accepted, recorded, and not relied upon

The weakest point is correctly stated. With the ratified changes the receiving session can still infer that a falsification programme exists and that a pre-registration tests a closure claim.

**Ruled: accepted as residual.** It is not removable without changing the source, and changing the source is refused under CG-R-41.

Two things about it, both to be recorded rather than assumed:

**It mis-points, and that is not protection.** The inference reaches the layer claim rather than this one, which is mildly favourable and must not be treated as a safeguard. A session that infers *some* falsification programme may still reason about what makes a defensible list rather than a derived one, and that is the fitting channel regardless of which claim it thinks it is serving.

**It belongs in the reconciliation, not only in the scrub record.** A stated limit on the re-derivation's independence is an input to grading the list, and the reconciliation reads it alongside CG-R-39's framing residual.

---

## CG-R-44 — The invocation is supplied and is filed as arrived

`invocation-category-derivation.md` is the arrived file for step B.5. It is filed into the bundle byte-identical with its sha256, as arrived, and is not scrubbed — it was written for this purpose and carries no design vocabulary.

**Two notes for the scrub record.** Its prohibition on cloning and web search is prose and does not enforce; the enforcement is that the receiving session is given an archive and no repository access, per CG-R-39. And its instruction not to ask what the task is for is likewise prose, and the session may ask anyway — if it does, that is reported in the reconciliation as an observation about what the bundle disclosed, not answered.

---

## Carried

- Gate B proceeds on these rulings. If any substitution would change the grid, the admission conditions, the naming rules or the output form, it is refused under the task's rule 3 and reported.
- Register debt: CG-R-17 … CG-R-44. Mine.
