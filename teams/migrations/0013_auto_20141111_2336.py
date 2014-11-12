# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0012_auto_20141111_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='grade',
            field=models.IntegerField(max_length=2, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='member',
            name='section',
            field=models.CharField(max_length=2, null=True, blank=True),
            preserve_default=True,
        ),
    ]
