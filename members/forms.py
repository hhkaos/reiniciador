from django import forms

from .models import Member
from django.contrib.auth.models import User

class SignupForm(forms.ModelForm):
    class Meta:
       model = Member
       fields = [
           'user', 'photo', 'bio', 'phone', 'role', 'status',
           'profiles', 'secondary_emails', 'groups'
       ]
    
