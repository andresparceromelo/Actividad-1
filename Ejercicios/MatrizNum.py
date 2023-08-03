def generar_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = [i * columnas + j + 1 for j in range(columnas)]
        matriz.append(fila)
    return matriz

def mostrar_matriz(matriz):
    for fila in matriz:
        print(" ".join(str(elemento) for elemento in fila))

def pedir_matriz():
    filas = int(input("Ingresa el número de filas: "))
    columnas = int(input("Ingresa el número de columnas: "))

    matriz_generada = generar_matriz(filas, columnas)
    mostrar_matriz(matriz_generada)

pedir_matriz()
