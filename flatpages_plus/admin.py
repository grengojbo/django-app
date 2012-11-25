# -*- mode: python; coding: utf-8; -*-
from django.conf import settings
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
#from modeltranslation.admin import TranslationAdmin
from flatpages_plus.forms import FlatpageForm
from flatpages_plus.models import FlatPage, Categories


#try:
#    from grappellifit.admin import TranslationAdmin, TranslationStackedInline
#    ModelAdmin = TranslationAdmin
#    StackedInlineAdmin = TranslationStackedInline
#except:
#    try:
#        from modeltranslation.admin import TranslationAdmin, TranslationStackedInline
#        ModelAdmin = TranslationAdmin
#        StackedInlineAdmin = TranslationStackedInline
#    except:
#        ModelAdmin = admin.ModelAdmin
#        StackedInlineAdmin = admin.StackedInline

ModelAdmin = admin.ModelAdmin
StackedInlineAdmin = admin.StackedInline

class CategoriesAdmin(ModelAdmin):
    list_display = ('name', 'is_enable', 'slug',)
    list_filter = ('is_enable',)
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)

class FlatPageAdmin(ModelAdmin):
    #form = FlatpageForm
    fieldsets = (
        (_('Title'), {
              'fields': ('title','url','category')
        }),
        (None, {'fields': (
            ('owner','status',),
            'content',
            'tags',
            'name',
        )}),
        (_('Advanced options'), {
            'classes': ('grp-collapse grp-closed',),
            'fields': (
                'sites',
                ('enable_comments', 'enable_social',),
                'registration_required', 
                'template_name',
                'views',
            )
        }),
    )
    #prepopulated_fields = {'url': ('title',)}
    list_display = ('url', 'title', 'name', 'category', 'status', 'owner', 'views', 'modified', 'created')
    list_filter = ('status', 'sites', 'enable_comments', 'registration_required', 'enable_social', 'category',)
    prepopulated_fields = {'url': ('title',)}
    search_fields = ('url', 'title', 'name', 'owner',)
    class Media:
        js = [
            "{0}grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js".format(settings.STATIC_URL),
            "{0}js/tinymce_setup.js".format(settings.STATIC_URL),
        ]
    #"{0}modeltranslation/js/force_jquery.js".format(settings.STATIC_URL),
    #"{0}modeltranslation/js/tabbed_translation_fields.js".format(settings.STATIC_URL),
    #class Media:
    #    js = [
    #        "{0}grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js".format(settings.STATIC_URL),
    #        "{0}js/tinymce_setup.js".format(settings.STATIC_URL),
    #    ]
    #    #css = {
    #    #    'screen': ('{0}modeltranslation/css/tabbed_translation_fields.css'.format(settings.STATIC_URL),),
    #    #}

admin.site.register(FlatPage, FlatPageAdmin)
admin.site.register(Categories, CategoriesAdmin)
