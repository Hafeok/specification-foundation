# Rulings — session close

**Issued by Emil.** Recorded, not proposed. Each supersedes the corresponding open item in `holding-note-structure-and-languages.md`, which is amended by reference rather than rewritten.

---

**R-1 — The closure falsifier tests the mechanism claim, not the resolution condition.**

The claim under test is: *declaring the residual changes actor disposal of open decisions* — from escaped to surfaced. This is a claim about actors, and the resolution condition depends on it holding.

The pre-registration is amended to name this claim explicitly, so no downstream work promotes the result to a test of the resolution condition. The resolution condition requires its own falsifier — whether a specification with no dangling references produces fewer escapes at declared seams than one with them — which needs two conforming specifications and a boundary between them, and is therefore deferred.

**R-2 — Projection depth and composition are independent axes. Composition depth is called scale.**

*Layer* denotes projection depth only: actor-general → software → sector. Determinations added, never contradicted, forward only.

*Scale* denotes granularity of act composition within a projection: fine to coarse. Acts compose across scales.

The two are **independent coordinates, not a hierarchy**. Nothing about a position on one implies anything about the other. A sector-specific act at fine scale and an actor-general act at coarse scale are both well formed. The term registry entry must state this, because the natural reading of two ordered axes is that they nest.

Consequence for the falsifier: it operates at one scale within one projection, and says so. This is the substantive answer to D12.

**R-3 — Actor instances are declared per specification.**

Not a fourth vocabulary. Instances are deployment facts — this team, this model version, this service principal — and tick far faster than any ontology should. Encoding a fast-ticking axis is prohibited. Actor *kinds* come from Layer 1 and remain stable; instances are read at act time.

**R-4 — The boundary composition check is committed as a design constraint; the build is deferred.**

Where specification A declares an object terminal and specification B declares the same object external, the fact-vocabulary types must agree. This is mechanically stateable and targets the seam where divergence is predicted to concentrate.

It requires two conforming specifications to exist, so it is a commitment now and buildable later. Boundary declaration fields must not be designed in a way that forecloses it.

**R-5 — The engineering process remains in `specification-languages` for now.**

It plausibly warrants its own repository on the act-vocabulary test, but has no content yet, and a fourth repository costs validators, cross-repo pinning and supersession machinery immediately. Splitting later is cheap; four repositories with one populated is not.

**R-6 — `meta/sessions/` is declared native in the seed, with an upstream proposal filed and non-blocking.**

Session records are provenance for determinations and are actor-general. They belong at Layer 1 and should be inherited by every projection rather than borrowed sideways from a peer. Three sessions have now reached for an explanatory note rather than a declared travel; the local declaration supersedes when the upstream lands.

---

## Amended by these rulings

- `holding-note-structure-and-languages.md` §7, items 1–6 — closed
- `prereg-closure-falsifier.md` — R-1 and R-2 amendments pending, alongside the Gate 0 rulings
- `specification-language-foundation.md` — R-3 closes the actor-instance open item in supersession S-2
- `boundary-declarations.md` §B-3 — R-4 closes the composition-check open item
