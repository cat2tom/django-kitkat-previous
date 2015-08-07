# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kitkat', '0006_auto_20150703_0450'),
    ]

    operations = [
        migrations.CreateModel(
            name='TemperaturePressure',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('temperature', models.FloatField()),
                ('pressure', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='TestEquipment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('electrometer', models.ForeignKey(blank=True, to='kitkat.Electrometer', null=True)),
                ('ionchamber', models.ForeignKey(blank=True, to='kitkat.IonChamber', null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='qatestresult',
            name='electrometer_id',
        ),
        migrations.RemoveField(
            model_name='qatestresult',
            name='ionchamber_id',
        ),
        migrations.AddField(
            model_name='testequipment',
            name='qa_test_result_id',
            field=models.ForeignKey(to='kitkat.QATestResult'),
        ),
        migrations.AddField(
            model_name='temperaturepressure',
            name='qa_test_result_id',
            field=models.ForeignKey(to='kitkat.QATestResult'),
        ),
    ]
