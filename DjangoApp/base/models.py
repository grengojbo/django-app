# -*- mode: python; coding: utf-8; -*-
""" Basic models, such as user profile """
from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from DjangoApp.base.managers import PublicationManager

class Publication(models.Model):
    slug = models.CharField(_(u'URL'), max_length=255)
    title = models.CharField(_(u'title'), max_length=255)
    author = models.ForeignKey(User, null=True, editable=False, verbose_name=_('author'), related_name='%(app_label)s_%(class)s_set')
    enabled = models.BooleanField(_('enabled'), default=True, db_index=True,
        help_text=_("If not set, publication is hidden from visitors anyway."))
    publication_start_date = models.DateTimeField(_('publication start date'), default=datetime.now, db_index=True,
        help_text=_("Publication will be visible to visitors starting from this date."))
    publication_end_date = models.DateTimeField(_('publication end date'), null=True, blank=True, db_index=True,
        help_text=_("Publication will be visible to visitors due to this date if set."))
    content = models.TextField(_(u'content'))

    objects = PublicationManager()

    class Meta:
        ordering = ['-publication_start_date']
        verbose_name = _(u'text page')
        verbose_name_plural = _(u'text pages')
        unique_together = ('slug')

    def __unicode__(self):
        return u'%s (%s)' % (self.title, self.slug)

    def get_absolute_url(self):
        return self.slug