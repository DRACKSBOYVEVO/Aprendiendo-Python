#Ejemplo de continue

Nombre = "Juan José"

Contador = 0

for i in Nombre:
    if i == " ": #me ignora el espacio en blanco
        continue
    Contador+=1

print(Contador)

#Ejemplo de pass, pass devuelve un null.
#y no es tal utilizado, pero hay que tenerlo en cuenta.

#clase nula

class MiClase:
    pass #pongo codigo mas tarde.


#Ejemplo de else

Numero_1 = 2
Numero_2 = 3

if Numero_1 == Numero_2:
    print("Son iguales")
else:
    print("No son iguales.")

#Ejemplo de break

Correo = "correo@hotmail.com"

for i in Correo:
    if i == "@":
        Arroba = True
        break;
        #Rompe el ciclo y continua el siclo de ejecucion