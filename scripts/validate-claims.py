#!/usr/bin/env python3
"""Validate SF- claim files against claim format v1.

Adapted at Gate 2 of the seeding session from Hafeok/decision-driven-design
scripts/validate-claims.py at commit d89ed55724c55f26a995b067907add2bcb580290.
The adaptation is the SF- identifier space and this header; the checks, their
classes and their exemptions are the source's. The instrument does not move
(CG-rule-03's note): the source validator stays in its repository; this is an
adaptation for a different identifier space, not a relocation.

Usage:
    validate-claims.py canon/claims/                   # directory of per-claim YAML files
    validate-claims.py canon/decisions/ --decisions    # directory of decision files

Exit code 0 = valid; 1 = violations printed to stderr. An empty directory is
valid and reports its zero denominator; a missing directory is an error, so a
mistyped path cannot pass as an empty set.

Two classes of finding, and the difference is a ruling rather than a taste:

  error    the claim is invalid. Exit 1.
  warning  printed, exit unaffected.

CHECK_CLASS below is the whole of that policy. THE CLASSES ARE INHERITED, NOT
LOCALLY EARNED: in the source they were promoted or held on hit lists against a
corpus of 89 claims; this repository's claim corpus is empty, so no local hit
list exists. The first local claim that legitimately fails an inherited error
class is a ruling request against the class, not a formatting chore. Changing a
value here is a ruling and should arrive with the hit list that justifies it.
"""

import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("PyYAML required: pip install pyyaml")

SUPPORTED_FORMATS = {1}
STATUSES = {"projected", "reported", "established", "retired"}
LIVE_STATUSES = {"projected", "reported", "established"}
KINDS = {"formal", "empirical", "conceptual", "normative"}
TEST_KINDS = {"conceptual", "normative"}
RETIRED_FROM = {"established", "reported", "projected", "unrecoverable"}
# The SF- space: a programme prefix (ruling Q; CG-rule-07 binds stability, not
# the prefix). Identifiers are never reused and never renumbered.
ID_RE = re.compile(r"^SF-[a-z]+-\d{2}$")

# Parentheticals are stripped before limb counting; in the source corpus every
# mutual-information term -- I(V;X) -- was a false positive for the
# clause-joining detector. Kept: the failure mode is notation-general.
PARENTHETICAL = re.compile(r"\([^()]*\)")

# The class of each non-mandatory check. See the module docstring: inherited
# from the source at the commit above, no local hit lists exist yet.
CHECK_CLASS = {
    # Falsifier presence at every live status (CG-rule-03's extracted wording;
    # error in the source with a hit list of 0 of 89).
    "falsifier-presence": "error",
    # Every live claim carries a falsifier, `test` no substitute. Warning in the
    # source (7 of 89, all conceptual/normative, all carrying a test).
    "falsifier-strict": "warning",
    # One proposition per claim. Not mechanically decidable -- see
    # single_limb(). A drafting prompt, NEVER an error: in the source it fires
    # on sound claims.
    "single-limb": "warning",
    # A retired claim records the maturity it held; `unrecoverable` is always
    # available, so the rule can never be unsatisfiable.
    "retired-from": "error",
}

errors = []
warnings = []


def err(where, msg):
    errors.append(f"  {where}: {msg}")


def flag(check, where, msg):
    """Record a finding at the class CHECK_CLASS gives it."""
    line = f"  {where}: [{check}] {msg}"
    (errors if CHECK_CLASS[check] == "error" else warnings).append(line)


def single_limb(statement):
    """One-proposition rule's proxy: clause-joining punctuation outside
    mathematical notation.

    There is no mechanical test for "one proposition", and the gap between that
    and what is counted here is the reason this check cannot be an error. It
    reports candidates; a human rules.

    RETIRED CLAIMS ARE EXEMPT, and the reason is here rather than at the call
    site because the next person to widen a rule will read it here. A retired
    claim's `statement` is a retirement record, not a proposition -- canon
    rewrites it as RETIRED -- "<the dead claim>". An epitaph may quote verbatim
    the compound statement that killed the claim, so running the rule over it
    flags the record of the defect as though it were the defect.
    """
    s = " ".join(str(statement).split())
    prev = None
    while prev != s:
        prev, s = s, PARENTHETICAL.sub(" ", s)
    s = re.sub(r"^RETIRED — ", "", s)
    return s.count(";")


