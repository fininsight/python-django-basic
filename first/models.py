from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=10)
    math = models.IntegerField()
    science = models.IntegerField()
    english = models.IntegerField()