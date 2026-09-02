#!/usr/bin/env python3
"""validate-core-order.py — SDP ordering + graph transclusion for canon/.

Adapted at Gate 2 of the seeding session from Hafeok/decision-driven-design
validate-core-order.py at commit d89ed55724c55f26a995b067907add2bcb580290.
Adaptations: sf: doc markers, canon/ as the document root, SF_UPSTREAM_DIR,
and the relation guard (E14) — see THE RELATION THIS VALIDATOR GOVERNS below.
The E/W codes are the source's; E14 is added here.

============================================================================
THE RELATION THIS VALIDATOR GOVERNS — read before pointing it at anything.

This validator governs PROJECTION, and only projection: the forward-only,
never-contradicted derivation of this repository from
Hafeok/actor-indexed-determination. Every check in it assumes that an upstream
object CANNOT legitimately be diverged from — E4's forward edge, E13's drifted
embed and W5's basis loss are all defects precisely because a projection may
not fail its upstream.

It must NEVER be applied to the CONFORMANCE relation (specification-languages
conforming to this foundation). A conforming instance may legitimately fail
the criterion — non-conformance is an admissible outcome, not a defect — so
every verdict this validator issues is wrong in that direction: it would
convert admissible outcomes into errors. "Downstream" reads as projection by
default, which is exactly why this notice sits here and why E14 refuses an
upstream.yaml declaring any relation other than projects-from. Conformance
has no validator, and this one does not become it by being pointed there.
============================================================================

Layer contract:
  canon/graph/  (YAML)  canonical claims and term definitions — source of truth
  canon docs    (md)    prose arguments; carry sf:contract blocks; EMBED
                        canonical objects in their one canonical home, REF them
                        everywhere else

Doc markers:
  <!-- sf:contract ... -->
  <!-- sf:embed id=term:closure -->
  ...exact canonical_md from the graph...
  <!-- /sf:embed -->
  <!-- sf:ref id=SF-core-01 -->                    (no content requirement)

Ordering errors E1–E5, transclusion errors E6–E11, upstream errors E12–E13 and
warnings W1–W7 as in the source. Added here:
  E14 canon/graph/upstream.yaml declares a relation other than projects-from

Usage: python3 validate-core-order.py [canon-dir]   (graph read from <canon-dir>/graph/)
Exit 1 on any error. Requires PyYAML.
"""

import hashlib
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

try:
    import yaml
except ImportError:
    print("PyYAML required: pip install pyyaml --break-system-packages", file=sys.stderr)
    sys.exit(1)

CONTRACT_RE = re.compile(r"<!--\s*sf:contract\s*(.*?)-->", re.DOTALL)
FIELD_RE = re.compile(r"^(requires|establishes|instances|status)\s*:\s*(.*)$")
EMBED_OPEN_RE = re.compile(r"<!--\s*sf:embed\s+id=([^\s>]+)\s*-->")
EMBED_CLOSE = "<!-- /sf:embed -->"
REF_RE = re.compile(r"<!--\s*sf:ref\s+id=([^\s>]+)\s*-->")


def term_key(term: str) -> str:
    return term.split("|")[0].strip().lower()


def term_pattern(term: str) -> re.Pattern:
    alts = [re.escape(a.strip()) for a in term.split("|") if a.strip()]
    alts = [a.replace(r"\-", r"[-\s]") for a in alts]
    return re.compile(r"\b(?:" + "|".join(alts) + r")(?:e?s)?\b", re.IGNORECASE)


def parse_contract(text: str):
    m = CONTRACT_RE.search(text)
    if not m:
        return None
    fields = {"requires": [], "establishes": [], "instances": [], "status": ""}
    for line in m.group(1).splitlines():
        fm = FIELD_RE.match(line.strip())
        if not fm:
            continue
        key, val = fm.group(1), fm.group(2).strip()
        if key == "status":
            fields["status"] = val
        else:
            fields[key] = [t.strip() for t in val.strip("[]").split(",") if t.strip()]
    return fields


