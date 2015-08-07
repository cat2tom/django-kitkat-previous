# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kitkat', '0007_auto_20150704_0218'),
    ]

    operations = [
        migrations.AddField(
            model_name='qatestdefinition',
            name='temp_pressure_required',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='qatestdefinition',
            name='test_equip_required',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]
