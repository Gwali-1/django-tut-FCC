from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

# Create your models here.


User = get_user_model()


# class User(AbstractUser):
#     pass

class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="profile")
    id_user = models.IntegerField()
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    profile = models.ImageField(upload_to="profile_images", default="wink.png")

    def __str__(self):
        return f"{self.user.username}'s profile"



