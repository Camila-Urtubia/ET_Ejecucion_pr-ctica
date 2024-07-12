from scipy.stats import gmean
# Importamos para poder crear números aleatorios:
import random
# Asignamos el valor mínimo (a) y el máximo (b):
a = 300000
b = 2500000



# Creamos una lista para almacenas únicamente los valores de sueldos:
valores = []
# Creamos diccionario para almacenar los números aleatorios que nos dieron junto a tu empleado por orden de vuelta:
sueldos = {}
# Agregamos la lista con nuestros empleados:
trabajadores = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez", "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]
# Creamos la lista final en donde se encuentran nuestros empleados junto a sus sueldos:
sueldo_trabajadores = []



# Creamos la función para generar los números aleatorios:
def asignar_sueldos():
 # Creamos un contador para que cada empleado quede con un solo sueldo:
 vuelta = 0
 for i in trabajadores:
     # Almacenamos los números aleatorios en una variable:
     aleatorio = random.randint(a, b)
     # Guardamos nuestro número aleatorio en nuestra lista "valores":
     valores.append(aleatorio)
     # Guardamos los trabajadores con su respectivo sueldo:
     sueldos[trabajadores[vuelta]] = aleatorio
     # Agregamos un valor al contador para que no se repitan los empleados ni el sueldo:
     vuelta = vuelta + 1

# Agregamos nuestros datos de empleados en nuestra lista final:
 sueldo_trabajadores.append(sueldos)
 print()
 print("Empleado                    Sueldo")
 print()
 # Imprimimos los empleados junto a su sueldo correspondiente:
 for i in sueldo_trabajadores:
     for clave, valor in i.items():
         print(f"{clave}                 ${valor}")



# Creamos la función para clasificar a los empleados según su sueldo:
def clasificar():
 print()
 print(f"Sueldos menores a $800.000")
 print()
 print("Nombre empleado               Sueldo")
 # Recorremos los datos guardados en nuestra lista final: 
 for i in sueldo_trabajadores:
     # En este caso "clave" serían los nombres de los empleados y "valor" su sueldo:
     for clave, valor in i.items():
         # Aplicamos una condición: si su sueldo es menor que 800.000 se verán reflejados en esta sección:
         if valor < 800000:
          print(f"{clave}               ${valor}")

 print()
 print(f"Sueldos entre a $800.000 y $2.000.000")
 print()
 print("Nombre empleado               Sueldo")

 for i in sueldo_trabajadores:
     for clave, valor in i.items():
         # Aplicamos una condición: si su sueldo es mayor que 800.000 pero menor que 2.000.000 se verán reflejados en esta sección:
         if valor > 800000 and valor < 2000000:
          print(f"{clave}               ${valor}")
 print()
 print(f"Sueldos superiores a $2.000.000")
 print()
 print("Nombre empleado               Sueldo")

 for i in sueldo_trabajadores:
     for clave, valor in i.items():
         # Aplicamos una condición: si su sueldo es mayor que 2.000.000 se verán reflejados en esta sección:
         if valor > 2000000:
          print(f"{clave}               ${valor}")



# Creamos la función para averigüar el sueldo más bajo:
def sueldo_más_bajo():
 print()
 # Ordenamos los sueldos de menor a mayor:
 valores.sort()
 # Le asignamos una variable al primer sueldo que se encuentra en la lista ordenada:
 menor = valores[0]

 for i in sueldo_trabajadores:
     for clave, valor in i.items():
         # Aplicamos una condición: Si el sueldo es igual al sueldo menor, se mostrará al respectivo empleado:
         if valor == menor:
            print(f"El sueldo más bajo es de ${valor}, y es del empleado {clave}")



