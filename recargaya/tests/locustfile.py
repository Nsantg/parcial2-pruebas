import random
from locust import HttpUser, task, between
from locust.env import Environment


MONTOS_VALIDOS = [1000, 5000, 9999, 10000, 20000, 29999, 30000, 50000]
MONTOS_INVALIDOS = [999, 50001]
PLANES = ["normal", "premium"]


class RecargaUser(HttpUser):
    wait_time = between(0.1, 0.5)
    host = "http://127.0.0.1:8000"

    @task(8)
    def recarga_valida(self):
        payload = {
            "monto": random.choice(MONTOS_VALIDOS),
            "plan": random.choice(PLANES),
        }
        with self.client.post("/recargas", json=payload, catch_response=True) as response:
            if response.status_code == 200:
                data = response.json()
                if data["estado"] not in ("aceptada", "rechazada"):
                    response.failure(f"Estado inesperado: {data['estado']}")
                else:
                    response.success()
            else:
                response.failure(f"HTTP {response.status_code}")

    @task(2)
    def recarga_invalida(self):
        payload = {
            "monto": random.choice(MONTOS_INVALIDOS),
            "plan": random.choice(PLANES),
        }
        with self.client.post("/recargas", json=payload, catch_response=True) as response:
            if response.status_code == 200:
                data = response.json()
                if data["estado"] == "rechazada":
                    response.success()
                else:
                    response.failure("Monto inválido debería ser rechazado")
            else:
                response.failure(f"HTTP {response.status_code}")
