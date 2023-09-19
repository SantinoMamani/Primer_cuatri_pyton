"""
La división de higiene está trabajando en un control de stock para productos sanitarios.
Debemos realizar la carga de 5 (cinco) productos de prevención de contagio, de cada una debe
obtener los siguientes datos:
1. El tipo (validar "barbijo", "jabón" o "alcohol")
2. El precio: (validar entre 100 y 300)
3. La cantidad de unidades ( no puede ser 0 ni negativo y no debe superar las 1000
unidades)
4. La marca y el Fabricante.
Se debe informar lo siguiente:
A. Del más caro de los barbijos, la cantidad de unidades y el fabricante.
B. Del ítem con más unidades, el fabricante.
C. Cuántas unidades de jabones hay en total.
"""
lista_productos = []


for i in range(5):
    barbijo_caro = 0
    unidades_barbijo = 0
    fabricante_barbijo = 0
    mas_unidades = 0
    bandera_unidades = False
    fabricantes_unidades = 0
    contador_jabones = 0

    tipo = input("Ingrese el tipo de producto (barbijo, jabon o alcohol) ")
    while tipo != "barbijo" and tipo != "jabones" and tipo != "alcohol":
        tipo = input("Reingrese el tipo de producto (barbijo, jabon o alcohol) ")
    lista_productos.append(tipo)

    precio = input("Ingrese el precio de producto")
    while precio > 100 or precio < 300:
        precio = input("Ingrese el precio de producto correcto")
    
    unidades = int(input("Ingrese la cantidad de unidades de producto( no puede ser 0 ni negativo y no debe superar las 1000 unidades)"))
    while unidades <= 0 and unidades > 1000:
        unidades = int(input("Reingrese la cantidad de unidades de producto( no puede ser 0 ni negativo y no debe superar las 1000 unidades)"))

    marca = input("Ingrese la marca del producto ")
    
    fabricante = input("Ingrese el fabricante del producto ")


 

    
    if tipo == "barbijo" and precio > barbijo_caro:
        barbijo_caro = precio
        unidades_barbijo = unidades
        fabricante_barbijo = fabricante

    if unidades > mas_unidades or bandera_unidades == False:
        unidades = mas_unidades
        fabricante_unidades =fabricante
        bandera_unidades = True

    if tipo == "jabones":
        contador_jabones += 1




print(f"El barbijo mas caro es de: {barbijo_caro} la cantidad de unidades: {unidades_barbijo} y el fabricante: {fabricante_barbijo}")
print(f"El fabricante de mas unidades: {fabricante_unidades}")
print(f"La cantidad total de jabones es de: {contador_jabones}")
