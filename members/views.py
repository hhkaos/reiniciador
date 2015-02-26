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
from django.http import JsonResponse



from .forms import SignupForm
from .models import Member
from .models import Group
from .models import Email
from .models import Profile


class SignupView(generic.FormView):
    form_class = SignupForm
    template_name = 'members/signup.html'

    def post(self, request, *args, **kwargs):
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            # Save photo
            context = request.POST
            m = Member.objects.get(user__username=context.get('primary_email').split("@")[0][:30])
            m.photo = request.FILES['photo']

            # Save profiles
            num_websites = context.get('num_websites');
            for i in range(1, int(num_websites) + 1):
                name = context.get('website_name_'+str(i))
                url = context.get('website_url_'+str(i))
                if name and url:
                    p, created = Profile.objects.get_or_create(url = url.strip(), name = name)
                    m.profiles.add(p)

            m.save()

            return HttpResponseRedirect(reverse('members:thanks')) # Redirect after POST
        else:
            #import ipdb; ipdb.set_trace()
            context = self.get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        form = SignupForm()
        context = self.get_context_data(**kwargs)
        context['form'] = form

        return self.render_to_response(context)
        '''return render(request, 'members/signup2.html', {
            'form': form,
        })'''

class ThanksView(generic.TemplateView):
    template_name = 'members/thanks.html'

class DashboardView(generic.TemplateView):
    template_name = 'members/dashboard.html'

class MemberListView(generic.TemplateView):
    template_name = 'members/member_list.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['members'] = Member.objects.all()

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
                u.last_activity = date.today()
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

class ResetPassView(generic.TemplateView):
    template_name = 'registration/reset_password.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['request'] = "GET"
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['request'] = "POST"
        return self.render_to_response(context)

class GroupView(generic.TemplateView):
    template_name = 'members/group.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['g'] = get_object_or_404(Group, name=context.get('name'))
        return self.render_to_response(context)

class AllMembersView(generic.TemplateView):
    template_name = 'members/all_members.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['members'] = Member.objects.all()

        return self.render_to_response(context)

class UserAPI(generic.TemplateView):
    template_name = 'members/userApi.html'

    def render_to_json_response(self, context, **response_kwargs):
        """
        Returns a JSON response, transforming 'context' to make the payload.
        """
        return JsonResponse(
            self.get_data(context),
            **response_kwargs
        )

    def get(self, request, *args, **kwargs):
        

        context = self.get_context_data(**kwargs)
        m = get_object_or_404(Member, id_iniciador=context['id'])

        context['member'] = m
        

        return self.render_to_response(context)
