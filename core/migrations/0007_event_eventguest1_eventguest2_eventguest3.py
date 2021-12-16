# Generated by Django 3.2.7 on 2021-11-09 04:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0006_delete_customads'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventGuest1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='Guest_images')),
                ('name', models.CharField(default='', max_length=255)),
                ('designation', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='EventGuest2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='Guest_images')),
                ('name', models.CharField(default='', max_length=255)),
                ('designation', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='EventGuest3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='Guest_images')),
                ('name', models.CharField(default='', max_length=255)),
                ('designation', models.CharField(default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=255)),
                ('place', models.CharField(default='', max_length=255)),
                ('date', models.CharField(default='', max_length=255)),
                ('time_start', models.CharField(default='', max_length=255)),
                ('time_end', models.CharField(default='', max_length=255)),
                ('writer', models.CharField(default='', max_length=255)),
                ('guest1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.eventguest1')),
                ('guest2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.eventguest2')),
                ('guest3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='core.eventguest3')),
            ],
        ),
    ]
