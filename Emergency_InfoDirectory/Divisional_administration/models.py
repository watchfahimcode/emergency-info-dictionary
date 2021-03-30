from django.db import models


# Create your models here.

class Divisional_administration(models.Model):
    id = models.IntegerField(primary_key=True, db_column='id')
    name = models.CharField(max_length=40, db_column='name')
    commissioner = models.CharField(max_length=50, db_column='commissioner')
    contact_no = models.CharField(max_length=20, db_column='contact_no')
    division = models.CharField(max_length=15, db_column='division')
