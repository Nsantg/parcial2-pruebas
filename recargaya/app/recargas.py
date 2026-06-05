MONTO_MINIMO = 1000
MONTO_MAXIMO = 50000

# (umbral, bonificacion_pct) — ordenados de mayor a menor
TABLA_BONIFICACIONES = [
    (10000, 10.0),
]


def _calcular_bonificacion_base(monto: float) -> float:
    for umbral, bonificacion in TABLA_BONIFICACIONES:
        if monto >= umbral:
            return bonificacion
    return 0.0


def procesar_recarga(monto: float, plan: str) -> dict:
    if monto < MONTO_MINIMO or monto > MONTO_MAXIMO:
        return {"monto": monto, "bonificacion_pct": 0.0, "estado": "rechazada"}

    bonificacion = _calcular_bonificacion_base(monto)

    return {"monto": monto, "bonificacion_pct": bonificacion, "estado": "aceptada"}
