# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-11 17:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('redcrossmain', '0026_auto_20160711_0139'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=40, null=True)),
                ('date', models.DateField(null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='disease6m',
            name='val',
            field=models.CharField(blank=True, choices=[(1, 'Unexplained Weight Loss'), (2, 'Ear piercing'), (3, 'Repeated Diarrhoea'), (4, 'Dental Extraction'), (5, 'Swollen Gland'), (6, 'Major Surgery'), (7, 'Continuous Low-grade fever'), (8, 'Minor Surgery'), (9, 'Tatooing'), (10, 'Blood Transfusion')], max_length=40, null=True),
        ),
    ]