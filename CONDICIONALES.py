#Condicion que evaluara 3 condiciones a la vez.

print("Esto es un programa para seleccionar becas!")

Distancia_Escuela = int(input("Introduce la distancia que hay de tu casa\n a la escuela en Km: "))
print(Distancia_Escuela)

Numero_Hermanos = int(input("Introduce el numero de hermanos en tu nucleo familiar: "))
print(Numero_Hermanos)

Salario_familiar = int(input("Introduce la cantidad de ingresos de tu familia: "))
print(Salario_familiar)

if Distancia_Escuela > 40 and Numero_Hermanos > 2 and Salario_familiar <= 40000:
    print("Excelente! Tienes derecho a una beca estudiantil, cuidala.")
else:
    print("Lo sentimos, no cumples con los requisitos requeridos.")


#=====================Ejercicio 3=========================

"""
2. 

- Crear una variable llamada "Nota" que tenga como valor 4.5
- Crear una variable llamada "Trabajo_Realizado" y que tenga como valor "Si"
- Calcular el valor de la variable "Nota_Final", ten en cuenta, que si la Nota es mayor o igual a  4 y el valor de la variable "Trabajo_Realizado" es igual que "Si", Entonces la Nota_Final sera igual a "aprobado", en caso contrario sera "suspendido"
"""


Trabajo_Realizado = input("¿Hiciste el trabajo?")
Nota = int(input("Dijite su nota por favor."))

if (Nota >= 4) and (Trabajo_Realizado == "si"):
    Nota_Final = 'aprobado'
else: 
    Nota_Final = 'suspendido'






