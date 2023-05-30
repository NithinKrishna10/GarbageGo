from django.contrib import admin
from .models import Scrap,ScrapCategory
# Register your models here.


admin.site.register(ScrapCategory)
admin.site.register(Scrap)