# Rulings — blind re-derivation

**Issued by Emil, 2026-09-03, accepting the bundle and the reconciliation rule.** Two rulings,
`CG-R-39` and `CG-R-40`, filed verbatim below the rule. Arrived as `rulings-cg-r-39-40.md`,
sha256 `e85c32509831353a9d06e10956c414c1b957bc59abca497dda408a1b08ddfa0d`, 47 lines, filed byte-identical under `inputs/`. The covering message is quoted
at the end. Gate 2 remains held for the re-derivation itself.

---

>
> ## CG-R-39 — A subagent does not count
>
> **Ruled: no.** The re-derivation is a separate session, separate context, bundle only.
>
> The reason is the framework's own. A subagent would be blind **by instruction**, in a checkout where the set and the list exist, under this session's direction. That is a constraint held in prose, and the admission test the governance seed applied says plainly that a rule held in prose is not enforced. The whole content of CG-R-35 is independence from the author; a guarantee of independence that rests on the author's instruction is the thing it was ruled against.
>
> There is a second reason, weaker but real: a subagent inherits its framing from this session's prompt, and framing is the channel by which a list gets fitted without anyone intending it.
>
> **The honest middle, stated so it is not discovered later:** a subagent result would not be worthless — it would still exercise the grid. It could not be cited as independent, which is the only property it was wanted for. So it costs a session to get the thing and nothing to skip it.
>
> ---
>
> ## CG-R-40 — No numeric threshold. The overlap decides the list's provenance grade, not its ratification.
>
> The proposal is right that no threshold is principled, and offering two-thirds anyway would be an arbitrary ceiling of exactly the kind already refused for the boundary ratio.
>
> But the aggregate is the wrong place to look. The signal is not what fraction of rows reproduced; it is **why** any row failed to.
>
> **Ruled, in two parts.**
>
> **Per row, and this needs no threshold.** A proposed-only row is retained only if it is defended **on the grid alone**, without citing the determination set. A row that can only be defended by pointing at the set is set-fitted and is struck. One such row is a finding regardless of overlap; the reconciliation rule already forbids the citation, and this makes the consequence explicit.
>
> **In aggregate, the overlap sets the list's provenance grade.** Two grades, both usable, recorded on the list and carried into every citation of the result:
>
> | Grade | Condition |
> |---|---|
> | **derived** | every retained row is defended on the grid alone |
> | **authored** | some retained rows survive on author judgement the grid does not reach |
>
> An **authored** list is not disqualifying. It is a weaker provenance, and it changes what the experiment may claim: the frame is then an artefact of this author's reading of the act type, not of a reproducible method, and any downstream reuse of the method inherits that.
>
> This is the same shape as *extracted* versus *originated* in the governance seed and *provisional* versus in-force under CG-R-1. A thing may be in force and weakly warranted, provided the difference is visible.
>
> **What triggers revising the method section** is therefore not a percentage. It is a **derived** grade failing to be achievable — if the grid cannot defend the rows the author believes belong, the grid underdetermines the list, and that is a finding about the method reported before any list is ratified.
>
> ---
>
> ## Carried
>
> - CG-R-36's amendment to §10 correctly recorded rather than applied to the arrived pre-registration. Gate 5 carries it.
> - Register debt: CG-R-17 … CG-R-40. Mine.

---

## Covering message, verbatim

> On the subagent: no, and the reason is your own admission test. A subagent would be blind by
> instruction, which is a constraint held in prose — and prose does not enforce. That's the
> same rule that failed event modelling on PR-1. Independence guaranteed by the author's
> instruction is precisely what CG-R-35 was ruled against.
>
> The honest part: a subagent result wouldn't be worthless, it just couldn't be cited as
> independent, which is the only property it was wanted for. So it costs a session to get it
> and nothing to skip it.
>
> On the threshold: no number. Two-thirds would be an arbitrary ceiling of the same kind
> already refused for the boundary ratio, and the aggregate is the wrong place to look anyway.
>
> The per-row rule needs no threshold: a proposed-only row is retained only if defended on the
> grid alone. One row that can only be defended by pointing at the set is a finding regardless
> of overlap.
>
> The aggregate then sets the list's provenance grade rather than its ratification — derived if
> every retained row is defended on the grid alone, authored if some survive on judgement the
> grid doesn't reach. An authored list is usable, weakly warranted, and changes what the
> experiment may claim: the frame becomes an artefact of one author's reading rather than of a
> reproducible method.
>
> Same shape as extracted/originated and provisional/in-force. A thing can be in force and
> weakly warranted as long as the difference is visible.
>
> What would trigger revising the method section isn't a percentage — it's a derived grade
> being unachievable. If the grid can't defend rows you believe belong, the grid
> underdetermines the list, and that's a finding about the method worth more than a ratified
> list.

---

## Consequences carried forward by this session

| Ruling | What it settles | What this session does |
|---|---|---|
| `CG-R-39` | No subagent. The re-derivation is a separate session, separate context, bundle only. Blindness by instruction is a constraint held in prose, and prose does not enforce | Nothing is run here. The bundle stands as filed; its launch is Emil's |
| `CG-R-40` | No numeric threshold. **Per row:** a proposed-only row is retained only if defended on the grid alone; one row defensible only by the set is a finding regardless of overlap. **In aggregate:** the overlap sets the list's **provenance grade** — *derived* if every retained row is defended on the grid alone, *authored* if any survives on judgement the grid does not reach — recorded on the list and carried into every citation. The method section is revised only if a derived grade is unachievable | The offered threshold in `rederivation-reconciliation-rule.md` §4 is **refused**; the file is not rewritten — a note is appended to it recording the refusal and the grade rule. The reconciliation, when it runs, assigns the grade and states it |

**On the framing channel.** `CG-R-39`'s second reason — that a subagent inherits this session's
framing, and framing is how a list gets fitted without intent — applies to the brief as well.
The brief was written by this session and carries its framing of the act type in §3 and of the
grid in §4.2. That is unavoidable, since the grid is the thing being tested for whether it
carries the list; it is recorded here so the reconciliation reads the re-derivation's rows
against the grid and not against the brief's phrasing of it.
