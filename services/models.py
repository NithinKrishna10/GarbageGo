from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    images = models.ImageField()


class Scrap(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category)
    description = models.TextField()
    weight = models.IntegerField(default=1)
    price = models.FloatField()
    image = models.ImageField()

class Waste(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category)
    description = models.TextField()
    weight = models.IntegerField(default=1)
    price = models.FloatField()
    image = models.ImageField()