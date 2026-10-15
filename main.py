
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

# Definir y crear la tabla completa
try:
    with motor.begin() as conexion:
        conexion.execute(text("""
            CREATE TABLE IF NOT EXISTS personas_luis (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(100) NOT NULL,
                apellido VARCHAR(100) NOT NULL,
                correo VARCHAR(150) NOT NULL,
                telefono VARCHAR(30),
                direccion VARCHAR(200),
                ciudad VARCHAR(100),
                pais VARCHAR(100),
                fecha_nacimiento DATE,
                ocupacion VARCHAR(100),
                empresa VARCHAR(150)
            )
        """))

    print("La tabla personas_luis está lista.")
    print("Tiene una clave primaria y diez atributos.")

except Exception as error:
    print("Ocurrió un error:", error)

finally:
    motor.dispose()

# Ejecutar el programa principal
if __name__ == "__main__":
    pass
