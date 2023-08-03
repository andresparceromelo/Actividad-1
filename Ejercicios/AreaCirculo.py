import math

def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def pedir_radio():
        radio = float(input("Ingresa el radio del círculo: "))
        area_circulo = calcular_area_circulo(radio)
        print("El área del círculo es:", area_circulo)
  
pedir_radio()
