# -*- coding: utf-8 -*-
"""
    django_geopostcodes.tests.test_helpers
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Test :py:module:`django_geopostcodes.helpers`.
"""
from __future__ import absolute_import, print_function, unicode_literals
import os
from django.utils import unittest
from ..helpers import import_localities
from ..models import Locality


class ImportLocalitiesTestCase(unittest.TestCase):

    def test_import_localities(self):
        self.assertEqual(Locality.objects.count(), 0)
        import_localities(os.path.join(os.path.dirname(__file__),
                                       'fixtures',
                                       'Sample_GeoPC_AU_Places.csv'),
                          "\t")
        self.assertEqual(Locality.objects.count(), 100)
