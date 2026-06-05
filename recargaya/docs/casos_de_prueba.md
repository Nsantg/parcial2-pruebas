# Tabla de Casos de Prueba — Módulo de Recargas RecargaYa

## Particiones de equivalencia y valores límite

| ID    | Descripción                                      | Monto      | Plan    | Bonificación Esperada | Resultado  |
|-------|--------------------------------------------------|------------|---------|-----------------------|------------|
| TC01  | Por debajo del mínimo absoluto                   | $999       | NORMAL  | —                     | rechazada  |
| TC02  | En el límite inferior válido                     | $1.000     | NORMAL  | 0%                    | aceptada   |
| TC03  | Justo antes de bonificación 10%                  | $9.999     | NORMAL  | 0%                    | aceptada   |
| TC04  | En el límite de bonificación 10%                 | $10.000    | NORMAL  | 10%                   | aceptada   |
| TC05  | Justo antes de bonificación 25%                  | $29.999    | NORMAL  | 10%                   | aceptada   |
| TC06  | En el límite de bonificación 25%                 | $30.000    | NORMAL  | 25%                   | aceptada   |
| TC07  | En el límite superior válido                     | $50.000    | NORMAL  | 25%                   | aceptada   |
| TC08  | Por encima del máximo absoluto                   | $50.001    | NORMAL  | —                     | rechazada  |
| TC09  | Por debajo del mínimo, plan PREMIUM              | $999       | PREMIUM | —                     | rechazada  |
| TC10  | Límite inferior, plan PREMIUM                    | $1.000     | PREMIUM | 0%                    | aceptada   |
| TC11  | Justo antes del 10%, plan PREMIUM                | $9.999     | PREMIUM | 0%                    | aceptada   |
| TC12  | Límite 10%, plan PREMIUM                         | $10.000    | PREMIUM | 10% + 5% = 15%        | aceptada   |
| TC13  | Justo antes del 25%, plan PREMIUM                | $29.999    | PREMIUM | 10% + 5% = 15%        | aceptada   |
| TC14  | Límite 25%, plan PREMIUM                         | $30.000    | PREMIUM | 25% + 5% = 30%        | aceptada   |
| TC15  | Límite superior, plan PREMIUM                    | $50.000    | PREMIUM | 25% + 5% = 30%        | aceptada   |
| TC16  | Por encima del máximo, plan PREMIUM              | $50.001    | PREMIUM | —                     | rechazada  |
| TC17  | Monto cero (borde inválido extremo)              | $0         | NORMAL  | —                     | rechazada  |
| TC18  | Monto negativo                                   | -$500      | NORMAL  | —                     | rechazada  |
| TC19  | Valor medio sin bonificación                     | $5.000     | NORMAL  | 0%                    | aceptada   |
| TC20  | Valor medio con bonificación 10%                 | $20.000    | NORMAL  | 10%                   | aceptada   |

## Reglas de negocio cubiertas

| Regla                                               | Casos que la cubren              |
|-----------------------------------------------------|----------------------------------|
| Monto mínimo $1.000                                 | TC01, TC02, TC09, TC10           |
| Monto máximo $50.000                                | TC07, TC08, TC15, TC16           |
| Sin bonificación entre $1.000 y $9.999              | TC02, TC03, TC10, TC11, TC19     |
| Bonificación 10% para monto >= $10.000              | TC04, TC05, TC12, TC13, TC20     |
| Bonificación 25% reemplaza al 10% para >= $30.000  | TC06, TC07, TC14, TC15           |
| +5% adicional para plan PREMIUM (con bono base)     | TC12, TC13, TC14, TC15           |
| PREMIUM sin bono base no recibe el +5%              | TC10, TC11                       |
