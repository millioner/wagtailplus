The wagtailplus.wagtailrollbacks Module
=======================================

This module enables users to "rollback" or revert to previous versions of a page, using Wagtail's default page
revisions. This is handled via a "history" tab is automatically added to the edit handler of every page model class.

Module Installation
-------------------
Simply add the module to ``settings.INSTALLED_APPS``::

    INSTALLED_APPS = (
        ...
        'wagtailplus.wagtailrollbacks',
        ...
    )

This module does not include any model classes, so there is no need to run ``manage.py syncdb`` or ``manage.py migrate``.