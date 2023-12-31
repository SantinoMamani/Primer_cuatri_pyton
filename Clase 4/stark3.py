from Stark2 import *
from data_stark import lista_personajes

# Desafío #03: (con biblioteca propia: stark_biblioteca) En base a lo resuelto en la parte 1, deberían crearse las siguientes funciones
# IMPORTANTE: Para todas y cada una de las funciones creadas, documentarlas escribiendo que es lo que hacen, que son los parámetros que reciben (si es una lista, un string, etc y que contendrá) y que es lo que retorna la función!
# . Crear la función ;stark_normalizar_datos()' la cual recibirá por parámetro la lista de héroes. La función deberá:
# ● Recorrer la lista y convertir al tipo de dato correcto las keys (solo con las keys que representan datos numéricos) por ejemplo fuerza (int),
# altura (float), etc__________________________
# ● Validar primero que el tipo de dato no sea del tipo al cual será casteado. Por ejemplo si una key debería ser entero (ejemplo fuerza)
# verificar antes que no se encuentre ya en ese tipo de dato.____________________________
# ● Si al menos un dato fue modificado, la función deberá retornar el valor booleano True__________
# ● En caso de que la lista esté vacía o ya se hayan normalizado anteriormente los datos se deberá retornar el valor booleano False_______________
# ● Crear una opción en el menú que me permita normalizar los datos (No se debería poder acceder a ninguna otra opción del menú hasta que
# los datos esten normalizados)_______________________
# ● En caso de que la llamada a la función retorne True mostrar un mensaje diciendo “Datos Normalizados” sino mostrar el mensaje “Hubo un error al normalizar los datos. Verifique que la lista no este vacía o que los datos ya no se hayan normalizado anteriormente”______


def stark_normalizar_datos(lista:list):# normaliza los datos de la lista que se le da como argumento (altura,peso,fuerza)
    """
Esta función normaliza los datos en la lista de héroes.

Recibe:
- lista (list): La lista de héroes a normalizar.

Retorna:
- bool: True si al menos un dato fue modificado, False en otros casos.
"""
    dato_modificado = False
    modificado_anteriormente = False
    if modificado_anteriormente == True or lista == [""]:
        return False
    elif modificado_anteriormente == False:
        for i in range(len(lista)):
            while lista[i]["altura"] != float(lista[i]["altura"]):#valida que no sea flotante si no  lo es lo castea a flotante
                lista[i]["altura"] = float(lista[i]["altura"])
                dato_modificado = True
            
            while lista[i]["peso"] != float(lista[i]["peso"]):#valida que no sea flotante si no  lo es lo castea a flotante
                lista[i]["peso"] = float(lista[i]["peso"])
                dato_modificado = True
            
            while lista[i]["fuerza"] != int(lista[i]["fuerza"]):#valida que no sea entero si no  lo es lo castea a entero
                lista[i]["fuerza"] = int(lista[i]["fuerza"])
                dato_modificado = True
    if dato_modificado == True:
        return True
#_____________________________________________________________________________________________________________________________

#Crear la función ”obtener_dato()” la cual recibirá por parámetro un
# diccionario el cual representara a un héroe y también recibirá un string que
# hace referencia a una “clave” del mismo
# Validar siempre que el diccionario no esté vacío y que el mismo tenga una key
# llamada “nombre”. Caso contrario la función retornara un False

def obtener_dato(dicionario:dict,key:str):#verifica que el diccionario ingresado no este vacio y que el string se igual a "nombre"
    """
        Esta función obtiene un dato específico de un diccionario.

        Recibe:
        - diccionario (dict): El diccionario que representa a un héroe.
        - key (str): La clave del dato que se desea obtener.

        Retorna:
        - bool: True si el diccionario no está vacío y contiene la clave "nombre", False en otros casos.
        """ 
    
    contador = 0
    if dicionario == {""}:
        return False
    for i in dicionario:
        if i == "nombre":
            contador += 1
    if contador == 0 :
        return False
    else:
        return True
#_____________________________________________________________________________________________________________________________

