# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.TextField(max_length=30)),
                ('established', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.TextField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='PulpoUser',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.TextField(max_length=20)),
                ('last_name', models.TextField(max_length=20)),
                ('birthdate', models.DateField()),
                ('has_car', models.BooleanField()),
            ],
        ),
        migrations.AddField(
            model_name='club',
            name='country',
            field=models.ForeignKey(related_name='clubs', to='pulpo_example.Country'),
        ),
    ]
