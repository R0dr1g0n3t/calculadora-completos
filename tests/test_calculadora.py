from app.calculadora import calcular_ingredientes


def test_calculo_basico():

    resultado = calcular_ingredientes(10, 2, "italiano")

    assert resultado["pan"] == 20
    assert resultado["vienesas"] == 20

def test_completo_tiene_chucrut():
    resultado = calcular_ingredientes(5, 2, "completo")

    assert "chucrut_gramos" in resultado

