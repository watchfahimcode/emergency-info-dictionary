from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.CharField(max_length=250, blank=True)
    profile_picture = models.ImageField(default='default.jpg',upload_to='profile_pictures')


    def __str__(self):
        return self.user.username


#new Model for Division
class Division(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

#new Model for District
class District(models.Model):
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

#new Model for Subdistrict
class Subdistrict(models.Model):
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete= models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
