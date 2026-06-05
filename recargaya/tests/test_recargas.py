import pytest
from app.recargas import procesar_recarga


class TestValidacionMonto:
    def test_monto_menor_al_minimo_es_rechazado(self):
        resultado = procesar_recarga(monto=999, plan="normal")
        assert resultado["estado"] == "rechazada"

    def test_monto_igual_al_minimo_es_aceptado(self):
        resultado = procesar_recarga(monto=1000, plan="normal")
        assert resultado["estado"] == "aceptada"

    def test_monto_mayor_al_maximo_es_rechazado(self):
        resultado = procesar_recarga(monto=50001, plan="normal")
        assert resultado["estado"] == "rechazada"

    def test_monto_igual_al_maximo_es_aceptado(self):
        resultado = procesar_recarga(monto=50000, plan="normal")
        assert resultado["estado"] == "aceptada"

    def test_monto_cero_es_rechazado(self):
        resultado = procesar_recarga(monto=0, plan="normal")
        assert resultado["estado"] == "rechazada"

    def test_monto_negativo_es_rechazado(self):
        resultado = procesar_recarga(monto=-500, plan="normal")
        assert resultado["estado"] == "rechazada"
