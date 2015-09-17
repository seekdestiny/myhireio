# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20150901_0309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='size',
            field=models.CharField(default=b'2~5', max_length=20, blank=True),
        ),
    ]
