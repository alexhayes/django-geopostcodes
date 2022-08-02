Usage
=====

Locality
--------

Presently there is a single model :py:class:`.Locality` which contains
localities as a flat structure as defined in the imported CSV.

The API is limited to just a custom query set manager
:py:class:`.LocalityQuerySet` at this stage.

You can query for localities as follows;

.. code-block:: python

    from django_geopostcodes.models import Locality
    from django.contrib.gis.measure import D

    # Find a locality by post code
    melbourne = Locality.objects.get(postcode='3000')

    # Find other localities 5km from Melbourne
    nearby = Locality.objects.filter(point__distance_lte=(melbourne.point, D(km=5)))

    # Find a locality that matches any text
    localities = Locality.objects.anything_icontains('Victoria')

    # Find any locality that starts with 'aus'
    within_australia = Locality.objects.anything_istartswith('aus')
