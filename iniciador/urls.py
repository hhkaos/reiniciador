from django.conf.urls import patterns, include, url
from django.contrib import admin
from . import views
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.HomeView.as_view(), name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^signup/', include('members.urls', namespace='members')),

    url(r'^admin/', include(admin.site.urls)),
)
