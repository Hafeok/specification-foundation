# specification-foundation

The foundation of the specification language: what must be expressible for a specification's
completeness to be decidable, and — when it lands — the criterion by which someone else's language
can be checked against it.

**The name is locally scoped.** This is the foundation *of the specification language*, not of the
framework. The framework's root is
[`actor-indexed-determination`](https://github.com/Hafeok/actor-indexed-determination), which holds
actor, capability, accountability and the index. Everything here projects from that root; nothing
here is foundational to it, and a reader must not infer otherwise from the repository's name.

**Status of the contents.** Everything canonical in this repository is `[PROPOSED]` unless its own
record says otherwise. A well-organised repository reads as more settled than its contents are;
this sentence exists to counteract that. In particular, the resolution condition has **no
falsifier**: the closure pre-registration filed as evidence tests a different claim (per ruling
R-1), and nothing in this repository may present its result as a test of the resolution condition.

---

## Relations

This repository stands in three relations, and they have different rules and different failure
meanings. Confusing them is the most likely structural error, because *downstream* reads as
projection by default.

| Relation | Requirement | Violation |
|---|---|---|
| **projects from** | must not contradict upstream; derivation forward only | defect; requires a supersession record |
| **conforms to** | must satisfy the criterion, with evidence published | admissible outcome; the instance is non-conforming |
| **governed by** | must comply | defect; not a variant |

- **Projects from `actor-indexed-determination`.** Determinations are added, never contradicted,
  forward only. A projection cannot be a legitimate variant of its upstream while contradicting it.
- **Peer of [`decision-driven-design`](https://github.com/Hafeok/decision-driven-design).** Neither
  depends on the other; both project from the same root. Nothing is borrowed sideways. The accepted
  cost of the peer relation: two projections mean two term registries, and drift between them is a
  real risk (see `terms/`).
- **Conformed to by `specification-languages`** (not yet created), which also holds the engineering
  process for now, per ruling R-5.

**Conformance is not projection.** Read the violation column: rows 1 and 3 are defects — something
went wrong and must be repaired. Row 2 is an **admissible outcome**: a conforming instance
genuinely may fail the criterion, and the criterion exists in order to be able to return that
verdict. No validator in this repository may ever be pointed at the conformance relation; the
ordering validator governs projection only. The conformance relation has **no validator at all**,
and will not acquire one in the seeding session — a recorded gap, discovered here rather than when
`specification-languages` is created.

**Governance is orthogonal — a third axis.** Not up, not sideways. Nothing is projected from
[`canon-governance`](https://github.com/Hafeok/canon-governance); everything complies with it.
Whether this repository is governed is asserted from that repository's registry, never declared
here — this README deliberately carries no such declaration, and none should be added. At the
commit cited below, that registry asserts nothing operationally: the rules bind as rules, and no
instrument evaluates this repository.

---

## Canon boundary

**Canon:** the foundation (the construct list), the resolution condition, the boundary
declarations, and the conformance criterion when it lands. Filed under `canon/`.

**Not canon:** bindings, tooling, the falsifier material (evidence about canon, under
`evidence/`), and session records (`meta/sessions/`).

---

## Governance and contribution

The rules under which content here is produced, corrected and ratified are held in
**`Hafeok/canon-governance`**, read at commit
**`ad6d1b0b861306561364cc8d3a3e554cfb92d90c`**. They are **cited, not restated**: restating them
here would recreate the two-sources-one-rule state that repository exists to end. Per `CG-R-10`,
this citation records what was read and complied with, not what is current: it advances only by a
deliberate act that states what changed between the refs, and going stale is its correct
behaviour. Two of the ten
(`CG-rule-08`, `CG-rule-10`) are provisional in their own records — in force, not citable as
established.

What is stated here is only what is local to this repository:

- **Claim ID prefix: `SF-`.** A prefix names a programme, not a repository; the prefix choice is a
  local naming convention, and what binds it is identifier stability (`CG-rule-07`): never reused,
  never renumbered, unique across the programme.
- **Sessions propose; Emil ratifies.** Gates hold until an explicit ratification message. Rulings
  are issued only from the `CG-R-` series held in `canon-governance`; nothing here issues one.
- **Session records** live under `meta/sessions/`, per `CG-rule-06`, inherited — not native here,
  not borrowed from the peer.
- **The term registry** is at `terms/registry.md` and is the repository's vocabulary of record for
  its own structural terms.

## Validators *(commitment — not built, as at 2026-09-01)*

Two validators, adapted from `decision-driven-design`, are Gate 2 of the seeding session and do
not exist yet: an ordering validator governing the **projection** relation only, and a claim
validator for `SF-` records. When they exist, a green run will mean **well formed, not correct**:
every reference can resolve and every determination be wrong. Nothing that validates here will
ever measure the conformance relation, by design.

---

## Licence

- **`LICENSE`** — Creative Commons Attribution 4.0 International, for the canon and prose.
- **`LICENSE-code`** — Apache License 2.0, for scripts.
- **`CITATION.cff`** — the citation form, fixed at seed so downstream reuse cites consistently.

Attribution is to the founding author personally. The editorial role — which is what makes
ratification mean anything — is intended to transfer to a custodial body; the authorship
attribution is not affected by that transfer.
