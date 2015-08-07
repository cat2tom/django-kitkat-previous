# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kitkat', '0002_auto_20150601_1147'),
    ]

    operations = [
        migrations.CreateModel(
            name='Electrometer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('electrometer_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='IonChamber',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('val1', models.IntegerField()),
                ('val2', models.IntegerField()),
                ('expected_reading_6MV', models.FloatField()),
                ('expected_reading_18MV', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='PhotonCheckCalibration',
            fields=[
                ('generictestinstance_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='kitkat.GenericTestInstance')),
            ],
            bases=('kitkat.generictestinstance',),
        ),
    ]
