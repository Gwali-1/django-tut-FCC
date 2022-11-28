from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
import uuid
import datetime

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


class Post(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    user = models.CharField(max_length=100)
    image = models.ImageField(upload_to="post_images")
    caption = models.TextField()
    created_at = models.DateTimeField(default=datetime.datetime.now)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return f"post by {self.user}"


class LikedPost(models.Model):
    post_id = models.CharField(max_length=100)
    username = models.CharField(max_length=100)


    def __str__(self):
        return self.usernamexs
