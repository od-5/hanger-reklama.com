# coding=utf-8
from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from .views import LandingView, CityDetailView
from .ajax import ticket

__author__ = 'alexy'


urlpatterns = patterns(
    'apps.landing.views',
    url(r'^$', 'home_view', name='index'),
    url(r'^(?P<slug>[\w-]+)$', CityDetailView.as_view(), name='city'),
    url(r'^thnx/$', TemplateView.as_view(template_name='ok.html'), name='thnx'),
    # url(r'^mail/$', TemplateView.as_view(template_name='landing/mail.html'), name='mail'),
    url(r'^ticket/$', ticket, name='ticket'),
)
