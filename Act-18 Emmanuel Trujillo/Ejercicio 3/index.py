def retornar_superficie(lado1, lado2):
    superficie = lado1 * lado2
    return superficie


# Bloque principal
print("Primer rectángulo")
lado1 = int(input("Ingrese el primer lado: "))
lado2 = int(input("Ingrese el segundo lado: "))

print("Segundo rectángulo")
lado3 = int(input("Ingrese el primer lado: "))
lado4 = int(input("Ingrese el segundo lado: "))

superficie1 = retornar_superficie(lado1, lado2)
superficie2 = retornar_superficie(lado3, lado4)

print("Superficie del primer rectángulo:", superficie1)
print("Superficie del segundo rectángulo:", superficie2)

if superficie1 > superficie2:
    print("El primer rectángulo tiene mayor superficie.")
elif superficie2 > superficie1:
    print("El segundo rectángulo tiene mayor superficie.")
else:
    print("Los dos rectángulos tienen la misma superficie.")