# -*- mode: python; coding: utf-8; -*-
""" Views for the base application """

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic.simple import direct_to_template
from registration.forms import RegistrationFormUniqueEmail
from userena.forms import SignupFormOnlyEmail

def home(request):
    """ Default view for the root """
    return render_to_response('base/home.html',
        context_instance=RequestContext(request))

def register(request):
    form = SignupFormOnlyEmail()
    return direct_to_template(request, "registration/ajax_registration.html", extra_context={'form': form })
