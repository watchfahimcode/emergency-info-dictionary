from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile (models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    about=models.CharField(max_length=100,blank=True)
    profile_picture=models.ImageField(default='default.jpg', upload_to='Profile_picture')
    def __str__(self):
        return self.user.username
