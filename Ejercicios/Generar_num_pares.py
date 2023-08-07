def generar_lista_pares():
    lista_pares = [numero for numero in range(2, 101, 2)]
    return lista_pares

def generar():
    lista_pares = generar_lista_pares()
    print("Lista de números pares entre 1 y 100:", lista_pares)

generar()
