# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-22 08:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0003_addamc_addemployee_addmachines_changeallocation'),
    ]

    operations = [
        migrations.AddField(
            model_name='changeallocation',
            name='Status',
            field=models.CharField(choices=[('active', 'ACTIVE'), ('ordered', 'ORDERED')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='addamc',
            name='Specification',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='changeallocation',
            name='ExistingUser',
            field=models.CharField(max_length=50),
        ),
    ]
