# Generated by Django 3.2.7 on 2021-10-16 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminPanel', '0007_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='added_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]