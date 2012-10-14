# -*- coding: utf-8 -*-

from modeltranslation.translator import translator, TranslationOptions
from flatpages_plus.models import FlatPage
from seoutils.models import Meta


class FlatPageTranslationOptions(TranslationOptions):
  """
  Класс настроек интернационализации полей модели FlatPage.
  """
  fields = ('title', 'content',)
translator.register(FlatPage, FlatPageTranslationOptions)

class MetaTranslationOptions(TranslationOptions):
  fields = ('title', 'keywords', 'desc')
translator.register(Meta, MetaTranslationOptions)
