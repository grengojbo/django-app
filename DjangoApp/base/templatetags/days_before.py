# -*- mode: python; coding: utf-8; -*-
import datetime

__author__ = 'jbo'

from django import template

register = template.Library()

@register.simple_tag
def days_before(d_year, d_month, d_day):
    "для осталось 18 дней"
    dt_st = datetime.date.today()
    dt_fin = datetime.date(int(d_year), int(d_month), int(d_day))
    delta = dt_fin - dt_st
    return delta.days