# Generated by Django 3.2.7 on 2021-11-16 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_restaurants'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsLetter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('email', models.CharField(blank=True, default='', max_length=255, null=True)),
            ],
        ),
    ]
