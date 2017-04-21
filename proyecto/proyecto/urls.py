""" URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
admin.autodiscover()
from django.views.static import serve
from django.contrib.auth.decorators import login_required

def protected_serve(request, path, document_root=None, show_indexes=False):
    return serve(request, path, document_root, show_indexes)


urlpatterns = [
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^$', TemplateView.as_view(template_name="usuarios/index.html"), name='inicio'),
    url(r'^password-reset/', auth_views.password_reset,  name='password_reset'),
    url(r'^password-reset-done/', auth_views.password_reset_done,  name='password_reset_done'),
    url(r'^password-reset-confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm,  name='password_reset_confirm'),
    url(r'^password-reset-complete/', auth_views.password_reset_complete,  name='password_reset_complete'),
    url(r'^password-change/', auth_views.password_change,  name='password_change'),
    url(r'^password-change-done/', auth_views.password_change_done,  name='password_change_done'),
    url(r'^login/', auth_views.login, name='login'),
    #url(r'^inicio/', include('inicio.urls'), name='inicio'),
    url(r'^usuarios/', include('usuarios.urls'), name='usuarios'),
    url(r'^admin/', admin.site.urls),
    url(r'^logout$', auth_views.logout, {'next_page': 'login'}, name='logout'),

   # url(r'^$', 'usuarios.views.main', name='main'),

]
