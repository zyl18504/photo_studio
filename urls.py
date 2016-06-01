#-*-coding=utf-8-*-
import os
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import photo_studio.views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'photo_studio.views.index', name='index'),
    url(r'^index$', 'photo_studio.views.index', name='index'),
    url(r'^detail$', 'photo_studio.views.detail', name='detail'),
    # url(r'^photo_studio/', include('photo_studio.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

)
    