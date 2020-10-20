"""
Este ejercicio trata de combinar varios conceptos y
funcionalidades de los tipos contenedor de Python.

En él vas a tener que implementar una función llamada ordena_ciudades(ciudades)
que reciba como argumento un diccionario con ciudades y su población y devuelva
una lista con los nombres de las ciudades de más de 200.000 habitantes. La lista
devuelta debe estar ordenada de mayor a menor según el número de habitantes de cada ciudad.
"""

d = {'Valencia': 794000, 'Salamanca': 144000, 'Cádiz': 116000, 'Madrid': 3200000}
['Madrid', 'Valencia']


"""La gracia de este ejercicio está en implementar la función ordena_ciudades(ciudades) 
en una sola línea de código. Esta es una de las soluciones posibles:"""

def ordena_ciudades(d):
    return sorted((k for k, v in d.items() if v >= 200000), key=lambda x: -d[x])

"""
En primer lugar, la función crea una tupla (a través de comprensión de tuplas) 
con los nombres de las ciudades de más de 200.000 habitantes.

Finalmente, esa tupla se pasa como argumento de la función sorted(). 
Para ordenar los elementos, se utiliza una función lambda que se pasa 
en el argumento key. Esta función, simplemente, cambia el signo al valor 
de la población del diccionario, para que las ciudades se ordenen de menor 
a mayor (siendo el resultado precisamente el contrario).

Una alternativa a esta implementación podría ser pasar 
el argumento reverse=True a la función sorted (lo que implica 
realizar una modificación en la función lambda):
"""

def ordena_ciudades(d):
    return sorted((k for k, v in d.items() if v >= 200000), key=lambda x: d[x], reverse=True)