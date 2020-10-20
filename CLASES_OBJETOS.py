#Aqui creare la clase
class productos:
    precio = 20
    Nombre = "Papitas"

Objeto_carrito = productos()
Objeto_carrito.precio #Aqui estoy heredando los datos de la clase productos
Objeto_carrito.Nombre

class Persona():
    def __init__(self, Nombre, Edad): #metodos Nombre, Edad
        self.nombre = "Juan José"
        self.Edad = 21
    def saludo(self):
        print("Hola, Amigo, ¿me llamo {} y tengo {} años y tu? ".format(self.nombre,self.Edad))
Hermana = Persona("Catalina",20) #Instancia de persona
Hermana.nombre
Hermana.Edad
Hermana.saludo()