def strip_markers(text: str) -> str:
    text = CONTRACT_RE.sub("", text)
    text = REF_RE.sub("", text)
    return text


def load_graph(canon: Path):
    """Return {id: obj} with obj = {canonical_md, home, kind, term?, aliases?}.

    Sources, in order:
      <canon>/graph/*.yaml      registries (terms:, claims: lists)
      <canon>/claims/*.yaml     one claim per file; a claim participates iff it
                                carries canonical_md
    """
    objects = {}
    cdir = canon / "claims"
    if cdir.is_dir():
        for cf in sorted(cdir.glob("*.yaml")):
            obj = yaml.safe_load(cf.read_text(encoding="utf-8")) or {}
            if not isinstance(obj, dict) or "canonical_md" not in obj:
                continue
            objects[obj.get("id", cf.stem)] = {
                "canonical_md": (obj.get("canonical_md") or "").strip(),
                "home": obj.get("canonical_home", ""),
                "kind": "claims",
                "term": "",
                "aliases": [],
                "file": f"claims/{cf.name}",
            }
    gdir = canon / "graph"
    if not gdir.is_dir():
        return objects
    for gf in sorted(gdir.glob("*.yaml")):
        if gf.name == "upstream.yaml":
            continue
        data = yaml.safe_load(gf.read_text(encoding="utf-8")) or {}
        for kind, key_home in (("terms", "established_by"), ("claims", "canonical_home")):
            for obj in data.get(kind, []) or []:
                oid = obj.get("id", "")
                objects[oid] = {
                    "canonical_md": (obj.get("canonical_md") or "").strip(),
                    "home": obj.get(key_home, ""),
                    "kind": kind,
                    "term": obj.get("term", ""),
                    "aliases": obj.get("aliases", []) or [],
                    "file": gf.name,
                }
    return objects


def find_embeds(text: str):
    """Yield (id, content, line, ok_closed)."""
    pos = 0
    while True:
        m = EMBED_OPEN_RE.search(text, pos)
        if not m:
            return
        line = text[: m.start()].count("\n") + 1
        end = text.find(EMBED_CLOSE, m.end())
        if end == -1:
            yield m.group(1), "", line, False
            return
        yield m.group(1), text[m.end():end].strip(), line, True
        pos = end + len(EMBED_CLOSE)


# ============================================================================
# Cross-repo upstream resolution (E12 / E13 / E14 / W5 / W6 / W7)
#
# specification-foundation PROJECTS FROM actor-indexed-determination.
# canon/graph/upstream.yaml pins every upstream id this repository depends on,
# at a version AND a status. Remote resolution is a SHALLOW CLONE of the pinned
# ref into a temp dir — never a live network fetch inside the checker.
#
# REUSE WARNING (E14, and the header notice). The pin machinery below is the
# part of this validator most tempting to point at specification-languages when
# it exists, because it looks like a generic cross-repository dependency
# checker. It is not: it encodes the projection rule that upstream cannot
# legitimately be diverged from. The conformance relation has the opposite
# shape — the conforming instance may fail — so upstream.yaml must declare
# relation: projects-from, and anything else refuses rather than validates.
# ============================================================================

REF_RE_ID = re.compile(r"<!--\s*sf:ref\s+id=([^\s>]+)\s*-->")


