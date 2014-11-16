from django.conf.urls import patterns, url, include
from . import views

urlpatterns = patterns('',
    url(r'^$', views.SignupView.as_view(), name='signup'),
    url(r'^thanks/$', views.ThanksView.as_view(), name='thanks'),

)
