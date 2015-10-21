# -*- coding: utf-8 -*-
"""
    django_geopostcodes.helpers
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Helper functions for django-geopostcodes.
"""
from __future__ import absolute_import, print_function, unicode_literals
import csv
from collections import namedtuple
from django.contrib.gis.geos import Point
from django.db.transaction import atomic
from .models import Locality
from django.utils.translation import ugettext_lazy as _


def import_localities(path, delimiter=';'):
    """
    Import localities from a CSV file.

    :param path: Path to the CSV file containing the localities.
    """

    LocalityExpected = namedtuple('LocalityExpected',
                              ('iso country language id region1 region2 '
                               'region3 region4 locality postcode suburb '
                               'latitude longitude elevation iso2 fips nuts '
                               'hasc stat timezone utc dst'))

    creates = []
    updates = []

    with open(path, mode="r") as infile:
        reader = csv.reader(infile, delimiter=str(delimiter))

        # Get names from column headers
        LocalityActual = namedtuple("LocalityActual", next(reader))

        # Use names to very the format of the file
        if LocalityActual._fields != LocalityExpected._fields:
            raise Exception(_("Expected fields ({expected_fields}) in {path} not ({actual_fields})").format(
                expected_fields=LocalityExpected._fields,
                path=path,
                actual_fields=LocalityActual._fields
            ))

        with atomic():
            for row in map(LocalityExpected._make, reader):
                defaults = row.__dict__
                defaults['point'] = Point(float(row.longitude),
                                          float(row.latitude))
                locality, created = Locality.objects.update_or_create(
                    id=row.id,
                    defaults=defaults
                )
                if created:
                    creates.append(locality)
                else:
                    updates.append(locality)

    return creates, updates
