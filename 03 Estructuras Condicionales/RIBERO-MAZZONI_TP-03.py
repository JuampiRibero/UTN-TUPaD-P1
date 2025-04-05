# Trabajo Práctico N°3 - Estructuras Condicionales

# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad = int(input("Ingrese su edad: "))
ADULTEZ = 18

if edad >= ADULTEZ:
  print("Es mayor de edad.")

# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”.

nota = int(input("Ingrese su nota: "))
NOTA_MINIMA = 6

if nota >= NOTA_MINIMA:
  print("Aprobado.")
else:
  print("Desaprobado.")

# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.

numero = int(input("Ingrese un número: "))

if numero % 2 == 0:
  print("Ha ingresado un número par.")
else:
  print("Por favor, ingrese un número par.")

# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece: ● Niño/a: menor de 12 años. ● Adolescente: mayor o igual que 12 años y menor que 18 años. ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. ● Adulto/a: mayor o igual que 30 años.

edad = int(input("Ingrese su edad: "))

if edad < 12:
  print("Eres un niño/a.")
elif 12 <= edad < 18:
  print("Eres un adolescente.")
elif 18 <= edad < 30:
  print("Eres un adulto/a joven.")
else:
  print("Eres un adulto/a.")

# 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string.

password = input("Ingrese su contraseña: ")

longitud = len(password)

if 8 <= longitud <= 14:
  print("Ha ingresado una contraseña correcta.")
else:
  print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")

# 6) Escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

from statistics import mode, median, mean
import random

numeros_aleatorios = [random.randint(1, 100) for i in range(50)] 

moda = round(mode(numeros_aleatorios), 2)

mediana = round(median(numeros_aleatorios), 2)

media = round(mean(numeros_aleatorios), 2)

print("Lista de números:", numeros_aleatorios)

print(f"La moda es: {moda}, la mediana es: {mediana} y la media es: {media}.")

if  moda < mediana < media:
  print("Entonces hay sesgo positivo.")
elif moda > mediana > media:
  print("Entonces hay sesgo negativo.")
else:
  print("Entonces no hay sesgo.")

# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

texto_usuario = input("Ingrese una palabra o frase: ")

ultimo_caracter = texto_usuario[-1]

if (ultimo_caracter.lower() == "a") or (ultimo_caracter.lower() == "e") or (ultimo_caracter.lower() == "i") or (ultimo_caracter.lower() == "o") or (ultimo_caracter.lower() == "u"):
  print(f"{texto_usuario}!")
else:
  print(texto_usuario)

# 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee: 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), lower() y title() de Python para convertir entre mayúsculas y minúsculas.

nombre = input("Ingrese su nombre: ")
numero = int(input("Ingrese una de las siguientes opciones: \n 1. Si quiere su nombre en mayúsculas \n 2. Si quiere su nombre en minúsculas \n 3. Si quiere su nombre con la primera letra mayúscula \n"))

if numero == 1:
  print(nombre.upper())
elif numero == 2:
  print(nombre.lower())
elif numero == 3:
  print(nombre.capitalize())
else:
  print("Opción no válida.")

# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla: ● Menor que 3: "Muy leve" (imperceptible). ● Mayor o igual que 3  y menor que 4: "Leve" (ligeramente perceptible). ● Mayor o igual que 4  y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños). ● Mayor o igual que 5  y menor que 6: "Fuerte" (puede causar daños en estructuras débiles). ● Mayor o igual que 6  y menor que 7: "Muy Fuerte" (puede causar daños significativos). ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

magnitud_terremoto = int(input("Ingrese la magnitud del terremoto: "))

if magnitud_terremoto < 3:
  print("Muy leve (imperceptible).")
elif 3 <= magnitud_terremoto < 4:
  print("Leve (ligeramente perceptible).")
elif 4 <= magnitud_terremoto < 5:
  print("Moderado (sentido por personas, pero generalmente no causa daños).")
elif 5 <= magnitud_terremoto < 6:
  print("Fuerte (puede causar daños en estructuras débiles).")
elif 6 <= magnitud_terremoto < 7:
  print("Muy Fuerte (puede causar daños significativos).")
else:
  print("Extremo (puede causar graves daños a gran escala).")

# 10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano.

hemisferio = input("¿En qué hemisferio estás? (N/S): ").upper()
mes = int(input("¿En qué mes estamos? (1-12): "))
dia = int(input("¿Qué día del mes es hoy? (1-31): "))

if hemisferio == "N":
    if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
        print("Estás en Invierno.")
    elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
        print("Estás en Primavera.")
    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
        print("Estás en Verano.")
    elif (mes == 9 and dia >= 21) or (mes == 10) or (mes == 11) or (mes == 12 and dia <= 20):
        print("Estás en Otoño.")
    else:
        print("Fecha inválida.")
elif hemisferio == "S":
    if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
        print("Estás en Verano.")
    elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
        print("Estás en Otoño.")
    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
        print("Estás en Invierno.")
    elif (mes == 9 and dia >= 21) or (mes == 10) or (mes == 11) or (mes == 12 and dia <= 20):
        print("Estás en Primavera.")
    else:
        print("Fecha inválida.")
else:
    print("Hemisferio inválido.")