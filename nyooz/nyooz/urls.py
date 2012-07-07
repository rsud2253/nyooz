from django.conf.urls import patterns, include, url
from nyooz_home.models import Local, Home, City
from nyooz_home.views import get_local

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'nyooz.views.home', name='home'),
    # url(r'^nyooz/', include('nyooz.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    'nyooz.nyooz_home.views',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^nyooz_home/',get_local),
)
