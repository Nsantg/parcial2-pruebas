MONTO_MINIMO = 1000
MONTO_MAXIMO = 50000


def procesar_recarga(monto: float, plan: str) -> dict:
    if monto < MONTO_MINIMO or monto > MONTO_MAXIMO:
        return {"monto": monto, "bonificacion_pct": 0.0, "estado": "rechazada"}

    bonificacion = 0.0
    if monto >= 10000:
        bonificacion = 10.0

    return {"monto": monto, "bonificacion_pct": bonificacion, "estado": "aceptada"}