def check_claim(c, where, default_format=None):
    fmt = c.get("format", default_format)
    if fmt not in SUPPORTED_FORMATS:
        err(where, f"format missing or unsupported: {fmt!r}")
        return
    cid = c.get("id", "<no id>")
    where = cid
    if not ID_RE.match(cid):
        err(where, f"id does not match SF-<area>-<nn>: {cid!r}")
    if c.get("kind") not in KINDS:
        err(where, f"kind missing or illegal: {c.get('kind')!r}")
    status = c.get("status")
    if status not in STATUSES:
        err(where, f"status missing or illegal: {status!r}")
        return
    if not c.get("statement"):
        err(where, "statement missing")
    if not c.get("region"):
        err(where, "region missing ('everywhere' must be written to be claimed)")
    if not c.get("changed"):
        err(where, "changed missing (staleness pin)")

    evidence = c.get("evidence") or []
    # Status entry conditions
    if status in ("reported", "established") and not evidence:
        err(where, f"status '{status}' requires at least one evidence entry")
    if status == "established" and not any(
        e.get("kind") in ("derivation",) for e in evidence if isinstance(e, dict)
    ):
        err(where, "status 'established' requires a derivation evidence entry "
                   "(credits filled if the theorem is borrowed)")
    if status == "retired" and not (c.get("supersedes") or c.get("notes")):
        err(where, "retired claim requires supersedes or a notes entry naming what killed it")

    # Falsifier presence at every live status. A definition's falsifier is its
    # `test`, for the kinds the format gives it to and no others.
    if status in LIVE_STATUSES:
        if not c.get("falsifier") and not (c.get("kind") in TEST_KINDS and c.get("test")):
            flag("falsifier-presence", where,
                 f"status '{status}' requires falsifier"
                 + (" (or test, for conceptual/normative kinds)"
                    if c.get("kind") in TEST_KINDS else ""))
        elif not c.get("falsifier"):
            flag("falsifier-strict", where,
                 f"{c.get('kind')} claim at '{status}' carries test and no falsifier; "
                 "every claim carries one, with no near-definitional exception")

    # One proposition per claim, as a drafting prompt. Never promote this to
    # error without an adjudication of its hit list: it fires on sound claims.
    # Retired claims are exempt -- see single_limb()'s docstring for why.
    limbs = single_limb(c.get("statement", "")) if status in LIVE_STATUSES else 0
    if limbs:
        flag("single-limb", where,
             f"statement joins ~{limbs + 1} limbs (one proposition per claim). "
             "Candidate for adjudication, not a verdict")

    # Retirement provenance. `unrecoverable` is a value and not a gap, so the
    # rule is always satisfiable and nothing here licenses inferring a status.
    rf = c.get("retired_from")
    if status == "retired" and not rf:
        flag("retired-from", where,
             "retired claim requires retired_from "
             f"({' | '.join(sorted(RETIRED_FROM))}); use 'unrecoverable' where the "
             "prior maturity cannot be established, and record the search in notes")
    if rf is not None:
        if status != "retired":
            flag("retired-from", where,
                 f"retired_from is legal only on a retired claim (status is '{status}')")
        if rf not in RETIRED_FROM:
            flag("retired-from", where, f"retired_from illegal: {rf!r}")
        if rf == "unrecoverable" and not c.get("notes"):
            flag("retired-from", where,
                 "retired_from 'unrecoverable' requires a notes entry recording what was "
                 "searched (that the notes do record it is not mechanically checkable)")


def check_decision(d, where):
    """Minimal decision checks: no escaped decisions (CG-rule-04's bite point)."""
    did = d.get("id", where)
    if not d.get("principal"):
        err(did, "decision has no accountable principal (escaped decision)")
    basis = d.get("basis") or d.get("basedOn") or []
    if not basis:
        err(did, "decision has no basedOn edges (escaped decision)")
    if not d.get("resolution"):
        err(did, "decision has no resolution")
    if not d.get("made"):
        err(did, "decision has no made timestamp/context")


def load(path):
    with open(path) as f:
        return yaml.safe_load(f)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    as_decisions = "--decisions" in sys.argv
    if not args:
        sys.exit(__doc__)
    target = Path(args[0])

    items, default_format = [], None
    if target.is_dir():
        # Non-record files (README.md and the like) are not claims; only *.yaml
        # participates. Zero yaml files is a valid empty set, reported with its
        # denominator so a green run shows what it ran over.
        for p in sorted(target.glob("*.yaml")):
            data = load(p)
            items.append((data, str(p)))
    elif not target.exists():
        # A mistyped path must not pass as an empty set.
        sys.exit(f"target does not exist: {target}")
    else:
        data = load(target)
        if isinstance(data, dict) and "claims" in data:
            default_format = data.get("format")
            items = [(c, target.name) for c in data["claims"]]
        elif isinstance(data, dict) and "decisions" in data:
            items = [(d, target.name) for d in data["decisions"]]
            as_decisions = True
        else:
            items = [(data, target.name)]

    ids = []
    for item, where in items:
        if as_decisions:
            check_decision(item, where)
        else:
            check_claim(item, where, default_format)
        if isinstance(item, dict) and item.get("id"):
            ids.append(item["id"])

    dupes = {i for i in ids if ids.count(i) > 1}
    if dupes:
        err("global", f"duplicate ids: {sorted(dupes)}")

    kind = "decisions" if as_decisions else "claims"
    if warnings:
        print(f"{len(warnings)} warning(s) across {len(items)} {kind} "
              "— reported, not fatal:", file=sys.stderr)
        print("\n".join(warnings), file=sys.stderr)
    if errors:
        print(f"INVALID — {len(errors)} violation(s) across {len(items)} {kind}:",
              file=sys.stderr)
        print("\n".join(errors), file=sys.stderr)
        sys.exit(1)
    tail = f", {len(warnings)} warning(s)" if warnings else ""
    print(f"valid: {len(items)} {kind}, ids unique, format rules satisfied{tail}")


if __name__ == "__main__":
    main()
