'''Ejercicio 1:
Pedir el nombre y el sueldo, incrementarle un 10% e informar el aumento de su
sueldo para esa persona.'''

nombre = input("Ingrese el nombre: ")
sueldo = float(input("Ingrese el sueldo: "))

aumento = sueldo * 0.10
nuevo_sueldo = sueldo + aumento

print(f"¡Hola {nombre}! Tu nuevo sueldo es ${nuevo_sueldo:.2f}, con un aumento de ${aumento:.2f}.")
