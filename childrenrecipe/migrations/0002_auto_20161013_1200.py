# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-10-13 12:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('childrenrecipe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recommend',
            name='introduce',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recommend',
            name='name',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
