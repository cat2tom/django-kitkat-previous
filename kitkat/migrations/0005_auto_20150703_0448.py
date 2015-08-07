# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kitkat', '0004_auto_20150625_0450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qatestresult',
            name='electrometer_id',
            field=models.ForeignKey(to='kitkat.Electrometer', blank=True),
        ),
        migrations.AlterField(
            model_name='qatestresult',
            name='ionchamber_id',
            field=models.ForeignKey(to='kitkat.IonChamber', blank=True),
        ),
    ]
