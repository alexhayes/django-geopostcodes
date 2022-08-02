Developer Documentation
=======================

Contributions
-------------

Contributions are more than welcomed!

To get setup do the following;

.. code-block:: bash

    mkvirtualenv --python=/usr/bin/python3 django-geopostcodes
    git clone https://github.com/alexhayes/django-geopostcodes.git
    cd django-geopostcodes
    pip install -r requirements/dev.txt

Note that you don't have to use Python 3 and indeed tox tests for many versions
of Python, but you may as well develop on it, what reason is there not to for
such a small application?!

Running Tests
-------------

Once you've checked out you should be able to run the tests.

.. code-block:: bash

    detox

or, alternatively;

.. code-block:: bash

    ./manage.py test


Migrations
----------

If you need to make modelling changes please run :code:`makemigrations` so that
the migration is included in your pull request.

.. code-block:: bash

    ./manage.py makemigrations


Creating translations
---------------------

Translations are welcomed! Please fork and then from the root

.. code-block:: bash

    cd django_geopostcodes
    ./../manage.py makemessages -l [LOCALE-NAME]

Then, edit the translations in :code:`django_geopostcodes/locale`, then;

.. code-block:: bash

    ./../manage.py compilemessages


Creating Documentation
----------------------

.. code-block:: bash

    cd docs
    make clean html

