# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0009_auto_20141109_0624'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='rank',
        ),
        migrations.AlterField(
            model_name='member',
            name='grade',
            field=models.IntegerField(blank=True, max_length=2, null=True, choices=[(8, b'8'), (9, b'9'), (10, b'10'), (11, b'11'), (12, b'12')]),
            preserve_default=True,
        ),
    ]
