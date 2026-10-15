#!/usr/bin/env python3
"""Calcula variaciones de cantidades comparables; no consulta servicios externos."""

import argparse
import json
import sys
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP, localcontext
from pathlib import Path


def numero(value):
    if value is None:
        return None
    if isinstance(value, bool) or not isinstance(value, (str, int, float, Decimal)):
        raise ValueError("Los valores deben ser números o null, sin separadores de miles.")
    try:
        result = Decimal(str(value))
    except InvalidOperation as exc:
        raise ValueError("Número inválido; usar punto decimal y omitir separadores de miles.") from exc
    if not result.is_finite() or result < 0:
        raise ValueError("Las cantidades deben ser finitas y no negativas.")
    return result


def comparar(fila):
    if not isinstance(fila, dict) or not isinstance(fila.get("indicador"), str) or not fila["indicador"].strip():
        raise ValueError("Cada fila debe tener un indicador de texto no vacío.")
    if type(fila.get("comparable")) is not bool:
        raise ValueError("Cada fila requiere comparable: true o false, decidido desde las fuentes.")
    if "actual" not in fila or "anterior" not in fila:
        raise ValueError("Cada fila requiere actual y anterior; usar null para datos ausentes.")
    actual, anterior = numero(fila["actual"]), numero(fila["anterior"])
    resultado = {
        "indicador": fila["indicador"],
        "actual": str(actual) if actual is not None else None,
        "anterior": str(anterior) if anterior is not None else None,
        "diferencia": None,
        "variacion_porcentual": None,
    }
    if actual is None or anterior is None:
        return {**resultado, "estado": "sin_datos"}
    if not fila["comparable"]:
        return {**resultado, "estado": "no_comparable"}
    with localcontext() as ctx:
        ctx.prec = max(50, len(actual.as_tuple().digits) + abs(actual.as_tuple().exponent)
                       + len(anterior.as_tuple().digits) + abs(anterior.as_tuple().exponent) + 10)
        diferencia = actual - anterior
        resultado["diferencia"] = str(diferencia)
        if anterior == 0:
            return {**resultado, "estado": "sin_base_porcentual"}
        porcentaje = (diferencia / anterior * 100).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        resultado["variacion_porcentual"] = format(abs(porcentaje) if porcentaje == 0 else porcentaje, ".2f")
    return {**resultado, "estado": "comparable"}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("archivo", nargs="?", help="Lista JSON; omitir para leer stdin.")
    args = parser.parse_args()
    try:
        content = Path(args.archivo).read_text(encoding="utf-8") if args.archivo else sys.stdin.read()
        filas = json.loads(content, parse_float=Decimal)
        if not isinstance(filas, list):
            raise ValueError("La entrada debe ser una lista JSON de indicadores.")
        resultado = [comparar(fila) for fila in filas]
    except (OSError, ValueError, InvalidOperation) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(resultado, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
