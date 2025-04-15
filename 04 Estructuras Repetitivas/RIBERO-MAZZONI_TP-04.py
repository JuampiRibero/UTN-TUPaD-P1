# Trabajo Práctico N°4 - Estructuras Repetitivas

# 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for i in range(0, 101):
  print(i)

# 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.

numero = int(input("Ingrese un número entero: "))

absoluto = abs(numero)

if numero == 0:
  cantidad_digitos = 1
else:
  cantidad_digitos = 0
  while absoluto > 0:
    absoluto //= 10
    cantidad_digitos += 1

print(f"El número {numero} tiene {cantidad_digitos} dígitos.")

# 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.

num1 = int(input("Ingrese un número entero: "))
num2 = int(input("Ingrese otro número entero: "))

inicio = min(num1, num2) + 1
fin = max(num1, num2)

suma = 0

for i in range(inicio, fin):
  suma += i
print(f"La suma de los número comprendidos entre {min(num1, num2)} y {max(num1, num2)}, excluyendolos, es {suma}.")

# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

numero = int(input("Ingrese un número entero: "))

suma = 0

while numero != 0:
  suma += numero
  numero = int(input("Ingrese un número entero: "))

print(f"La suma de los números ingresados es {suma}.")

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random

aleatorio = random.randint(0, 9)

intentos = 1

numero = int(input("Ingrese un número entero entre 0 y 9: "))

while numero != aleatorio:
  print("¡Intetalo de nuevo!")
  numero = int(input("Ingrese un número entero: "))
  intentos += 1

print(f"¡Adivinaste! El número era el {numero}. Lo hiciste con {intentos} intentos.")

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.

for i in range(100, -1, -2):
  print(i)

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.

numero = int(input("Ingrese un número entero positivo: "))

inicio = 0
fin = numero

suma = 0

for i in range(inicio, fin+1):
  suma += i
print(f"La suma de los número comprendidos entre {inicio} y {fin}, incluyéndolos es {suma}.")

# 8)  Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).

pares = 0
impares = 0
negativos = 0
positivos = 0

cantidad_numeros = 100

for i in range(cantidad_numeros):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    if numero < 0:
        negativos += 1
    elif numero > 0:
        positivos += 1

print(f"Cantidad de números pares: {pares}.")
print(f"Cantidad de números impares: {impares}.")
print(f"Cantidad de números negativos: {negativos}.")
print(f"Cantidad de números positivos: {positivos}.")

# 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).

cantidad_numeros = 100

suma = 0

for i in range(cantidad_numeros):
  numero = int(input(f"Ingrese el número {i + 1}: "))
  suma += numero
  
media = round((suma/cantidad_numeros), 2)

print(f"La media de los números ingresados es {media}.")

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero = input("Ingrese un número: ")

numero_invertido = ""

indice = len(numero) - 1

for i in range(indice, -1, -1):
    numero_invertido += numero[i]

print(f"El número invertido es: {numero_invertido}.")