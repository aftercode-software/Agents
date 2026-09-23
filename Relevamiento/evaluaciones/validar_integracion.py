#!/usr/bin/env python3
"""Check skill mirrors, shared contract and local reference links, read-only.

Run from any directory. This is structural validation, not a behavior test.
"""

from pathlib import Path
import re
import sys


def validate(root: Path) -> list[str]:
    errors = []
    skill_roots = []
    for owner, name in (
        ("Relevamiento", "relevamiento"),
        ("Presupuestos", "aftercode-presupuesto-integral"),
    ):
        canonical = root / owner / "skills" / name
        mirror = root / owner / ".codex" / "skills" / name
        skill_roots.extend((canonical, mirror))
        if not canonical.is_dir() or not mirror.is_dir():
            errors.append(f"Missing skill directory: {owner}/{name}")
            continue
        originals = {p.relative_to(canonical) for p in canonical.rglob("*") if p.is_file()}
        copies = {p.relative_to(mirror) for p in mirror.rglob("*") if p.is_file()}
        for path in sorted(originals ^ copies):
            errors.append(f"Missing counterpart: {owner}/{path}")
        for path in sorted(originals & copies):
            if (canonical / path).read_bytes() != (mirror / path).read_bytes():
                errors.append(f"Mirror differs: {owner}/{path}")

    contract = Path("references/traspaso-presupuestos.md")
    versions = []
    for skill in skill_roots:
        target = skill / contract
        if target.is_file():
            versions.append(target.read_bytes())
        else:
            errors.append(f"Missing contract: {target.relative_to(root)}")
        for document in skill.rglob("*.md"):
            source = document.read_text(encoding="utf-8")
            for link in re.findall(r"\[[^\]]*\]\(([^)\s]+)\)", source):
                if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", link) or link.startswith("#"):
                    continue
                local = link.split("#", 1)[0]
                if not (document.parent / local).exists():
                    errors.append(f"Broken link: {document.relative_to(root)} -> {link}")
    if versions and len(set(versions)) != 1:
        errors.append("Shared contract differs between skills")
    return errors


if __name__ == "__main__":
    failures = validate(Path(__file__).resolve().parents[2])
    if failures:
        print("\n".join(failures), file=sys.stderr)
        sys.exit(1)
    print("OK: both mirrors, four shared contracts and local Markdown links match.")
