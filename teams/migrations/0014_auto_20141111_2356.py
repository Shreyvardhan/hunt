# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0013_auto_20141111_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='grade',
            field=models.CharField(max_length=222, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='member',
            name='section',
            field=models.CharField(max_length=222, null=True, blank=True),
            preserve_default=True,
        ),
    ]
