# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('email', models.EmailField(max_length=75, serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, blank=True)),
                ('email', models.ForeignKey(related_name='email_set', to='members.Email')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('photo', models.FileField(null=True, upload_to=b'photos/', blank=True)),
                ('bio', models.TextField(blank=True)),
                ('phone', models.CharField(max_length=100, blank=True)),
                ('role', models.CharField(max_length=100, blank=True)),
                ('status', models.CharField(blank=True, max_length=100, choices=[(b'active', b'Active'), (b'inactive', b'Inative'), (b'unknown', b'Unknown')])),
                ('last_activity', models.DateField(null=True)),
                ('groups', models.ManyToManyField(to='members.Group', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('url', models.URLField(serialize=False, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='member',
            name='profiles',
            field=models.ManyToManyField(to='members.Profile', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='member',
            name='secondary_emails',
            field=models.ManyToManyField(to='members.Email', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='member',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
