# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kitkat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ionchamber',
            name='expected_reading_18MV',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='ionchamber',
            name='expected_reading_6MV',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='ionchamber',
            name='val1',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ionchamber',
            name='val2',
            field=models.IntegerField(default=0),
        ),
    ]
