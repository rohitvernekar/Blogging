# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categorycomment',
            options={},
        ),
        migrations.RemoveField(
            model_name='page',
            name='comment',
        ),
        migrations.AlterField(
            model_name='categorycomment',
            name='category',
            field=models.ForeignKey(to='rango.Category', null=True),
        ),
    ]
