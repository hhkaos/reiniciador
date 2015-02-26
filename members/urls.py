from django.conf.urls import patterns, url, include
from . import views

urlpatterns = patterns('',
    url(r'^signup/$', views.SignupView.as_view(), name='signup'),
    url(r'^list/$', views.MemberListView.as_view(), name='member_list'),
    #(?P<username>\w+)
    url(r'^group/(?P<name>\w+)/$', views.GroupView.as_view(), name='group'),
    url(r'^member/(?P<id>\w+)/$', views.UserAPI.as_view(), name='user-api'),
    url(r'^dashboard/$', views.DashboardView.as_view(), name='dashboard'),
    url(r'^profile/$', views.ProfileView.as_view(), name='profile'),
    url(r'^all/$', views.AllMembersView.as_view(), name='all-members'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^password/reset/$', 'django.contrib.auth.views.password_reset', {'post_reset_redirect' : '/members/password/reset/done/'}, name='password_reset'),
    url(r'^password/reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    url(r'^password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm', {'post_reset_redirect' : '/members/password/done/'}, name='password_reset_confirm'),
    url(r'^password/done/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
    url(r'^revision/(?P<username>\w+)/(?P<hash>\w+)/(?P<status>\w+)/$', views.ReviewView.as_view(), name='review'),
    url(r'^signup/thanks/$', views.ThanksView.as_view(), name='thanks'),

)
