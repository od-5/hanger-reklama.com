# coding=utf-8
from django.contrib import admin

from .models import City

__author__ = 'alexy'


class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'price_item', 'count', 'price', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    fieldsets = (
        (None, {'fields': ('name', 'second_name', 'phone', 'price_item', 'count', 'price', 'slug')}),
        (u'SEO', {'fields': ('meta_title', 'meta_desc', 'meta_key')}),
    )


admin.site.register(City, CityAdmin)