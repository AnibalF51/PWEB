# Generated by Django 3.1.2 on 2020-10-23 22:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0007_auto_20201023_2346'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='birthday',
            new_name='date_birthday',
        ),
        migrations.RenameField(
            model_name='client',
            old_name='sexo',
            new_name='gender',
        ),
    ]
