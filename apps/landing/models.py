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
    phone = models.CharField(max_length=100, verbose_name=u'Телефон', blank=True, null=True)
    count = models.PositiveIntegerField(verbose_name=u'Количество экземпляров', blank=True, null=True)
    price = models.PositiveIntegerField(verbose_name=u'Стоимость, руб', blank=True, null=True)
    slug = models.SlugField(max_length=100, verbose_name=u'URL города')
