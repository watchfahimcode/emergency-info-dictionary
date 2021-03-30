from django.db import models

# Create your models here.
class Subdistrict_administration(models.Model):
    id = models.IntegerField(primary_key=True, db_column='id')
    name = models.CharField(max_length=30, db_column='name')
    uno = models.CharField(max_length=40, db_column='uno')
    contact_no = models.CharField(max_length=30, db_column='contact_no')
    subdistrict = models.CharField(max_length=30, db_column='subdistrict')
    district = models.CharField(max_length=20, db_column='district')
    division = models.CharField(max_length=20, db_column='division')