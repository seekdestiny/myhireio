# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('name', models.CharField(max_length=50, serialize=False, primary_key=True)),
                ('tag_name', models.CharField(max_length=100, blank=True)),
                ('product', models.CharField(default=b'', max_length=1500)),
                ('why_us', models.CharField(max_length=1500, blank=True)),
                ('traction', models.CharField(default=b'', max_length=500)),
                ('funding', models.CharField(max_length=500, blank=True)),
                ('size', models.CharField(default=b'2-5', max_length=20, blank=True)),
                ('last_active', models.DateTimeField(default=datetime.datetime.now, blank=True)),
                ('market', models.CharField(max_length=100, blank=True)),
                ('company_link', models.CharField(max_length=51, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='JobPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(default=b'', max_length=1500)),
                ('requirements', models.CharField(default=b'', max_length=1500)),
                ('skills', models.CharField(default=b'', max_length=500)),
                ('location', models.CharField(default=b'', max_length=100)),
                ('salary', models.CharField(default=b'', max_length=50)),
                ('equity', models.CharField(default=b'', max_length=50)),
                ('job_type', models.CharField(default=b'', max_length=20)),
                ('job_title', models.CharField(default=b'', max_length=30)),
                ('responsibility', models.CharField(default=b'', max_length=1000)),
                ('company', models.ForeignKey(to='jobs.Company')),
            ],
        ),
    ]
