from django.db import models

# Create your models here.
class Police_station(models.Model):
    police_station_id = models.IntegerField(primary_key=True, db_column='police_station_id')
    name = models.CharField(max_length=30, db_column='name')
    address = models.CharField(max_length=40, db_column='address')
    contact_no = models.CharField(max_length=30, db_column='contact_no')
    subdistrict = models.CharField(max_length=30, db_column='subdistrict')
    district = models.CharField(max_length=20, db_column='district')
    division = models.CharField(max_length=20, db_column='division')

    def __str__(self):
        return self.name+","+self.subdistrict+","+self.district+","+self.division
