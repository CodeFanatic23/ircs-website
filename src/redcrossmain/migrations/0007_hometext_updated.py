# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-06 10:43
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('redcrossmain', '0006_hometext'),
    ]

    operations = [
        migrations.AddField(
            model_name='hometext',
            name='updated',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 7, 6, 10, 43, 26, 436021, tzinfo=utc)),
            preserve_default=False,
        ),
    ]