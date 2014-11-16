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


class HomeView(generic.TemplateView):
    template_name = 'members/home.html'
