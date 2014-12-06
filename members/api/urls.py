from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    url(r'^members$', views.MemberList.as_view(), name='member-list'),
    url(r'^members/(?P<pk>\d+)$', views.MemberDetail.as_view(), name='member-detail'),
)
