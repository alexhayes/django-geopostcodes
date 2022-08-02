# -*- coding: utf-8 -*-
"""
    django_geopostcodes.tests.test_models
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Tests for django-geopostcodes models.
"""
from __future__ import absolute_import, print_function, unicode_literals
import os
import unittest
from django.contrib.gis.geos import Point
from django_geopostcodes.helpers import import_localities
from ..models import Locality


class LocalityQuerySetTestCase(unittest.TestCase):

    def setUp(self):
        import_localities(os.path.join(os.path.dirname(__file__),
                                       'fixtures',
                                       'Sample_GeoPC_AU_Places.csv'),
                          "\t")

    def test_distance(self):
        self.assertEqual(Locality.objects.count(), 100)
        self.assertEqual(Locality.objects.filter(point=Point(149.075273, -33.648855)).count(), 1)
        self.assertEqual(Locality.objects.filter(point__distance_lte=(Point(149.075273, -33.648855), 0.00001)).count(), 1)
        self.assertEqual(Locality.objects.filter(point__distance_lte=(Point(149.075273, -33.648855), 0.2)).count(), 5)

    def test_anything_contains(self):
        self.assertEqual(Locality.objects.count(), 100)
        self.assertEqual(Locality.objects.anything_contains('Australia').count(), 100)
        self.assertEqual(Locality.objects.anything_contains('New South').count(), 100)
        self.assertEqual(Locality.objects.anything_contains('Victoria').count(), 0)
        self.assertEqual(Locality.objects.anything_contains('Blayney').count(), 7)
        self.assertEqual(Locality.objects.anything_contains('Panuara').count(), 1)
        self.assertEqual(Locality.objects.anything_contains('Cowra').count(), 9)
        self.assertEqual(Locality.objects.anything_contains('2866').count(), 5)

    def test_anything_icontains(self):
        self.assertEqual(Locality.objects.count(), 100)
        self.assertEqual(Locality.objects.anything_icontains('Austr').count(), 100)
        self.assertEqual(Locality.objects.anything_icontains('New South Wales').count(), 100)
        self.assertEqual(Locality.objects.anything_icontains('Vic').count(), 0)
        self.assertEqual(Locality.objects.anything_icontains('Blayney').count(), 7)
        self.assertEqual(Locality.objects.anything_icontains('Panu').count(), 1)
        self.assertEqual(Locality.objects.anything_icontains('Cowr').count(), 9)
        self.assertEqual(Locality.objects.anything_icontains('286').count(), 17)
        self.assertEqual(Locality.objects.anything_icontains('28').count(), 76)

    def test_anything_exact(self):
        self.assertEqual(Locality.objects.count(), 100)
        self.assertEqual(Locality.objects.anything_exact('Australia').count(), 100)
        self.assertEqual(Locality.objects.anything_exact('New South').count(), 0)
        self.assertEqual(Locality.objects.anything_exact('Victoria').count(), 0)
        self.assertEqual(Locality.objects.anything_exact('Blayney').count(), 7)
        self.assertEqual(Locality.objects.anything_exact('Panuara').count(), 1)
        self.assertEqual(Locality.objects.anything_exact('Cowra').count(), 9)
        self.assertEqual(Locality.objects.anything_exact('Cowr').count(), 0)
        self.assertEqual(Locality.objects.anything_exact('2866').count(), 5)
        self.assertEqual(Locality.objects.anything_exact('28').count(), 0)

    def test_anything_iexact(self):
        self.assertEqual(Locality.objects.count(), 100)
        self.assertEqual(Locality.objects.anything_iexact('Australia').count(), 100)
        self.assertEqual(Locality.objects.anything_iexact('New South').count(), 0)
        self.assertEqual(Locality.objects.anything_iexact('Victoria').count(), 0)
        self.assertEqual(Locality.objects.anything_iexact('Blayney').count(), 7)
        self.assertEqual(Locality.objects.anything_iexact('Panuara').count(), 1)
        self.assertEqual(Locality.objects.anything_iexact('Cowra').count(), 9)
        self.assertEqual(Locality.objects.anything_iexact('Cowr').count(), 0)
        self.assertEqual(Locality.objects.anything_iexact('2866').count(), 5)
        self.assertEqual(Locality.objects.anything_iexact('28').count(), 0)

    def test_anything_startswith(self):
        self.assertEqual(Locality.objects.count(), 100)
        self.assertEqual(Locality.objects.anything_startswith('Aus').count(), 100)
        self.assertEqual(Locality.objects.anything_startswith('ustralia').count(), 0)
        self.assertEqual(Locality.objects.anything_startswith('New South').count(), 100)
        self.assertEqual(Locality.objects.anything_startswith('Victoria').count(), 0)
        self.assertEqual(Locality.objects.anything_startswith('Blayn').count(), 7)
        self.assertEqual(Locality.objects.anything_startswith('ayney').count(), 0)
        self.assertEqual(Locality.objects.anything_startswith('Panuara').count(), 1)
        self.assertEqual(Locality.objects.anything_startswith('Cowra').count(), 9)
        self.assertEqual(Locality.objects.anything_startswith('Cowr').count(), 9)
        self.assertEqual(Locality.objects.anything_startswith('owra').count(), 0)
        self.assertEqual(Locality.objects.anything_startswith('2866').count(), 5)
        self.assertEqual(Locality.objects.anything_startswith('66').count(), 0)
        self.assertEqual(Locality.objects.anything_startswith('28').count(), 76)

    def test_anything_istartswith(self):
        self.assertEqual(Locality.objects.count(), 100)
        self.assertEqual(Locality.objects.anything_startswith('Aus').count(), 100)
        self.assertEqual(Locality.objects.anything_startswith('ustralia').count(), 0)
        self.assertEqual(Locality.objects.anything_startswith('New South').count(), 100)
        self.assertEqual(Locality.objects.anything_startswith('Victoria').count(), 0)
        self.assertEqual(Locality.objects.anything_startswith('Blayn').count(), 7)
        self.assertEqual(Locality.objects.anything_startswith('ayney').count(), 0)
        self.assertEqual(Locality.objects.anything_startswith('Panuara').count(), 1)
        self.assertEqual(Locality.objects.anything_startswith('Cowra').count(), 9)
        self.assertEqual(Locality.objects.anything_startswith('Cowr').count(), 9)
        self.assertEqual(Locality.objects.anything_startswith('owra').count(), 0)
        self.assertEqual(Locality.objects.anything_startswith('2866').count(), 5)
        self.assertEqual(Locality.objects.anything_startswith('66').count(), 0)
        self.assertEqual(Locality.objects.anything_startswith('28').count(), 76)

    def test_chain(self):
        self.assertEqual(Locality.objects.anything_icontains('Mandurama').filter(point__distance_lte=(Point(149.075273, -33.648855), 0.00001)).count(), 1)
        self.assertEqual(Locality.objects.anything_icontains('New South').filter(point__distance_lte=(Point(149.075273, -33.648855), 0.00001)).count(), 1)
        self.assertEqual(Locality.objects.anything_icontains('Panuara').filter(point__distance_lte=(Point(149.075273, -33.648855), 0.00001)).count(), 0)