# Crear la función 'obtener_nombre' la cual recibirá por parámetro un diccionario el
# cual representara a un héroe y devolverá un string el cual contenga su nombre
# formateado de la siguiente manera:
# Nombre: Howard the Duck
# Validar siempre que el diccionario no este vacío y que la key que se pide exista. Caso
# contrario la función retornara un False

def obtener_nombre(dicionario:dict):#devuelve un string formateado con el nombre
    """
        Esta función obtiene el nombre de un héroe.

        Recibe:
        - diccionario (dict): El diccionario que representa a un héroe.

        Retorna:
        - str: El nombre del héroe en formato "Nombre: nombre_del_héroe".
        """
    if dicionario == [""]:
        return False
    if obtener_dato(dicionario,"nombre"):
        return f"Nombre:{dicionario['nombre']}"

#______________________________________________________________________________________________________________________________

# Crear la función 'obtener_nombre_y_dato' la misma recibirá por parámetro un
# diccionario el cual representara a un héroe y una key (string) la cual
# representará el dato que se desea obtener.

# ● La función deberá devolver un string el cual contenga el nombre y dato
# (key) del héroe a imprimir. El dato puede ser 'altura','fuerza','peso',O
# CUALQUIER OTRO DATO.

# ● El string resultante debe estar formateado de la siguiente manera:
# (suponiendo que la key es fuerza)
# Nombre: Venom | fuerza: 500
# ● Validar siempre que la lista no este vacía. Caso contrario la función
# retornara un False

# NOTA: Reutilizar las funciones del punto anterior

def obtener_nombre_y_dato(dicionario:dict,key:str):#decuelve el nombre del heroe y el dato quese pasa por argumento 
    """
    Esta función obtiene el nombre y un dato específico de un héroe.

    Recibe:
    - diccionario (dict): El diccionario que representa a un héroe.
    - key (str): La clave del dato que se desea obtener.

    Retorna:
    - str: Una cadena formateada que contiene el nombre del héroe y el dato correspondiente.
    """
    if dicionario == [""]:
        return False
    return f"{obtener_nombre(dicionario)} | {key}: {dicionario[key]}"

#_______________________________________________________________________________

# 3.1 Crear la función “obtener_maximo()” la cual recibirá como parámetro una lista y
# una key (string) la cual representará el dato al cual se le debe calcular su cantidad
# MÁXIMA.
# ● Validar siempre que la lista no esté vacía y que el dato que está buscando sea
# un int o un float. Caso contrario la función retornara un False
# ● En caso de que el dato que se está buscando en el diccionario es de tipo int o
# float retornar el mayor que haya encontrado en la búsqueda.


def obtener_maximo(lista:list,key:str):#verifica que la key reprecente a un numero y devuelve el maximo en float
    """
    Esta función obtiene el valor máximo de un dato específico en una lista de héroes.

    Recibe:
    - lista (list): La lista de héroes.
    - key (str): La clave del dato a considerar.

    Retorna:
    - float or False: El valor máximo encontrado o False si la lista está vacía o el dato no es numérico.
    """
    maximo_float = 0
    if lista == [""]:
        return False
    for heroe in lista:
        if isinstance(heroe, dict):
            valor = heroe.get(key)
            if valor is not None and (isinstance(valor, int) or isinstance(valor, float)):
                if maximo_float is None or valor > maximo_float:
                    maximo_float = valor
    
    return maximo_float if maximo_float is not None else False

#____________________________________________________________________________________________
# 3.2 Crear la función “obtener_minimo()” la cual recibirá como parámetro una lista y
# una key (string) la cual representará el dato al cual se le debe calcular su cantidad
# MÍNIMA.
# ● Validar siempre que la lista no esté vacía y que el dato que está buscando sea
# un int o un float. Caso contrario la función retornara un False
# ● En caso de que el dato que se está buscando en el diccionario es de tipo int o
# float retornar el menor que haya encontrado en la búsqueda.

