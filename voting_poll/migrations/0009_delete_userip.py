# Generated by Django 3.1.7 on 2021-10-05 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voting_poll', '0008_userip'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserIp',
        ),
    ]