# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-05 20:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_contact'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contact',
        ),
    ]
