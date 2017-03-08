# -*- coding: utf-8 -*-
"""Django modelling for http://www.geopostcodes.com"""
# :copyright: (c) 2015 Alex Hayes and individual contributors,
#                 All rights reserved.
# :license:   MIT License, see LICENSE for more details.


from collections import namedtuple

version_info_t = namedtuple(
    'version_info_t', ('major', 'minor', 'micro', 'releaselevel', 'serial'),
)

VERSION = version_info_t(0, 2, 2, '', '')
__version__ = '{0.major}.{0.minor}.{0.micro}{0.releaselevel}'.format(VERSION)
__author__ = 'Alex Hayes'
__contact__ = 'alex@alution.com'
__homepage__ = 'http://github.com/alexhayes/django-geopostcodes'
__docformat__ = 'restructuredtext'

# -eof meta-

default_app_config = 'django_geopostcodes.apps.DjangoGeoPostCodesAppConfig'
