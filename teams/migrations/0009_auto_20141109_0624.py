# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0008_auto_20141109_0601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='cheated',
            field=models.BooleanField(default=False, verbose_name='Cheaters?'),
            preserve_default=True,
        ),
    ]
