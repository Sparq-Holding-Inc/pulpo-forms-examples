# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pulpo_example', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pulpouser',
            name='has_car',
            field=models.BooleanField(default=False),
        ),
    ]
