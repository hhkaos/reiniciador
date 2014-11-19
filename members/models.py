from datetime import date

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from model_utils import Choices
from model_utils.models import TimeStampedModel

from django.contrib.auth.models import User

@python_2_unicode_compatible
class Member(TimeStampedModel):
    STATUS = Choices(
        ('active', 'Active'),
        ('inactive', 'Inative'),
        ('pending', 'Pending'),
        ('unknown', 'Unknown'),
    )

    photo = models.FileField(upload_to='photos/', null=True, blank=True)
    user = models.OneToOneField(User)
    bio = models.TextField(blank=True)
    phone = models.CharField(blank=False, max_length=100)
    role = models.CharField(blank=True, max_length=100)
    status = models.CharField(blank=False, choices=STATUS, max_length=100)
    last_activity = models.DateField(null=False, default=date.today)

    profiles = models.ManyToManyField('Profile', blank=True)
    secondary_emails = models.ManyToManyField('Email', blank=True)
    groups = models.ManyToManyField('Group', null=False)

    def __str__(self):
        return u"{self.user.first_name} {self.user.last_name}".format(self=self)

class Profile(models.Model):
    NETWORK = Choices(
        ('linkedin', 'Linkedin'),
        ('twitter', 'Twitter'),
        ('other', 'Other'),
    )

    url = models.URLField(primary_key=True)
    name = models.CharField(max_length=200, blank=True)
    network = models.CharField(null=True, choices=NETWORK, max_length=100)

    def __str__(self):
        return self.url

@python_2_unicode_compatible
class Group(models.Model):
    name = models.CharField(null=False, blank=False, max_length=100, primary_key=True)
    email = models.ForeignKey(
        'Email', related_name='email_set', null=True, blank=True)

    def __str__(self):
        return self.name

class Email(models.Model):
    email = models.EmailField(primary_key=True, null=False)

    def __str__(self):
        return self.email
