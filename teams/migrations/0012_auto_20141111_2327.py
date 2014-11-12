# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0011_team_last_level_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='name',
            field=models.CharField(max_length=254, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='member',
            name='team',
            field=models.ForeignKey(related_name='members', blank=True, to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
