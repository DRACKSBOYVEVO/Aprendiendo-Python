"""
Condiciones en Python

Las condiciones que se suelen usar con más frecuencia son:

     a == b –> Indica si a es igual a b
    a < b
    a > b
    not –> NO: niega la condición que le sigue.
    and –> Y: junta dos condiciones que tienen que cumplirse las dos
    or –> O: junta dos condiciones y tienen que cumplirse alguna de las dos.
"""

Mi_Posicion=3
if (Mi_Posicion==1):
    print("Espectacular Juan, se ha hecho justicia a pesar del coche")
    print("Ya queda menos para ganar el mundal")
elif (Mi_Posicion>1):
    print("Gran carrera de Juan, lástima que el coche no esté a la altura")
else:
    print("No ha podido terminar la carrera por una avería mecánica")