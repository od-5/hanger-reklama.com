# coding=utf-8
from annoying.decorators import ajax_request
from annoying.functions import get_object_or_None
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from django.views.generic.base import ContextMixin
from django_geoip.models import IpRange

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


def home_view(request):
    ip = request.META.get('REMOTE_ATTR', '')
    try:
        geoip_record = IpRange.objects.by_ip(ip)
        city_name = geoip_record.city.name
        city = get_object_or_None(City, name__iexact=city_name)
        if city:
            return HttpResponseRedirect(reverse('landing:city', args=(city.slug,)))
    except IpRange.DoesNotExist:
        city_name = None
    context = {
        'city_list': City.objects.all(),
        'location': city_name,
        'ip': ip
    }
    return render(request, 'index.html', context)