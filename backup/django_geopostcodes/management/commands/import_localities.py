# -*- coding: utf-8 -*-
"""
    django_geopostcodes.management.commands.import_localities
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Import a GeoPostCodes Locality file.
"""
from __future__ import absolute_import, print_function, unicode_literals

import logging

from django.core.management.base import BaseCommand
from django_geopostcodes.helpers import import_localities
from django.utils.translation import ugettext_lazy as _


logger = logging.getLogger('console.' + __name__)


class Command(BaseCommand):
    """
    Import a GeoPostCodes Locality file.
    """
    help = _("Import a GeoPostCodes Places.csv file.")

    def add_arguments(self, parser):
        parser.add_argument('infile', type=str, help=_("Path to CSV file."))
        parser.add_argument('--delimiter', type=str, default=';', help=_("Set the CSV delimiter."))

    def handle(self, *args, **options):
        import_localities(options['infile'], options['delimiter'])
