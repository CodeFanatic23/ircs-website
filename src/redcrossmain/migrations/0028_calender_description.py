# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-11 18:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('redcrossmain', '0027_auto_20160711_2328'),
    ]

    operations = [
        migrations.AddField(
            model_name='calender',
            name='description',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]