# -*- coding: utf-8 -*-
"""
    django_geopostcodes.management.commands.import_localities
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Import a GeoPostCodes Locality file.
"""
from __future__ import absolute_import, print_function, unicode_literals
import logging
from optparse import make_option
from django.core.management.base import BaseCommand, CommandError
from django_geopostcodes.helpers import import_localities
from django.utils.translation import ugettext_lazy as _


logger = logging.getLogger('console.' + __name__)


class Command(BaseCommand):
    """
    Import a GeoPostCodes Locality file.
    """
    args = 'infile'
    help = _("Import a GeoPostCodes Locality file.")
    option_list = BaseCommand.option_list + (
        make_option('--delimiter',
                    dest='delimiter',
                    default=';',
                    help=_("Set the CSV delimiter."),
                    ),
    )

    def handle(self, *args, **options):
        if len(args) != 1:
            raise CommandError(_("Expected '%s' arguments.") % self.args)

        import_localities(args[0], options['delimiter'])


