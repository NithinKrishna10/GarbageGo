from django.db import models

# Create your models here.


class WasteCategory(models.Model):
    name = models.CharField(max_length=100)

class Waste(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(WasteCategory, on_delete=models.CASCADE)
    description = models.TextField()
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='scrap_images/')

    created_at = models.DateTimeField(auto_now_add=True)

