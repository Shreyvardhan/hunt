# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0006_team_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='level',
            field=models.IntegerField(default=0, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(unique=True, max_length=254, verbose_name='Name'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='team',
            name='rank',
            field=models.IntegerField(default=9001, null=True, editable=False, blank=True),
            preserve_default=True,
        ),
    ]
