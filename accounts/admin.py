from django.contrib import admin

# Register your models here.
from .models import Address,City,UserProfile,User,District


admin.site.register(User)
admin.site.register(Address)
admin.site.register(UserProfile)
admin.site.register(City)
admin.site.register(District)
# admin.site.register()