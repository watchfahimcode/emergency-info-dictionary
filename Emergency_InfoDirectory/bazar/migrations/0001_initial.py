# Generated by Django 3.1.7 on 2021-03-24 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bazar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bazar_id', models.IntegerField()),
                ('bazar_name', models.CharField(max_length=50)),
                ('contact_no', models.IntegerField()),
                ('address', models.CharField(max_length=50)),
                ('union', models.CharField(max_length=50)),
                ('subdistrict', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
                ('division', models.CharField(max_length=50)),
            ],
        ),
    ]
