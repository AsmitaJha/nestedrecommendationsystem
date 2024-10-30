from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    favorite_genres=models.ManyToManyField("movierecommendation.Genre")
    favorite_music_genres=models.ManyToManyField("musicrecommendation.Genre")
    favorite_magazine_categories=models.ManyToManyField("magazinerecommendation.Category")
