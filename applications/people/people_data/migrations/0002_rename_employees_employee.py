# Generated by Django 4.2.4 on 2023-09-21 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people_data', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Employees',
            new_name='Employee',
        ),
    ]
