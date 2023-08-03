def encontrar_max_min(lista):
    maximo = max(lista)
    minimo = min(lista)
    return maximo, minimo

def pedir_numeros():
    lista_numeros = [int(x) for x in input("Ingresa los números de la lista separados por espacios: ").split()]
    maximo, minimo = encontrar_max_min(lista_numeros)
    print("El número más grande es:", maximo)
    print("El número más pequeño es:", minimo)

pedir_numeros()
