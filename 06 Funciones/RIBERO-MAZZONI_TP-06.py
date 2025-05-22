# Trabajo Práctico N°6 - Funciones

# 1) Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el programa principal.

def imprimir_hola_mundo():
  print("Hola Mundo!")
  
imprimir_hola_mundo()

# 2) Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado. Por ejemplo, si se llama con saludar_usuario ("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa principal solicitando el nombre al usuario.

def saludar_usuario(nombre):
  return f"Hola {nombre}!"

nombre = input("Ingresa tu nombre: ")

print(saludar_usuario(nombre))

# 3) Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.

def informacion_personal(nombre, apellido, edad, residencia):
  return f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}."

nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = input("Ingresa tu edad: ")
residencia = input("Ingresa tu lugar de residencia: ")

print(informacion_personal(nombre, apellido, edad, residencia))

# 4) Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

from math import pi

def calcular_area_circulo(radio):
  area = pi * radio * radio
  return area

def calcular_perimetro_circulo(radio):
  perimetro = 2 * pi * radio
  return perimetro

radio = float(input("Ingresa el radio del círculo: "))

print(f"El área del círculo es {calcular_area_circulo(radio):.2f}m2 y su perímetro {calcular_perimetro_circulo(radio):.2f}m.")

# 5) Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

def segundos_a_horas(segundos):
  horas = segundos / 60 / 60
  return horas

segundos = int(input("Ingresa la cantidad de segundos: "))

print(f"{segundos} segundos equivalen a {segundos_a_horas(segundos):.2f} horas.")

# 6) Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro e imprima la tabla de multiplicar de ese número del 1 al 10. Pedir al usuario el número y llamar a la función.

def leer_entero_validado(mensaje, min = float("-Inf"), max = float("Inf")):
    numero = int(input(f"{mensaje}: "))
    while numero < min or numero > max:
        numero = int(input(f"ERROR. {mensaje}: "))
    return numero

def tabla_multiplicar(numero):
  print(f"\nTabla de multiplicar del {numero}:")
  for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

numero = leer_entero_validado("Ingresa un número entero positivo", 1)

tabla_multiplicar(numero)

# 7)  Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

def leer_entero_validado(mensaje, min = float("-Inf"), max = float("Inf")):
    numero = int(input(f"{mensaje}: "))
    while numero < min or numero > max:
        numero = int(input(f"ERROR. {mensaje}: "))
    return numero

def operaciones_basicas(a, b):
  suma = a + b
  resta = a - b
  multiplicacion = a * b
  division = "Indefinida (no se puede dividir por cero)" if b == 0 else a / b
  return (suma, resta, multiplicacion, division)

a = leer_entero_validado("Ingresa un número")
b = leer_entero_validado("Ingresa otro número")

resultados = operaciones_basicas(a, b)

print(f"\nResultados de las operaciones entre {a} y {b}:")
print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]}")

# 8) Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

def leer_flotante_validado(mensaje, min = float("-Inf"), max = float("Inf")):
    numero = float(input(f"{mensaje}: "))
    while numero < min or numero > max:
        numero = float(input(f"ERROR. {mensaje}: "))
    return numero

def calcular_imc(peso, altura):
  imc = peso / (altura * altura)
  return imc

peso = leer_flotante_validado("Ingresa tu peso en kilogramos", 1)
altura = leer_flotante_validado("Ingresa tu altura en metros", 1)

print(f"Tu IMC es {calcular_imc(peso, altura):.2f}.")

# 9) Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el  resultado usando la función.

def leer_flotante_validado(mensaje, min = float("-Inf"), max = float("Inf")):
    numero = float(input(f"{mensaje}: "))
    while numero < min or numero > max:
        numero = float(input(f"ERROR. {mensaje}: "))
    return numero

def celsius_a_fahrenheit(celsius):
  fahrenheit = (celsius * 9/5) + 32
  return fahrenheit

celsius = leer_flotante_validado("Ingresa la temperatura en °C", 0)

print(f"La temperatura de {celsius}°C equivale a {celsius_a_fahrenheit(celsius):.2f}°F.")

# 10) Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos. Solicitar los números al usuario y mostrar el resultado usando esta función.

def leer_entero_validado(mensaje, min = float("-Inf"), max = float("Inf")):
    numero = int(input(f"{mensaje}: "))
    while numero < min or numero > max:
        numero = int(input(f"ERROR. {mensaje}: "))
    return numero

def calcular_promedio(a, b, c):
  promedio = (a + b + c) / 3
  return promedio

a = leer_entero_validado("Ingresa la primer nota", 1, 10)
b = leer_entero_validado("Ingresa la segunda nota", 1, 10)
c = leer_entero_validado("Ingresa la tercer nota", 1, 10)

print(f"El promedio de las notas ingresadas es {calcular_promedio(a, b, c):.2f}.")