# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-16 16:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_treasure_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='treasure',
            name='img_url',
        ),
    ]
