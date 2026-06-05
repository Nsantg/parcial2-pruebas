from fastapi import FastAPI
from pydantic import BaseModel, field_validator
from app.recargas import procesar_recarga

app = FastAPI(title="RecargaYa API")


class RecargaRequest(BaseModel):
    monto: float
    plan: str

    @field_validator("plan")
    @classmethod
    def plan_valido(cls, v: str) -> str:
        if v.lower() not in ("normal", "premium"):
            raise ValueError("plan debe ser 'normal' o 'premium'")
        return v.lower()


class RecargaResponse(BaseModel):
    monto: float
    bonificacion_pct: float
    estado: str


@app.post("/recargas", response_model=RecargaResponse)
def crear_recarga(recarga: RecargaRequest) -> RecargaResponse:
    resultado = procesar_recarga(monto=recarga.monto, plan=recarga.plan)
    return RecargaResponse(**resultado)
