# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0003_auto_20141106_1311'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='date_joined',
        ),
    ]
