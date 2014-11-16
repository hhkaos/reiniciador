# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='network',
            field=models.CharField(max_length=100, null=True, choices=[(b'linkedin', b'Linkedin'), (b'twitter', b'Twitter'), (b'facebook', b'Facebook'), (b'personal_site', b'Personal site'), (b'other', b'Other')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='member',
            name='status',
            field=models.CharField(blank=True, max_length=100, choices=[(b'active', b'Active'), (b'inactive', b'Inative'), (b'pending', b'Pending'), (b'unknown', b'Unknown')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
    ]
