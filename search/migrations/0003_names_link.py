# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-25 18:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_auto_20161125_1240'),
    ]

    operations = [
        migrations.AddField(
            model_name='names',
            name='link',
            field=models.CharField(default=django.utils.timezone.now, max_length=500),
            preserve_default=False,
        ),
    ]