def load_upstream_graph(clone_dir: Path):
    """Index every upstream object by id: {id: {status, canonical_md, ...}}.

    E12/W5 need *every* claim id and its status, whether or not it carries
    canonical_md. Terms come from the graph registry; claims from
    core/claims/*.yaml (the upstream repository's layout).
    """
    core = clone_dir / "core"
    objs = {}
    cdir = core / "claims"
    if cdir.is_dir():
        for cf in sorted(cdir.glob("*.yaml")):
            d = yaml.safe_load(cf.read_text(encoding="utf-8")) or {}
            if not isinstance(d, dict) or "id" not in d:
                continue
            objs[d["id"]] = {
                "status": str(d.get("status", "")),
                "canonical_md": (d.get("canonical_md") or "").strip(),
                "statement": (d.get("statement") or "").strip(),
                "region": (d.get("region") or "").strip(),
            }
    gdir = core / "graph"
    if gdir.is_dir():
        for gf in sorted(gdir.glob("*.yaml")):
            data = yaml.safe_load(gf.read_text(encoding="utf-8")) or {}
            for entry in (data.get("terms", []) or []) + (data.get("claims", []) or []):
                if "id" in entry:
                    objs[entry["id"]] = {
                        "status": str(entry.get("status", "")),
                        "canonical_md": (entry.get("canonical_md") or "").strip(),
                        "statement": (entry.get("statement") or "").strip(),
                        "region": (entry.get("region") or "").strip(),
                    }
    return objs


def pinned_content_digest(obj: dict) -> str:
    """sha256 over the fields a pin is instrumented on: statement, region,
    canonical_md. Status is NOT hashed — W5 already instruments it, and folding
    it in here would make one class fire twice for the same movement. Fields
    are joined with a separator that cannot occur in YAML block scalars, so
    moving text between fields changes the digest."""
    parts = [obj.get("statement", ""), obj.get("region", ""), obj.get("canonical_md", "")]
    return "sha256:" + hashlib.sha256("\x00".join(parts).encode("utf-8")).hexdigest()


def resolve_upstream(upstream_yaml: Path, errors, warnings):
    """Shallow-clone the pinned ref and return (graph, pins). graph is None if
    unavailable or refused."""
    spec = yaml.safe_load(upstream_yaml.read_text(encoding="utf-8")) or {}
    up = spec.get("upstream", {})
    # E14: the relation guard. This file participates in projection checking
    # only; see the module header and the section comment above. A missing
    # relation field is refused too — projection must be declared, not assumed,
    # because "downstream reads as projection by default" is the error this
    # guard exists to stop.
    relation = up.get("relation", "")
    if relation != "projects-from":
        errors.append(
            f"E14 {upstream_yaml}: relation is {relation!r}, not 'projects-from' — this "
            f"validator governs projection only and refuses to evaluate any other relation. "
            f"The conformance relation has no validator, by recorded design."
        )
        return None, []
    repo, ref = up.get("repo", ""), up.get("ref", "")
    pins = up.get("pins", []) or []
    if not repo or not ref:
        errors.append(f"E12 {upstream_yaml}: upstream repo/ref not specified")
        return None, pins
    # allow a pre-cloned dir (CI cache / offline) via env, else shallow-clone
    pre = os.environ.get("SF_UPSTREAM_DIR")
    if pre and Path(pre).is_dir():
        return load_upstream_graph(Path(pre)), pins
    tmp = Path(tempfile.mkdtemp(prefix="sf-upstream-"))
    r = subprocess.run(
        ["git", "clone", "--depth", "1", "--branch", ref, repo, str(tmp)],
        capture_output=True, text=True,
    )
    if r.returncode != 0:
        errors.append(
            f"E12 upstream clone failed for {repo}@{ref} — cannot resolve pins "
            f"(set SF_UPSTREAM_DIR to a local checkout to check offline). "
            f"git: {r.stderr.strip().splitlines()[-1] if r.stderr.strip() else 'unknown'}"
        )
        return None, pins
    return load_upstream_graph(tmp), pins


def load_pinned_ids(canon: Path):
    """The pin ids from canon/graph/upstream.yaml, read locally (no clone).
    Pinned upstream ids satisfy requires/refs in local docs: upstream precedes
    every local doc in the reading order, so the cross-repo edge points
    backward by construction."""
    upstream_yaml = canon / "graph" / "upstream.yaml"
    if not upstream_yaml.is_file():
        return set()
    spec = yaml.safe_load(upstream_yaml.read_text(encoding="utf-8")) or {}
    return {p.get("id", "") for p in (spec.get("upstream", {}).get("pins", []) or [])}


