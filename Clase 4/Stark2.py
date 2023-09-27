# Desafío #02:
# Usando como base lo realizado en el anterior desafío realizar los siguientes
# informes en un menú
# A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género NB
# B. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
# C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
# D. Recorrer la lista y determinar cuál es el superhéroe más débil de género M
# E. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB
# F. Recorrer la lista y determinar la fuerza promedio de los superhéroes de género NB
# G. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
# H. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
# I. Listar todos los superhéroes agrupados por color de ojos.
# J. Listar todos los superhéroes agrupados por tipo de inteligencia
# NOTA: Se debe aplicar el tema Funciones visto en clase para cada opción del menú
from data_stark import lista_personajes
def nombre_NB(lista:list):
    for i in range(len(lista)):
        genero = lista[i]["genero"]
        nombre = lista[i]["nombre"]
        if genero == "NB":
            print(f"superhéroe de género NB {nombre}")

def f_mas_alta(lista:list):
    altura_maxima_f = 0
    for i in range(len(lista)):
        nombre = lista[i]["nombre"]
        genero = lista[i]["genero"]
        altura = float(lista[i]["altura"])
        if genero == "F" and altura > altura_maxima_f:
            altura_maxima_f = altura
            nombre_altura_maxima_f = nombre
    print (f"el superhéroe más alto con {altura_maxima_f} de género F {nombre_altura_maxima_f}")

def m_mas_alta(lista:list):
    altura_maxima_m = 0
    for i in range(len(lista)):
        nombre = lista[i]["nombre"]
        genero = lista[i]["genero"]
        altura = float(lista[i]["altura"])
        if genero == "M" and altura > altura_maxima_m:
            altura_maxima_m = altura
            nombre_altura_maxima_m = nombre
    print (f"el superhéroe más alto con {altura_maxima_m} de género M {nombre_altura_maxima_m}")


def m_mas_debil(lista:list):
    fuerza_minima = 0
    for i in range(len(lista)):
        genero = lista[i]["genero"]
        nombre = lista[i]["nombre"]
        fuerza = int(lista[i]["fuerza"])
        if genero == "M" :
            if fuerza_minima == 0 or fuerza < fuerza_minima:
                fuerza_minima = fuerza
                nombre_debil_m = nombre
    print(f"el superhéroe {nombre_debil_m} más débil con {fuerza_minima} fuerza de género M")

def nb_mas_debil(lista):
    fuerza_minima = 0
    for i in range(len(lista)):
        genero = lista[i]["genero"]
        nombre = lista[i]["nombre"]
        fuerza = int(lista[i]["fuerza"])
        if genero == "NB" :
            if fuerza_minima == 0 or fuerza < fuerza_minima:
                fuerza_minima = fuerza
                nombre_debil_nb = nombre
    print(f"el superhéroe {nombre_debil_nb} más débil con {fuerza_minima} fuerza de género NB")

def promedio_fuerza_genero(lista:list,g:str):
    str(g)
    contador = 0
    acumulador = 0
    for i in range(len(lista)):
        genero = lista[i]["genero"]
        fuerza = int(lista[i]["fuerza"])
        if genero == g :
            contador += 1
            acumulador += fuerza
    promedio_de_fuerza = acumulador / contador
    print(f"la fuerza promedio es de {promedio_de_fuerza} los superhéroes de género NB")

def contador_color_ojos(lista:list):
    contador_yellow = 0
    contador_Yellow_without_irises = 0
    contador_Red = 0
    contador_Blue = 0
    contador_Green = 0
    contador_brown = 0
    contador_Silver = 0
    contador_Hazel = 0
    for i in range(len(lista)):
        color_ojos = lista[i]["color_ojos"]
        match color_ojos:
            case "Brown":
                contador_brown += 1
            case "Yellow":
                contador_yellow += 1
            case "Yellow (without irises)":
                contador_Yellow_without_irises += 1
            case "Blue":
                contador_Blue += 1
            case "Green":
                contador_Green += 1
            case "Hazel":
                contador_Hazel += 1
            case "Silver":
                contador_Silver += 1
            case "Red":
                contador_Red += 1
    print(f"{contador_Blue} tienen color azul \n{contador_brown} tienen color marron \n{contador_Green} tienen color verde \n{contador_Red} tiene el color rojo \n{contador_Hazel} tienen color avellana \n{contador_Silver} tienen color Plata \n{contador_yellow} tienen color amarillo \n{contador_Yellow_without_irises} tienen color Amarillo sin iris")

