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


class TestBonificacion10Pct:
    def test_monto_justo_antes_del_limite_no_tiene_bonificacion(self):
        resultado = procesar_recarga(monto=9999, plan="normal")
        assert resultado["bonificacion_pct"] == 0.0

    def test_monto_en_limite_10000_tiene_bonificacion_10(self):
        resultado = procesar_recarga(monto=10000, plan="normal")
        assert resultado["bonificacion_pct"] == 10.0

    def test_monto_intermedio_tiene_bonificacion_10(self):
        resultado = procesar_recarga(monto=20000, plan="normal")
        assert resultado["bonificacion_pct"] == 10.0

    def test_monto_justo_antes_de_25_pct_tiene_bonificacion_10(self):
        resultado = procesar_recarga(monto=29999, plan="normal")
        assert resultado["bonificacion_pct"] == 10.0


class TestBonificacion25Pct:
    def test_monto_en_limite_30000_tiene_bonificacion_25(self):
        resultado = procesar_recarga(monto=30000, plan="normal")
        assert resultado["bonificacion_pct"] == 25.0

    def test_monto_maximo_tiene_bonificacion_25(self):
        resultado = procesar_recarga(monto=50000, plan="normal")
        assert resultado["bonificacion_pct"] == 25.0

    def test_bonificacion_25_reemplaza_al_10(self):
        resultado_30000 = procesar_recarga(monto=30000, plan="normal")
        resultado_29999 = procesar_recarga(monto=29999, plan="normal")
        assert resultado_30000["bonificacion_pct"] == 25.0
        assert resultado_29999["bonificacion_pct"] == 10.0
