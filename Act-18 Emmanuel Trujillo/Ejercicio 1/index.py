def mostrar_menor():
    valor1 = int(input("Ingrese el primer valor: "))
    valor2 = int(input("Ingrese el segundo valor: "))
    valor3 = int(input("Ingrese el tercer valor: "))

    menor = valor1

    if valor2 < menor:
        menor = valor2

    if valor3 < menor:
        menor = valor3

    print("El menor es:", menor)


# Bloque principal
mostrar_menor()
mostrar_menor()