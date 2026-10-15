
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL

# Leer las variables del archivo .env
load_dotenv()

# Obtener los datos para conectarse a MySQL
usuario = os.getenv("DB_USER")
contrasena = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
puerto = int(os.getenv("DB_PORT", "3306"))
base_datos = os.getenv("DB_NAME")

# Crear la dirección de conexión
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
    # Crear la tabla si todavía no existe
    with motor.begin() as conexion:
        conexion.execute(text("""
            CREATE TABLE IF NOT EXISTS personas_luis (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(20) NOT NULL,
                apellido VARCHAR(20) NOT NULL,
                correo VARCHAR(50) NOT NULL,
                telefono VARCHAR(15),
                direccion VARCHAR(30),
                ciudad VARCHAR(100),
                pais VARCHAR(100),
                fecha_nacimiento DATE,
                ocupacion VARCHAR(30),
                empresa VARCHAR(50)
            )
        """))

    print("La tabla personas_luis está lista.")
    print("Tiene una clave primaria y diez atributos.")

except Exception as error:
    print("Ocurrió un error:", error)

finally:
    # Cerrar las conexiones
    motor.dispose()


if __name__ == "__main__":
    pass

