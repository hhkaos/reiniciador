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

from .models import Member
from .models import Group

class SignupView(generic.FormView):
    #model = Member
    form_class = SignupForm
    '''fields = [
        'user', 'photo', 'bio', 'phone', 'role', 'status',
        'profiles', 'secondary_emails', 'groups'
    ]'''
    template_name = 'members/signup.html'
    #success_url = '/thanks/'

    def post(self, request, *args, **kwargs):
        context = request.POST# self.get_context_data(**kwargs)
        #import ipdb; ipdb.set_trace()



        u, created = User.objects.get_or_create(
            email = context.get('primary_email'),
            first_name = context.get('first_name'),
            last_name = context.get('last_name'),
            username = context.get('primary_email'),
        )
        if created:
            import ipdb; ipdb.set_trace()
            print 'yiah'
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
                m.save()


        print "POST"
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

        return HttpResponseRedirect('signup/thanks')

class ThanksView(generic.TemplateView):
        template_name = 'members/thanks.html'
