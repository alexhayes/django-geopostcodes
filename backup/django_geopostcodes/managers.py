# -*- coding: utf-8 -*-
"""
    django_geopostcodes.managers
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Django model managers for django-geopostcodes.
"""
from __future__ import absolute_import, print_function, unicode_literals
from django.contrib.gis.db.models.query import GeoQuerySet
from django.db.models.manager import Manager
from django.contrib.gis.db import models


class LocalityQuerySet(GeoQuerySet):
    """
    Locality QuerySet.
    """
    anything_fields = ('country',
                       'region1', 'region2', 'region3', 'region4',
                       'locality', 'postcode', 'suburb')

    def anything(self, lookup_type, value, fields=anything_fields):
        queries = [models.Q(**{'%s__%s' % (field, lookup_type): value}) for field in fields]

        # Take one Q object from the list
        query = queries.pop()

        # Or the Q object with the ones remaining in the list
        for item in queries:
            query |= item

        return self.filter(query)

    def anything_icontains(self, value, fields=anything_fields):
        return self.anything('icontains', value, fields)

    def anything_contains(self, value, fields=anything_fields):
        return self.anything('contains', value, fields)

    def anything_exact(self, value, fields=anything_fields):
        return self.anything('exact', value, fields)

    def anything_iexact(self, value, fields=anything_fields):
        return self.anything('iexact', value, fields)

    def anything_startswith(self, value, fields=anything_fields):
        return self.anything('startswith', value, fields)

    def anything_istartswith(self, value, fields=anything_fields):
        return self.anything('istartswith', value, fields)

    def anything_endswith(self, value, fields=anything_fields):
        return self.anything('endswith', value, fields)

    def anything_iendswith(self, value, fields=anything_fields):
        return self.anything('iendswith', value, fields)


class LocalityManager(Manager.from_queryset(LocalityQuerySet)):
    "Overrides Manager to return Geographic QuerySets."

    # This manager should be used for queries on related fields
    # so that geometry columns on Oracle and MySQL are selected
    # properly.
    use_for_related_fields = True
