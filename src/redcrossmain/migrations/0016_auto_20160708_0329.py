# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-07 21:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('redcrossmain', '0015_rti'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rti',
            old_name='teders',
            new_name='tenders',
        ),
    ]
