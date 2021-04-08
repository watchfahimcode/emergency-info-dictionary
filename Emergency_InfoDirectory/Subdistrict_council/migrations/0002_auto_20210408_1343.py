# Generated by Django 3.1.7 on 2021-04-08 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Subdistrict_council', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subdistrict_counil',
            fields=[
                ('id', models.IntegerField(db_column='id', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='name', max_length=30)),
                ('chairman', models.CharField(db_column='chairman', max_length=40)),
                ('contact_no', models.CharField(db_column='contact_no', max_length=30)),
                ('subdistrict', models.CharField(db_column='subdistrict', max_length=30)),
                ('district', models.CharField(db_column='district', max_length=20)),
                ('division', models.CharField(db_column='division', max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Subdistrict_council',
        ),
    ]
