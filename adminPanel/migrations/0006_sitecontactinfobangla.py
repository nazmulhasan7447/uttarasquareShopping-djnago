# Generated by Django 3.2.7 on 2021-10-10 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminPanel', '0005_aboutus'),
    ]

    operations = [
        migrations.CreateModel(
            name='SiteContactInfoBangla',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('address', models.TextField()),
            ],
        ),
    ]
