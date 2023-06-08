from django.contrib import admin
from .models import PickupRequest,Item,Invoice,PickupTracker
# Register your models here.

admin.site.register(PickupRequest)
admin.site.register(Item)
admin.site.register(Invoice)
admin.site.register(PickupTracker)