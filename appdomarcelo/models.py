from django.db import models

# Create your models here.
class Jogos(models.Model):
  title = models.CharField(max_length=50)
  director = models.CharField(max_length=50)
  genre = models.CharField(max_length=50)
  release_date = models.DateField()

class rejogar(models.Model):
  OPTIONS = [
    ("N", "Never"),
    ("S", "Sometimes"),
    ("A", "Always"),
  ]
  title = models.CharField(max_length=50)
  how_often = models.CharField(max_length=1,choices=OPTIONS)
  enjoyability = models.IntegerField()
  