from django.contrib import admin
from .models import Profile,Post,LikedPost


# Register your models here.

class Profileadmin(admin.ModelAdmin):
    list_display = ("id","id_user","location","bio")


admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(LikedPost)