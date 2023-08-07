def realizar_operaciones(numero1, numero2):
    suma = numero1 + numero2
    resta = numero1 - numero2
    multiplicacion = numero1 * numero2
    division = numero1 / numero2
    return suma, resta, multiplicacion, division

def pedir_numeros():
    numero1 = float(input("Ingresa el primer número: "))
    numero2 = float(input("Ingresa el segundo número: "))
    
    suma, resta, multiplicacion, division = realizar_operaciones(numero1, numero2)
    
    print(f"Suma: {suma}")
    print(f"Resta: {resta}")
    print(f"Multiplicación: {multiplicacion}")
    print(f"División: {division}")

pedir_numeros()
