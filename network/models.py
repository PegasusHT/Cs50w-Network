from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    followers = models.IntegerField(default=0)
    following_num = models.IntegerField(default=0)
    pass

class Posts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="of_user")
    likes = models.IntegerField(default=0)
    content = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    liked_by = models.ManyToManyField(User, blank=True, related_name= "Liked")

    def __str__(self):
        return self.user.username

class Followings(models.Model):
    following = models.ManyToManyField(User, blank=True, related_name="fwing_users")
    followed_by = models.ManyToManyField(User, blank=True, related_name="fwby_users")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followings")

    def __str__(self):
        return self.user.username