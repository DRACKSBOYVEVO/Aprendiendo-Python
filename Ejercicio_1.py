"""
Herramienta de seguimiento de palabras clave en Google (Kwranking)

Vas a desarrollar una aplicación paso a paso para realizar el seguimiento
en Google de un conjunto de palabras clave. En concreto, para conocer en qué
orden rankea cada una de las palabras clave en el buscador para un dominio determinado.
Los datos se guardarán en una base de datos y se podrán exportar a Excel.

Las palabras clave equivalen a las palabras que introduce un usuario en el
campo de búsqueda de Google. Por ejemplo, imagina una web de recetas y un
usuario que quiere buscar el texto macarrones con tomate. Lo que se pretende
es conocer en qué posición aparece la web de recetas en los resultados del buscador
cuando se introducen, precisamente, las palabras macarrones con tomate.

"""

"""Ejercicio #1: Menú de la aplicación Kwranking"""

"""
Este ejercicio tiene como objetivo ser una primera toma de 
contacto con la aplicación Kwranking. Esta aplicación es una aplicación 
de consola, es decir, se ejecutará desde el terminal. 
No hay que implementar una interfaz gráfica.
"""

"""
    Requisitos

    Implementar un menú de aplicación con las siguientes opciones:
        [1] – Importar palabras clave
        [2] – Mostrar palabras clave
        [0] – Salir
    Implementar una función carga_keywords() que lea un fichero llamado keywords.txt:
        El fichero tendrá una(s) palabra(s) clave por línea.
        No hay que separar las palabras clave con ningún carácter, solo enter.
        El fichero se leerá línea a línea, guardando la palabra clave correspondiente como un nuevo elemento de una lista.
        La función devolverá una lista de palabras clave.
    Cuando se introduzca la opción de menú [1], se invocará a la función carga_keywords(). La lista resultante se asignará a una variable del programa llamada keywords.
    Cuando se introduzca la opción de menú [2], se mostrará el listado de palabras clave de 20 en 20, es decir, una vez mostradas 20 palabras clave, el usuario deberá pulsar la tecla enter para ver las siguientes.
    Cuando se introduzca la opción de menú [0], el programa finalizará.
    
    Consideraciones a tener en cuenta en el fichero keywords.txt

    A continuación, te muestro un ejemplo de cómo debe ser el fichero
    keywords.txt:

    macarrones
    macarrones con tomate y queso
    receta de macarrones

Como puedes observar, cada línea se corresponde con una serie 
de palabras clave a posicionar de un blog de recetas.

El fichero debe estar en el mismo directorio que el programa Python.
"""

"""Ejercicio #1: Crear menú de la aplicación e importar palabras clave desde un fichero."""



"""Función para mostrar el menú"""
def muestra_menu():
    print('')
    print('')
    print('-------- Kwranking --------')
    print('')
    print('[1] – Importar palabras clave')
    print('[2] – Mostrar palabras clave')
    print('[0] – Salir')

    """Función carga_keywords()"""

    def carga_keywords():
        keywords = []
        try:
            with open('keywords.txt') as fichero:
                for kw in fichero:
                    kw = kw.replace('\n', '')
                    keywords.append(kw)
        except FileNotFoundError:
            print('No se encuentra el fichero keywords.txt')
        return keywords

    """
    Cuando se lee un fichero línea a línea, Python tiene en cuenta el carácter salto de línea \n. 
    Por eso, se elimina este carácter de cada una de las palabras clave con kw.replace('\n', '').
    """

    """Función para mostrar las palabras clave"""

    def muestra_keywords(keywords):
        contador = 0
        for kw in keywords:
            print(kw)
            contador += 1
            if contador == 20:
                contador = 0
                input('Mostrar más...')

    """El programa principal"""

    def run():

        keywords = []

        while True:
            muestra_menu()
            opcion = input('Selecciona una opción > ')
            opcion = int(opcion)
            if opcion == 0:
                break
            elif opcion == 1:
                keywords = carga_keywords()
            elif opcion == 2:
                muestra_keywords(keywords)
            else:
                print('Opción no válida')

    if __name__ == '__main__':
        run()