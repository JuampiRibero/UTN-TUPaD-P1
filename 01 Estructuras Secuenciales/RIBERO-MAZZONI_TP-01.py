# Trabajo Práctico N°1 - Estructuras Secuenciales

# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.

print("Hola Mundo!\n")

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.

nombre = input("Por favor ingrese su nombre: ")
print(f"Hola {nombre}!\n")

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.

nombre = input("Por favor ingrese su nombre: ")
apellido = input("Por favor ingrese su apellido: ")
edad = int(input("Por favor ingrese su edad: "))
residencia = input("Por favor ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}\n")

# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.

radio = float(input("Por favor ingrese el radio del círculo: "))
pi = 3.14159
area = pi * radio * radio
perimetro = 2 * pi * radio
print(f"El área del circulo es {area}, mientras que su perímetro es {perimetro}\n")

# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.

segundos = int(input("Por favor ingrese la cantidad de segundos: "))
horas = segundos / 60 / 60
print(f"La cantidad de {segundos} seg, equivale a {horas} hs\n")

# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.

numero = int(input("Por favor ingrese un número: "))
print(f"{numero} x 1 = {numero * 1}")
print(f"{numero} x 2 = {numero * 2}")
print(f"{numero} x 3 = {numero * 3}")
print(f"{numero} x 4 = {numero * 4}")
print(f"{numero} x 5 = {numero * 5}")
print(f"{numero} x 6 = {numero * 6}")
print(f"{numero} x 7 = {numero * 7}")
print(f"{numero} x 8 = {numero * 8}")
print(f"{numero} x 9 = {numero * 9}")
print(f"{numero} x 10 = {numero * 10}\n")

# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

numero1 = int(input("Por favor ingrese un número entero distinto de cero: "))
numero2 = int(input("Por favor ingrese otro número entero distinto de cero: "))
suma = numero1 + numero2
division = (numero1 / numero2)
multiplicacion = numero1 * numero2
resta = numero1 - numero2
print(f"{numero1} + {numero2} = {suma}")
print(f"{numero1} / {numero2} = {division}")
print(f"{numero1} * {numero2} = {multiplicacion}")
print(f"{numero1} - {numero2} = {resta}\n")

# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente modo: IMC = peso en kg / (altura en m * altura en m)

altura = float(input("Por favor ingrese su altura en metros: "))
peso = float(input("Por favor ingrese su peso en kg: "))
imc = peso / altura ** 2
print(f"El IMC es de {imc}\n")

# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia: Temperatura en Fahrenheint = (9/5) * Temperatura en Celcius + 32

temp = float(input("Por favor ingrese la temperatura en Celcius: "))
tempEquivalente = (9/5) * temp + 32
print(f"La temperatura de {temp}°C, equivale a {tempEquivalente}°F\n")

#  10) Crear un programa que pida al usuario  3 números e imprima por pantalla el promedio de dichos números.

numero1 = float(input("Por favor ingrese un número: "))
numero2 = float(input("Por favor ingrese otro número: "))
numero3 = float(input("Por favor ingrese otro número: "))
promedio = (numero1 + numero2 + numero3) / 3
print(f"El promedio de los 3 números ingresados es {promedio}")