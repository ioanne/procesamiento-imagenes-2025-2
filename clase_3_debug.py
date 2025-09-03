def calcular_promedio(*args):
    return sum(args) / len(args)

operaciones = {
    "imprimir": print,
    "sumar": sum,
    "maximo": max,
    "minimo": min,
    "contar": len,
    "calcular_promedio": calcular_promedio
}

def ejecutar_operacion(operaciones, operacion, *args):
    funcion = operaciones.get(operacion)
    if funcion:
        return funcion(args)
    return "No existe la operación"

resultado = ejecutar_operacion(operaciones, "restar", 1,2)
print(resultado)

