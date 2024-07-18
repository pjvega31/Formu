from django.db import models

class Driver(models.Model):
    name = models.CharField(max_length=100)
    team = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=100)
    drivers = models.ManyToManyField(Driver)
    fastest_lap_driver = models.ForeignKey(Driver, related_name='fastest_lap_driver', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name
