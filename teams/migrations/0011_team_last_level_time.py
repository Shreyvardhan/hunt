# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0010_auto_20141111_2302'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='last_level_time',
            field=models.DateTimeField(null=True, verbose_name='Time When Last Level Was Cleared', blank=True),
            preserve_default=True,
        ),
    ]
