# Generated by Django 4.2.7 on 2023-11-27 00:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_bookinguser_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='boatschedule',
            old_name='to_lacation',
            new_name='to_location',
        ),
    ]
