# Generated by Django 3.1.7 on 2021-03-25 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('hospital_id', models.IntegerField(db_column='hospital_id', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='name', max_length=40)),
                ('category', models.CharField(db_column='category', max_length=40)),
                ('address', models.CharField(db_column='address', max_length=50)),
                ('contact_no', models.CharField(db_column='contact_no', max_length=20)),
                ('subdistrict', models.CharField(db_column='subdistrict', max_length=30)),
                ('district', models.CharField(db_column='district', max_length=30)),
                ('division', models.CharField(db_column='division', max_length=15)),
            ],
        ),
    ]
