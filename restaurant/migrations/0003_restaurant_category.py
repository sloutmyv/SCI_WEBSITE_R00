# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-06-04 16:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_restaurant_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='category',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
