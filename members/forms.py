from django import forms

from .models import Member
from django.contrib.auth.models import User

class SignupForm(forms.ModelForm):
    #your_name = forms.CharField(label='Your name', max_length=100)
    #template_name = 'members/signup.html'

    xxx = forms.ModelChoiceField(queryset=User.objects.all())


    class Meta:
       model = Member
       fields = [
           'user', 'photo', 'bio', 'phone', 'role', 'status',
           'profiles', 'secondary_emails', 'groups'
       ]
    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass
