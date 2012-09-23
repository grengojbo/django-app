# -*- mode: python; coding: utf-8; -*-
__author__ = 'jbo'

from django.conf import settings
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from DjangoApp.base.models import Publication

class PublicationAdmin(admin.ModelAdmin):
    class Media:
        js = [
            "{0}/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js".format(settings.STATIC_URL),
            "{0}/grappelli/tinymce_setup/tinymce_setup.js".format(settings.STATIC_URL),
        ]

admin.site.register(Publication, PublicationAdmin)