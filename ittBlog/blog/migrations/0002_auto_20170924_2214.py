# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-24 22:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='mod_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='n_comments',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='n_pingbacks',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='pub_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='entry',
            name='rating',
            field=models.IntegerField(null=True),
        ),
    ]