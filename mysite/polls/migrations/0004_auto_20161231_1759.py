# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-31 16:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20161231_1627'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='random',
            name='rand',
        ),
        migrations.DeleteModel(
            name='Random',
        ),
    ]
