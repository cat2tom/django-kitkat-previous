# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kitkat', '0002_auto_20150623_0744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qatestdefinition',
            name='frequency',
            field=models.CharField(default=b'Fred', max_length=20),
        ),
        migrations.AlterField(
            model_name='qatestdefinition',
            name='test_name',
            field=models.CharField(default=b'Fred', max_length=50),
        ),
    ]
