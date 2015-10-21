# -*- coding: utf-8 -*-
"""
    django_geopostcodes.admin
    ~~~~~~~~~~~~~~~~~~~~~~~~

    Django admin definition for django-geopostcodes.

"""
from __future__ import absolute_import, print_function, unicode_literals
from django.contrib.gis import admin
from .models import Locality


class LocalityAdmin(admin.OSMGeoAdmin):
    list_display = ['id', 'iso', 'country', 'language', 'region1', 'region2',
                    'region3', 'region4', 'locality', 'postcode', 'suburb',
                    'latitude', 'longitude', 'elevation', 'iso2', 'fips',
                    'nuts', 'hasc', 'stat', 'timezone', 'utc', 'dst']
    list_filter = ['iso',
                   'country',
                   'language',
                   'timezone',
                   'utc',
                   'dst']
    search_fields = ['iso', 'country', 'language', 'region1', 'region2',
                    'region3', 'region4', 'locality', 'postcode', 'suburb',
                    'latitude', 'longitude', 'elevation', 'iso2', 'fips',
                    'nuts', 'hasc', 'stat', 'timezone', 'utc', 'dst']

admin.site.register(Locality, LocalityAdmin)

