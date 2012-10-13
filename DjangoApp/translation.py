# -*- coding: utf-8 -*-

from modeltranslation.translator import translator, TranslationOptions
from flatpages_plus.models import FlatPage


class FlatPageTranslationOptions(TranslationOptions):
    """
    Класс настроек интернационализации полей модели FlatPage.
    """
    
    fields = ('title', 'content',)

translator.register(FlatPage, FlatPageTranslationOptions)
