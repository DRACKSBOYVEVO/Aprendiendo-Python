"""
Bucle ‘for’ con Listas y función ‘range’

A continuación, se presenta un ejemplo del uso del
bucle for con tipos de estructuras de datos listas
con la función range() y la función len():
"""

oracion = 'Juan entiende muy bien Python'
frases = oracion.split() # split() convierte a una lista cada palabra
print ("La oración analizada es:"+ oracion+ ".\n")
for palabra in range(len(frases)):
    print ("Palabra: {0}, en la frase su posición es: {1}".format(frases[palabra], palabra))

