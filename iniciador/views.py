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

from members.models import Group
from members.models import Member

class HomeView(generic.TemplateView):
    template_name = 'members/home.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['num_members'] = len(Member.objects.exclude(status='inactive').exclude(status='pending'))
        context['num_groups'] = len(Group.objects.all())
        context['groups'] = Group.objects.all()
        return self.render_to_response(context)


class WebsiteView(generic.TemplateView):
    template_name = 'members/website.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)
