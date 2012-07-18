from django.conf.urls import *
from nyooz_home.models import Local, Home, City
from nyooz_home import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'nyooz.views.home', name='home'),
    # url(r'^nyooz/', include('nyooz.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^nyooz_home/',views.get_local,{'template_name': 'LOCAL/index.html'}),
)

#if settings.DEBUG:
#        urlpatterns+= patterns('',
#                (r'^debuginfo/$', views.debug),
#        )


