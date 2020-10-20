"""
En ocasiones, tenemos que repetir varias veces una determinada tarea hasta
conseguir nuestro objetivo. En Python esto se realiza con el comando while.
A modo de ejemplo while en Python se usa así:
"""
print("Ejemplo 1 while en python"+".\n")
vuelta = 1
while vuelta < 10:
    print("Vuelta " + str(vuelta))
    vuelta += 1

"""
for en Python

En ocasiones, tenemos que repetir varias veces una determinada tarea hasta conseguir 
nuestro objetivo. En Python esto se realiza con el comando for. A modo de ejemplo 
for en Python se usa así:
"""

print("Ejemplo 1 for en python"+".\n")

for vuelta in range(1,10): #Comienza desde el 1 al 10
    print("Vuelta "+str(vuelta))

#for se puede utilizar con cualquier objeto con el que se pueda iterar
# (ir saltando de elemento en elemento),
# como verás en este ejemplo con una lista:

print("Ejemplo 2 for en python"+".\n")
coches = ("Ferrari", "Tesla", "BMW", "Audi")
for coche in coches:
    print(coche)

#Si lo combinas con la función enumerate, además irá dándole un número a cada elemento:

print("Ejemplo 3 con enumerate for en python"+".\n")
Coches = ('Ferrari', 'Tesla', 'BMW', 'Audi')
for i, Coches in enumerate(Coches):
    print(str(i) + " - "+ Coches)

"""
Bucle ‘while’ controlado por Conteo

A continuación, se presenta un ejemplo del uso del bucle while controlado por conteo:
"""

suma, numero = 0, 1

while numero <= 10:
    suma = numero + suma
    numero = numero + 1
print ("La suma es " + str(suma))

"""
En este ejemplo tiene un contador con un valor inicial de cero, cada iteración del while 
manipula esta variable de manera que incremente su valor en 1, por lo que después de su 
primera iteración el contador tendrá un valor de 1, luego 2, y así sucesivamente.

Eventualmente cuando el contador llegue a tener un valor de 10, la condición del 
ciclo numero <= 10 sera False, por lo que el ciclo terminará arrojando el siguiente resultado.
"""



"""
Bucle ‘while’ controlado por Evento

A continuación, se presenta un ejemplo del uso del bucle while controlado por Evento:
"""

promedio, total, contar = 0.0, 0, 0

print ("Introduzca la nota de un estudiante (-1 para salir): ")
grado = int(raw_input())
while grado != -1:
    total = total + grado
    contar = contar + 1
    print ("Introduzca la nota de un estudiante (-1 para salir): "
    grado = int(raw_input()))
promedio = total / contar
print ("Promedio de notas del grado escolar es: " + str(promedio))


