# Arrived inputs — notation falsifier pre-registration

Every input is filed with its sha256 before use, byte-identical to the delivered bundle
(`notation-falsifier-bundle.zip`, sha256 `64c70ab5b698da8b2f7d1e8bfb8ba124dcfbfa69177ecc8fd84b75b787979985`).
Hashes are of the filed copy. Line counts are measured, not stated.

**Filing an input is not placement.** These copies are session records — provenance for what
this session was given. Nothing here is canon, and filing here creates no claim ID and no
canonical location. The four artefacts this session produces are its own; the inputs are what it
worked from.

---

## 1. The instruction set and the design

| # | File | sha256 | Lines | Status |
|---|---|---|---|---|
| 1 | `prompt.md` (`session-notation-falsifier-prereg.md`; also attached separately to the invocation, byte-identical) | `1dd3cee41275a7c608d92628858136c60ec990267457da8d82a87c0269553f72` | 140 | the instruction set; filed in the arrival commit |
| 2 | `inputs/prereg-notation-inference-load.md` (also attached separately, byte-identical) | `9d29b2fdaa3c740d8975e86910fd865fd674d03d4862f6ed20df66b83c221a34` | 125 | `[PROPOSED]` by its own header; **the design this session works from.** Matches the hash the invocation names (`9d29b2fd…`) |
| 3 | `inputs/prereg-residual-declaration-mechanism.md` | `36c5b767e34ed73790a7666f268c9165711dc8b047a3e3933b0435b600001d40` | 119 | `[PROPOSED]` by its own header; the **layer** pre-registration, included for contrast, **not work to do**. Matches the hash the invocation names (`36c5b767…`). Cites two rulings, `CG-R-17` and `CG-R-18`, that do not exist in the register at the ref read — see Gate 0 report, I-1 |

## 2. The binding under test

`inputs/domain-state-change-binding/`, sixteen files. The schema is what arm R will be written
against; the examples, tools and manifest are context.

| File | sha256 | Lines |
|---|---|---|
| `README.md` | `86079e9c64f4f40a77259d1c9b200e9cb79395d537217030f1cc6d1879ac63ae` | 117 |
| `schema/determination.schema.json` | `4df4db09cf11d9a0cc02b4fee762fb9b71c3194dd1cb59691ccb6cba52fc67c6` | 255 |
| `conformance/manifest.yaml` | `4bc78fb6e751735c50678dd8de00f074551867bc16e7ab55df3952af868b315a` | 165 |
| `examples/ordering.eventmodel.yaml` | `06d32bfa002ee0d69a22a15c09b767c80d085908bfd374936095c506c8bc87bb` | 74 |
| `examples/place-order.determinations.yaml` | `81ca01cbbdf0e7cd8dcac869467ba7a082cbf7deafbaee0bca333e7a490156dc` | 246 |
| `examples/fulfilment.eventmodel.yaml` | `f01036d2ffe3bca6e860c3d091e06cbbc44e781153d413681f15f61b14fc1216` | 27 |
| `examples/fulfilment.determinations.yaml` | `e57e51f2f2b3db9aca36f10fad81c032d0dea6eebbf986933df96c934eb20081` | 69 |
| `examples/broken.eventmodel.yaml` | `8acd9d7728cbfc5b0b50d674a2bdce5f51e9816ad384db74afd2447b5443a1ad` | 50 |
| `examples/seam-defect/fulfilment.eventmodel.yaml` | `ab9f2245b96c045688867f1169e583f2ec250a0784549220b948199861c0d209` | 30 |
| `examples/seam-defect/fulfilment.determinations.yaml` | `5b5255ca270a75e11537d09c0d6b462d47d2f32bdecd93b377e560f5841f6c41` | 76 |
| `tools/run_all.sh` | `8ea152050f55a081f2c3039edb6760858de7ebdabdf5e021c58585b8e9c8ef9f` | 24 |
| `tools/validate.py` | `829b37163797ae342488c2b0b18ccccee401254233c743f08dbec0cfef4563ef` | 29 |
| `tools/prove_prohibitions.py` | `22e59b0596b592110971fb2cc373637b205a606c338079b01a2131f9f59bef11` | 55 |
| `tools/check_resolution.py` | `47264f487c48e187b27bd74ca744afcf37bf8bd843e14112488a23f3e8e7254e` | 157 |
| `tools/check_composition.py` | `3726c9e3efdcd5e5ee634e752447d5207f14eb47e158df4c97f45bf8e441b376` | 166 |
| `tools/check_conformance.py` | `41d74d5a8457a2e4ce3da3d602ababdc7e86f1946b580088ea33143fcd4d9327` | 164 |

**The binding's checks were run, not taken on the README's word.** Outcome and two defects in
the runner are in the Gate 0 report, §3.

## 3. Verification against independent copies

Nothing in this bundle has an independent copy reachable from this session. The binding's schema
`$id` points at `Hafeok/specification-languages`, which this repository's README records as not
yet created, and nothing in `specification-foundation` or `canon-governance` carries any of these
files. The hashes are on the record so that a later cross-check — when the binding is filed at
its home, or when the pre-registration is committed for execution — can establish what this
session cannot: that these are the states the executing session works from.

---

## Addendum, 2026-09-03 — the Gate 0 rulings arrived

Appended, not rewritten (`CG-rule-02`).

| File | sha256 | Lines | Status |
|---|---|---|---|
| `inputs/rulings-cg-r-20-28.md` | `dfd5b58f8bc6091b5aebfd9aba42ca2bd33278e8d238c85a6bbc13be818900fc` | 105 | **rulings, issued** — `CG-R-20` … `CG-R-28`, by Emil, ratifying Gate 0. Filed byte-identical; quoted with consequences in `rulings-gate0.md`. Not yet rows in the `canon-governance` register, by the issuer's own statement |

## Addendum, 2026-09-03 — the Gate 1 rulings arrived

| File | sha256 | Lines | Status |
|---|---|---|---|
| `inputs/rulings-cg-r-29-34.md` | `d86e1294b6c99f277e5fb4c12fab1dded722c48e91d11efc7c2076005a197d5c` | 74 | **rulings, issued** — `CG-R-29` … `CG-R-34`, by Emil, ratifying Gate 1 as provisional. Filed byte-identical; quoted with consequences in `rulings-gate1.md`. Not yet register rows |

## Addendum, 2026-09-04 — the Gate 2 rulings arrived

| File | sha256 | Lines | Status |
|---|---|---|---|
| `inputs/rulings-cg-r-35-38.md` | `d6b8f4e1aa1b8cbaab210da9db173a22099eddc94df7e67033654c5ed7168b4f` | 64 | **rulings, issued** — `CG-R-35` … `CG-R-38`, by Emil, 2026-09-03, holding Gate 2 pending blind re-derivation. Filed byte-identical; quoted with consequences in `rulings-gate2.md`. Not yet register rows |

## Addendum, 2026-09-04 — rulings on the re-derivation bundle arrived

| File | sha256 | Lines | Status |
|---|---|---|---|
| `inputs/rulings-cg-r-39-40.md` | `e85c32509831353a9d06e10956c414c1b957bc59abca497dda408a1b08ddfa0d` | 47 | **rulings, issued** — `CG-R-39`, `CG-R-40`, by Emil, 2026-09-03, accepting the bundle and the reconciliation rule. Filed byte-identical; quoted with consequences in `rulings-rederivation.md`. Not yet register rows |
