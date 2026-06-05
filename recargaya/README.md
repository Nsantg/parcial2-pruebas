# RecargaYa — Módulo de Recargas de Celular

Módulo desarrollado con TDD, BDD y CI/CD para gestionar recargas de celular
con bonificaciones según monto y plan del usuario.

## Reglas de negocio

| Condición                        | Bonificación         |
|----------------------------------|----------------------|
| Monto < $1.000 o > $50.000       | Recarga rechazada    |
| $1.000 – $9.999                  | 0%                   |
| $10.000 – $29.999                | +10% datos           |
| $30.000 – $50.000                | +25% datos           |
| Plan PREMIUM (con bono base > 0) | +5% adicional        |

---

## Requisitos previos

```bash
python -m venv .venv
# Windows
.venv\Scripts\pip install -r requirements.txt
```

---

## Cómo ejecutar los tests unitarios (pytest)

```bash
cd recargaya
..\.venv\Scripts\pytest tests/test_recargas.py -v
```

Salida esperada: **20 passed**.

---

## Cómo ejecutar los escenarios BDD (behave)

```bash
cd recargaya
behave features/
```

Corre todos los escenarios definidos en `features/recargas.feature`
incluyendo los `Scenario Outline` con valores límite para plan normal y premium.

---

## Cómo ejecutar el servidor FastAPI

```bash
cd recargaya
..\.venv\Scripts\uvicorn app.main:app --reload
```

- API disponible en: `http://127.0.0.1:8000`
- Documentación Swagger: `http://127.0.0.1:8000/docs`

### Ejemplo de request

```bash
curl -X POST http://127.0.0.1:8000/recargas \
  -H "Content-Type: application/json" \
  -d '{"monto": 30000, "plan": "premium"}'
```

### Ejemplo de response

```json
{
  "monto": 30000.0,
  "bonificacion_pct": 30.0,
  "estado": "aceptada"
}
```

---

## Cómo ejecutar la prueba de carga (Locust)

Con el servidor FastAPI corriendo en otra terminal:

```bash
cd recargaya
locust -f tests/locustfile.py --headless -u 30 -r 10 --run-time 30s --host http://127.0.0.1:8000
```

- `-u 30` → 30 usuarios simultáneos
- `-r 10` → 10 usuarios nuevos por segundo al arranque
- `--run-time 30s` → duración de la prueba

**Criterio de éxito:** columna `95%` < 300ms en el reporte final.

---

## Estructura del proyecto

```
recargaya/
├── app/
│   ├── __init__.py
│   ├── main.py              ← API REST FastAPI
│   └── recargas.py          ← lógica de negocio
├── features/
│   ├── recargas.feature     ← escenarios BDD Gherkin
│   └── steps/
│       └── recargas_steps.py
├── docs/
│   └── casos_de_prueba.md   ← tabla de particiones y valores límite
├── tests/
│   ├── test_recargas.py     ← tests unitarios TDD
│   └── locustfile.py        ← prueba de carga
├── .github/workflows/
│   └── ci.yml               ← pipeline CI/CD
├── requirements.txt
└── README.md
```
