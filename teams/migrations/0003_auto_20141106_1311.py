# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_auto_20141106_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='grade',
            field=models.IntegerField(blank=True, max_length=2, null=True, choices=[(6, b'6'), (7, b'7'), (8, b'8'), (9, b'9'), (10, b'10'), (11, b'11'), (12, b'12')]),
            preserve_default=True,
        ),
    ]
