"""
Operaciones más habituales con diccionarios en Python

Es similar a las listas, con el matiz de que dado que los diccionarios no tienen orden, no tienen funciones en las que se tenga en cuenta la posición.

    diccionario.get(‘key’): Devuelve el valor que corresponde con la key introducida.
    diccionario.pop(‘key’): Devuelve el valor que corresponde con la key introducida, y luego borra la key y el valor.
    diccionario.update({‘key’:’valor’}): Inserta una determinada key o actualiza su valor si ya existiera.
    «key» in diccionario: Devuelve verdadero (True) o falso (False) si la key (no los valores) existe en el diccionario.
    «definicion» in diccionario.values(): Devuelve verdadero (True) o falso (False) si definición existe en el diccionario (no como key).
"""


datos_basicos = {
    "nombres":"Juan José",
    "apellidos":"Henao Gutiérrez",
    "cedula":"1.152.470.384",
    "fecha_nacimiento":"12/06/1999",
    "lugar_nacimiento":"San Rafael, Medellín, Colombia",
    "nacionalidad":"Colombiana",
    "estado_civil":"Soltero"
}
clave = datos_basicos.keys() #Claves principales del diccionario
valor = datos_basicos.values() #Valores del diccionario
cantidad_datos = datos_basicos.items() #Elementos

for clave, valor in cantidad_datos:
    print (clave + ": " + valor)

