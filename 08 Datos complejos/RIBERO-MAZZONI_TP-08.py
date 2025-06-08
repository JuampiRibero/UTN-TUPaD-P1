# Trabajo Práctico N°8 - Datos Complejos

# 1) Dado el diccionario precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}. Añadir las siguientes frutas con sus respectivos precios: Naranja = 1200, Manzana = 1500, Pera = 2300.

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)

# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, actualizar los precios de las siguientes frutas: Banana = 1330, Manzana = 1700, Melón = 2800.

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)

# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios.

print(list(precios_frutas.keys()))

# 4) Escribí un programa que permita almacenar y consultar números telefónicos. Permití al usuario cargar 5 contactos con su nombre como clave y número como valor. Luego, pedí un nombre y mostrale el número asociado, si existe.

contactos = {}

print("Cargá 5 contactos:")
for i in range(5):
  nombre = input(f"Ingresá el nombre del contacto {i+1}: ")
  numero = input(f"Ingresá el número de {nombre}: ")
  contactos[nombre] = numero

consulta = input("\nIngresá el nombre del contacto que querés buscar: ")

if consulta in contactos:
  print(f"El número de {consulta} es: {contactos[consulta]}")
else:
  print(f"No se encontró el contacto {consulta}.")

# 5) Solicita al usuario una frase e imprime. Las palabras únicas (usando un set). Un diccionario con la cantidad de veces que aparece cada palabra.

frase = input("Ingresá una frase: ")

palabras = frase.split()

palabras_unicas = set(palabras)
print(f"\nPalabras únicas:\n{palabras_unicas}")

recuento = {}

for palabra in palabras:
  if palabra in recuento:
    recuento[palabra] += 1
  else:
    recuento[palabra] = 1

print(f"\nCantidad de veces que aparece cada palabra:\n{recuento}")

# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. Luego, mostrá el promedio de cada alumno.

alumnos = {}

print("Cargá 3 alumnos:")
for i in range(3):
  nombre = input(f"Ingresá el nombre del alumno {i+1}: ")
  notas = []
  for j in range(3):
    nota = float(input(f"Ingresá la nota {j+1} de {nombre}: "))
    notas.append(nota)
  alumnos[nombre] = tuple(notas)

print("\nPromedios de los alumnos:")
for nombre, notas in alumnos.items():
  promedio = sum(notas) / len(notas)
  print(f"{nombre}: {promedio:.2f}")

# 7)  Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2. Mostrá los que aprobaron ambos parciales. Mostrá los que aprobaron solo uno de los dos. Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).

parcial_1 = {"Juan", "Luis", "Raul", "Ana"}
parcial_2 = {"Raul", "Lucía", "Ana", "Marcos"}

aprobaron_ambos_parciales = parcial_1 & parcial_2
print("Aprobaron ambos parciales:", aprobaron_ambos_parciales)

aprobaron_solo_un_parcial = parcial_1 ^ parcial_2
print("Aprobaron solo uno de los dos:", aprobaron_solo_un_parcial)

al_menos_uno = parcial_1 | parcial_2
print("Aprobaron al menos un parcial:", al_menos_uno)

# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. Permití al usuario consultar el stock de un producto ingresado, agregar unidades al stock si el producto ya existe, agregar un nuevo producto si no existe.

productos = {
  "pan": 15,
  "leche": 5,
  "huevos": 30
}

print(f"Productos actuales: {productos}")

nombre = input("\nIngresá el nombre del producto a consultar: ").lower()

if nombre in productos:
  print(f"Stock actual de '{nombre}': {productos[nombre]}")
  agregar = input("¿Querés agregar unidades al stock? (s/n): ").lower()
  if agregar == "s":
    unidades = int(input("¿Cuántas unidades querés agregar?: "))
    productos[nombre] += unidades
    print(f"Nuevo stock de '{nombre}': {productos[nombre]}")
else:
  print(f"El producto '{nombre}' no existe.")
  nuevo = input("¿Querés agregarlo como nuevo producto? (s/n): ").lower()
  if nuevo == "s":
    unidades = int(input("¿Cuántas unidades tiene?: "))
    productos[nombre] = unidades
    print(f"Producto '{nombre}' agregado con {unidades} unidades.")

print(f"\nStock final: {productos}")

# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos. Permití consultar qué actividad hay en cierto día y hora.

agenda = {
  ("lunes", "10:00"): "Reunión de equipo",
  ("martes", "14:00"): "Clase de inglés",
  ("miercoles", "16:00"): "Clase de programación I",
  ("viernes", "18:00"): "Gimnasio"
}

print("Agenda actual:")
for clave, evento in agenda.items():
  print(f"{clave[0].capitalize()} a las {clave[1]} → {evento}")

dia = input("\nIngresá el día: ").lower()
hora = input("Ingresá la hora (formato hh:mm): ")

clave = (dia, hora)

if clave in agenda:
  print(f"\nEl evento el {dia} a las {hora} es: {agenda[clave]}")
else:
  print(f"\nNo hay eventos registrados el {dia} a las {hora}.")

# 10)  Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde las capitales sean las claves, los países sean los valores.

paises = {
  "Argentina": "Buenos Aires",
  "Francia": "París",
  "Italia": "Roma",
  "Brasil": "Brasilia"
}

capitales = {}

for pais, capital in paises.items():
  capitales[capital] = pais

print(f"Diccionario invertido: {capitales}")