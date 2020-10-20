"""
Al igual que la sentencia if y el bucle while, la estructura for
también puede combinarse con una sentencia else.

El nombre de la sentencia else es equivocada, ya que el bloque else se
ejecutará en todos los casos, es decir, cuando la expresión condicional
del bucle for sea False, (a comparación de la sentencia if).
"""

db_connection = "127.0.0.1","5432","root","nomina"
for parametro in db_connection:
    print (parametro)
else:
    print ("""El comando PostgreSQL es: 
$ psql -h {server} -p {port} -U {user} -d {db_name}""".format(
        server=db_connection[0], port=db_connection[1],
        user=db_connection[2], db_name=db_connection[3]))

