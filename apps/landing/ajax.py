# coding=utf-8
import urllib
import urlparse
import urllib2
import json

from annoying.decorators import ajax_request
from django.views.decorators.csrf import csrf_exempt

__author__ = 'alexy'


@ajax_request
@csrf_exempt
def ticket(request):
    name = request.POST.get('name')
    phone = request.POST.get('phone')
    mail = request.POST.get('mail')
    theme = request.POST.get('theme')
    city = request.POST.get('city')
    headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)'}
    values = {'name': name.encode('utf-8'), 'phone': phone.encode('utf-8'), 'mail': mail.encode('utf-8'), 'theme': theme.encode('utf-8'), 'city': city.encode('utf-8')}
    print values
    data = urllib.urlencode(values)
    print data
    req = urllib2.Request('http://reklamadoma.com/ticket/hanger/', data, headers)
    response = urllib2.urlopen(req)
    answer = json.load(response)

    if answer['success']:
        return {
            'success': True,
            'name': name,
            'phone': phone,
            'mail': mail,
            'theme': theme
        }
    return {
        'success': False
    }
