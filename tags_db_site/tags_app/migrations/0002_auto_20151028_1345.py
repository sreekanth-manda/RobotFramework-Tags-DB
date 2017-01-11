# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tags_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Releases',
            fields=[
                ('ReleaseID', models.AutoField(serialize=False, primary_key=True)),
                ('ProductID', models.IntegerField()),
                ('ReleaseTag', models.CharField(max_length=32)),
                ('ReleaseName', models.CharField(max_length=32)),
                ('Description', models.CharField(max_length=512)),
            ],
            options={
                'db_table': 'tblrelease',
            },
        ),
        migrations.RenameField(
            model_name='tags',
            old_name='TagCreatedTime',
            new_name='CreatedTime',
        ),
        migrations.RenameField(
            model_name='tags',
            old_name='TagDescription',
            new_name='Description',
        ),
        migrations.AddField(
            model_name='tags',
            name='TagType',
            field=models.CharField(default=b'FeatureTag', max_length=256),
        ),
        migrations.AlterModelTable(
            name='tags',
            table='tbltag',
        ),
    ]
