from django.db import models
from waste.models import Waste,WasteCategory
from accounts.models import Address,User
import datetime
# Create your models here.
current_date = datetime.date.today()


    # quantity = models.PositiveIntegerField()
    # email = models.EmailField()
class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    ]

    customer = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    waste_type = models.ForeignKey(WasteCategory,on_delete=models.CASCADE)
    address = models.ForeignKey(Address,on_delete=models.CASCADE)
    pickup_date = models.DateField()
    additional_notes = models.TextField(blank=True)
    is_ordered = models.BooleanField(default=False)
    waste_weight = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    waste_weight = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    
    price = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES,default='Booked')
    Order_day  = models.IntegerField(default = current_date.day)
    Order_month  = models.IntegerField(default = current_date.month)
    Order_year  = models.IntegerField(default = current_date.year)

    def __str__(self):
        return f"Order #{self.pk} - {self.customer.name}"


class Order_details(models.Model):
    order_id = models.ForeignKey(Order,on_delete=models.CASCADE)







class OrderDetail(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('canceled', 'Canceled'),
    ]

    waste_weight = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return f"Order Detail #{self.pk} - Order #{self.order.pk}"