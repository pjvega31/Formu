from django.db import models

class Driver(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Evita duplicados
    team = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Evita duplicados
    drivers = models.ManyToManyField(Driver, related_name='teams')  # Añade related_name para claridad
    fastest_lap_driver = models.ForeignKey(
        Driver,
        related_name='fastest_lap_in_team',
        on_delete=models.SET_NULL,  # Cambia a SET_NULL para evitar eliminación cascada
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

