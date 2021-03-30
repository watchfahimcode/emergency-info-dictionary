# Generated by Django 3.1.7 on 2021-03-25 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('hotel_id', models.IntegerField(db_column='hotel_id', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='name', max_length=30)),
                ('address', models.CharField(db_column='address', max_length=40)),
                ('contact_no', models.CharField(db_column='contact_no', max_length=30)),
                ('subdistrict', models.CharField(db_column='subdistrict', max_length=30)),
                ('district', models.CharField(db_column='district', max_length=20)),
                ('division', models.CharField(db_column='division', max_length=20)),
            ],
        ),
    ]
