
from data_stark import lista_personajes

# A. Recorrer la lista imprimiendo por consola todos los datos de cada superhéroe
# B. Recorrer la lista y mostrar la identidad y el peso del superhéroe con mayorfuerza (MÁXIMO)
# C. Recorrer la lista y mostrar nombre e identidad del superhéroe más bajo (MÍNIMO)
# D. Recorrer la lista y determinar el peso promedio de los superhéroes masculinos (PROMEDIO)
# E. Recorrer la lista y mostrar nombre y peso de los superhéroes (cualquier género) 
# los cuales su fuerza supere a la fuerza promedio de todas las superhéroes de género femenino

while True:
    opcion = input("\nA (todos los datos de cada superhéroe)\nB (la identidad y el peso del superhéroe con mayorfuerza)\nC (nombre e identidad del superhéroe más bajo)\nD (el peso promedio de los superhéroes masculinos)\nE (nombre y peso de los superhéroes)\nF (para salir) \nseleciones opcion:")
    match opcion:
        case"A" | "a":
            for i in range(len(lista_personajes)):
                print(lista_personajes[i])
        case"B" | "b":
            mayor_fuerza = int(lista_personajes[0]["fuerza"])
            for i in range(len(lista_personajes)):
                fuerza =  int(lista_personajes[i]["fuerza"])
                identida = lista_personajes[i]["identidad"]
                peso = lista_personajes[i]["peso"]
                if fuerza > mayor_fuerza :
                    mayor_fuerza = fuerza
                    identidad_mayor_fuerza = identida
                    peso_mayor_fuerza = peso
            print(f"la identidad: {identidad_mayor_fuerza} y el peso: {peso_mayor_fuerza} del superhéroe con mayorfuerza: {mayor_fuerza}")
        case"C" | "c":
            menor_altura = 100000
            for i in range(len(lista_personajes)):
                nombre = lista_personajes[i]["nombre"]
                identidad = lista_personajes[i]["identidad"]
                altura = float((lista_personajes[i]["altura"]))
                if altura < menor_altura:
                    menor_altura = altura
                    nombre_menor_altura = nombre
                    identida_menor_altura = identidad
            print(f"nombre: {nombre_menor_altura} e identidad: {identida_menor_altura} del superhéroe más bajo con: {menor_altura}")
        case"D" | "d":
            cantidad_M = 0
            acumulador_peso_M = 0
            for i in range(len(lista_personajes)):
                genero = lista_personajes[i]["genero"]
                peso = float(lista_personajes[i]["peso"])
                if genero == "M":
                    cantidad_M += 1
                    acumulador_peso_M += peso
            promedio_peso_M =  acumulador_peso_M / cantidad_M
            print(f"el peso promedio: {promedio_peso_M:.2f} de los superhéroes masculinos")
        case"E" | "e":
            for i in range(len(lista_personajes)):
                nombre = lista_personajes[i]["nombre"]
                peso = float(lista_personajes[i]["peso"])
                print(f"nombre: {nombre}  peso: {peso}")
        case "F" | "f":
            break




