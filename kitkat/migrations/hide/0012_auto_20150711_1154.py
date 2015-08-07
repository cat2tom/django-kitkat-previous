# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('kitkat', '0011_auto_20150711_1154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qatestresult',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]
