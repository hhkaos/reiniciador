from django.conf.urls import patterns, url, include
from . import views

urlpatterns = patterns('',
    url(r'^$', views.SignupView.as_view(), name='signup'),
    url(r'^miembros/$', views.MemberListView.as_view(), name='member_list'),
    #(?P<username>\w+)
    url(r'^thanks/$', views.ThanksView.as_view(), name='thanks'),

)
