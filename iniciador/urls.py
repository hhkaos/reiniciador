from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from . import views
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.HomeView.as_view(), name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^members/', include('members.urls', namespace='members')),

    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$',
            'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, }),
    )
