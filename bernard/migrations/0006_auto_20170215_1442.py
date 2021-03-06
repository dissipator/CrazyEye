# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-15 06:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bernard', '0005_auto_20170215_1016'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schedulelog',
            old_name='date',
            new_name='start_date',
        ),
        migrations.AddField(
            model_name='schedulelog',
            name='end_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='schedulelog',
            name='errors',
            field=models.TextField(blank=True, null=True),
        ),
    ]
