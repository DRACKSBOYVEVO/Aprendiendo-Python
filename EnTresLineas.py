"""

Escribe un programa que reciba como entrada (por teclado) una secuencia
de palabras separadas por espacios en blanco e imprima las palabras ordenadas
alfanuméricamente, en mayúsculas y después de haber eliminado todas las duplicadas.

Imagina que se proporciona la siguiente entrada al programa:
$> Lo mejor del lenguaje Python es que es un lenguaje del que no te aburres

La salida correspondiente al programa será:
ABURRES DEL ES LENGUAJE LO MEJOR NO PYTHON QUE TE UN
"""

"""Solución con tres líneas de código"""

s = input('Introduce una secuencia de palabras > ')
words = s.upper().split(' ')
print(' '.join(sorted(set(words))))

"""Solución con dos líneas de código"""

"""s = input('Introduce una secuencia de palabras > ')"""
"""print(' '.join(sorted(set(s.upper().split(' ')))))"""

"""Solución con una línea de código"""
"""print(' '.join(sorted(set(input('Introduce ... > ').upper().split(' ')))))"""

"""
    Explicación de cada palabra!

Voy a desgranar lo que hace cada una de las funciones:

    split(' '): Crea una lista formada por cada una de las palabras de la cadena de entrada.
    
    set(): Crea un conjunto formado por las palabras de la lista que se pasa como argumento. 
    Al tratarse de un conjunto, las palabras duplicadas se eliminan.
    
    sorted(list(...)): Devuelve una lista ordenada con los elementos del iterable que se pasa como argumento.
    
    ' '.join(...): Crea una cadena compuesta por los elementos de la lista ordenada separados por el carácter espacio.
"""