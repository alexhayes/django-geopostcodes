.. highlight:: shell

============
Installation
============


Stable release
--------------

To install django-geopostcodes, run this command in your terminal:

.. code-block:: console

    $ pip install django_geopostcodes

This is the preferred method to install django-geopostcodes, as it will always install the most recent stable release.

If you don't have `pip`_ installed, this `Python installation guide`_ can guide
you through the process.

.. _pip: https://pip.pypa.io
.. _Python installation guide: http://docs.python-guide.org/en/latest/starting/installation/


From sources
------------

The sources for django-geopostcodes can be downloaded from the `Github repo`_.

You can either clone the public repository:

.. code-block:: console

    $ git clone git://github.com/alexhayes/django_geopostcodes

Or download the `tarball`_:

.. code-block:: console

    $ curl -OJL https://github.com/alexhayes/django_geopostcodes/tarball/master

Once you have a copy of the source, you can install it with:

.. code-block:: console

    $ python setup.py install


.. _Github repo: https://github.com/alexhayes/django_geopostcodes
.. _tarball: https://github.com/alexhayes/django_geopostcodes/tarball/master

Django Settings
---------------

Then place ``django_geopostcodes`` in your ``INSTALLED_APPS``;

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_geopostcodes',
        ...
    )


Data Import
-----------

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
