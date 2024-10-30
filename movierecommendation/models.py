from django.db import models

# Create your models here.
class Genre(models.Model):
    name=models.CharField(max_length=100)
    
class Movie(models.Model):
    title=models.CharField(max_length=255)
    genre=models.ForeignKey(Genre,on_delete=models.CASCADE)
