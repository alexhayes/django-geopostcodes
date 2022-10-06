# -*- coding: utf-8 -*-
"""
    django_geopostcodes.tests.test_helpers
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Test :py:module:`django_geopostcodes.helpers`.
"""
from __future__ import absolute_import, print_function, unicode_literals
import os

from django.test import TestCase
from django_geopostcodes.helpers import import_localities
from django_geopostcodes.models import Locality


def create_sample_localities():
    import_localities(os.path.join(os.path.dirname(__file__),
                                   'fixtures',
                                   'Sample_GeoPC_AU_Places.csv'),
                      "\t")


class ImportLocalitiesTestCase(TestCase):

    def test_import_localities(self):
        self.assertEqual(Locality.objects.count(), 0)
        create_sample_localities()
        self.assertEqual(Locality.objects.count(), 100)
