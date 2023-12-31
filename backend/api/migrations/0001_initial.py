# Generated by Django 4.2.7 on 2023-11-26 14:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BoatSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_location', models.CharField(max_length=300)),
                ('to_lacation', models.CharField(max_length=300)),
                ('departure_datetime', models.DateTimeField()),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='FerryType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='BookingUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=300)),
                ('last_name', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=254)),
                ('nationality', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('total_ticket', models.SmallIntegerField()),
                ('is_paid', models.BooleanField(default=False)),
                ('boatschedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.boatschedule')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.bookinguser')),
            ],
        ),
        migrations.AddField(
            model_name='boatschedule',
            name='ferry_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.ferrytype'),
        ),
    ]
