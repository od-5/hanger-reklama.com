# coding=utf-8
from django.http import HttpResponse, HttpResponseRedirect
from core.models import Setup

__author__ = 'alexy'


def get_robots_txt(request):
    """
    Функция отображения robots.txt
    """
    setup = Setup.objects.all().first()
    try:
        content = setup.robots_txt
    except:
        content = u'User-agent: *'
    return HttpResponse(content, content_type='text/plain')


def get_sitemap_xml(request):
    """
    Функция отображения sitemap.xml
    """
    setup = Setup.objects.first()
    try:
        content = setup.sitemap
    except:
        content = u'User-agent: *'
    return HttpResponse(content, content_type='text/xml')

