# -*- mode: python; coding: utf-8; -*-
""" Default urlconf for DjangoApp """

from django.conf.urls.defaults import *
from django.conf import settings
from django.conf.urls import include, patterns
#from session_csrf import anonymous_csrf
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import ugettext_lazy as _
from django.views.generic.simple import direct_to_template
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from dajaxice.core import dajaxice_autodiscover, dajaxice_config

from profiles.forms import SignupFormExtra

from django.contrib import admin
from filebrowser.sites import site
admin.autodiscover()
dajaxice_autodiscover()

# django-session-csrf monkeypatcher
#import session_csrf
#session_csrf.monkeypatch()


def bad(request):
    """ Simulates a server error """
    1 / 0

urlpatterns = patterns('',
    (r'^grappelli/', include('grappelli.urls')),
    #(r'^sitemap\.xml$', 'sitemap.view', name='sitemap_xml'),
    (r'^admin/filebrowser/', include(site.urls)),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    #(r'^admin/$', anonymous_csrf(admin.site.admin_view(admin.site.index))),
    (r'^admin/', include(admin.site.urls)),
    #url(r'^', include('debug_toolbar_user_panel.urls')),
    (r'^accounts/', include('userena.urls')),
    (r'^messages/', include('userena.contrib.umessages.urls')),
    (r'^bad/$', bad),
    (r'^contact/', include('knowledge.urls')),
    #(r'', include('DjangoApp.base.urls')),
    url(r'^$', direct_to_template, {'template': 'static/promo.html'}, name='promo'),
    (r'^i18n/', include('django.conf.urls.i18n')),
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
    #(r'^accounts/', include('registration.backends.default.urls')),
)

#https://docs.djangoproject.com/en/dev/topics/i18n/translation/#url-internationalization
#urlpatterns += i18n_patterns('',
#    url(_(r'^about/$'), 'about.view', name='about'),
#    url(_(r'^news/'), include(news_patterns, namespace='news')),
#)

## In DEBUG mode, serve media files through Django.
if settings.DEBUG:
    # Remove leading and trailing slashes so the regex matches.
    media_url = settings.MEDIA_URL.lstrip('/').rstrip('/')
    urlpatterns += patterns('',
        (r'^%s/(?P<path>.*)$' % media_url, 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}),
    )

urlpatterns += patterns('flatpages_plus.views',
    (r'^(?P<url>.*)$', 'flatpage'),
)

# Add media and static files
urlpatterns += staticfiles_urlpatterns()
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
