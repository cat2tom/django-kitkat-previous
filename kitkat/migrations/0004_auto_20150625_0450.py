# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kitkat', '0003_remove_qatestdefinition_daftness'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qatestdefinition',
            name='frequency',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='qatestdefinition',
            name='test_name',
            field=models.CharField(max_length=50),
        ),
    ]
