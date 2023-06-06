from accounts.models import User
from django.db import models
from accounts.models import Address
import datetime
# Create your models here.
current_date = datetime.date.today()

class PickupRequest(models.Model):
    PICKUP_TYPE_CHOICES = (
        ('Waste', 'Waste'),
        ('Scrap', 'Scrap'),
    )

    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    pickup_type = models.CharField(max_length=10, choices=PICKUP_TYPE_CHOICES)
    pickup_date = models.DateField()
    pickup_address = models.ForeignKey(Address,on_delete=models.CASCADE)
    pickup_latitude = models.DecimalField(max_digits=50, decimal_places=30, blank=True, null=True)
    pickup_longitude = models.DecimalField(max_digits=50, decimal_places=30, blank=True, null=True)
    weight = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,default=50)
    special_instructions = models.TextField(blank=True)
    pickup_status = models.CharField(max_length=20, default='pending')
    pickup_day  = models.IntegerField(default = current_date.day)
    pickup_month  = models.IntegerField(default = current_date.month)
    pickup_year  = models.IntegerField(default = current_date.year)

    def __str__(self):
        return f"PickupRequest - {self.pk}"




class Item(models.Model):
    pickup_request = models.ForeignKey(PickupRequest, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # image = models.ImageField(upload_to='pickup_images/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Feedback(models.Model):
    pickup_request = models.OneToOneField(PickupRequest, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback for PickupRequest - {self.pickup_request.pk}"

class Invoice(models.Model):
    pickup_request = models.OneToOneField(PickupRequest, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Invoice for PickupRequest - {self.pickup_request.pk}"