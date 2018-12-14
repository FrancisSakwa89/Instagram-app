# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-14 15:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0003_auto_20181214_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='caption',
            field=models.TextField(default='photo'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='photos/'),
        ),
        migrations.AlterField(
            model_name='image',
            name='name',
            field=models.CharField(default='people', max_length=60),
        ),
        migrations.AlterField(
            model_name='image',
            name='poster',
            field=models.ForeignKey(default='now', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='image',
            name='postername',
            field=models.CharField(default='me', max_length=60),
        ),
    ]
