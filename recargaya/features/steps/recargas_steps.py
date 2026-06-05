from behave import given, when, then
from app.recargas import procesar_recarga


@given("el sistema de recargas está disponible")
def step_sistema_disponible(context):
    pass


@given('un usuario con plan "{plan}"')
def step_usuario_con_plan(context, plan):
    context.plan = plan.lower()


@when("solicita una recarga de ${monto:d}")
def step_solicita_recarga(context, monto):
    context.resultado = procesar_recarga(monto=monto, plan=context.plan)


@then("la recarga es rechazada")
def step_recarga_rechazada(context):
    assert context.resultado["estado"] == "rechazada", (
        f"Se esperaba 'rechazada' pero fue '{context.resultado['estado']}'"
    )


@then("no se calcula bonificación")
def step_sin_bonificacion(context):
    assert context.resultado["bonificacion_pct"] == 0.0


@then("la recarga es aceptada")
def step_recarga_aceptada(context):
    assert context.resultado["estado"] == "aceptada", (
        f"Se esperaba 'aceptada' pero fue '{context.resultado['estado']}'"
    )


@then("la bonificación es del {bonificacion:d}%")
def step_bonificacion_esperada(context, bonificacion):
    assert context.resultado["bonificacion_pct"] == float(bonificacion), (
        f"Se esperaba {bonificacion}% pero fue {context.resultado['bonificacion_pct']}%"
    )


@then('el resultado es "{resultado}"')
def step_resultado(context, resultado):
    assert context.resultado["estado"] == resultado, (
        f"Se esperaba '{resultado}' pero fue '{context.resultado['estado']}'"
    )


@then("la bonificación esperada es {bonificacion:d}%")
def step_bonificacion_outline(context, bonificacion):
    assert context.resultado["bonificacion_pct"] == float(bonificacion), (
        f"Se esperaba {bonificacion}% pero fue {context.resultado['bonificacion_pct']}%"
    )
