from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100)
    
class Magazine(models.Model):
    title=models.CharField(max_length=100)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
