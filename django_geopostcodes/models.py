# -*- coding: utf-8 -*-
"""
    django_geopostcodes.models
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    Django models for django-geopostcodes.

"""
from __future__ import absolute_import, print_function, unicode_literals
from django.contrib.gis.db import models
from django.utils.translation import ugettext_lazy as _
from django_countries.fields import CountryField
from .managers import LocalityManager


class Locality(models.Model):
    """
    Defines an Locality as defined in GeoPostCodes GeoPC_xx_Places.csv files.
    """
    iso = CountryField(_('iso'), db_index=True, help_text=_('ISO 3166-1 Country code'))
    country = models.CharField(_('country'), max_length=50, help_text=_('Country name'))
    language = models.CharField(_('language'), max_length=2, db_index=True, help_text=_('ISO 639-1 language code'))
    region1 = models.CharField(_('region 1'), max_length=80, db_index=True, help_text=_('Administrative region level 1'))
    region2 = models.CharField(_('region 2'), max_length=80, db_index=True, help_text=_('Administrative region level 2'))
    region3 = models.CharField(_('region 3'), max_length=80, db_index=True, help_text=_('Administrative region level 3'))
    region4 = models.CharField(_('region 4'), max_length=80, db_index=True, help_text=_('Administrative region level 4'))
    locality = models.CharField(_('locality'), max_length=80, db_index=True, help_text=_('Locality name'))
    postcode = models.CharField(_('postcode'), max_length=15, db_index=True, help_text=_('ZIP/Postal code'))
    suburb = models.CharField(_('suburb'), max_length=80, help_text=_('Locality subdivision'))
    latitude = models.FloatField(_('latitude'), help_text=_('Latitude coordinates in WGS84'))
    longitude = models.FloatField(_('longitude'), help_text=_('Longitude coordinates in WGS84'))
    elevation = models.IntegerField(_('elevation'), help_text=_('Elevation in meters'))
    point = models.PointField(db_index=True)
    iso2 = models.CharField(_('ISO2'), max_length=10, help_text=_('ISO 3166-2 Region code'))
    fips = models.CharField(_('FIPS'), max_length=10, help_text=_('NGA Geopolitical code (formerly FIPS PUB 10-4)'))
    nuts = models.CharField(_('NUTS'), max_length=12, help_text=_('European subdivision code'))
    hasc = models.CharField(_('HASC'), max_length=12, help_text=_('Hierarchical administrative subdivision code'))
    stat = models.CharField(_('STAT'), max_length=20, help_text=_('National statistics/census code'))
    timezone = models.CharField(_('timezone'), max_length=30, help_text=_('Time zone name (Olson)'))
    utc = models.CharField(_('utc'), max_length=10, help_text=_('Coordinated Universal Time'))
    dst = models.CharField(_('dst'), max_length=10, help_text=_('Daylight Saving Time'))

    objects = LocalityManager()

    class Meta:
        verbose_name = _('locality')
        verbose_name_plural = _('localities')

    def __str__(self):
        return self.locality
