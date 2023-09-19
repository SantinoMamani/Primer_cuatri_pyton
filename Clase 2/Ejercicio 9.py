"""Ejercicio 9:
Dadas las siguientes listas:
edades = [25,36,18,23,45]
nombre = ["Juan","Ana","Sol","Mario","Sonia"]
y considerando que la posición en la lista corresponde a la misma persona,
mostar el nombre de la persona más joven"""

lista_edad = [25,36,18,23,45]
lista_nombre = ["Juan","Ana","Sol","Mario","Sonia"]

bandera = True

for i in lista_edad and lista_nombre:
    if bandera == True or i < menor:
        bandera = False
        menor = i
print(menor)