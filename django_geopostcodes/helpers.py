# -*- coding: utf-8 -*-
"""
    django_geopostcodes.helpers
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Helper functions for django-geopostcodes.
"""
from __future__ import absolute_import, print_function, unicode_literals

import csv

from django.contrib.gis.geos import Point
from django.db.transaction import atomic

from .models import Locality


def import_localities(path, delimiter=';'):
    """
    Import localities from a CSV file.

    :param path: Path to the CSV file containing the localities.
    """

    creates = []
    updates = []

    with open(path, mode="r") as infile:
        reader = csv.DictReader(infile, delimiter=str(delimiter))

        with atomic():
            for row in reader:
                row['point'] = Point(float(row['longitude']),
                                     float(row['latitude']))
                locality, created = Locality.objects.update_or_create(
                    id=row['id'],
                    defaults=row
                )
                if created:
                    creates.append(locality)
                else:
                    updates.append(locality)

    return creates, updates
