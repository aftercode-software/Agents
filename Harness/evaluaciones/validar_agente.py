#!/usr/bin/env python3
"""Validate the preparer skill mirror and its local references, read-only."""

from pathlib import Path
import re
import sys


def validate(owner: Path) -> list[str]:
    errors = []
    name = "aftercode-harness-preparer"
    primary = owner / "skills" / name
    mirror = owner / ".codex" / "skills" / name
    for path in (owner / "AGENTS.md", primary / "SKILL.md", mirror / "SKILL.md"):
        if not path.is_file():
            errors.append(f"Missing {path.relative_to(owner)}")
    if not primary.is_dir() or not mirror.is_dir():
        return errors

    original_files = {path.relative_to(primary) for path in primary.rglob("*") if path.is_file()}
    mirror_files = {path.relative_to(mirror) for path in mirror.rglob("*") if path.is_file()}
    for relative in sorted(original_files ^ mirror_files):
        errors.append(f"Missing mirror counterpart: {relative}")
    for relative in sorted(original_files & mirror_files):
        if (primary / relative).read_bytes() != (mirror / relative).read_bytes():
            errors.append(f"Mirror differs: {relative}")

    for tree in (primary, mirror):
        for document in tree.rglob("*.md"):
            content = document.read_text(encoding="utf-8")
            for link in re.findall(r"\[[^\]]*\]\(([^)\s]+)\)", content):
                if link.startswith("#") or re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", link):
                    continue
                target = link.split("#", 1)[0]
                if not (document.parent / target).exists():
                    errors.append(f"Broken link: {document.relative_to(owner)} -> {link}")
    return errors


if __name__ == "__main__":
    failures = validate(Path(__file__).resolve().parents[1])
    if failures:
        print("\n".join(failures), file=sys.stderr)
        sys.exit(1)
    print("OK: preparer skill, mirror and local references match.")