def obtener_minimo(lista:list,key:str):#verifica que la key reprecente a un numero y devuelve el minimo en float
    """
    Esta función obtiene el valor mínimo de un dato específico en una lista de héroes.

    Recibe:
    - lista (list): La lista de héroes.
    - key (str): La clave del dato a considerar.

    Retorna:
    - float or False: El valor mínimo encontrado o False si la lista está vacía o el dato no es numérico.
    """
    primera_ves = True
    if lista == [""]:
        return False
    for e_lista in lista:
        dato = e_lista[key]
        if dato.isalpha():
            return False 
        elif  dato.isalpha() == False:
            for i in range(len(lista)):
                dato_float = float(lista[i][key])
                if primera_ves == True:
                    primera_ves = False
                    manimo_float = dato_float
                elif dato_float < manimo_float:
                    manimo_float = dato_float
    return manimo_float


#_____________________________________________________________________________________

# 3.3 Crear la función 'obtener_dato_cantidad()' la cual recibira tres parámetros:

# ● La lista de héroes
# ● Un número que me indique el valor a buscar (puede ser la altura
# máxima, la altura mínima o cualquier otro dato)
# ● Un string que representa la key del dato a calcular, por ejemplo: ‘altura’,
# ‘peso’, ‘edad’, etc.
# La función deberá retornar una lista con el héroe o los heroes que cumplan
# con la condición pedida. Reutilizar las funciones hechas en los puntos 3.1 y
# 3.2
# Ejemplo de llamada:
# mayor_altura = obtener_maximo(lista_heroes,”altura”)
# lista_heroes_max_altura = obtener_dato_cantidad(lista_heroes,mayor_altura,”altura”)
# El objetivo de estás llamadas es obtener todos los superhéroes que tengan la altura
# correspondiente a la altura máxima, y la misma función me podria servir tanto como
# para altura menor, como la mayor o alguna altura que yo le especifique también.

def obtener_dato_cantidad(lista:list,numero:float,key:str):#devuelve una lista de heros que tengan la mismo dato en comun
    """
    Esta función obtiene una lista de héroes que tienen un dato específico en común.

    Recibe:
    - lista (list): La lista de héroes.
    - numero (float): El número que se debe buscar en el dato.
    - key (str): La clave del dato a considerar.

    Retorna:
    - list: Una lista de héroes que cumplen con la condición dada.
    """
    lista_heroes = []
    dato_maximo = obtener_maximo(lista,key)
    dato_maximo_p = True
    dato_minimo = obtener_minimo(lista,key)
    dato_minimo_p = True
    dato_p = True
    for i in range(len(lista)):
        dato = float(lista[i][key])
        if dato_maximo_p == True:
            if dato_maximo == dato and dato_maximo == numero:
                dato_maximo_p = False
                lista_heroes.append(lista[i])
        if dato_maximo_p == False:
            if dato_maximo == dato and dato_maximo == numero:
                lista_heroes.append(lista[i])
        if dato_minimo_p == True:
            if dato_minimo == dato and dato_minimo == numero:
                dato_minimo_p
                lista_heroes.append(lista[i])
        if dato_minimo_p == False:
            if dato_minimo == dato and dato_minimo == numero:
                lista_heroes.append(lista[i])
        if dato_p == True:
            if dato == numero:
                comparar = float(lista[i][key])
                dato_p = False
                lista_heroes.append(lista[i])
        if  dato_p == False:
            if dato == comparar:
                lista_heroes.append(lista[i])
    return lista_heroes

#_______________________________________________________________________

# 3.4 Crear la función stark_imprimir_heroes la cual recibirá un parametro:

# ● La lista de héroes

# Validar que la lista de héroes no esté vacía para realizar sus acciones, caso
# contrario no hará nada y retornara False
# En caso de que la lista no este vacia imprimir la información completa de
# todos los heroes de la lista que se le pase
# Ejemplo de llamada:

# mas_pesado = obtener_maximo(lista_heroes,”peso”)
# lista_mas_pesados = 'obtener_dato_cantidad(lista_heroes,mas_pesado ,”peso”)
# stark_imprimir_heroes(lista_mas_pesados) -> Imprimo sólo los héroes más
# pesados
# stark_imprimir_heroes(lista_heroes) -> Imprimo todos los héroes

def stark_imprimir_heroes(lista:list):#imprime la lista que se le pasa como argumento
    """
    Esta función imprime la lista de héroes.

    Recibe:
    - lista (list): La lista de héroes a imprimir.
    """
    if lista == [""]:
        return False
    print(lista)

