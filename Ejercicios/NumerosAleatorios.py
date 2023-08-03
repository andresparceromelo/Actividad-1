import random
def generar_lista_aleatoria(longitud):
    lista_aleatoria = [random.randint(1, 100) for _ in range(longitud)]
    return lista_aleatoria

def pedir_tamaño():
    longitud = int(input("Ingresa la longitud de la lista: "))
    lista_generada = generar_lista_aleatoria(longitud)
    print("Lista generada:", lista_generada)

pedir_tamaño()
