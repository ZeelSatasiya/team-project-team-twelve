# Generated by Django 4.1.2 on 2022-11-25 22:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jwtapp', '0010_alter_mio_flight_schedule_time_passenger'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Passenger',
            new_name='Mio_passenger',
        ),
        migrations.AlterField(
            model_name='mio_flight_schedule',
            name='time',
            field=models.TimeField(default=datetime.time(22, 18, 49, 363639)),
        ),
    ]
