from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=15, primary_key=True)
    date_formed = models.DateField()

class Driver(models.Model):
    name = models.CharField(max_length=30, primary_key=True)
    dob = models.DateField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE)


