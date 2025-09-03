letras = ["a", "c", "d", "e"]

for letra in letras:
    print(letra)
    if letra == "b":
        break
else:
    print("Se recorrió toda la lista sin encontrar 'b'")

letras = ["a", "c", "d", "e", "b", "f"]


for letra in letras:
    if letra == "b":
        continue # por el próximo
    print(letra)

## Loop infinito
# while True:
#     print(1)
#     continue

condicion = True
while condicion:
    print(1)
    break
else:
    print("No se ejecuta porque el while termina con un break")

condicion = True
while condicion: # Si sale el while por la condición, se ejecuta el else
    print(1)
    condicion = False
else:
    print("El while terminó porque la condición es False")

contador = 0
maximo_contador = 5
while contador < maximo_contador: # Acá evalua la condición
    print(contador)
    contador += 1

# Como evitamos el uso de if elif else excesivos.
letras = {
    "a": "A",
    "b": "B",
    "c": "C",
    "d": "D",
    "e": "E"
}
valor = "a"
if letras.get(valor) == "A":
    print("Es A")
elif letras.get(valor) == "B":
    print("Es B")
elif letras.get(valor) == "C":
    print("Es C")
elif letras.get(valor) == "D":
    print("Es D")
elif letras.get(valor) == "E":
    print("Es E")
else:
    print("No es ninguna")

def buscar_letra(letras, letra):
    return letras.get(letra, "No es ninguna")

buscar_letra(letras, valor)

operaciones = {
    "imprimir": print,
    "sumar": sum,
    "maximo": max,
    "minimo": min,
    "contar": len
}

def ejecutar_operacion(operaciones, operacion, *args):
    funcion = operaciones.get(operacion)
    if funcion:
        return funcion(args)
    return "No existe la operación"


class MiClase:
    pass

# Clase abstracta define comportamientos pero no los implementa
class Vehiculo: # Clase
    def acelerar(self, intensidad):
        pass

    def frenar(self, intensidad):
        pass

    def doblar(self, direccion):
        pass


class Auto(Vehiculo): # Clase
    def acelerar(self, intensidad):
        # Implementamos el metodo
        print(f"Acelerando el auto con intensidad {intensidad}")

    def frenar(self, intensidad):
        # Implementamos el metodo
        print(f"Frenando el auto con intensidad {intensidad}")

    def doblar(self, direccion):
        # Implementamos el metodo
        print(f"Doblando el auto a la {direccion}")

print("--- Auto ---")
auto = Auto() # Instancia de Auto
auto.acelerar(5)
auto.frenar(3)
auto.doblar("derecha")

# Polimorfismo
class AutoBMW(Auto):
    # Sobreescribir métodos
    def acelerar(self, intensidad):
        print(f"Acelerando el bmw con mayor intensidad {intensidad}")

    # extendemos el método
    def frenar(self, intensidad):
        super().frenar(intensidad)
        print("Activando sistema de frenos ABS")

print("--- Auto BMW ---")
auto_bmw = AutoBMW()
auto_bmw.acelerar(10)
auto_bmw.frenar(5)
auto_bmw.doblar("izquierda")


class Auto(Vehiculo):
    def __init__(self, velocidad):
        self.velocidad = velocidad
    def acelerar(self, intensidad):
        self.velocidad += intensidad
        print(f"Acelerando el auto a {self.velocidad} km/h")

# Encapsulamiento
class Auto(Vehiculo):
    def __init__(self):
        self._velocidad = 0

    def acelerar(self, intensidad):
        self._velocidad += intensidad
        print(f"Acelerando el auto a {self._velocidad} km/h")

    # Es la manera que tiene python de convertir un metodo en un atributo
    # Esto protege el atributo de ser modificado directamente
    @property # Es un decorador de python
    def velocidad(self): # Atributo
        return self._velocidad

    def frenar(self, intensidad):
        self._velocidad -= intensidad
        if self._velocidad < 0:
            self._velocidad = 0
        print(f"Frenando el auto a {self._velocidad} km/h")

    def chocar_contra_pared(self, velocidad = 0):
        self._velocidad = 0
        print("El auto ha chocado contra la pared")

auto = Auto()
auto._velocidad = 100 # No se debe hacer. Esta mal.