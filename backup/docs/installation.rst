============
Installation
============

You can install django-geopostcodes either via the Python Package Index (PyPI)
or from github.

To install using pip;

.. code-block:: bash

    $ pip install django-geopostcodes

From github;

.. code-block:: bash

    $ pip install git+https://github.com/alexhayes/django-geopostcodes.git

Then place ``django_geopostcodes`` in your ``INSTALLED_APPS``;

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_geopostcodes',
        ...
    )


Import
======

django-geopostcodes by itself only provides models and helpers, you must
purchase and import the geo post code data from `geopostcodes.com`_.

Upon purchase from `geopostcodes.com`_ you will be able to down a zip file that
contains files that can be imported into django-geopostcodes.

Currently django-geopostcodes only supports localities, however feel free to
fork and add support for regions and businesses.

Once you've completed your purchase from `geopostcodes.com`_ you will be able
to download a ZIP file containing data in a number of formats. Inside the ZIP
file there should be a folder called ``CSV`` and within this folder should be a
file titled ``GeoPC_XX_Places.csv`` where ``XX`` is the two letter ISO country
code.

You can import this file into django-geopostcodes as follows;

.. code-block:: bash

    python manage.py import_localities /path/to/GeoPC_XX_Places.csv


.. _geopostcodes.com: http://www.geopostcodes.com
