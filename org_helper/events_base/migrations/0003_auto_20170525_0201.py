# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-25 02:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('events_base', '0002_auto_20170524_1002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventplace',
            name='date_add',
            field=models.DateTimeField(default=datetime.datetime(2017, 5, 25, 2, 1, 32, 512402, tzinfo=utc)),
        ),
    ]
