def suma_lista(lista):
    suma = sum(lista)
    return suma

def pedir_lista():
    lista_numeros = [int(x) for x in input("Ingresa los números de la lista separados por espacios: ").split()]
    resultado_suma = suma_lista(lista_numeros)
    print("La suma de los números en la lista es:", resultado_suma)


pedir_lista()
