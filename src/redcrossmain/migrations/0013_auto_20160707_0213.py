# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-06 20:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('redcrossmain', '0012_post_title_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title_slug',
            field=models.SlugField(editable=False),
        ),
    ]