def check_upstream(canon: Path, errors, warnings, local_ids=frozenset()):
    """Run E12/E13/E14/W5/W6/W7 over canon/graph/upstream.yaml against a
    shallow clone of the pinned ref. local_ids: ids in this repo's own graph —
    embeds/refs of those are checked by the local passes (E6–E9)."""
    upstream_yaml = canon / "graph" / "upstream.yaml"
    if not upstream_yaml.is_file():
        print("  upstream  no canon/graph/upstream.yaml — nothing pinned yet (0 pins)")
        return
    graph, pins = resolve_upstream(upstream_yaml, errors, warnings)
    if graph is None:
        return

    pinned = {}
    for pin in pins:
        oid = pin.get("id", "")
        pinned[oid] = pin.get("status_at_pin", "")
        # E12: pinned id must still exist upstream at ref
        if oid not in graph:
            errors.append(f"E12 pinned id '{oid}' no longer exists upstream at the pinned ref")
            continue
        # W5: basis loss — upstream status moved since the pin was set
        up_status = graph[oid].get("status", "")
        if up_status and pin.get("status_at_pin") and up_status != pin["status_at_pin"]:
            warnings.append(
                f"W5 basis loss: '{oid}' is '{up_status}' upstream but pinned at "
                f"'{pin['status_at_pin']}' — a determination basedOn it is escaped until "
                f"the pin is consciously advanced"
            )
        # W6: content movement — the case status cannot see
        pinned_digest = pin.get("content_hash", "")
        live_digest = pinned_content_digest(graph[oid])
        if not pinned_digest:
            warnings.append(
                f"W6 uninstrumented pin: '{oid}' carries no content_hash — its statement and "
                f"region can move at the pinned ref with nothing firing. Add "
                f"content_hash: {live_digest}"
            )
        elif pinned_digest != live_digest:
            warnings.append(
                f"W6 pinned content moved: '{oid}' is pinned at content_hash "
                f"{pinned_digest} but resolves to {live_digest} at the ref — the statement or "
                f"region moved while the status held. Read the change, then advance the pin "
                f"consciously (a governed decision, not a mechanical bump)"
            )

    # E13: any canon doc that EMBEDS a pinned id must match upstream
    # canonical_md byte-for-byte; any sf:ref to an unpinned/unknown id is a
    # dangling cross-repo reference. Scope: canon/ only — evidence/ and meta/
    # are not projection surfaces and are never scanned.
    for p in sorted(canon.rglob("*.md")):
        text = p.read_text(encoding="utf-8")
        for oid, content, line, closed in find_embeds(text):
            if oid in local_ids:
                continue  # local graph object — checked by the local passes
            if oid not in pinned:
                errors.append(f"E13 {p}:{line}: embeds unpinned upstream id '{oid}'")
                continue
            if oid not in graph:
                continue  # already E12'd
            if content != graph[oid].get("canonical_md", ""):
                errors.append(
                    f"E13 {p}:{line}: '{oid}' embed drifted from upstream "
                    f"canonical_md at the pinned ref — re-project from upstream, never edit here"
                )
        for m in REF_RE_ID.finditer(text):
            oid = m.group(1)
            if oid in local_ids:
                continue
            if oid not in pinned:
                line = text[: m.start()].count("\n") + 1
                warnings.append(
                    f"W5 {p}:{line}: sf:ref to '{oid}' is not pinned in "
                    f"canon/graph/upstream.yaml — add a pin or the reference is unversioned"
                )

    # W7: local ids that shadow the pinned upstream registry. Ranges over the
    # WHOLE upstream registry, never the pin list — a pin-scoped check misses
    # the unpinned collision it exists for.
    shadowed = 0
    gdir = canon / "graph"
    if gdir.is_dir():
        for gf in sorted(gdir.glob("*.yaml")):
            if gf.name == "upstream.yaml":
                continue
            data = yaml.safe_load(gf.read_text(encoding="utf-8")) or {}
            for entry in (data.get("terms", []) or []) + (data.get("claims", []) or []):
                oid = entry.get("id", "")
                if not oid or oid not in graph:
                    continue
                shadowed += 1
                governing = entry.get("shadows_upstream", "")
                if not governing:
                    warnings.append(
                        f"W7 undeclared shadow: '{oid}' is established locally "
                        f"({entry.get('established_by', 'unknown doc')}) and also exists in "
                        f"the upstream registry at the pinned ref, with no governing decision "
                        f"cited. Establishing an id that collides with pinned upstream "
                        f"requires an explicit decision — add shadows_upstream: "
                        f"<decision-id>, or rename"
                    )

    print(
        f"  upstream  {len(pins)} pins resolved against the pinned ref, "
        f"{sum(1 for w in warnings if w.startswith('W5'))} basis-loss, "
        f"{sum(1 for w in warnings if w.startswith('W6'))} content-drift, "
        f"{shadowed} shadowed id(s)"
    )


