# -*- coding: utf-8 -*-
from django.utils.translation import ugettext as _
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

@login_required

def usuarios(request):
    template = loader.get_template('usuarios/index.html')
    return HttpResponse(template.render({}, request))
