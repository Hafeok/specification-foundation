# Rulings — Gate A (leak audit)

**Issued by Emil, 2026-09-03, ratifying the audit.** Four rulings, `CG-R-41` … `CG-R-44`, filed
verbatim below the rule. Arrived as `rulings-cg-r-41-44.md`, sha256 `00402d71bf94218e1e74fbf7b0d87f95c90e203db00d1f631ab89f75c6de84a5`, 61 lines, with the
receiving session's invocation `invocation-category-derivation.md`, sha256 `424e53963e2fce9eb55e7b6b5858a3d3480ef3ae34f53b48c8fbdf1084af977d`, 35 lines;
both filed byte-identical under `inputs/`. The covering message is quoted at the end.

---

>
> ## CG-R-41 — Canon copies are extracted, never substituted
>
> SS-1 and SS-3 sit in a canon copy the derivation needs. The two options offered were substitute or withhold, and both are wrong for the same reason.
>
> **Substituting inside a canon copy produces a document that looks like canon and is not.** In a programme whose discipline is byte-identical filing and supersession-never-rewrites, a doctored canon text in circulation is a worse artefact than the leak it repairs. Withholding signals concealment and removes something the derivation needs.
>
> **Ruled: extract.** The bundle carries an **extract** of the supersession record, not a copy — the construct content the derivation requires, with a provenance line naming the source document, its sha256, and the section range extracted.
>
> This drops SS-1 and SS-3 without altering a word: both are purpose and open-item lines, which are metadata about why the record exists rather than construct content. If the derivation needs both construct-list states, the extract carries both.
>
> What the receiving session sees is that it was given an extract. That is ordinary and uninformative — being handed the relevant part of a document is unremarkable, and it discloses far less than either a modified text or a missing one.
>
> **This generalises.** No canon document is modified for a bundle, ever. Extract with provenance, or hand it over whole and accept the leak.
>
> ---
>
> ## CG-R-42 — SC-3: prefer dropping the schema; substitute only if the grid cites it
>
> **The visibility fact you asked for: the organisation is public.** Two of its repositories were confirmed publicly readable during the governance seed, and a third was fetched over the open web during this programme. Treat the pointer as reaching a public org, and the brief's do-not-read as a constraint held in prose, which does not enforce.
>
> **Ruled, in preference order:**
>
> 1. **If the grid does not cite the schema, drop it.** No substitution, no leak, no modified artefact. Check whether the derivation actually needs it before doing anything else — the categories are drawn from the constructs, and the schema may be redundant.
> 2. **If the grid cites it**, substitute the `$id` with a neutral URN, and add a header line in the bundled copy stating that it is a modified copy with a URL neutralised, carrying the original's sha256. Record both hashes in the scrub record.
>
> The header is not optional. A silently altered schema is the same defect as a doctored canon copy, one register down. "A URL was neutralised" is routine and discloses nothing worth having.
>
> ---
>
> ## CG-R-43 — The residual inference is accepted, recorded, and not relied upon
>
> The weakest point is correctly stated. With the ratified changes the receiving session can still infer that a falsification programme exists and that a pre-registration tests a closure claim.
>
> **Ruled: accepted as residual.** It is not removable without changing the source, and changing the source is refused under CG-R-41.
>
> Two things about it, both to be recorded rather than assumed:
>
> **It mis-points, and that is not protection.** The inference reaches the layer claim rather than this one, which is mildly favourable and must not be treated as a safeguard. A session that infers *some* falsification programme may still reason about what makes a defensible list rather than a derived one, and that is the fitting channel regardless of which claim it thinks it is serving.
>
> **It belongs in the reconciliation, not only in the scrub record.** A stated limit on the re-derivation's independence is an input to grading the list, and the reconciliation reads it alongside CG-R-39's framing residual.
>
> ---
>
> ## CG-R-44 — The invocation is supplied and is filed as arrived
>
> `invocation-category-derivation.md` is the arrived file for step B.5. It is filed into the bundle byte-identical with its sha256, as arrived, and is not scrubbed — it was written for this purpose and carries no design vocabulary.
>
> **Two notes for the scrub record.** Its prohibition on cloning and web search is prose and does not enforce; the enforcement is that the receiving session is given an archive and no repository access, per CG-R-39. And its instruction not to ask what the task is for is likewise prose, and the session may ask anyway — if it does, that is reported in the reconciliation as an observation about what the bundle disclosed, not answered.
>
> ---
>
> ## Carried
>
> - Gate B proceeds on these rulings. If any substitution would change the grid, the admission conditions, the naming rules or the output form, it is refused under the task's rule 3 and reported.
> - Register debt: CG-R-17 … CG-R-44. Mine.

---

## Covering message, verbatim

> SS-1 and SS-3 get a third option: extract, don't substitute. Modifying a canon copy produces
> a document that looks like canon and isn't — in a programme built on byte-identical filing
> and supersession-never-rewrites, a doctored canon text in circulation is worse than the leak
> it repairs. An extract carrying the source document's name, hash and section range drops both
> hits without altering a word, since both are purpose and open-item lines rather than
> construct content.
>
> The receiving session sees that it got an extract. Being handed the relevant part of a
> document is unremarkable and discloses far less than a modified text or a missing one.
>
> The visibility fact for SC-3: the organisation is public. Two repositories were confirmed
> publicly readable during the governance seed, and I fetched a third over the open web in this
> conversation. So the pointer does reach the design, and the brief's do-not-read is prose.
>
> Preference order: drop the schema if the grid doesn't cite it — check that first, since the
> categories come from the constructs and the schema may be redundant. Only substitute if it's
> actually needed, and then say in the file that it's a modified copy.
>
> The invocation is attached for step B.5. It's filed as arrived and not scrubbed.
>
> One thing in CG-R-43 worth holding onto: the residual inference mis-points at the layer claim
> rather than this one, and that is not protection. A session that infers some falsification
> programme may still reason about what makes a defensible list rather than a derived one — the
> fitting channel doesn't care which claim it thinks it's serving.

---

## Consequences applied at Gate B

| Ruling | What it settles | Applied as |
|---|---|---|
| `CG-R-41` | Canon copies are **extracted, never substituted**; an extract carries the source's name, sha256 and section range; generalises to every bundle | the supersession record is replaced in the bundle by an extract of its construct content (both supersessions' retired position, superseding position, basis and consequence), dropping SS-1 and SS-3 without altering a word |
| `CG-R-42` | The organisation is public; the `$id` reaches the design; **drop the schema if the grid does not cite it**, else neutralise the URL with a header | the grid (Axis A × Axis B) cites the four canon documents and not the schema; the schema's only roles were optional corroboration and the naming vocabulary, which the brief already enumerates. **Dropped.** The brief's two references to it are reworded; recorded in the scrub record as a method-adjacent change with the reasoning |
| `CG-R-43` | The residual inference — a falsification programme exists; a pre-registration tests a closure claim — is accepted, recorded, **not relied upon**; mis-pointing is not protection; it belongs in the reconciliation as a limit on independence | recorded in the scrub record and carried to the reconciliation beside `CG-R-39`'s framing residual |
| `CG-R-44` | The invocation is filed into the bundle byte-identical, unscrubbed; its no-clone, no-search and do-not-ask instructions are prose; a question about purpose, if asked, is reported in the reconciliation, not answered | filed as `INVOCATION.md`; its consistency with the scrubbed brief checked and recorded |
