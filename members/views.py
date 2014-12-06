from datetime import date
import hashlib

from django.shortcuts import render
from braces.views import LoginRequiredMixin

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
                #photo = safe_filename,
                user = u,
                bio = context.get('bio'),
                phone = context.get('phone'),
                role = context.get('role'),
                status = 'pending',
            )

            if created:
                #import ipdb; ipdb.set_trace()
                m.photo = request.FILES['photo']
                m.save()

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
                    if name and url:
                        p, created = Profile.objects.get_or_create(url = url.strip(), name = name)
                        m.profiles.add(p)

                m.save()

                if settings.DEBUG == True:
                    mail_to = "hhkaos@gmail.com"
                else:
                    mail_to = context.get('primary_email')

                msg = EmailMultiAlternatives(
                    subject = "Solicitud de alta",
                    body = "Hemos recibido tu solicitud de alta",
                    from_email = settings.FROM_EMAIL,
                    to=[mail_to]
                )
                msg.tags = ["iniciador", "alta"]
                msg.metadata = {'user_id': u.id}
                msg.template_name = "alta-iniciador"           # A Mandrill template name
                msg.global_merge_vars = {                        # Content blocks to fill in
                    'WEBSITE': "<a href='" + context.get('linkedin') + "/*|TRACKINGNO|*'>Linkedin</a>"
                }
                print "Mail sent to:" + mail_to
                msg.send()

                response = msg.mandrill_response[0]
                mandrill_id = response['_id']
            else:
                print "El miembro ya existe"
        else:
            print "El username ya existe"

        return HttpResponseRedirect(reverse('members:thanks'))

class ThanksView(generic.TemplateView):
    template_name = 'members/thanks.html'

class MemberListView(generic.TemplateView):
    template_name = 'members/member_list.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['members'] = Member.objects.all()

        return self.render_to_response(context)

class PingMembersView(generic.TemplateView):
    template_name = 'members/ping.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        members = Member.objects.exclude(status='inactive').exlude(status='pending')
        check = []
        notify = []
        today = date.today()

        for m in members:
            d = today - m.last_activity
            #import ipdb; ipdb.set_trace()
            if d.days == 60:
                m.status = 'unknown'
                m.save()
                check.append(m)

            elif d.days == 70:
                notify.append(m)

        for c in check:
            msg = EmailMultiAlternatives(
                to = [c.user.email],
                from_email = settings.FROM_EMAIL
            )
            groups = []
            for g in members[0].groups.all():
                groups.append(g.name)
            groups = ', '.join(g for g in groups)

            msg.tags = ["iniciador", "check", today]
            msg.template_name = "checkeo-iniciador"
            msg.global_merge_vars = {
                'NAME': c.user.first_name,
                'GROUPS': groups,
                'EMAIL': c.user.email,
                'PHONE': c.phone,
                'WEBSITE': settings.SERVER,
                'LINK': 'http://' + settings.SERVER + '/members/revision/' + c.user.username,
                'HASH': hashlib.sha224(str(c.last_activity) + str(c.user.id)).hexdigest()
            }

            msg.send()
            response = msg.mandrill_response[0]
            mandrill_id = response['_id']

        #TODO: Terminar la notificacion a la organizacion
        for n in notify:
            msg = EmailMultiAlternatives(
                to=[n.user.email],
                from_email = settings.FROM_EMAIL
            )
            msg.tags = ["iniciador", "notify", today]
            msg.template_name = "notificar-iniciador"           # A Mandrill template name
            msg.global_merge_vars = {                        # Content blocks to fill in
                'WEBSITE': "<a href='/*|TRACKINGNO|*'>Linkedin</a>",
                #user data
            }

            #msg.send()
            #response = msg.mandrill_response[0]
            #mandrill_id = response['_id']

        context['notified'] = notify
        context['checked'] = check

        return self.render_to_response(context)

class ReviewView(generic.TemplateView):
    template_name = 'members/review.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        u = Member.objects.get(user__username = context.get('username'))
        valid_hash = hashlib.sha224(str(u.last_activity) + str(u.user.id)).hexdigest()

        #b8b60ecfb50dbe3aa504c776934e2bd3a3b5e67670e6b1bbabe4d426 == 1/08/2014

        # Check if usernanme - hash is valid
        if context.get('hash') == valid_hash:
            context['valid'] = True
            status = context.get('status')
            #import ipdb; ipdb.set_trace()
            if status == 'valid':
                u.status = 'active'
                u.last_activity = date.today()
                u.save()
            elif status == 'invalid':
                pass
            elif status == 'unsuscribe':
                u.status = 'inactive'
                u.save()
                #TODO: send an email to the organization
            else:
                pass
        else:
            context['valid'] = False

        return self.render_to_response(context)



#TODO: Add decorator
class ProfileView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'members/profile.html'

    login_url = "/members/login/"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)
