#Aqui estoy llamando al elemento de una lista con su indice.
#Los elementos de una lista o una tupla, siempre comienzan desde 0
Lista_vacia = []
Mercado_Semana = ['Papalla','Sandia',2,5.8,['Hola Amigo'],True,False]
Mercado_Semana.append(10) #Se agrega este elemento al final de la lista.
Mercado_Semana.extend([4.5]) #sirve para mover elementos.
Mercado_Semana.remove(2) #Para eliminar elemetos de una lista
Mercado_Semana.index('Sandia') #Para saber el indice del elemento.
Mercado_Semana.reverse() #poner los elementos alreves
#print (Mercado_Semana) #para imprimir la lista.

#aqui se puede hacer una condicion que recorra la lista y imprima los valores
#o los elementos que contiene esa lista.
for elementos in Mercado_Semana:
    print (elementos)

#Aqui voy agregar mas elementos a la lista que tengo
