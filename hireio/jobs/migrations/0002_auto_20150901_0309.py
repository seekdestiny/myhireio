# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='company_link',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='last_active',
            field=models.DateTimeField(),
        ),
    ]
