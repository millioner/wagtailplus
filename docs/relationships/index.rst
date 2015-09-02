The Relationships Module
========================

This module uses Wagtail's implementation of ``django-taggit`` to automatically create relationships between individual
pieces of content. The relationship between any two pieces of content is assigned a numerical score (decimal) between
0 and 1, based on configurable scoring factors.

Module Installation
-------------------
First, add the module to ``settings.INSTALLED_APPS``::

    INSTALLED_APPS = (
        ...
        'wagtailplus.wagtailrelationships',
        ...
    )

Then run ``manage.py syncdb`` (Django < 1.7) or ``manage.py migrate`` (Django >= 1.7). The following settings my
be added to ``settings.py`` to influence the score assigned to two pieces of content::

    AUTHORITATIVE_FACTOR    = [0.25]
    CATEGORY_FACTOR         = [0.25]
    LIKE_TYPE_FACTOR        = [0.25]
    TAG_FACTOR              = [0.25]

Scoring Factors
---------------


Authoritative Factor
^^^^^^^^^^^^^^^^^^^^


Category Factor
^^^^^^^^^^^^^^^


Like Type Factor
^^^^^^^^^^^^^^^^


Tag Factor
^^^^^^^^^^

