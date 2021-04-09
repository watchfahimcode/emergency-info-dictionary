from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.CharField(max_length=250, blank=True)
    profile_picture = models.ImageField(default='default.jpg',upload_to='profile_pictures')


    def __str__(self):
        return self.user.username