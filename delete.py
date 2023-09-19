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

# Obrim un cursor:
cursor = bd.cursor()

# Preparem la instrucció per l'eliminació:
sql = "DELETE FROM vehicles WHERE matricula=%s"
matricula = 'ABC2222'

# Ara insertarem les dades, executant la sentència SQL indicant la matricula en concret:
cursor.execute(sql, [matricula])

# Ens assegurem que les dades es confirmen correctament i queden ben escrites:
bd.commit()

# Revisem si s'ha eliminat:
if (cursor.rowcount > 0):
    print("S'ha esborrat el vehicle correctament.")
else:
    print("No s'ha trobat cap vehicle amb aquesta matrícula.")

# Tanquem els connexions:
cursor.close()
bd.close()