# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-22 07:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20170422_0650'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='yzm_text',
        ),
        migrations.RemoveField(
            model_name='student',
            name='yzm_url',
        ),
    ]