# Creamos la función para averigüar el sueldo más alto:
def sueldo_más_alto():
 print()
 # Ordenamos nuestros sueldos de menor a mayor:
 valores.sort()
 # Y luego invertimos la lista, quedándonos de mayor a menor:
 valores.reverse()
 # Al primer valor de la lista (que vendría siendo el mayor) lo guardamos en una variable:
 mayor = valores[0]

 for i in sueldo_trabajadores:
     for clave, valor in i.items():
         # Aplicamos una condición: Si el sueldo es igual al sueldo mayor, se mostrará al respectivo empleado:
         if mayor == valor:
            print(f"El sueldo más alto es de ${valor}, y es del empleado {clave}")



# Creamos la función para encontrar el promedio de todos los sueldos:
def promedio_de_sueldos():
   # Almacenamos la suma de toda nuestra lista que solo contiene nuestros sueldos en una variable:
   suma = sum(valores)
   # Almacenamos la división de nuestro valor anterior para finalmente encontrar el promedio:
   promedio = suma / 10
   print()
   print(f"El promedio total de todos los sueldos es de: ${promedio}")



# Creamos la función para la media geométrica:
def media_geométrica():
 from scipy.stats import gmean
 # Colocamos la lista en donde solo se encuentran los sueldos:
 mediag = gmean(valores)
 print()
 print(f"La media geométrica es: {mediag}")
 print()



# Creamos la función para el reporte de sueldos:
def reporte_de_sueldos():
 print("Nombre empleado       Sueldo Base       Descuento salud         Decuento AFP        Sueldo liquido")
 for i in sueldo_trabajadores:
     for clave, valor in i.items():
        # Encontramos el 7 % del sueldo fijo y lo almacenamos en una variable:
        descuento = (valor * 7) / 100
        # Encontramos el 12 % del sueldo fijo y lo almacenamos en una variable:
        descuento_afp = (valor * 12) / 100
        # Encontramos el valor final que quedaría luego de aplicar los descuentos anteriores:
        liquido = valor - descuento - descuento_afp
        print(f"{clave}            ${valor}            ${descuento}           ${descuento_afp}         ${liquido}")
 


# Creamos la función de nuestro menú:
def menu():
 print("Menú Principal")
 while True:
    print("1. Asignar sueldos aleatorios. ")
    print("2. Clasificar sueldos. ")
    print("3. Ver estadísticas. ")
    print("4. Reporte de sueldos. ")
    print("5. Salir del Programa.")
    op = (int(input("Ingrese la opción que desea realizar: ")))
    print()

    if op == 1:
        # Para que los valores no se vayan agrupando, borramos las listas si el usuario desea generar nuevamente sueldos aleatorios:
        valores.clear()
        sueldo_trabajadores.clear()
        print()
        print("¡Sueldos asignados con éxito!")
        asignar_sueldos()
        print()
        print()
 
    elif op == 2:
       print()
       # Aplicamos una condición: Si nuestros sueldos ya fueron generados, podremos acceder a esta opción:
       if valores:
        print()
        clasificar()
        print()
        print()
        print()
       # De lo contrario: nos mostrará un mensaje:
       else:
          print("¡Aún no se han asignado los sueldos!")
          print()

    elif op == 3:
     # Aplicamos una condición: Si nuestros sueldos ya fueron generados, podremos acceder a esta opción:
     if valores: 
        print()
        print("Seleccione una opción: ")
        print("1. Sueldo más alto.")
        print("2. Sueldo más bajo.")
        print("3. Promedio de sueldos. ")
        print("4. Media geométrica ")
        reporte = int(input())

        if reporte == 1:
             sueldo_más_alto()
             print()

        elif reporte == 2:
             sueldo_más_bajo()
             print()

        elif reporte == 3:
             promedio_de_sueldos()
             print()

        elif reporte == 4:
             media_geométrica()

     # De lo contrario: nos mostrará un mensaje:
     else:
        print("¡Los sueldos aún no han sido asignados!") 


    elif op == 4:
       if valores: 
        print()
        reporte_de_sueldos()
        print()
        print()
       else:
          print("¡Aún no se generan los sueldos!")
          print()

    elif op == 5:
       print("Finalizando programa...")
       print("Desarrollado por Camila Urtubia")
       print("RUT 21.755.406-3")
       break

# Llamamos al menú:
menu()