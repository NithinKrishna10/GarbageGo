from django.db import models

# Create your models here.



class WasteCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='waste_category', blank=True)
    recyclable = models.BooleanField(default=False)
    hazardous = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
class Waste(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(WasteCategory, on_delete=models.CASCADE,default=None)
    description = models.TextField()
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='scrap_images/')

    created_at = models.DateTimeField(auto_now_add=True)

