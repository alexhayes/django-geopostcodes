========================
 pip requirements files
========================


Index
=====

* :file:`requirements/default.txt`

    Default requirements for Python 2.7+.

* :file:`requirements/test.txt`

    Requirements needed to run the full unittest suite via ./runtests.py

* :file:`requirements/doc.txt`

    Extra requirements required to build the Sphinx documentation.

* :file:`requirements/pkgutils.txt`

    Extra requirements required to perform package distribution maintenance.


Examples
========

Installing requirements
-----------------------

::

    $ pip install -U -r requirements/default.txt


Running the tests
-----------------

::

    $ pip install -U -r requirements/default.txt
    $ pip install -U -r requirements/test.txt