#__________________________________________________________________________

# 4.1 Crear la función 'sumar_dato_heroe' la cual recibirá como parámetro una lista de
# héroes y un string que representara el dato/key de los héroes que se requiere sumar.
# Validar que cada héroe sea tipo diccionario y que no sea un diccionario vacío antes
# de hacer la suma. La función deberá retorna la suma de todos los datos según la key
# pasada por parámetro

def sumar_dato_heroe(lista:list,key:str):#devuelve la sumatoria de el la que que se le pase
    """
    Devuelve la sumatoria de un dato específico de los héroes en la lista.
    
    Args:
    - lista (list): La lista de héroes en forma de diccionarios.
    - key (str): La clave del dato que se quiere sumar en cada héroe.

    Returns:
    - suma (float): La sumatoria del dato específico en todos los héroes de la lista.
    """
    suma = 0
    for e_lista in lista:
        if isinstance(e_lista, dict):
            dato = e_lista.get(key)
            if dato is not None:
                if isinstance(dato, (int, float)):
                    suma += dato
    return suma

#______________________________________________________________________________

# 4.2 Crear la función ‘dividir’ la cual recibirá como parámetro dos números
# (dividendo y divisor). Se debe verificar si el divisor es 0, en caso de serlo, retornar
# False, caso contrario realizar la división entre los parámetros y retornar el resultado

def dividir(dividendo:int,divisor:int):#devuelve el resultadod e la divicion
    """
    Realiza la división de dos números enteros y retorna el resultado.

    Args:
    - dividendo (int): El número que se va a dividir.
    - divisor (int): El número por el cual se va a dividir el dividendo.

    Returns:
    - resultado (float): El resultado de la división si el divisor no es cero, de lo contrario retorna False.
    """
    resustado = 0
    if divisor == 0:
        return False
    elif divisor != 0:
        resustado = dividendo / divisor
    return resustado

#_____________________________________________________________________________

# 4.3 Crear la función ‘calcular_promedio’ la cual recibirá como parámetro una lista de
# héroes y un string que representa el dato del héroe que se requiere calcular el
# promedio. La función debe retornar el promedio del dato pasado por parámetro
# IMPORTANTE: hacer uso de las las funciones creadas en los puntos 4.1 y 4.2

def calcular_promedio(lista:list,key:str):#devolvera el promedo del dato que se quiera sacar
    """
    Calcula el promedio de un dato específico de los héroes en la lista.
    
    Args:
    - lista (list): La lista de héroes en forma de diccionarios.
    - key (str): La clave del dato del héroe del cual se quiere calcular el promedio.

    Returns:
    - promedio (float): El promedio del dato específico en todos los héroes de la lista.
    """
    promedio = 0
    cantida = 0
    sumatoria = sumar_dato_heroe(lista,key)
    for e_lista in lista:
        for e_dic in e_lista:
            if e_dic == key:
                cantida += 1
    promedio = dividir(sumatoria,cantida)
    return promedio

#______________________________________________________________________________

# 4.4 Crear la función ‘mostrar_promedio_dato’ la cual recibirá como parámetro una
# lista de héroes y un string que representa la clave del dato
# ● Se debe validar que el dato que se encuentra en esa clave sea de tipo int o
# float. Caso contrario retornaria False
# ● Se debe validar que la lista a manipular no esté vacía , en caso de que esté
# vacía se retornaria también False


def mostrar_promedio_dato(lista:list,key:str):#devuelve si la lista esta vacia o  que la key no sea entero o float
    """
    Verifica si la lista no está vacía y si el dato en la clave especificada es de tipo int o float.

    Args:
    - lista (list): La lista de héroes en forma de diccionarios.
    - key (str): La clave del dato que se quiere verificar en cada héroe.

    Returns:
    - False si la lista está vacía o el dato en la clave no es de tipo int o float, de lo contrario, no retorna nada.
    """
    if lista == [""]:
        return False
    else:
        for e_lita in lista:
            if e_lita[key].isalpha():
                return False
#____________________________________________________________

# 5.1 Crear la función "imprimir_menu" que imprima el menú de opciones por pantalla,
# el cual permite utilizar toda la funcionalidad ya programada.

