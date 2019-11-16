from django.db import models
from django.contrib.auth.models import User
from pyuploadcare.dj.models import ImageField

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    profile_pic = ImageField(blank=True, manual_crop="800x800")
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username


class Post(models.Model):
    image = ImageField(blank=False, manual_crop="800x800")
    name = models.CharField(max_length=144, blank=True, default="Post")
    caption = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    profile = models.ForeignKey(User)
    
    def __str__(self):
        return f"{self.name} - {self.caption}"

class Comment(models.Model):
    comment = models.CharField(max_length=256)
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post)

    def __str__(self):
        return self.comment


