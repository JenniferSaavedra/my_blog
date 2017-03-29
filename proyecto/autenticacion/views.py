# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.template import loader
from django.utils.translation import ugettext as _


def login(request):
    template = loader.get_template('autenticacion/login.html')
    return HttpResponse(template.render({}, request))
