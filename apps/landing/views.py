# coding=utf-8
from annoying.decorators import ajax_request
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView, DetailView
from django.views.generic.base import ContextMixin

from .models import City

__author__ = 'alexy'


class CityListMixin(ContextMixin):
    """
    Миксин добавляет список городов в контекст
    """
    def get_context_data(self, **kwargs):
        kwargs = super(CityListMixin, self).get_context_data(**kwargs)
        kwargs.update({'city_list': City.objects.all()})
        return kwargs


class LandingView(TemplateView, CityListMixin):
    template_name = 'index.html'


class CityDetailView(DetailView, CityListMixin):
    model = City
    template_name = 'index.html'
