# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-26 10:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_image_image_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='category_name',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='name',
            new_name='location_name',
        ),
    ]
