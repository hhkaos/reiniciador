from django.conf.urls import patterns, url, include
from . import views

urlpatterns = patterns('',
    url(r'^signup/$', views.SignupView.as_view(), name='signup'),
    url(r'^list/$', views.MemberListView.as_view(), name='member_list'),
    #(?P<username>\w+)
    url(r'^group/(?P<name>\w+)/$', views.GroupView.as_view(), name='group'),
    url(r'^profile/$', views.ProfileView.as_view(), name='profile'),
    url(r'^all/$', views.AllMembersView.as_view(), name='all-members'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
    url(r'^ping/$', views.PingMembersView.as_view(), name='ping'),
    url(r'^revision/(?P<username>\w+)/(?P<hash>\w+)/(?P<status>\w+)/$', views.ReviewView.as_view(), name='review'),
    url(r'^signup/thanks/$', views.ThanksView.as_view(), name='thanks'),

)
