def procesar_recarga(monto: float, plan: str) -> dict:
    if monto < 1000 or monto > 50000:
        return {"monto": monto, "bonificacion_pct": 0.0, "estado": "rechazada"}

    return {"monto": monto, "bonificacion_pct": 0.0, "estado": "aceptada"}
