# Outstanding dependencies

Dependencies this session cannot discharge itself, recorded per the Gate 2 acknowledgement as
entries rather than notes. Each names its owner and what it blocks. Removing an entry requires
the dependency actually landing, with a pointer to where.

| # | Dependency | Owner | Blocks | State |
|---|---|---|---|---|
| OD-1 | **Input 8** — the prior falsifier session's Gate 0 output, from `claude/closure-falsifier-prereg-w1mm7d`. Not reconstructed here, per the invocation. When it arrives it also anchors the pre-registration's hash (`145ed0a2…`, matching the delivered copy) | Emil | **Gate 3** — placement of the falsifier material, and the one available cross-check of the five unanchored inputs | open, 2026-09-01 |
| OD-2 | **The ruling-register append** — CG-R-10, -11, -12 (Gate 1) and CG-R-13, -14, -15 (Gate 2) are owed rows in `canon-governance`'s `registry/rulings.yaml`, the register the next ruling must append to (CG-R-8). Until the append, six rulings exist only as this repository's verbatim filings (`rulings-gate1.md`, `rulings-gate2.md`) — a downstream repository as sole record of programme rulings, which is exactly the state the register exists to end | Emil (acknowledged in the Gate 2 ratification: "the debt is on me") | nothing in this session mechanically; every future reader of the register, materially | open, 2026-09-01 |
