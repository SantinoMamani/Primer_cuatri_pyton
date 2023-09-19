""" 
A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
género NB
B. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
D. Recorrer la lista y determinar cuál es el superhéroe más débil de género M
E. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB
F. Recorrer la lista y determinar la fuerza promedio de los superhéroes de
género NB
G. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
H. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
I. Listar todos los superhéroes agrupados por color de ojos.
J. Listar todos los superhéroes agrupados por tipo de inteligencia """

from data_stark import lista_personajes

def mostrar_nb():
    for i in range(len(lista_personajes)):
        nombre = lista_personajes[i]["nombre"]
        genero = lista_personajes[i]["genero"]       
        if genero == "NB":
            print(f"{nombre}")

def mas_alto_Fem():
    mas_alto_f = 0
    for i in range(len(lista_personajes)):
        nombre = lista_personajes[i]["nombre"]
        genero = lista_personajes[i]["genero"]    
        altura = float(lista_personajes[i]["altura"])
        if genero == "F" and altura > mas_alto_f:
            mas_alto_f = altura
            nombre_mas_alto_f = nombre
    print(f"{nombre_mas_alto_f}") 
    
    
def mas_alto_Mas():
    mas_alto_m = 0
    for i in range(len(lista_personajes)):
        nombre = lista_personajes[i]["nombre"]
        genero = lista_personajes[i]["genero"]    
        altura = float(lista_personajes[i]["altura"])
        if genero == "M" and altura > mas_alto_m:
            mas_alto_m = altura
            mas_alto_m = nombre
    print(f"{mas_alto_m}") 
    
def mas_debil_Masculino():
    mas_debil_m = 0
    for i in range(len(lista_personajes)):
        nombre = lista_personajes[i]["nombre"]
        genero = lista_personajes[i]["genero"]    
        fuerza = int(lista_personajes[i]["fuerza"])
        if genero == "M":
            if mas_debil_m == 0 or fuerza < mas_debil_m:
                mas_debil_m = fuerza
                mas_debil_nombre = nombre
    print(f"{mas_debil_nombre}, {mas_debil_m}")
    
    
def mas_debil_nb():
    nb_mas_debil = 0
    for i in range(len(lista_personajes)):
        nombre = lista_personajes[i]["nombre"]
        genero = lista_personajes[i]["genero"]    
        fuerza = int(lista_personajes[i]["fuerza"])
        if genero == "NB":
            if nb_mas_debil == 0 or fuerza < nb_mas_debil:
                nb_mas_debil = fuerza
                mas_debil_nombre = nombre
    print(f"{mas_debil_nombre}, {nb_mas_debil}")


def promedio_nb():
    acumulador_nb = 0
    contador_nb = 0
    for i in range(len(lista_personajes)):
        nombre = lista_personajes[i]["nombre"]
        genero = lista_personajes[i]["genero"]
        fuerza = int(lista_personajes[i]["fuerza"])
        if genero == 'NB':
            acumulador_nb += fuerza
            contador_nb += 1 
    promedio_total_nb = acumulador_nb / contador_nb
    
    print(f"{promedio_total_nb}")

def contar_colores_ojos():
    colores_ojos = {}  
    for personaje in lista_personajes:
        color_ojos = personaje['color_ojos']
        if color_ojos in colores_ojos:
            colores_ojos[color_ojos] += 1
        else:
            colores_ojos[color_ojos] = 1
    for color, cantidad in colores_ojos.items():
        print(f"Color de ojos '{color}': {cantidad} superhéroes")    

def contar_colores_pelo():
    colores_pelo = {}  
    for personaje in lista_personajes:
        color_pelo = personaje['color_pelo']
        if color_pelo in colores_pelo:
            colores_pelo[color_pelo] += 1
        else:
            colores_pelo[color_pelo] = 1
    for color, cantidad in colores_pelo.items():
        print(f"Color de pelo '{color}': {cantidad} superhéroes") 
    
def contador_color_ojos ():
    diccionario_color_ojos = {}
    
    for personaje in lista_personajes:
        if personaje ["color_ojos"] in diccionario_color_ojos:
            diccionario_color_ojos[personaje["color_ojos"]] += 1
        else:
            diccionario_color_ojos[personaje["color_ojos"]] = 1
    print(f"Cantidad de personajes por color de ojos: {diccionario_color_ojos}")
    
    
def contador_tipo_inteligencia ():
    diccionario_tipo_inteligencia = {}
    
    for personaje in lista_personajes:
        if personaje ["inteligencia"] in diccionario_tipo_inteligencia:
            diccionario_tipo_inteligencia[personaje["inteligencia"]] += 1
        else:
            diccionario_tipo_inteligencia[personaje["inteligencia"]] = 1
    print(f"Cantidad de personajes por cada tipo de inteligencia es: {diccionario_tipo_inteligencia}")
    
        
while True:
    opcion = input("\nA. todos los datos de cada superhéroe\nB. Recorrer la lista y determinar cuál es el superhéroe más alto de género F\nC. Recorrer la lista y determinar cuál es el superhéroe más alto de género M\nD. Recorrer la lista y determinar cuál es el superhéroe más débil de género M\nE. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB\nF. Recorrer la lista y determinar la fuerza promedio de los superhéroes de género NB\nG. Determinar cuántos superhéroes tienen cada tipo de color de ojos.\nH. Determinar cuántos superhéroes tienen cada tipo de color de pelo.\nI. Listar todos los superhéroes agrupados por color de ojos.\nJ. Listar todos los superhéroes agrupados por tipo de inteligencia\nK. Salir:")
    match opcion:
        case"A" | "a":
            mostrar_nb()
        case"B" | "b":
            mas_alto_Fem()
        case "C" | "c":
            mas_alto_Mas()
        case "D" | "d":
            mas_debil_Masculino()
        case "E" | "e":
            mas_debil_nb()
        case "F" | "f":
            promedio_nb()
        case "G" | "g":
            contar_colores_ojos()
        case "H" | "h":
            contar_colores_pelo()
        case "I" | "i":
            contador_color_ojos()
        case "J" | "j":
            contador_tipo_inteligencia()
        case "K" | "k":
            break