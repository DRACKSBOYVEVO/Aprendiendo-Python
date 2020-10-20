
#=============Ejercicio 1 ===============
Componentes_Computador = {
    #llave      #Valor
    "Gabinete":"Coosair",
    "Memoria RAM":64,
    "Procesador":"ryzen 5 3400G",
    "Tarjeta Grafica":"RTX 2080Ti",
    "Placa madre":"Asus Rock Republic Gaming",
    "R. Liquida": "Coorsair",
    "HHD":2,
    "SSD":480,
    "NvMe M.2":256,
    "Monitor":"240Hz",
    "Mause":"Ryzer",
    "Deademas":"Coorsair",
    "Silla":"Color ful"

}
print(Componentes_Computador.keys())#comendo para ver las llaves de los elementos del diccionario.

#=============Ejercicio 2===============
"""
1. Crea un diccionario con los siguientes pares de valores

Manzana = apple
Naranja = Orange
Platano = banana
Limon = Lemon

- Mostrar la traduccion para cada palabra
-Añadir como nuevo elemento pina = pineapple
-hacer un buble for para mostrar todos los elementos del diccionario.
"""

Frutas = {
    "Manzana":"apple",
    "Narajan":"Orange",
    "Platano":"Banano",
    "Limon":"Lemon"
}

Frutas["Piña"] = "Pineapple" #Estoy añadiendo un nuevo elemento
#Aqui en este bucle estoy recorriendo los elementos de la lista
for clave,valor in Frutas.items():
    print("{} En ingles seria: {}".format(clave,valor))
