# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_auto_20141116_0003'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='id',
        ),
        migrations.AlterField(
            model_name='group',
            name='email',
            field=models.ForeignKey(related_name='email_set', blank=True, to='members.Email', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.CharField(max_length=100, serialize=False, primary_key=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='member',
            name='last_activity',
            field=models.DateField(default=datetime.date.today, null=True),
            preserve_default=True,
        ),
    ]
