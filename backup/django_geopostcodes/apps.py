# -*- coding: utf-8 -*-
"""
    django_geopostcodes.apps
    ~~~~~~~~~~~~~~~~~~~~~~~~

    Django app definition for django-geopostcodes.
"""
from __future__ import absolute_import, print_function, unicode_literals
from django.apps import AppConfig


class DjangoGeoPostCodesAppConfig(AppConfig):
    name = 'django_geopostcodes'
    label = 'geopc'
    verbose_name = 'Django GeoPostCodes'
