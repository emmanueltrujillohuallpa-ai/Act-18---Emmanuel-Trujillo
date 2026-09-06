def contar_a(texto):
    cantidad = 0

    for letra in texto:
        if letra == "a" or letra == "A":
            cantidad = cantidad + 1

    return cantidad


# Bloque principal
texto = input("Ingrese un texto: ")

cantidad = contar_a(texto)

print("La cantidad de letras a o A es:", cantidad)