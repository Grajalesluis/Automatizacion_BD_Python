

import os
from dotenv import load_dotenv
from faker import Faker
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL

# --------------------------------------------------
# 1. Cargar la configuracion
# --------------------------------------------------

load_dotenv()

usuario = os.getenv("DB_USER")
contrasena = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
puerto = int(os.getenv("DB_PORT", "3306"))
base_datos = os.getenv("DB_NAME")

# Crear la URL de conexion
url = URL.create(
    "mysql+pymysql",
    username=usuario,
    password=contrasena,
    host=host,
    port=puerto,
    database=base_datos
)

# Crear el motor de conexion
motor = create_engine(url)

# Configurar Faker en español colombiano
fake = Faker("es_CO")

# Cantidad de registros para la prueba
TOTAL_REGISTROS = 100

# Tamano de cada lote de insercion
TAMANO_LOTE = 100


try:
    # --------------------------------------------------
    # 2. Crear la tabla si no existe
    # --------------------------------------------------

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

    print("Tabla personas_luis lista.")

    # --------------------------------------------------
    # 3. Generar e insertar los registros
    # --------------------------------------------------

    insert_sql = text("""
        INSERT INTO personas_luis (
            nombre,
            apellido,
            correo,
            telefono,
            direccion,
            ciudad,
            pais,
            fecha_nacimiento,
            ocupacion,
            empresa
        )
        VALUES (
            :nombre,
            :apellido,
            :correo,
            :telefono,
            :direccion,
            :ciudad,
            :pais,
            :fecha_nacimiento,
            :ocupacion,
            :empresa
        )
    """)

    insertados = 0

    # Abrir una transaccion para insertar los lotes
    with motor.begin() as conexion:

        for inicio in range(0, TOTAL_REGISTROS, TAMANO_LOTE):

            # Determinar cuantos registros tiene este lote
            cantidad = min(
                TAMANO_LOTE,
                TOTAL_REGISTROS - inicio
            )

            # Generar los datos del lote
            lote = []

            for _ in range(cantidad):
                persona = {
                    "nombre": fake.first_name()[:20],
                    "apellido": fake.last_name()[:20],
                    "correo": fake.unique.email()[:50],
                    "telefono": fake.numerify(
                        text="3#########"
                    )[:15],
                    "direccion": fake.street_address()[:30],
                    "ciudad": fake.city()[:100],
                    "pais": "Colombia",
                    "fecha_nacimiento": fake.date_of_birth(
                        minimum_age=18,
                        maximum_age=80
                    ),
                    "ocupacion": fake.job()[:30],
                    "empresa": fake.company()[:50]
                }

                lote.append(persona)

            # Insertar todo el lote en una operacion
            conexion.execute(insert_sql, lote)

            insertados += len(lote)

            print(
                f"Registros insertados en esta ejecucion: "
                f"{insertados}/{TOTAL_REGISTROS}"
            )

    # --------------------------------------------------
    # 4. Verificar el total de registros en la tabla
    # --------------------------------------------------

    with motor.connect() as conexion:
        total_tabla = conexion.execute(
            text("SELECT COUNT(*) FROM personas_luis")
        ).scalar_one()

    print("\nProceso terminado correctamente.")
    print(f"Registros agregados en esta ejecucion: {insertados}")
    print(f"Total de registros en la tabla: {total_tabla}")

except Exception as error:
    print("Ocurrio un error:", error)

finally:
    # Cerrar las conexiones
    motor.dispose()


if __name__ == "__main__":
    pass
