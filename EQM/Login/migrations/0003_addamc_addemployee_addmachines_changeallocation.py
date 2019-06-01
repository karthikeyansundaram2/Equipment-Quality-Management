# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-21 13:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0002_auto_20170821_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddAMC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category', models.CharField(max_length=100)),
                ('SubCategory', models.CharField(max_length=100)),
                ('MachineName', models.CharField(max_length=100)),
                ('Make', models.CharField(max_length=10)),
                ('CurrentStatus', models.CharField(choices=[('inuse', 'INUSE'), ('idle', 'IDLE'), ('underrepair', 'UNDER REPAIR'), ('scrap', 'SCRAP'), ('discoursed', 'DISCOURSED')], default='', max_length=20)),
                ('PurchaseDate', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('Vendor', models.CharField(max_length=100)),
                ('Installationfees', models.CharField(max_length=100)),
                ('Specification', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='AddEmployee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EmployeeId', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='AddMachines',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MachineName', models.CharField(max_length=100)),
                ('Manufacturer', models.CharField(max_length=100)),
                ('Model', models.CharField(max_length=100)),
                ('SerialNumber', models.CharField(max_length=10)),
                ('Status', models.CharField(choices=[('active', 'ACTIVE'), ('ordered', 'ORDERED')], default='', max_length=20)),
                ('OperatingSystem', models.CharField(max_length=50)),
                ('Category', models.CharField(max_length=50)),
                ('EmployeeId', models.CharField(max_length=15)),
                ('Location', models.CharField(max_length=45)),
                ('Department', models.CharField(max_length=30)),
                ('SupportLink', models.CharField(max_length=100)),
                ('ServiceDate', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('Specification', models.CharField(max_length=300)),
                ('PurchasePrice', models.CharField(max_length=100)),
                ('Description', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='ChangeAllocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category', models.CharField(max_length=100)),
                ('SubCategory', models.CharField(max_length=100)),
                ('EarlierAllocationDate', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('NewDepartment', models.CharField(max_length=25)),
                ('ExistingDepartment', models.CharField(max_length=10)),
                ('ExistingUser', models.CharField(choices=[('active', 'ACTIVE'), ('ordered', 'ORDERED')], default='', max_length=20)),
                ('NewUser', models.CharField(max_length=50)),
                ('AllocationDate', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('MachineName', models.CharField(max_length=100)),
            ],
        ),
    ]
