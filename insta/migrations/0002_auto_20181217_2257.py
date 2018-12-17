# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-17 19:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='photo',
        ),
        migrations.AddField(
            model_name='profile',
            name='profpic',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='photos/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='image',
            name='caption',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='image',
            name='name',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='image',
            name='poster',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='image',
            name='postername',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='likes',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insta.Image'),
        ),
        migrations.AlterField(
            model_name='likes',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
