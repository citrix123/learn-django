# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-07 19:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=250)),
                ('title', models.CharField(max_length=250)),
                ('name', models.CharField(max_length=250)),
            ],
        ),
    ]
