# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=500)),
                ('branch', models.CharField(max_length=500)),
                ('gender', models.CharField(default=b'?', max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female'), (b'?', b'Unknown')])),
                ('date_of_birth', models.DateField(null=True, blank=True)),
                ('race', models.CharField(default=b'?', max_length=10, choices=[(b'ASIAN', b'Asian'), (b'BLACK', b'Black'), (b'LATINO', b'Latino'), (b'WHITE', b'White'), (b'OTHER', b'Other'), (b'?', b'Unknown')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
