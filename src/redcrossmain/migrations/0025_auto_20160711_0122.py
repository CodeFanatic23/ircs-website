# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-10 19:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('redcrossmain', '0024_auto_20160711_0037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blooddonation',
            name='date',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='blooddonation',
            name='date_of_birth',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='blooddonation',
            name='time',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]