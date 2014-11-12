# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0015_log'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='level',
            field=models.IntegerField(default=0, null=True, verbose_name='Level', blank=True),
            preserve_default=True,
        ),
    ]
