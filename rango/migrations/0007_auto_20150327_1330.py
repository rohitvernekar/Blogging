# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0006_remove_userprofile_categoryid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='desc',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='Address',
            field=models.TextField(default=b'Enter your address'),
            preserve_default=True,
        ),
    ]
