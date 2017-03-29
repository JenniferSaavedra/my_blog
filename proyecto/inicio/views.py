# -*- coding: utf-8 -*-
from django.utils.translation import ugettext as _
from django.http import HttpResponse
from django.template import loader


def inicio(request):
    template = loader.get_template('inicio/index.html')
    return HttpResponse(template.render({}, request))
