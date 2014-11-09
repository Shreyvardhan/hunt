# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0005_auto_20141109_0423'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='level',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