def imprimir_menu():
    """
    Imprime un menú de opciones en pantalla.
    """
    print("1\n2\n3\n4\n5\n6\n7\n8\n9\n0")

#_________________                  ______________________________          _____________________________         ____________________

#Crear la función “validar_entero” la cual recibirá por parámetro un string de
# número el cual deberá verificar que sea sea un string conformado únicamente por
# dígitos. Retornara True en caso de serlo, False caso contrario

def validar_entero(string:str):#valida  que el string ingresado sea solo digitos
    """
    Verifica si un string contiene solo dígitos.

    Args:
    - string (str): El string que se quiere verificar.

    Returns:
    - True si el string contiene solo dígitos, False de lo contrario.
    """
    if string.isdigit():
        return True
    else:
        return False

#________________________________________________________________________________________________________________________________

# 5.3 Crear la función 'stark_menu_principal' la cual se encargará de imprimir el menú
# de opciones y le pedirá al usuario que ingrese el número de una de las opciones
# elegidas y deberá validarlo. En caso de ser correcto dicho número, lo retornara
# casteado a int , caso contrario retorna False. Reutilizar las funciones del ejercicio 5.1
# y 5.2

def stark_menu_principal():
    """
    Imprime el menú principal y valida la entrada del usuario.

    Returns:
    - int: El número ingresado por el usuario si es un número válido, False de lo contrario.
    """
    imprimir_menu()
    n_ingresado = input("ingrese un numero ")
    if validar_entero(n_ingresado):
        return int(n_ingresado)
    else:
        return False

# 6.Crear la función stark_marvel_app la cual recibirá por parámetro la lista de héroes
# y se encargará de la ejecución principal de nuestro programa.
# Utilizar if/elif o match según prefiera. Debe informar por consola en caso de
# seleccionar una opción incorrecta y volver a pedir el dato al usuario. Reutilizar las
# funciones con prefijo stark_ donde crea correspondiente.

def stark_marvel_app(lista:list):
    """
    Función principal que ejecuta el programa y controla el flujo de las opciones del menú.

    Args:
    - lista (list): La lista de héroes en forma de diccionarios.

    Notes:
    - Esta función hace uso de varias funciones previamente definidas.

    """
    while True:
        opcion = stark_menu_principal()
        while opcion == False:  
            print("ERROR INGRESE DE EL DATO VUELTA")
            opcion = stark_menu_principal()
        match opcion:
            case 1:
                print(stark_normalizar_datos(lista))
            case 2:
                print(stark_imprimir_heroes(lista))
            case 3:
                break
# 7. Una vez realizadas y probadas las funciones resolver en un menú los siguientes
# puntos del desafio anterior.
# A. Normalizar datos (No se debe poder acceder a los otros puntos)
# B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
# género NB
# C. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
# D. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
# E. Recorrer la lista y determinar cuál es el superhéroe más débil de género M
# F. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB
# G. Recorrer la lista y determinar la fuerza promedio de los superhéroes de
# género NB
# H. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
# I. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
# J. Listar todos los superhéroes agrupados por color de ojos.
# K. Listar todos los superhéroes agrupados por tipo de inteligencia

normalizado = False  # Variable para controlar si los datos están normalizados

