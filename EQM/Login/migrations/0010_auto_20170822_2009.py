# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-22 14:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0009_auto_20170822_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='LoginId',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='login',
            name='password',
            field=models.CharField(max_length=30),
        ),
    ]
