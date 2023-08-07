def calcular_media(lista):
    total = sum(lista)
    media = total / len(lista)
    return media


mi_lista = [2, 4, 6, 8, 10]
media_calculada = calcular_media(mi_lista)
print(f"La media de la lista es: {media_calculada}")
