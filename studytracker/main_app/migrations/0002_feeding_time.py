# Generated by Django 4.0.6 on 2022-07-11 20:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feeding',
            name='time',
            field=models.DurationField(default=datetime.timedelta(0)),
        ),
    ]