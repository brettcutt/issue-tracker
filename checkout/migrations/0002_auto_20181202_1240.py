# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-02 02:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('checkout', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('features', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='upvote',
            name='upvoted_feature',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='features.Features'),
        ),
        migrations.AddField(
            model_name='upvote',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
