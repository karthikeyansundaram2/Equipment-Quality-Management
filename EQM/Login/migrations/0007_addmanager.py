# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-22 13:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0006_auto_20170822_1729'),
    ]

    operations = [
        migrations.CreateModel(
            name='addmanager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ManagerName', models.CharField(max_length=100)),
                ('ManagerId', models.CharField(max_length=100)),
                ('Department', models.CharField(max_length=100)),
                ('MobileNumber', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]