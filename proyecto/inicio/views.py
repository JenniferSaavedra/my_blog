# -*- coding: utf-8 -*-
from django.utils.translation import ugettext as _
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test



def es_gerente(user):
    return user.groups.filter(name='Estudiante').exists()


@user_passes_test(es_gerente, login_url='/usuarios/')
@login_required()
def inicio(request):
    template = loader.get_template('inicio/inicio.html')
    return HttpResponse(template.render({}, request))
