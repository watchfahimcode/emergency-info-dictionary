# Generated by Django 3.1.7 on 2021-04-08 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bazar', '0004_remove_bazar_union'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bazar',
            old_name='bazar_name',
            new_name='name',
        ),
    ]
