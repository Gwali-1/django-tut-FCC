from django.contrib import admin
from .models import Profile


# Register your models here.

class Profileadmin(admin.ModelAdmin):
    list_display = ("id","id_user","location","bio")


admin.site.register(Profile)