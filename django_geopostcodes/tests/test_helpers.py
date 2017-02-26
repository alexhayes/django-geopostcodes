# -*- coding: utf-8 -*-
"""
    django_geopostcodes.tests.test_helpers
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Test :py:module:`django_geopostcodes.helpers`.
"""
from __future__ import absolute_import, print_function, unicode_literals
import os

try:
    # django 1.7
    from django.utils.unittest import TestCase
except ImportError:
    # django 1.8+
    from django.test import TestCase

from ..helpers import import_localities
from ..models import Locality


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