while True:
    opcion = stark_menu_principal()
    while opcion == False:  
        print("ERROR INGRESE UN DATO VÁLIDO")
        opcion = stark_menu_principal()

    if opcion == 1:
        if not normalizado:
            normalizado = stark_normalizar_datos(lista_personajes)
            if normalizado:
                print("Datos Normalizados")
            else:
                print("Hubo un error al normalizar los datos. Verifique que la lista no esté vacía o que los datos no se hayan normalizado anteriormente.")
        else:
            print("Los datos ya han sido normalizados previamente.")
    
    elif opcion == 2:
        if not normalizado:
            print("Debe normalizar los datos primero (opción A).")
        else:
            for personaje in lista_personajes:
                if personaje["genero"] == "NB":
                    print(f"Nombre: {personaje['nombre']}")
        
    elif opcion == 3:
        if not normalizado:
            print("Debe normalizar los datos primero (opción A).")
        else:
            superheroe_mas_alto_F = f_mas_alta(lista_personajes)
            if superheroe_mas_alto_F:
                print(f"El superhéroe más alto de género F es: {superheroe_mas_alto_F['nombre']} con una altura de {superheroe_mas_alto_F['altura']} cm.")
    
    elif opcion == 4:
        if not normalizado:
            print("Debe normalizar los datos primero (opción A).")
        else:
            superheroe_mas_alto_M = m_mas_alta(lista_personajes)
            if superheroe_mas_alto_M:
                print(f"El superhéroe más alto de género M es: {superheroe_mas_alto_M['nombre']} con una altura de {superheroe_mas_alto_M['altura']} cm.")
            else:
                print("No se encontraron superhéroes de género M.")
    
    elif opcion == 5:
        if not normalizado:
            print("Debe normalizar los datos primero (opción A).")
        else:
            superheroe_mas_debil_M = m_mas_debil(lista_personajes)
            if superheroe_mas_debil_M:
                print(f"El superhéroe más débil de género M es: {superheroe_mas_debil_M['nombre']} con una fuerza de {superheroe_mas_debil_M['fuerza']}.")
            else:
                print("No se encontraron superhéroes de género M.")
    
    elif opcion == 6:
        if not normalizado:
            print("Debe normalizar los datos primero (opción A).")
        else:
            superheroe_mas_debil_NB = nb_mas_debil(lista_personajes)
            if superheroe_mas_debil_NB:
                print(f"El superhéroe más débil de género NB es: {superheroe_mas_debil_NB['nombre']} con una fuerza de {superheroe_mas_debil_NB['fuerza']}.")
            else:
                print("No se encontraron superhéroes de género NB.")
    
    elif opcion == 7:
        if not normalizado:
            print("Debe normalizar los datos primero (opción A).")
        else:
            fuerza_promedio_NB = calcular_promedio(lista_personajes, "fuerza")
            if fuerza_promedio_NB:
                print(f"La fuerza promedio de los superhéroes de género NB es: {fuerza_promedio_NB}")
            else:
                print("No se encontraron superhéroes de género NB.")

    
    elif opcion == 8:
        if not normalizado:
            print("Debe normalizar los datos primero (opción A).")
        else:
            color_de_ojos = contador_color_ojos(lista_personajes)
            if color_de_ojos:
                for color, cantidad in color_de_ojos.items():
                    print(f"Hay {cantidad} superhéroes con color de ojos {color}.")
                else:
                    print("No se encontraron datos de color de ojos.")
    
    elif opcion == 9:
        if not normalizado:
            print("Debe normalizar los datos primero (opción A).")
        else:
            color_de_pelo = contador_color_pelo(lista_personajes)
            if color_de_pelo:
                for color, cantidad in color_de_pelo.items():
                    print(f"Hay {cantidad} superhéroes con color de pelo {color}.")
                else:
                    print("No se encontraron datos de color de pelo.")
    
    elif opcion == 10:
        if not normalizado:
            print("Debe normalizar los datos primero (opción A).")
        else:
            superheroes_por_color_ojos = agrupacio_superheroes_ojos(lista_personajes)
            if superheroes_por_color_ojos:
                for color, superheroes in superheroes_por_color_ojos.items():
                    print(f"Superhéroes con color de ojos {color}:")
                    for heroe in superheroes:
                        print(f"Nombre: {heroe['nombre']}")
                else:
                    print("No se encontraron datos de color de ojos.")
    
    elif opcion == 11:
        if not normalizado:
            print("Debe normalizar los datos primero (opción A).")
        else:
            superheroes_por_inteligencia = agrupacion_por_inteligencia(lista_personajes)
            if superheroes_por_inteligencia:
                for inteligencia, superheroes in superheroes_por_inteligencia.items():
                    print(f"Superhéroes con inteligencia {inteligencia}:")
                    for heroe in superheroes:
                        print(f"Nombre: {heroe['nombre']}")
                else:
                    print("No se encontraron datos de tipo de inteligencia.")
    
    elif opcion == 0:
        break
    
    else:
        print("Opción no válida. Por favor, ingrese un número del 1 al 11.")