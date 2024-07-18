from django.db import models
from django.contrib.auth.models import User

class Constructor(models.Model):
    name = models.CharField(max_length=100)
    rank = models.IntegerField()

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    wins = models.IntegerField(default=0)
    points = models.FloatField(default=0)

    def __str__(self):
        return f"{self.name} (User: {self.user.username})"

class Driver(models.Model):
    name = models.CharField(max_length=100)
    team = models.ForeignKey(Constructor, on_delete=models.CASCADE)
    dnf = models.BooleanField(default=False)
    points = models.FloatField(default=0)

    def __str__(self):
        return self.name

class Race(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField(null=True, blank=True)
    has_sprint = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class RacePicks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    team_1 = models.ForeignKey(Constructor, related_name='team_1', on_delete=models.CASCADE)
    team_2 = models.ForeignKey(Constructor, related_name='team_2', on_delete=models.CASCADE)
    team_3 = models.ForeignKey(Constructor, related_name='team_3', on_delete=models.CASCADE)
    red_bull_racing_driver = models.ForeignKey(Driver, related_name='red_bull_racing_driver', on_delete=models.CASCADE, default=1)
    scuderia_ferrari_driver = models.ForeignKey(Driver, related_name='scuderia_ferrari_driver', on_delete=models.CASCADE, default=1)
    mclaren_racing_driver = models.ForeignKey(Driver, related_name='mclaren_racing_driver', on_delete=models.CASCADE, default=1)
    mercedes_amg_petronas_driver = models.ForeignKey(Driver, related_name='mercedes_amg_petronas_driver', on_delete=models.CASCADE, default=1)
    aston_martin_driver = models.ForeignKey(Driver, related_name='aston_martin_driver', on_delete=models.CASCADE, default=1)
    alpine_driver = models.ForeignKey(Driver, related_name='alpine_driver', on_delete=models.CASCADE, default=1)
    visa_cash_app_rb_driver = models.ForeignKey(Driver, related_name='visa_cash_app_rb_driver', on_delete=models.CASCADE, default=1)
    kick_sauber_driver = models.ForeignKey(Driver, related_name='kick_sauber_driver', on_delete=models.CASCADE, default=1)
    haas_driver = models.ForeignKey(Driver, related_name='haas_driver', on_delete=models.CASCADE, default=1)
    williams_driver = models.ForeignKey(Driver, related_name='williams_driver', on_delete=models.CASCADE, default=1)
    fastest_lap_driver = models.ForeignKey(Driver, related_name='fastest_lap_driver', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"Race Picks for {self.user.username} - {self.race.name}"

class RaceResult(models.Model):
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    position = models.IntegerField()
    is_dnf = models.BooleanField(default=False)
    is_fastest_lap = models.BooleanField(default=False)
    points = models.FloatField(default=0)

    def save(self, *args, **kwargs):
        points_dict = {
            1: 34, 2: 31, 3: 28, 4: 25, 5: 22.5, 6: 20, 7: 17.5,
            8: 15, 9: 13, 10: 11, 11: 9, 12: 7.5, 13: 6, 14: 4.5,
            15: 3.5, 16: 2.75, 17: 2, 18: 1.5, 19: 1, 20: 0.5
        }
        if self.is_dnf:
            self.points = 0
        else:
            self.points = points_dict.get(self.position, 0)
        super().save(*args, **kwargs)
        self.update_user_picks()

    def update_user_picks(self):
        race_picks = RacePicks.objects.filter(race=self.race)
        for pick in race_picks:
            if self.driver in [
                pick.red_bull_racing_driver, pick.scuderia_ferrari_driver, pick.mclaren_racing_driver,
                pick.mercedes_amg_petronas_driver, pick.aston_martin_driver, pick.alpine_driver,
                pick.visa_cash_app_rb_driver, pick.kick_sauber_driver, pick.haas_driver,
                pick.williams_driver
            ]:
                pick.user.team.points += self.points

            if self.driver.team in [pick.team_1, pick.team_2, pick.team_3]:
                pick.user.team.points += self.points

            if self.is_fastest_lap and pick.fastest_lap_driver == self.driver:
                pick.user.team.points += 7
                pick.user.team.save()

            pick.user.team.save()

    def __str__(self):
        return f"{self.driver.name} - {self.race.name} - Position: {self.position} - Points: {self.points}"

class SprintResult(models.Model):
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    position = models.IntegerField()
    is_dnf = models.BooleanField(default=False)
    is_fastest_lap = models.BooleanField(default=False)
    points = models.FloatField(default=0)

    def save(self, *args, **kwargs):
        points_dict = {
            1: 17, 2: 15.5, 3: 14, 4: 12.5, 5: 11.25, 6: 10, 7: 8.75,
            8: 7.5, 9: 6.5, 10: 5.5, 11: 4.5, 12: 3.75, 13: 3, 14: 2.25,
            15: 1.75, 16: 1.375, 17: 1, 18: 0.75, 19: 0.5, 20: 0.25
        }
        if self.is_dnf:
            self.points = 0
        else:
            self.points = points_dict.get(self.position, 0)
        super().save(*args, **kwargs)
        self.update_user_picks()

    def update_user_picks(self):
        race_picks = RacePicks.objects.filter(race=self.race)
        for pick in race_picks:
            if self.driver in [
                pick.red_bull_racing_driver, pick.scuderia_ferrari_driver, pick.mclaren_racing_driver,
                pick.mercedes_amg_petronas_driver, pick.aston_martin_driver, pick.alpine_driver,
                pick.visa_cash_app_rb_driver, pick.kick_sauber_driver, pick.haas_driver,
                pick.williams_driver
            ]:
                pick.user.team.points += self.points

            if self.driver.team in [pick.team_1, pick.team_2, pick.team_3]:
                pick.user.team.points += self.points

            if self.is_fastest_lap and pick.fastest_lap_driver == self.driver:
                pick.user.team.points += 3.5
                pick.user.team.save()

            pick.user.team.save()

    def __str__(self):
        return f"{self.driver.name} - {self.race.name} - Position: {self.position} - Points: {self.points}"

class Matchup(models.Model):
    race = models.ForeignKey(Race, on_delete=models.CASCADE)
    team_a = models.ForeignKey(Team, related_name='matchup_team_a', on_delete=models.CASCADE)
    team_b = models.ForeignKey(Team, related_name='matchup_team_b', on_delete=models.CASCADE)
    winner = models.ForeignKey(Team, related_name='matchup_winner', on_delete=models.SET_NULL, null=True, blank=True)

    def determine_winner(self):
        team_a_points = self.team_a.points
        team_b_points = self.team_b.points
        self.winner = self.team_a if team_a_points > team_b_points else self.team_b
        self.save()

    def __str__(self):
        return f"Matchup {self.team_a.name} vs {self.team_b.name} - Race: {self.race.name}"
