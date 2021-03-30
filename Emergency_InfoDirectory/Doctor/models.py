from django.db import models


# Create your models here.
class Doctor(models.Model):
    doc_id = models.IntegerField(primary_key=True, db_column='doc_id')
    name = models.CharField(max_length=40, db_column='name')
    speciality = models.CharField(max_length=40, db_column='speciality')
    chamber_name = models.CharField(max_length=50, db_column='chamber_name')
    consultation_hour = models.CharField(max_length=20, db_column='consultation_hour')
    consultation_fee = models.IntegerField(db_column='consultation_fee')
    contact_no = models.CharField(max_length=20, db_column='contact_no')
    subdistrict = models.CharField(max_length=30, db_column='subdistrict')
    district = models.CharField(max_length=30, db_column='district')
    division = models.CharField(max_length=15, db_column='division')