# I. Listar todos los superhéroes agrupados por color de ojos.
def agrupacio_superheroes_ojos(lista:list):
    heroes_ojos_Red = []
    heroes_ojos_Brown = []
    heroes_ojos_Yellow = []
    heroes_ojos_Yellow_without_irises = []
    heroes_ojos_Blue = []
    heroes_ojos_Green = []
    heroes_ojos_Hazel = []
    heroes_ojos_Silver = []
    for i in range(len(lista)):
        color_ojos = lista[i]["color_ojos"]
        nombre_super = lista[i]["nombre"]
        match color_ojos:
            case "Brown":
                heroes_ojos_Brown.append(nombre_super)
            case "Yellow":
                heroes_ojos_Yellow.append(nombre_super)
            case "Yellow (without irises)":
                heroes_ojos_Yellow_without_irises.append(nombre_super)
            case "Blue":
                heroes_ojos_Blue.append(nombre_super)
            case "Green":
                heroes_ojos_Green.append(nombre_super)
            case "Hazel":
                heroes_ojos_Hazel.append(nombre_super)
            case "Silver":
                heroes_ojos_Silver.append(nombre_super)
            case "Red":
                heroes_ojos_Red.append(nombre_super)
    print(f"{heroes_ojos_Blue} tienen color azul \n{heroes_ojos_Brown} tienen color marron \n{heroes_ojos_Green} tienen color verde \n{heroes_ojos_Red} tiene el color rojo \n{heroes_ojos_Hazel} tienen color avellana \n{heroes_ojos_Silver} tienen color Plata \n{heroes_ojos_Yellow} tienen color amarillo \n{heroes_ojos_Yellow_without_irises} tienen color Amarillo sin iris")


def contador_color_pelo(lista:list):
    contador_yellow = 0
    contador_brown = 0
    contador_Black = 0
    contador_Auburn = 0
    contdor_Red_Orange = 0
    contador_White = 0
    contador_Blond = 0
    contador_Green = 0
    contador_Red = 0
    contador_Brown_White = 0
    for i in range(len(lista)):
        color_pelo = lista[i]["color_pelo"]
        match color_pelo:
            case "Brown":
                contador_brown += 1
            case "Yellow":
                contador_yellow += 1
            case "Black":
                contador_Black += 1
            case "Green":
                contador_Green += 1
            case "Hazel":
                contador_White += 1
            case "Auburn":
                contador_Auburn += 1
            case "Red":
                contador_Red += 1
            case "Red / Orange":
                contdor_Red_Orange += 1
            case "Brown / White":
                contador_Brown_White += 1
            case "Blond":
                contador_Blond += 1

    print(f"{contador_brown} tienen color marron \n{contador_Green} tienen color verde \n{contador_Red} tiene el color rojo \n{contador_White} tienen color blanco \n{contador_Auburn} tienen color Castaño \n{contador_yellow} tienen color amarillo \n{contador_Black} tienen color negro \n{contador_Blond} tienen color Rubio \n{contador_Brown_White} tienen Cafe Blanco \n{contdor_Red_Orange} tiene color Naranja roja")

# J. Listar todos los superhéroes agrupados por tipo de inteligencia
def agrupacion_por_inteligencia(lista:list):
    high = []
    average = []
    good = []
    nada = []
    for i in range(len(lista)):
        inteligencia = lista[i]["inteligencia"]
        nombre_super = lista[i]["nombre"]
        match inteligencia:
            case "high":
                high.append(nombre_super)
            case "average":
                average.append(nombre_super)
            case "good":
                good.append(nombre_super)
            case "":
                nada.append(nombre_super)
    print(f"{high} tienen nivel de inteligencia alta \n{average} tienen nivel de inteligencia promedio \n{good} tienen nivel de inteligencia buena \n{nada} tiene niuvel de inteligencia nulo")

""" while True:
    opcion = input("A el nombre de cada superhéroe de género NB \nB cuál es el superhéroe más alto de género F \nC el superhéroe más alto de género M \nD el superhéroe más débil de género M \nE el superhéroe más débil de género NB \nF el la fuerza promedio de los superhéroes de género NB \nG cuántos superhéroes tienen cada tipo de color de ojos \nH cuántos superhéroes tienen cada tipo de color de pelo \nI los superhéroes agrupados por color de ojos \nJ los superhéroes agrupados por tipo de inteligencia \nS (SALIR) ")

    match opcion:
        case "A" | "a" :
            nombre_NB(lista_personajes)
        case "B" | "b" :
            f_mas_alta(lista_personajes)
        case "C" | "c":
            m_mas_alta(lista_personajes)
        case "D" | "d":
            m_mas_debil(lista_personajes)
        case "E" | "e":
            nb_mas_debil(lista_personajes)
        case "F" | "f":
            promedio_fuerza_genero(lista_personajes,"NB")
        case "G" | "g":
            contador_color_ojos(lista_personajes)
        case "H" | "h":
            contador_color_pelo(lista_personajes)
        case "I" | "i":
            agrupacio_superheroes_ojos(lista_personajes)
        case "J" | "j":
            agrupacion_por_inteligencia(lista_personajes)
        case "S" | "s" :
            break """

