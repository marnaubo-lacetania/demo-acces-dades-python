# Importem el connector de MySQL per a Python.
import mysql.connector

# Establim la connexió amb el servidor de BBDD:
bd = mysql.connector.connect(
    host="localhost",           #Nom o adreça IP del servidor
    user="root",                #Credencials
    password="",
    database="taller"           #Nom de la BD
)

# Obrim un cursor que apuntarà al resultat de la consulta que li indicarem en .execute()
cursor = bd.cursor()
cursor.execute("SELECT * FROM vehicles")

# Tenim diferents maneres d'accedir (fetch) als resultats de la consulta:
#   en blocs de X ==> .fetchMany()
#   un a un ==> .fecthone()
#   tots ==> .fetchall()
# En el nostre cas, consultarem tots els resultats de cop.
# 
# Quan treballem amb grans volums de dades ens pot interessar treballar en grups o un a un per 
# no tenir problemes de manipulació massiva en memòria.
files = cursor.fetchall()

# Quan ja hem consultat to el que volem de la BD (no pas abans) tancarem el cursor i la connexió. 
# Sempre cal tancar-la per evitar connexions obertes sense necessitat.
cursor.close()
bd.close()

# Per cada una de les files consultades, volquem informació per consola:
for fila in files:
    print("Dades del cotxe amb matrícula ", fila[0], " ==> ", fila)
    
