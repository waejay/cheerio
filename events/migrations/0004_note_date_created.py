# Generated by Django 2.2.2 on 2019-08-26 05:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20190826_0501'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 26, 5, 29, 12, 825374)),
        ),
    ]
