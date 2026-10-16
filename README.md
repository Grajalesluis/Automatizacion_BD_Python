# Automatización de base de datos con Python, Faker y SQLAlchemy

## Descripción

Este proyecto automatiza la creación y el llenado de una tabla MySQL mediante Python. Se utiliza la biblioteca Faker para generar datos ficticios de personas y SQLAlchemy para administrar la conexión y ejecutar las operaciones sobre la base de datos.

El programa crea la tabla `personas_luis` si no existe e inserta 100.000 registros utilizando lotes de 1.000 registros.

## Tecnologías utilizadas

- Python
- MySQL
- SQLAlchemy
- PyMySQL
- Faker
- python-dotenv
- DBeaver para consultar y verificar los datos

## Estructura del proyecto

- `main.py`: programa principal para crear la tabla e insertar los registros.
- `probar_conexion.py`: script auxiliar para probar la conexión con la base de datos.
- `prueba_generar_datos.py`: script auxiliar para probar la generación de datos.
- `.env.example`: plantilla de las variables de conexión.
- `.gitignore`: archivos y carpetas excluidos del control de versiones.
- `requirements.txt`: dependencias del proyecto.
- `Evidencia_DBeaver.png`: evidencia de la consulta de verificación.

## Requisitos previos

1. Tener Python instalado.
2. Tener un servidor MySQL en funcionamiento.
3. Contar con una base de datos llamada `actividad3`.
4. Tener Git instalado si se desea clonar el repositorio.

## Instalación

Clona el repositorio y entra en la carpeta del proyecto:

```bash
git clone URL_DEL_REPOSITORIO
cd actividad3_BD_Python
```

Crea un entorno virtual:

```bash
python -m venv .venv
```

Activa el entorno virtual en Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Instala las dependencias:

```bash
pip install -r requirements.txt
```

## Configuración de la conexión

Copia `.env.example` y crea un archivo llamado `.env` en la raíz del proyecto.

Configura las siguientes variables con los datos de tu entorno MySQL:

```dotenv
DB_HOST=localhost
DB_PORT=3306
DB_USER=tu_usuario
DB_PASSWORD=tu_contraseña
DB_NAME=actividad3
```

Reemplaza los valores de ejemplo por tus credenciales reales. El archivo `.env` no debe publicarse en GitHub.

## Ejecución

Con el entorno virtual activado, ejecuta:

```bash
python main.py
```

El programa crea la tabla `personas_luis` si no existe, genera datos ficticios e inserta 100.000 registros en lotes de 1.000. Al finalizar, muestra la cantidad insertada y el total de registros de la tabla.


## Verificación en MySQL

En DBeaver, selecciona la base de datos `actividad3` y ejecuta:

```sql
SELECT COUNT(*)
FROM personas_luis;
```

El resultado esperado tras la primera ejecución correcta es `100000`.


## Evidencia

El archivo `Evidencia_DBeaver.png` contiene la captura de la consulta de verificación del total de registros.

## Autor

Luis Fernando Grajales
