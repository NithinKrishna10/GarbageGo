from django.db import models

class ScrapCategory(models.Model):
    name = models.CharField(max_length=100)

class Scrap(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(ScrapCategory, on_delete=models.CASCADE)
    description = models.TextField()
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='scrap_images/')

    created_at = models.DateTimeField(auto_now_add=True)
