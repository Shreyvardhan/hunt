# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0004_remove_team_date_joined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='team',
            field=models.ForeignKey(related_name='members', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
