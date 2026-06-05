MONTO_MINIMO = 1000
MONTO_MAXIMO = 50000

# (umbral, bonificacion_pct) — ordenados de mayor a menor, el primero que aplique gana
TABLA_BONIFICACIONES = [
    (30000, 25.0),
    (10000, 10.0),
]


def _monto_valido(monto: float) -> bool:
    return MONTO_MINIMO <= monto <= MONTO_MAXIMO


def _calcular_bonificacion_base(monto: float) -> float:
    return next(
        (bono for umbral, bono in TABLA_BONIFICACIONES if monto >= umbral),
        0.0,
    )


def procesar_recarga(monto: float, plan: str) -> dict:
    if not _monto_valido(monto):
        return {"monto": monto, "bonificacion_pct": 0.0, "estado": "rechazada"}

    bonificacion = _calcular_bonificacion_base(monto)

    return {"monto": monto, "bonificacion_pct": bonificacion, "estado": "aceptada"}
