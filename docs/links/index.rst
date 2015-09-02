The Links Module
================

This module provides database storage for links - both email addresses and external URLs. Links are treated as
top-level entities in the Wagtail's administration dashboard, alongside pages, images, and documents. Links are
integrated into Wagtail's rich-text editor, replacing the default behavior of ad-hoc data entry each time a link
is included in HTML content. This allows for centralized control of links, minimizing broken link occurrences
throughout site content.

Module Installation
-------------------
First, add the module to ``settings.INSTALLED_APPS``::

    INSTALLED_APPS = (
        ...
        'wagtailplus.wagtaillinks',
        ...
    )

Then run ``manage.py syncdb`` (Django < 1.7) or ``manage.py migrate`` (Django >= 1.7).

Dashboard Menu
--------------

.. image:: https://raw.githubusercontent.com/rfosterslo/wagtailplus/master/images/links.png

Rich Text Integration
---------------------


.. image:: https://raw.githubusercontent.com/rfosterslo/wagtailplus/master/images/links-rich-text.png