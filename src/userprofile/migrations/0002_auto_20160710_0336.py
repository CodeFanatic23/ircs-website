# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-09 22:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='favourite_movie',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='likes_cheese',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='contact_number',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='subscribe_to_newsletter',
            field=models.BooleanField(default=False),
        ),
    ]
