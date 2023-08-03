def es_par_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"

def pedir_numero():
    numero = int(input("Ingresa un número: "))
    resultado = es_par_impar(numero)
    print(f"El número {numero} es {resultado}.")

pedir_numero()
