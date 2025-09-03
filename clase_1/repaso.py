

def acumulador(nuevo_valor, lista=[]):
    lista.append(nuevo_valor)
    return lista


def funcion_inventada(nuevo_valor, lista):
    lista.append(nuevo_valor)
    return lista


def foo(a, b):
    print(a, b)


def foo(*args):
    for arg in args:
        print(arg)

def foo(arg1, arg2, arg3=None):
    print(arg1, arg2, arg3)


def foo(arg1, arg2, *args, arg3, arg4):
    print(arg1, arg2)
    for arg in args:
        print(arg)

lista = []
lista2= lista.copy()

def foo(arg1, arg2, *args, arg3, arg4, **kwargs):
    print(arg1, arg2)
    for arg in args:
        print(arg)
    print(kwargs)


def foo2(*args, **kwargs):
    print(args)
    print(kwargs)


def foo(*args, **kwargs):
    foo2(*args, **kwargs)



"""
Tenemos 2 tipos de argumentos.

Por posición y por nombre

posición
foo(1,2,3)

Permitir recibir todos los atributos que querramos por posición
def foo(*args):
    pass
    

Permitir recibir todos los atributos que querramos por nombre
def foo(**kwargs):
    for k,v in kwargs.items():
        print(k)
        print(v)

def foo(arg1, arg2):
    pass




nombre:
foo(valor1=10, valor=20)


"""

pepe = 10
def foo2():
    # Alcance local de pepe
    # pepe vive dentro de foo2
    global pepe # Esto es re peligroso si no lo sabemos usar.
    pepe = 9
# acá no existe pepe.

for pepe in range(0,10):
    print(pepe)
# Acá no va existir mas pepe.
# pero lo sigo accediendo, porque? porque aun no se lo cargo el recolector de basura.

pepe
