from django.contrib import admin
from . models import Post,Category,Comments,Tag
# Register your models here.


admin.site.register(Category)
admin.site.register(Comments)
admin.site.register(Post)
admin.site.register(Tag)

