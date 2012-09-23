# -*- mode: python; coding: utf-8; -*-
__author__ = 'jbo'

from datetime import datetime
from django.db.models import Q
from django.db.models import query


class PublicationQuerySet(query.QuerySet):

    def expired(self):
        return self.filter(publication_end_date__lt=datetime.now())

    def future(self):
        return self.filter(publication_start_date__gt=datetime.now())

    def enabled(self):
        return self.filter(enabled=True)

    def disabled(self):
        return self.filter(enabled=False)

    def unpublished(self):
        return self.filter(~self._published_q())

    def published(self):
        return self.filter(self._published_q())

    def _published_q(self):
        now = datetime.now()
        q = Q(publication_end_date__gte=now)|Q(publication_end_date=None)
        q &= Q(publication_start_date__lte=now)
        q &= Q(enabled=True)
        return q
