"""
Bucle ‘for’ con Listas

Operaciones más habituales con listas en Python

Las operaciones más habituales que se realizan en Python son las siguientes:

    lista[i]: Devuelve el elemento que está en la posición i de la lista.
    lista.pop(i): Devuelve el elemento en la posición i de una lista y luego lo borra.
    lista.append(elemento): Añade elemento al final de la lista.
    lista.insert(i, elemento): Inserta elemento en la posición i.
    lista.extend(lista2): Fusiona lista con lista2.
    lista.remove(elemento): Elimina la primera vez que aparece elemento.
"""

animales = ['gato', 'perro', 'serpiente']
for animal in animales:
    print ("El animal es: {0}, tamaño de palabra es: {1}".format(animal, len(animal)))

# Acceder a un elemento de la lista.
print(animales[1])
#perro

# pop: Extraemos a perro (que está en la posición número 1) de la lista. gato está en la posición 0.
animales.pop(1)
print(animales)
#['perro']

# append: Añadimos a cocodrilo al final de la lista
animales.append("cocodrilo")
print (animales)
#['serpiente', 'cocodrilo']

# del:Eliminamos el elemento de la primera posición de la lista (gato)
del(animales[0])

# insert: Añadimos a mono en la primera posición
animales.insert(0, "mono")
print (animales)
['mono', 'cocodrilo']

# extend: Juntamos los pilotos del 2013 y los del 2014. Fernando estará repetido.
animales.extend(animales)
print (animales)
['gato', 'cocodrilo', 'gato', 'ardilla']

#remove: Borramos la primera vez que aparece Fernando Alonso
animales.remove("Fernando Alonso")
print (animales)
['cocodrilo', 'gato', 'ardilla']
