# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_auto_20150326_1420'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorycomment',
            name='title',
            field=models.CharField(default=b'null', max_length=100),
            preserve_default=True,
        ),
    ]
