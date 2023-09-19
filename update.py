# Importem el connector de MySQL per a Python.
import mysql.connector
# Importem eines per a treball amb dates:
from datetime import date

# Establim la connexió amb el servidor de BBDD:
bd = mysql.connector.connect(
    host="localhost",           #Nom o adreça IP del servidor
    user="root",                #Credencials
    password="",
    database="taller"           #Nom de la BD
)

# Obrim un cursor per realitzar l'actualització:
cursor = bd.cursor()

# Preparem la instrucció per l'actualització:
sql = "UPDATE vehicles SET marca=%(marca)s, data_alta=%(data_alta)s WHERE matricula=%(matricula)s"

# Ara executem l'actualització, utilitzant la consulta SQL i els paràmetres necessaris per construir-la:
cursor.execute(sql, { 'marca': 'Ford', 'matricula': 'ABC2222', 'data_alta': date(2020, 5, 15)})

# Ens assegurem que les dades es confirmen correctament i queden ben escrites:
bd.commit()

# Revisem si s'ha actualitzat:
if (cursor.rowcount > 0):
    print("S'ha actualitzat el vehicle correctament.")
else:
    print("No s'ha trobat cap vehicle amb aquesta matrícula.")

# Tanquem els connexions:
cursor.close()
bd.close()