# Generated by Django 3.2.7 on 2021-11-09 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20211109_1030'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='guest1_img',
            field=models.ImageField(blank=True, null=True, upload_to='Guest_images'),
        ),
        migrations.AddField(
            model_name='event',
            name='guest2_img',
            field=models.ImageField(blank=True, null=True, upload_to='Guest_images'),
        ),
        migrations.AddField(
            model_name='event',
            name='guest3_img',
            field=models.ImageField(blank=True, null=True, upload_to='Guest_images'),
        ),
    ]
