def mostrar_ordenados(valor1, valor2, valor3):
    if valor1 > valor2:
        aux = valor1
        valor1 = valor2
        valor2 = aux

    if valor1 > valor3:
        aux = valor1
        valor1 = valor3
        valor3 = aux

    if valor2 > valor3:
        aux = valor2
        valor2 = valor3
        valor3 = aux

    print("Ordenados de menor a mayor:")
    print(valor1, valor2, valor3)


def cargar_valores():
    valor1 = int(input("Ingrese el primer entero: "))
    valor2 = int(input("Ingrese el segundo entero: "))
    valor3 = int(input("Ingrese el tercer entero: "))

    mostrar_ordenados(valor1, valor2, valor3)


# Bloque principal
cargar_valores()