# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kitkat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GenericTestInstance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('test_type', models.CharField(max_length=20, choices=[(b'DailyPhotonTest', b'DailyPhotonTest'), (b'OtherTest', b'OtherTest')])),
            ],
        ),
        migrations.AlterField(
            model_name='testinstance',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.CreateModel(
            name='DailyPhotonTestInstance',
            fields=[
                ('generictestinstance_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='kitkat.GenericTestInstance')),
                ('reading', models.FloatField()),
            ],
            bases=('kitkat.generictestinstance',),
        ),
        migrations.AddField(
            model_name='generictestinstance',
            name='machine',
            field=models.ForeignKey(to='kitkat.Machine'),
        ),
    ]
