The Rollbacks Module
====================

This module enables users to "rollback" or revert to previous versions of a page, using Wagtail's default page
revisions. This is handled via a "history" tab is automatically added to the edit handler of every page model class.
Users are presented with a confirmation page prior to actually reverting to a previous version, and the actions they
may take are based on existing user page permissions.


Module Installation
-------------------
Simply add the module to ``settings.INSTALLED_APPS``::

    INSTALLED_APPS = (
        ...
        'wagtailplus.wagtailrollbacks',
        ...
    )

This module does not include any model classes, so there is no need to run ``manage.py syncdb`` or ``manage.py migrate``.

.. image:: https://raw.githubusercontent.com/rfosterslo/wagtailplus/master/images/rollbacks.png

.. image:: https://raw.githubusercontent.com/rfosterslo/wagtailplus/master/images/rollbacks_confirm.png