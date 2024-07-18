import os
import django

# Configura el entorno de Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
django.setup()

from myapp.models import Race, SprintResult

# Paso 1: Obtener la carrera "Austrian GP"
race = Race.objects.get(name="Austrian GP")

# Paso 2: Obtener todos los resultados del sprint para la carrera "Austrian GP"
sprint_results = SprintResult.objects.filter(race=race)

# Calcular puntos por piloto para el sprint
driver_points = {}
for result in sprint_results:
    driver_name = result.driver.name
    if driver_name not in driver_points:
        driver_points[driver_name] = {'sprint': 0, 'fastest_lap_points': 0, 'bono': 0, 'total': 0}
    driver_points[driver_name]['sprint'] = result.points  # Solo cuenta los puntos por la posición

# Ajustar el bono específico al piloto con la vuelta rápida
for result in sprint_results:
    if result.is_fastest_lap:
        driver_points[result.driver.name]['bono'] = 1

# Calcular el total sumando los puntos de la posición y el bono
for driver_name in driver_points:
    driver_points[driver_name]['total'] = driver_points[driver_name]['sprint'] + driver_points[driver_name]['bono']

# Imprimir los puntos por piloto
print("Puntos por piloto:")
for driver_name, points in driver_points.items():
    print(f"| {driver_name:<17} | Puntos Sprint: {points['sprint']:<14} | Fastest Lap: {points['fastest_lap_points']} | Bono: {points['bono']} | Total: {points['total']:<8} |")

# Calcular puntos por equipo de constructores para el sprint
constructor_points = {}
for result in sprint_results:
    team_name = result.driver.team.name
    if team_name not in constructor_points:
        constructor_points[team_name] = {'points': 0, 'fastest_lap_points': 0}
    constructor_points[team_name]['points'] += result.points

# Imprimir los puntos por equipo de constructores
print("Puntos por equipo de constructores:")
for constructor_name, points in constructor_points.items():
    total_points = points['points'] + points['fastest_lap_points']
    print(f"| {constructor_name:<25} | Puntos Sprint: {points['points']:<14} | Fastest Lap: {points['fastest_lap_points']} | Total: {total_points:<8} |")
