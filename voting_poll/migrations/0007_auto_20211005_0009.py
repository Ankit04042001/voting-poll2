# Generated by Django 3.1.7 on 2021-10-04 18:39

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voting_poll', '0006_auto_20211004_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio',
            name='click_sound',
            field=cloudinary.models.CloudinaryField(max_length=255),
        ),
    ]
