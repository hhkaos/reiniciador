from django import forms
from django.conf import settings

from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives

from .models import Member
from .models import Group
from .models import Profile
from django.contrib.auth.models import User

'''class SignupForm(forms.ModelForm):
    class Meta:
       model = Member
       fields = [
           'user', 'photo', 'bio', 'phone', 'role', 'status',
           'profiles', 'secondary_emails', 'groups'
       ]'''

class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    photo = forms.FileField(required=True)
    bio = forms.CharField(max_length=400, required=True)
    linkedin = forms.URLField(max_length=300, required=True)
    twitter = forms.URLField(max_length=300, required=True)
    primary_email = forms.EmailField(required=True)
    secondary_emails = forms.CharField(max_length=400, required=False)
    phone = forms.CharField(max_length=200, required=True)
    role = forms.CharField(max_length=200, required=True)
    groups = forms.ModelMultipleChoiceField(queryset=Group.objects.all(), required=True)

    def save(self):

        data = self.cleaned_data

        u = User.objects.create(
            email = data.get("primary_email"),
            first_name = data.get("first_name"),
            last_name = data.get("last_name"),
            username = data.get("primary_email"),
        )
        password = User.objects.make_random_password()
        u.set_password(password)
        u.save()

        m = Member.objects.create(
            user = u,
            bio = data.get('bio'),
            phone = data.get('phone'),
            role = data.get('role'),
            status = 'pending',
        )

        #import ipdb; ipdb.set_trace()
        groups = data.get("groups")

        for g in groups:
            g = Group.objects.get(name = g)
            m.groups.add(g)

        emails = data.get('secondary_emails');
        if emails:
            for e in emails.split(','):
                e, created = Email.objects.get_or_create(email = e.strip())
                m.secondary_emails.add(e)

        linkedin = data.get('linkedin')
        l, created = Profile.objects.get_or_create(url = linkedin, network = 'linkedin')
        m.profiles.add(l)

        twitter = data.get('twitter')
        t, created = Profile.objects.get_or_create(url = twitter, network = 'twitter')
        m.profiles.add(t)

        # Send mail to user
        #import ipdb; ipdb.set_trace()
        mail_to = settings.ADMIN_EMAIL if settings.DEBUG else data.get("primary_email")

        msg = EmailMultiAlternatives(
            subject = "Solicitud de alta",
            from_email = settings.FROM_EMAIL,
            to = [mail_to]
        )
        msg.tags = ["iniciador", "alta"]
        msg.metadata = {'user_id': m.id}
        msg.template_name = "alta-iniciador"
        msg.global_merge_vars = {
            'NAME': data.get("first_name"),
            'PASSWORD': password,
            #'WEBSITE': "<a href='" + data.get('linkedin') + "/*|TRACKINGNO|*'>Linkedin</a>"
        }
        print "Mail sent to:" + mail_to
        msg.send()

        # Send mail to iniciador
        mail_to = settings.ADMIN_EMAIL if settings.DEBUG else settings.FROM_EMAIL

        msg = EmailMultiAlternatives(
            subject = "Nueva solicitud de alta",
            from_email = settings.FROM_EMAIL,
            to = [mail_to]
        )
        msg.tags = ["iniciador", "alta", "gerencia", "user-" + str(m.id)]
        msg.metadata = {'user_id': m.id}
        msg.template_name = "aviso-a-gerencia-alta"
        msg.global_merge_vars = {
            'NAME': data.get("first_name"),
            'LASTNAME': data.get("last_name"),
            'UID': m.id,
            'SERVER': settings.SERVER,
            #'WEBSITE': "<a href='" + data.get('linkedin') + "/*|TRACKINGNO|*'>Linkedin</a>"
        }
        print "Mail sent to:" + mail_to
        msg.send()

        #response = msg.mandrill_response[0]
        #mandrill_id = response['_id']

    def clean_primary_email(self):
        cleaned_data = super(SignupForm, self).clean()
        primary_email = cleaned_data.get("primary_email")

        try:
            user = User.objects.get(email = primary_email)
        except User.DoesNotExist:
            user = None

        if user:
            self.add_error('primary_email', "Ya existe un usuario con este correo, si has escrito tu email personal ponte en contacto con gerencia@iniciador.com")
        else:
            return primary_email

    '''
    TODO: Validate email properly formed
    def clean_secondary_emails(self):

    TODO: Validate phone numbers
    '''
