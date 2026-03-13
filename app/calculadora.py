def calcular_ingredientes(personas, completos_por_persona, tipo):

    total_completos = personas * completos_por_persona

    ingredientes = {
        "pan": total_completos,
        "vienesas": total_completos,
        "palta_gramos": total_completos * 50,
        "tomate_gramos": total_completos * 40,
    }

    if tipo == "completo":
        ingredientes["chucrut_gramos"] = total_completos * 30

    if tipo == "dinamico":
        ingredientes["chucrut_gramos"] = total_completos * 30

    return ingredientes
