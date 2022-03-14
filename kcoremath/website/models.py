from django.db import models

# Create your models here.
class Score(models.Model):
    attempts = models.IntegerField()
    correct = models.IntegerField()
    incorrect = models.IntegerField()
    date = models.DateField()
    proficiency = models.DecimalField()