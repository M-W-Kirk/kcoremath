from django.db import models

# Create your models here.
class Score(models.Model):
    user = models.OneToOneField()
    attempts = models.IntegerField()
    correct = models.IntegerField()
    incorrect = models.IntegerField()
    date = models.DateField()
    proficiency = models.DecimalField()
    core_bucks = models.DecimalField()