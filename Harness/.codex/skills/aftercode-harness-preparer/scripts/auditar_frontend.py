#!/usr/bin/env python3
"""Comprueba integridad del perfil frontend instalado desde harness-base."""

import argparse
from pathlib import Path


STATIC_DOCS = {
    Path("docs/feature-list.md"),
    Path("docs/metrics.md"),
    Path("docs/specs.md"),
}


def expected_files(base: Path) -> dict[Path, Path]:
    expected: dict[Path, Path] = {}
    for layer in ("common", "frontend"):
        source = base / "scaffold" / layer
        if not source.is_dir():
            raise ValueError(f"Falta el perfil: {source}")
        for path in source.rglob("*"):
            if path.is_file():
                expected[path.relative_to(source)] = path

    validator = base / "scripts" / "validate.py"
    if not validator.is_file():
        raise ValueError(f"Falta el validador: {validator}")
    expected[Path("scripts/validate.py")] = validator
    return expected


def audit(base: Path, destination: Path) -> tuple[list[Path], list[Path]]:
    if not destination.is_dir():
        raise ValueError(f"No existe el frontend destino: {destination}")

    missing: list[Path] = []
    changed_static: list[Path] = []
    for relative, source in sorted(expected_files(base).items()):
        target = destination / relative
        if not target.is_file():
            missing.append(relative)
        elif relative.parts[0] == ".agents" or relative in STATIC_DOCS:
            if target.read_bytes() != source.read_bytes():
                changed_static.append(relative)
    return missing, changed_static


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", type=Path, required=True, help="Ruta local de harness-base")
    parser.add_argument("--destino", type=Path, required=True, help="Repositorio frontend preparado")
    args = parser.parse_args()

    try:
        missing, changed_static = audit(args.base.expanduser().resolve(), args.destino.expanduser().resolve())
    except ValueError as error:
        parser.error(str(error))

    for path in missing:
        print(f"FALTA: {path}")
    for path in changed_static:
        print(f"ESTÁTICO MODIFICADO: {path}")
    if missing or changed_static:
        return 1
    print("OK: perfil frontend completo y archivos estáticos idénticos a harness-base.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
