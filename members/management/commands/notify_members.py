from django.core.management.base import BaseCommand, CommandError
from datetime import date
import hashlib

from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.models import User, Group

from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives

from members.models import Member
from members.models import Group
from members.models import Email
from members.models import Profile

class Command(BaseCommand):
    args = '<poll_id poll_id ...>'
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        #context = self.get_context_data(**kwargs)

        members = Member.objects.exclude(status='inactive').exclude(status='pending')
        check = []
        notify = []
        today = date.today()


        self.stdout.write('DEBUG: %s' % settings.DEBUG)

        for m in members:
            d = today - m.last_activity
            self.stdout.write('%s = %i' % (m.user.username, d.days))
            #import ipdb; ipdb.set_trace()
            if (d.days == 60) | (d.days == 34):
                m.status = 'unknown'
                m.save()
                check.append(m)
                self.stdout.write('Notificado (%i dias): "%s"' % (d.days, m.user.username))

            elif d.days == 70:
                notify.append(m)
                self.stdout.write('Notificado (70 dias): "%s"' % m.user.username)

        # Send emails to user that need to validate their data
        for c in check:

            mail_to = settings.ADMIN_EMAIL if settings.DEBUG else c.user.email

            msg = EmailMultiAlternatives(
                to = [mail_to],
                from_email = settings.FROM_EMAIL
            )
            groups = []
            for g in c.groups.all():
                groups.append(g.name)
            groups = ', '.join(g for g in groups)

            emails = [c.user.email]
            for e in c.secondary_emails.all():
                emails.append(e.email)
            emails = ', '.join(e for e in emails)


            msg.tags = ["iniciador", "check", today]
            msg.template_name = "checkeo-iniciador"
            msg.global_merge_vars = {
                'NAME': c.user.first_name,
                'GROUPS': groups,
                'EMAIL': emails,
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

        #context['notified'] = notify
        #context['checked'] = check

        #self.stdout.write('Notificado los miembros "%s"' % poll_id)
        self.stdout.write('Notificados los miembros')
