# Generated by Django 2.2.2 on 2019-08-26 05:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20190825_0318'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='event_pw',
            new_name='event_code',
        ),
    ]