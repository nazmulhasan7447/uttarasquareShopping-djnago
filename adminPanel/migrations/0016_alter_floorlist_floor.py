# Generated by Django 3.2.7 on 2021-11-23 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminPanel', '0015_floordetails_floor_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='floorlist',
            name='floor',
            field=models.CharField(choices=[('0', 'Ground Floor'), ('1', '1st Floor'), ('2', '2nd Floor'), ('3', '3rd Floor'), ('4', '4th Floor'), ('5', '5th Floor'), ('6', '6th Floor'), ('7', '7th Floor'), ('8', '8th Floor'), ('9', '9th Floor'), ('10', '10th Floor'), ('11', '11th Floor'), ('12', '12th Floor'), ('13', '13th Floor'), ('14', '14th Floor')], default='', max_length=255),
        ),
    ]
