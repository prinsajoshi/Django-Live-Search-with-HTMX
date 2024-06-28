from django.db import models

# Create your models here.
class Movie(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField(max_length=1000)
    year=models.IntegerField(default=2000)