# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kitkat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='qatestdefinition',
            name='daftness',
            field=models.ForeignKey(default=1, to='kitkat.TestInstance'),
            preserve_default=False,
        ),
    ]
