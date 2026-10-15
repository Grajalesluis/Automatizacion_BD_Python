
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL

# Leer los datos del archivo .env
load_dotenv()

# Obtener los datos de conexión
usuario = os.getenv("DB_USER")
contrasena = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
puerto = int(os.getenv("DB_PORT", "3306"))
base_datos = os.getenv("DB_NAME")

# Preparar la conexión con MySQL
url = URL.create(
    "mysql+pymysql",
    username=usuario,
    password=contrasena,
    host=host,
    port=puerto,
    database=base_datos
)

motor = create_engine(url)

# Comprobar si la conexión funciona
try:
    with motor.connect() as conexion:
        resultado = conexion.execute(text("SELECT DATABASE()"))
        print("Conexión exitosa.")
        print("Base de datos:", resultado.scalar())

except Exception as error:
    print("Error de conexión:", error)

finally:
    motor.dispose()
