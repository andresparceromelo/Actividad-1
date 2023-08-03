def fahrenheit_a_celsius(grados_fahrenheit):
    grados_celsius = (grados_fahrenheit - 32) * 5 / 9
    return grados_celsius

def pedir_grados():
    fahrenheit = float(input("Ingresa la temperatura en grados Fahrenheit: "))
    celsius = fahrenheit_a_celsius(fahrenheit)
    print(f"{fahrenheit} grados Fahrenheit son equivalentes a {celsius} grados Celsius.")

pedir_grados()