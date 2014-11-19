from django.shortcuts import render

from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import redirect

from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives

from django.shortcuts import render
from django.shortcuts import get_object_or_404
#from django.shortcuts import get_or_create
from django.views import generic

from .forms import SignupForm
from .models import Member
from .models import Group
from .models import Email
from .models import Profile

class SignupView(generic.FormView):
    form_class = SignupForm
    template_name = 'members/signup.html'

    def post(self, request, *args, **kwargs):
        context = request.POST # self.get_context_data(**kwargs)

        u, created = User.objects.get_or_create(
            email = context.get('primary_email'),
            first_name = context.get('first_name'),
            last_name = context.get('last_name'),
            username = context.get('primary_email'),
        )
        if created:
            #
            m, created = Member.objects.get_or_create(
                photo = context.get('photo'),
                user = u,
                bio = context.get('bio'),
                phone = context.get('phone'),
                role = context.get('role'),
                status = 'pending',
            )

            if created:
                groups = request.POST.getlist('groups')
                for g in groups:
                    g, created = Group.objects.get_or_create(name = g)
                    m.groups.add(g)


                emails = context.get('secondary_emails');
                for e in emails.split(','):
                    e, created = Email.objects.get_or_create(email = e.strip())
                    m.secondary_emails.add(e)


                linkedin = context.get('linkedin')
                l, created = Profile.objects.get_or_create(url = linkedin, network = 'linkedin')
                m.profiles.add(l)

                twitter = context.get('twitter')
                t, created = Profile.objects.get_or_create(url = twitter, network = 'twitter')
                m.profiles.add(t)

                num_websites = context.get('num_websites');
                for i in range(1, int(num_websites) + 1):
                    #import ipdb; ipdb.set_trace()
                    name = context.get('website_name_'+str(i))
                    url = context.get('website_url_'+str(i))
                    p, created = Profile.objects.get_or_create(url = url.strip(), name = name)
                    m.profiles.add(p)

                m.save()


        print "POST"
        msg = EmailMultiAlternatives(
            subject="Solicitud de alta",
            body="Hemos recibido tu solicitud de alta",
            from_email="hhkaos@gmail.com",
            to=[context.get('primary_email')]
        )
        msg.tags = ["iniciador", "alta"]
        msg.metadata = {'user_id': u.id}
        msg.send()
        response = msg.mandrill_response[0]
        mandrill_id = response['_id']
        '''msg = EmailMultiAlternatives(
            subject="Djrill Message",
            body="This is the text email body",
            from_email="Djrill Sender <djrill@example.com>",
            to=["Recipient One <hhkaos@gmail.com>"],
            headers={'Reply-To': "Service <support@example.com>"} # optional extra headers
        )
        msg.attach_alternative("<p>This is the HTML email body</p>", "text/html")

        # Optional Mandrill-specific extensions:
        msg.tags = ["one tag", "two tag", "red tag", "blue tag"]
        msg.metadata = {'user_id': "8675309"}

        # Send it:
        msg.send()'''

        return HttpResponseRedirect('/signup/thanks')

class ThanksView(generic.TemplateView):
        template_name = 'members/thanks.html'
