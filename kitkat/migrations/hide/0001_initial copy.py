# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
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
            name='GenericTestInstance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('test_type', models.CharField(max_length=20, choices=[(b'', b'-------'), (b'Daily Photon Test', b'Daily Photon Test'), (b'Other Test', b'Other Test')])),
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
            name='Machine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('machine_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='QAFloatComponent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('num', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='QATestAttributeDefinition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(max_length=30)),
                ('attribute_type', models.CharField(max_length=30, choices=[(b'', b'-------'), (b'Bool Value', b'Bool Value'), (b'Float Value', b'Float Value'), (b'Float Average Value', b'Float Average Value'), (b'Calc Bool Value', b'Calc Bool Value'), (b'Calc Float Value', b'Calc Float Value')])),
            ],
        ),
        migrations.CreateModel(
            name='QATestAttributeResult',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='QATestDefinition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('test_name', models.CharField(max_length=50)),
                ('frequency', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='QATestResult',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('electrometer_id', models.ForeignKey(to='kitkat.Electrometer')),
                ('ionchamber_id', models.ForeignKey(to='kitkat.IonChamber')),
                ('machine_id', models.ForeignKey(to='kitkat.Machine')),
                ('qa_test_def_id', models.ForeignKey(to='kitkat.QATestDefinition')),
            ],
        ),
        migrations.CreateModel(
            name='TestInstance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reading', models.FloatField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('machine', models.ForeignKey(to='kitkat.Machine')),
            ],
        ),
        migrations.CreateModel(
            name='BoolValue',
            fields=[
                ('qatestattributeresult_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='kitkat.QATestAttributeResult')),
                ('value', models.BooleanField()),
            ],
            bases=('kitkat.qatestattributeresult',),
        ),
        migrations.CreateModel(
            name='CalcBoolValue',
            fields=[
                ('qatestattributeresult_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='kitkat.QATestAttributeResult')),
                ('value', models.BooleanField()),
            ],
            bases=('kitkat.qatestattributeresult',),
        ),
        migrations.CreateModel(
            name='CalcFloatValue',
            fields=[
                ('qatestattributeresult_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='kitkat.QATestAttributeResult')),
                ('value', models.FloatField()),
            ],
            bases=('kitkat.qatestattributeresult',),
        ),
        migrations.CreateModel(
            name='DailyPhotonTestInstance',
            fields=[
                ('generictestinstance_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='kitkat.GenericTestInstance')),
                ('reading', models.FloatField()),
            ],
            bases=('kitkat.generictestinstance',),
        ),
        migrations.CreateModel(
            name='FloatAverageValue',
            fields=[
                ('qatestattributeresult_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='kitkat.QATestAttributeResult')),
                ('entered_values', models.CharField(max_length=100)),
                ('value', models.FloatField()),
            ],
            bases=('kitkat.qatestattributeresult',),
        ),
        migrations.CreateModel(
            name='FloatValue',
            fields=[
                ('qatestattributeresult_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='kitkat.QATestAttributeResult')),
                ('value', models.FloatField()),
            ],
            bases=('kitkat.qatestattributeresult',),
        ),
        migrations.AddField(
            model_name='qatestattributeresult',
            name='qa_test_attr_def_id',
            field=models.ForeignKey(to='kitkat.QATestAttributeDefinition'),
        ),
        migrations.AddField(
            model_name='qatestattributeresult',
            name='qa_test_result_id',
            field=models.ForeignKey(to='kitkat.QATestResult'),
        ),
        migrations.AddField(
            model_name='qatestattributedefinition',
            name='qa_test_def_id',
            field=models.ForeignKey(to='kitkat.QATestDefinition'),
        ),
        migrations.AddField(
            model_name='generictestinstance',
            name='machine',
            field=models.ForeignKey(to='kitkat.Machine'),
        ),
    ]