def main() -> int:
    canon = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("canon")
    if not canon.is_dir():
        # A mistyped path must not pass as an empty set.
        print(f"FAIL canon directory does not exist: {canon}", file=sys.stderr)
        return 1
    docs = sorted(canon.glob("[0-9][0-9]-*.md"))
    if not docs:
        # No numbered canon docs yet. Run the upstream checks only, and say so.
        errors, warnings = [], []
        check_upstream(canon, errors, warnings)
        for w in warnings:
            print(f"  warn  {w}")
        for e in errors:
            print(f"  FAIL  {e}")
        print(f"\nupstream-only mode (0 numbered canon docs): "
              f"{len(errors)} errors, {len(warnings)} warnings")
        if errors:
            print("canon: FAILED — pins do not resolve, embeds drifted, or a non-projection "
                  "relation was refused")
            return 1
        print("canon: OK — every pin resolves at the pinned ref; no drift")
        return 0

    graph = load_graph(canon)
    pinned_ids = load_pinned_ids(canon)
    errors, warnings = [], []
    contracts, established_by, order = {}, {}, {}
    embedded_ids = {}  # id -> doc name

    # ---- pass 1: contracts and term registry -------------------------------
    for i, p in enumerate(docs):
        order[p] = i
        c = parse_contract(p.read_text(encoding="utf-8"))
        if c is None:
            errors.append(f"E1 {p.name}: no sf:contract block")
            continue
        contracts[p] = c
        for raw in c["establishes"]:
            k = term_key(raw)
            if k in established_by:
                errors.append(
                    f"E2 term '{k}' established by both "
                    f"{established_by[k][1].name} and {p.name}"
                )
            else:
                established_by[k] = (i, p, raw)
            if graph:
                gid = f"term:{k}"
                if gid not in graph:
                    warnings.append(
                        f"W4 {p.name}: establishes '{k}' with no graph entry {gid} "
                        f"yet (migration gap)"
                    )
                elif graph[gid]["home"] != p.name:
                    errors.append(
                        f"E10 {p.name}: establishes '{k}' but graph says "
                        f"established_by {graph[gid]['home'] or '(unset)'}"
                    )
        both = {term_key(t) for t in c["requires"]} & {term_key(t) for t in c["establishes"]}
        for k in sorted(both):
            errors.append(f"E5 {p.name}: '{k}' in both requires and establishes")

    if graph:
        declared = set(established_by)
        for gid, obj in graph.items():
            if obj["kind"] == "terms" and gid.removeprefix("term:") not in declared:
                errors.append(
                    f"E10 graph {obj['file']}: {gid} has no establishing doc contract"
                )

    # ---- pass 2: ordering + embeds/refs per doc ----------------------------
    for p, c in contracts.items():
        i = order[p]
        raw_text = p.read_text(encoding="utf-8")
        body = strip_markers(raw_text)

        for raw in c["requires"] + c["instances"]:
            k = term_key(raw)
            if k not in established_by:
                if f"term:{k}" in pinned_ids:
                    # established upstream, pinned — a backward edge by construction
                    if not term_pattern(raw).search(body):
                        warnings.append(f"W2 {p.name}: requires '{k}' but never uses it")
                    continue
                errors.append(f"E3 {p.name}: requires '{k}', established nowhere")
                continue
            j, q, _ = established_by[k]
            if j > i:
                errors.append(
                    f"E4 {p.name}: forward edge — requires '{k}' "
                    f"established later, in {q.name}"
                )
            elif j == i:
                errors.append(f"E5 {p.name}: '{k}' required from itself")
            if not term_pattern(raw).search(body):
                warnings.append(f"W2 {p.name}: requires '{k}' but never uses it")

        for oid, content, line, closed in find_embeds(raw_text):
            if not closed:
                errors.append(f"E11 {p.name}:{line}: unclosed sf:embed ({oid})")
                continue
            if oid not in graph:
                errors.append(f"E9 {p.name}:{line}: embed of unknown id '{oid}'")
                continue
            if oid in embedded_ids:
                errors.append(
                    f"E8 {p.name}:{line}: '{oid}' already embedded in {embedded_ids[oid]}"
                )
                continue
            embedded_ids[oid] = p.name
            obj = graph[oid]
            if obj["home"] and obj["home"] != p.name:
                errors.append(
                    f"E7 {p.name}:{line}: '{oid}' embedded outside its "
                    f"canonical home {obj['home']}"
                )
            if content != obj["canonical_md"]:
                errors.append(
                    f"E6 {p.name}:{line}: '{oid}' drifted from graph — "
                    f"edit {obj['file']} and re-project, never the doc"
                )

        for m in REF_RE.finditer(raw_text):
            if m.group(1) not in graph and m.group(1) not in pinned_ids:
                line = raw_text[: m.start()].count("\n") + 1
                errors.append(f"E9 {p.name}:{line}: ref to unknown id '{m.group(1)}'")

    for gid, obj in graph.items():
        if gid not in embedded_ids and obj.get("canonical_md"):
            warnings.append(
                f"W3 graph object '{gid}' has a canonical_md but is embedded nowhere "
                f"(registry-only objects — no canonical_md — are exempt)"
            )

    # ---- pass 3: body linter for undeclared forward use --------------------
    for k, (j, q, raw) in sorted(established_by.items(), key=lambda kv: kv[1][0]):
        gid = f"term:{k}"
        alias_raw = raw
        if gid in graph and graph[gid]["aliases"]:
            alias_raw = "|".join([graph[gid].get("term") or k] + graph[gid]["aliases"])
        pat = term_pattern(alias_raw)
        for p, c in contracts.items():
            if order[p] >= j:
                continue
            declared = {term_key(t) for t in c["requires"] + c["establishes"] + c["instances"]}
            if k in declared:
                continue
            body = strip_markers(p.read_text(encoding="utf-8"))
            m = pat.search(body)
            if m:
                line = body[: m.start()].count("\n") + 1
                warnings.append(
                    f"W1 {p.name}:{line}: uses '{m.group(0)}' before {q.name} "
                    f"establishes it — forward pointer or escaped edge? "
                    f"(apply the deletion test)"
                )

    # ---- pass 4: cross-repo upstream resolution ----------------------------
    check_upstream(canon, errors, warnings, local_ids=set(graph))

    for w in warnings:
        print(f"  warn  {w}")
    for e in errors:
        print(f"  FAIL  {e}")
    print(
        f"\n{len(docs)} documents, {len(established_by)} terms, "
        f"{len(graph)} graph objects, {len(embedded_ids)} embedded, "
        f"{len(errors)} errors, {len(warnings)} warnings"
    )
    if errors:
        print("canon: FAILED — forward edges and drifted embeds are escaped seams")
        return 1
    print("canon: OK — edges point backward, embeds match the graph")
    return 0


if __name__ == "__main__":
    sys.exit(main())
