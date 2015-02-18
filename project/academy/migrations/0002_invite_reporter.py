# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='invite',
            name='reporter',
            field=models.CharField(blank=True, max_length=255, null=True, choices=[(b'lois-lane', b'Lois Lane'), (b'clark-kent', b'Clark Kent'), (b'jimmy-olson', b'Jimmy Olson')]),
            preserve_default=True,
        ),
    ]
