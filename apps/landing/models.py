# coding=utf-8
from django.core.urlresolvers import reverse
from django.db import models

from core.base_model import CommonPage

__author__ = 'alexy'


class City(CommonPage):
    class Meta:
        verbose_name = u'Город'
        verbose_name_plural = u'Города'
        app_label = 'landing'

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('landing:city', args=(self.slug,))

    name = models.CharField(max_length=100, verbose_name=u'Название')
    second_name = models.CharField(
        max_length=100, verbose_name=u'Название города в предложном падеже',
        help_text=u'в Ростове-На-Дону, в Волгограде'
    )
    phone = models.CharField(max_length=100, verbose_name=u'Телефон', blank=True, null=True)
    count = models.PositiveIntegerField(verbose_name=u'Количество экземпляров', blank=True, null=True)
    price_item = models.PositiveIntegerField(verbose_name=u'Стоимость за экземпляр, коп', default=30)
    price = models.PositiveIntegerField(verbose_name=u'Стоимость, руб', blank=True, null=True)
    slug = models.SlugField(max_length=100, verbose_name=u'URL города')
