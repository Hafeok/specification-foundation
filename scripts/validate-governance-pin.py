#!/usr/bin/env python3
"""validate-governance-pin.py — assert the README's canon-governance pin
matches the recorded value.

Written at Gate 2 of the seeding session, on the Gate 1 caution: the pinned
citation lives in the README, the document most likely to be edited casually,
and under CG-R-10 that pin is load-bearing — it records what was read and
complied with, and it advances only by a deliberate act. This check is the
mechanical defence for the one place staleness would be silently wrong.

NOT adapted from anywhere: this is new code, first written here. (Stated
because everything else in scripts/ is an adaptation and silence would imply
the same provenance.)

What it checks:
  1. meta/canon-governance-ref.yaml exists and carries repo + a 40-hex ref.
  2. README.md contains that exact ref at least once.
  3. Every 40-hex token in README.md is either that ref or listed in the pin
     file's `also_cited` allowlist — so a second, different hash cannot sit in
     the README unaccounted for.

What it cannot check: that the recorded ref is the one actually read and
complied with. The pin file is the value of record; changing it IS the
deliberate act CG-R-10 requires, and this check only ensures the README and
the record move together, never which of them is right.

Exit 0 = pin consistent; 1 = mismatch. Requires PyYAML.
"""

import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("PyYAML required: pip install pyyaml")

HEX40 = re.compile(r"\b[0-9a-f]{40}\b")


def main() -> int:
    pin_file = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("meta/canon-governance-ref.yaml")
    readme = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("README.md")

    if not pin_file.is_file():
        print(f"FAIL pin record does not exist: {pin_file}", file=sys.stderr)
        return 1
    if not readme.is_file():
        print(f"FAIL README does not exist: {readme}", file=sys.stderr)
        return 1

    spec = yaml.safe_load(pin_file.read_text(encoding="utf-8")) or {}
    ref = str(spec.get("ref", ""))
    repo = str(spec.get("repo", ""))
    also = {str(a) for a in (spec.get("also_cited") or [])}
    if not repo or not HEX40.fullmatch(ref):
        print(f"FAIL {pin_file}: repo missing or ref is not a 40-hex commit: {ref!r}",
              file=sys.stderr)
        return 1

    text = readme.read_text(encoding="utf-8")
    cited = HEX40.findall(text)
    errors = []
    if ref not in cited:
        errors.append(
            f"README does not cite the recorded ref {ref} — the pin record and the README "
            f"have moved apart. Under CG-R-10 they advance together, by a deliberate act."
        )
    for h in sorted(set(cited)):
        if h != ref and h not in also:
            errors.append(
                f"README carries an unaccounted 40-hex hash {h} — either it is a stale or "
                f"silently advanced governance pin (fix the citation), or it is a legitimate "
                f"second citation (add it to also_cited in {pin_file}, which is itself a "
                f"deliberate, reviewable act)."
            )

    if errors:
        for e in errors:
            print(f"FAIL {e}", file=sys.stderr)
        return 1
    print(
        f"governance pin: OK — README cites {repo}@{ref}; "
        f"{len(set(cited))} hash(es) in README, all accounted for"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
