# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kitkat', '0005_auto_20150703_0448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qatestresult',
            name='electrometer_id',
            field=models.ForeignKey(blank=True, to='kitkat.Electrometer', null=True),
        ),
        migrations.AlterField(
            model_name='qatestresult',
            name='ionchamber_id',
            field=models.ForeignKey(blank=True, to='kitkat.IonChamber', null=True),
        ),
    ]
