# Generated by Django 2.2.1 on 2019-06-06 07:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pract', '0005_auto_20190605_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petition',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 20, 7, 15, 43, 62084, tzinfo=utc)),
        ),
    ]