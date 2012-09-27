# -*- mode: python; coding: utf-8; -*-
"""urlconf for the base application"""

from django.conf.urls import url, patterns


urlpatterns = patterns('kvazar.base.views',
    url(r'^$', 'home', name='home'),
    url(r'^register/', 'register', name='register_form')
)
