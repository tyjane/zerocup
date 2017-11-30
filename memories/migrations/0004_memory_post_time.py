# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('memories', '0003_auto_20171129_0002'),
    ]

    operations = [
        migrations.AddField(
            model_name='memory',
            name='post_time',
            field=models.DateTimeField(null=True, default=django.utils.timezone.now),
        ),
    ]
