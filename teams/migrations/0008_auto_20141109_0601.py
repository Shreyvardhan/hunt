# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0007_auto_20141109_0558'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='cheated',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='team',
            name='level',
            field=models.IntegerField(default=0, null=True, verbose_name='Level', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='team',
            name='rank',
            field=models.IntegerField(default=9001, verbose_name='Rank', null=True, editable=False, blank=True),
            preserve_default=True,
        ),
    ]
