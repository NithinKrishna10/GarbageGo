from django.contrib import admin
from .models import WasteCategory,Waste
# Register your models here.

admin.site.register(Waste)
admin.site.register(WasteCategory)