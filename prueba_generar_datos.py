
from faker import Faker

# Configurar Faker en español
fake = Faker("es_CO")

# Generar 5 personas ficticias
for i in range(5):

    nombre = fake.first_name()
    apellido = fake.last_name()
    correo = fake.email()
    telefono = fake.phone_number()
    direccion = fake.address().replace("\n", ", ")
    ciudad = fake.city()
    pais = fake.current_country()
    fecha_nacimiento = fake.date_of_birth(
        minimum_age=18,
        maximum_age=80
    )
    ocupacion = fake.job()
    empresa = fake.company()

    # Mostrar los datos generados
    print(f"\nPersona {i + 1}")
    print("Nombre:", nombre)
    print("Apellido:", apellido)
    print("Correo:", correo)
    print("Teléfono:", telefono)
    print("Dirección:", direccion)
    print("Ciudad:", ciudad)
    print("País:", pais)
    print("Fecha de nacimiento:", fecha_nacimiento)
    print("Ocupación:", ocupacion)
    print("Empresa:", empresa)
