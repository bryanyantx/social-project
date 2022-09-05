# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2022-08-30 06:17
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 30, 6, 17, 32, 962982, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 30, 6, 17, 32, 962440, tzinfo=utc)),
        ),
    ]
