# Importem el connector de MySQL per a Python.
import mysql.connector
# Importem eines per a treball amb dates:
from datetime import date;

# Establim la connexió amb el servidor de BBDD:
bd = mysql.connector.connect(
    host="localhost",           #Nom o adreça IP del servidor
    user="root",                #Credencials
    password="",
    database="taller"           #Nom de la BD
)

# Obrim un cursor que utilitzarem per executar la consulta d'inserció:
cursor = bd.cursor()

# Preparem un diccionari (objecte) amb les dades que volem insertar:
dades = {
    'matricula': 'ABC2222',
    'marca': 'Toyota',
    'any': 2016,
    'data_alta': date(2018, 3, 20),
}

# Preparem la instrucció per la inserció:
sql = (
    "INSERT INTO vehicles(matricula, marca, any, data_alta) "
    "VALUES (%(matricula)s, %(marca)s, %(any)s, %(data_alta)s)"
)

# Ara insertarem les dades, executant la sentència SQL conjuntament amb les dades a insertar:
cursor.execute(sql, dades)

# Ens assegurem que les dades es confirmen correctament i queden ben escrites:
bd.commit()

# Tanquem els connexions:
cursor.close()
bd.close()