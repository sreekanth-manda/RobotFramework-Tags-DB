# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('TagID', models.AutoField(serialize=False, primary_key=True)),
                ('TagName', models.CharField(max_length=32)),
                ('TagDescription', models.CharField(max_length=256)),
                ('TagCreatedTime', models.DateTimeField()),
            ],
            options={
                'db_table': 'tags',
            },
        ),
    ]
