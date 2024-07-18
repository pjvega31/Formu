from myapp.models import RaceResult, Race, Driver

# Obtener la carrera "Austrian GP"
austrian_gp = Race.objects.get(name="Austrian GP")

# Borrar todos los resultados de la carrera para esta carrera
RaceResult.objects.filter(race=austrian_gp).delete()

# Datos de los nuevos resultados de la carrera
race_data = [
    {'driver_name': 'George Russell', 'position': 1, 'is_dnf': False, 'is_fastest_lap': False},
    {'driver_name': 'Oscar Piastri', 'position': 2, 'is_dnf': False, 'is_fastest_lap': False},
    {'driver_name': 'Carlos Sainz', 'position': 3, 'is_dnf': False, 'is_fastest_lap': False},
    {'driver_name': 'Lewis Hamilton', 'position': 4, 'is_dnf': False, 'is_fastest_lap': False},
    {'driver_name': 'Max Verstappen', 'position': 5, 'is_dnf': False, 'is_fastest_lap': False},
    {'driver_name': 'Nico Hülkenberg', 'position': 6, 'is_dnf': False, 'is_fastest_lap': False},
    {'driver_name': 'Sergio Pérez', 'position': 7, 'is_dnf': False, 'is_fastest_lap': False},
    {'driver_name': 'Kevin Magnussen', 'position': 8, 'is_dnf': False, 'is_fastest_lap': False},
    {'driver_name': 'Daniel Ricciardo', 'position': 9, 'is_dnf': False, 'is_fastest_lap': False},
    {'driver_name': 'Pierre Gasly', 'position': 10, 'is_dnf': False, 'is_fastest_lap': False},
    {'driver_name': 'Charles Leclerc', 'position': 11, 'is_dnf': False, 'is_fastest_lap': False},
    {'driver_name': 'Esteban Ocon', 'position': 12, 'is_dnf': False, 'is_fastest_lap': False},
    {'driver_name': 'Lance Stroll', 'position': 13, 'is_dnf': False, 'is_fastest_lap': False},
    {'driver_name': 'Yuki Tsunoda', 'position': 14, 'is_dnf': False, 'is_fastest_lap': False},
    {'driver_name': 'Alexander Albon', 'position': 15, 'is_dnf': False, 'is_fastest_lap': False},
    {'driver_name': 'Valtteri Bottas', 'position': 16, 'is_dnf': False, 'is_fastest_lap': False},
    {'driver_name': 'Guanyu Zhou', 'position': 17, 'is_dnf': False, 'is_fastest_lap': False},
    {'driver_name': 'Fernando Alonso', 'position': 18, 'is_dnf': False, 'is_fastest_lap': True},
    {'driver_name': 'Logan Sargeant', 'position': 19, 'is_dnf': False, 'is_fastest_lap': False},
    {'driver_name': 'Lando Norris', 'position': 20, 'is_dnf': True, 'is_fastest_lap': False},
]

# Insertar los nuevos resultados de la carrera
for data in race_data:
    driver_name = data['driver_name'].encode('latin-1').decode('utf-8')
    try:
        driver = Driver.objects.get(name=driver_name)
    except Driver.DoesNotExist:
        print(f"Driver matching query does not exist: {driver_name}")
        continue

    RaceResult.objects.create(
        race=austrian_gp,
        driver=driver,
        position=data['position'],
        is_dnf=data['is_dnf'],
        is_fastest_lap=data['is_fastest_lap'],
        points=0  # Establece los puntos a 0 para que el cálculo se realice en el método save
    )



