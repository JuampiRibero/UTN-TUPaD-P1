# Trabajo Práctico N°7 - Recursividad

import sys

sys.setrecursionlimit(20000)

# 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa función para calcular y mostrar en pantalla el factorial de todos los números enteros entre 1 y el número que indique el usuario.

def factorial(x):
  if x == 0:
    return 1
  else:
    return x * factorial(x - 1)

num = int(input("Ingresa un número entero positivo: "))

for i in range(1, num + 1):
    print(f"Factorial de {i} es {factorial(i)}")

# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.

def fibonacci(pos):
  if pos == 0:
    return 0
  elif pos == 1:
    return 1
  else:
    return fibonacci(pos - 1) + fibonacci(pos - 2)
  
num = int(input("Ingresa la posición hasta la que deseas ver la serie de Fibonacci: "))

print("Serie de Fibonacci:")
for i in range(num + 1):
    print(f"F({i}) = {fibonacci(i)}")

# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, utilizando la fórmula 𝑛𝑚 = 𝑛 ∗ 𝑛(𝑚−1). Prueba esta función en un algoritmo general.

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

base = float(input("Ingresa la base: "))
exponente = int(input("Ingresa el exponente (entero no negativo): "))

resultado = potencia(base, exponente)
print(f"{base}^{exponente} = {resultado}")

# 4) Crear una función recursiva en Python que reciba un número entero positivo en base decimal y devuelva su representación en binario como una cadena de texto.

def decimal_a_binario(num):
    if num == 0:
        return ""
    else:
        return decimal_a_binario(num // 2) + str(num % 2)

num = int(input("Ingresa un número entero positivo: "))

if num == 0:
    print("El número binario es: 0")
else:
    binario = decimal_a_binario(num)
    print(f"El número {num} en binario es: {binario}")

# 5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es.

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])
  
texto = input("Ingresa una palabra sin espacios ni tildes: ").lower()

if es_palindromo(texto):
    print("Es un palíndromo.")
else:
    print("No es un palíndromo.")

# 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo y devuelva la suma de todos sus dígitos.

def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)

num = int(input("Ingresá un número entero positivo: "))

if num > 0:
    resultado = suma_digitos(num)
    print(f"La suma de los dígitos de {num} es: {resultado}")
else:
    print("Por favor, ingresá un número entero positivo mayor que cero.")

# 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al último nivel con un solo bloque. Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el nivel más bajo y devuelva el total de bloques que necesita para construir toda la pirámide.

def contar_bloques(num):
    if num == 1:
        return 1
    else:
        return num + contar_bloques(num - 1)

nivel = int(input("Ingresá la cantidad de bloques del nivel más bajo: "))

if nivel > 0:
    total = contar_bloques(nivel)
    print(f"Para construir la pirámide se necesitan {total} bloques en total.")
else:
    print("Por favor, ingresá un número entero positivo.")

# 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces aparece ese dígito dentro del número.

def contar_digito(num, digito):
    if num == 0:
        return 0
    else:
        ultimo_digito = num % 10
        suma_actual = 1 if ultimo_digito == digito else 0
        return suma_actual + contar_digito(num // 10, digito)
      
num = int(input("Ingrese un número entero positivo: "))

digito = int(input("Ingrese un dígito entre 0 y 9: "))

if 0 <= digito <= 9 and num >= 0:
    resultado = contar_digito(num, digito)
    print(f"El dígito {digito} aparece {resultado} veces en el número {num}.")
else:
    print("Error: Debe ingresar un número entero positivo y un dígito entre 0 y 9.")