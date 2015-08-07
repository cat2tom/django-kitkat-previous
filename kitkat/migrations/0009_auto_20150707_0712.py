# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kitkat', '0008_auto_20150705_0747'),
    ]

    operations = [
        migrations.RenameField(
            model_name='floataveragevalue',
            old_name='value',
            new_name='mean_value',
        ),
        migrations.AddField(
            model_name='qatestattributedefinition',
            name='form_order',
            field=models.SmallIntegerField(default=0),
            preserve_default=False,
        ),
    ]
