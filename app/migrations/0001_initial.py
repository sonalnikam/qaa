# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-14 10:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='car_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=400)),
                ('from_id', models.CharField(max_length=400)),
                ('to', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Registern',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=400)),
                ('Username', models.CharField(max_length=400)),
                ('Password', models.CharField(max_length=400)),
                ('CPassword', models.CharField(max_length=400)),
            ],
        ),
    ]
