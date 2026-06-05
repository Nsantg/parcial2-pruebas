MONTO_MINIMO = 1000
MONTO_MAXIMO = 50000


def procesar_recarga(monto: float, plan: str) -> dict:
    if monto < MONTO_MINIMO or monto > MONTO_MAXIMO:
        return {"monto": monto, "bonificacion_pct": 0.0, "estado": "rechazada"}

    return {"monto": monto, "bonificacion_pct": 0.0, "estado": "aceptada"}
