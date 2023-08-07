def calcular_factorial(numero):
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    return factorial

def pedir_numero():
    numero = int(input("Ingresa un número: "))
    resultado_factorial = calcular_factorial(numero)
    print(f"El factorial de {numero} es: {resultado_factorial}")


pedir_numero()
