'''Pedir al usuario que ingrese los datos de 5 alumnos y guardarlos en sus
respectivas listas. Validar el ingreso de datos según su criterio.
Datos:
nombre, sexo (f/m), nota (validar).
Una vez cargados los datos:
Mostrar el nombre del hombre con nota más baja
Mostrar el promedio de notas de las mujeres'''



nombres = ["Juan","Pedro","Sol","Paco","Ana"]
sexo = ["m","m","f","m","f"]
notas = [6,8,10,8,5]

nota_min = None
acumulador_notas_mujeres = 0
contador_mujeres = 0 

for _ in range(5):
    nombre = input('Ingrese el nombre del alumno')
    while nombre.isdigit():
        nombre = input('Ingrese un nombre valido')

    genero = input('Ingrese el genero del alumno (f/m)')
    while genero not in ['f', 'm']:
        genero = input('Ingrese un genero valido (f/m)')

    nota = input('Ingrese la nota del alumno')
    while nota.isalpha():
        nota = input('Ingrese una nota valida(caracter numerico)')
    while int(nota) < 0:
        nota = input('Ingrese una nota de mayor o igual a 0')

    nombres.append(nombre)
    sexo.append(genero)
    notas.append(nota)

    print('alumno cargado con exito')
# Mostrar el nombre del hombre con nota más baja
for i in range(len(nombres)):

    if nota_min is None or (notas[i] < nota_min):
        nota_min = notas[i]
        nombre_min = nombres[i]

    if sexo[i] == 'f':
        acumulador_notas_mujeres += notas[i]
        contador_mujeres += 1 

print(f'El nombre del alumno con menor nota es {nombre_min}')

# Mostrar el promedio de notas de las mujeres
promedio_notas_mujeres = acumulador_notas_mujeres / contador_mujeres

print(f'El promedio de las notas de las mujeres es: {promedio_notas_mujeres}')

