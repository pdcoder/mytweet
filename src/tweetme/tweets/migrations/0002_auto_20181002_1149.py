# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-10-02 11:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tweets',
            options={'verbose_name': 'Tweet', 'verbose_name_plural': 'Tweets'},
        ),
    ]
