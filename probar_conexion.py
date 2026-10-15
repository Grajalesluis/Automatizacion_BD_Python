
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL

# Cargar las variables del archivo .env
load_dotenv()

# Obtener las credenciales
usuario = os.getenv("DB_USER")
contrasena = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
puerto = int(os.getenv("DB_PORT", "3306"))
base_datos = os.getenv("DB_NAME")

# Construir la URL de conexión
url = URL.create(
    "mysql+pymysql",
    username=usuario,
    password=contrasena,
    host=host,
    port=puerto,
    database=base_datos
)

# Crear el motor de conexión
motor = create_engine(url)

try:
    # Abrir una conexión y ejecutar una consulta sencilla
    with motor.connect() as conexion:
        resultado = conexion.execute(
            text("SELECT DATABASE()")
        )

        print("Conexión exitosa.")
        print("Base de datos:", resultado.scalar())

except Exception as error:
    print("Error de conexión:", error)

finally:
    # Liberar los recursos de conexión
    motor.dispose()
