# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-28 22:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_auto_20181129_0913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upvote',
            name='upvoted_feature',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='features.Features'),
        ),
    ]