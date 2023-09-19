""" # Ejercicio 6:
# Utilizar For
# Dada la siguiente lista:
# [82, 3, 49, 38, 94, 85, 97, 92, 64, 8, 75, 37, 67, 45, 12, 55, 48, 78, 29, 58]
# mostrar el mayor. """

lista = [82, 3, 49, 38, 94, 85, 97, 92, 64, 8, 75, 37, 67, 45, 12, 55, 48, 78, 29, 58]

bandera = True

for numero in lista:
    if bandera == True or numero > mayor:
        bandera = False
        mayor = numero

print(mayor)