# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0014_auto_20141111_2356'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='Time', null=True)),
                ('attempt', models.CharField(max_length=254, null=True, blank=True)),
                ('correct', models.BooleanField(default=False, verbose_name='Sahi tha ki nahin?')),
                ('team', models.ForeignKey(related_name='logs', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
