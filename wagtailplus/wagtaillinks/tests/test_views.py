"""
Contains application unit tests.
"""
from django.core.urlresolvers import reverse

from wagtailplus.utils.views import tests
from ..models import Link


class TestLinkIndexView(tests.BaseTestIndexView):
    url_namespace   = 'wagtaillinks'
    template_dir    = 'wagtaillinks/links'

    def _create_sequential_instance(self, index):
        Link.objects.create(
            link_type       = Link.LINK_TYPE_EXTERNAL,
            title           = 'Link #{0}'.format(index),
            external_url    = 'http://www.site-{0}.com'.format(index)
        )

class TestLinkCreateView(tests.BaseTestCreateView):
    url_namespace   = 'wagtaillinks'
    template_dir    = 'wagtaillinks/links'
    model_class     = Link
    filter_keys     = ['title']

    def _get_post_data(self):
        return {
            'link_type':    Link.LINK_TYPE_EXTERNAL,
            'title':        'Test Link',
            'external_url': 'http://www.test.com'
        }

class TestLinkUpdateView(tests.BaseTestUpdateView):
    url_namespace   = 'wagtaillinks'
    template_dir    = 'wagtaillinks/links'
    model_class     = Link

    def _get_instance(self):
        return Link.objects.create(
            link_type       = Link.LINK_TYPE_EXTERNAL,
            title           = 'Test Link',
            external_url    = 'http://www.test.com'
        )

    def _get_post_data(self):
        return {
            'link_type':    Link.LINK_TYPE_EXTERNAL,
            'title':        'Test Link Changed',
            'external_url': 'http://www.test.com'
        }

class TestLinkDeleteView(tests.BaseTestDeleteView):
    url_namespace   = 'wagtaillinks'
    template_dir    = 'wagtaillinks/links'
    model_class     = Link

    def _get_instance(self):
        return Link.objects.create(
            link_type       = Link.LINK_TYPE_EXTERNAL,
            title           = 'Test Link',
            external_url    = 'http://www.test.com'
        )

class TestEmailLinkChooserView(tests.BaseTestChooserView):
    url_namespace   = 'wagtaillinks'
    template_dir    = 'wagtaillinks/chooser'
    model_class     = Link

    def _create_sequential_instance(self, index):
        return Link.objects.create(
            link_type   = Link.LINK_TYPE_EMAIL,
            title       = 'Test Email #{0}'.format(index),
            email       = 'somebody-{0}@something.com'.format(index)
        )

    def get(self, params=None):
        if not params:
            params = {}

        return self.client.get(
            reverse('wagtailadmin_choose_page_email_link'),
            params
        )

class TestExternalLinkChooserView(tests.BaseTestChooserView):
    url_namespace   = 'wagtaillinks'
    template_dir    = 'wagtaillinks/chooser'
    model_class     = Link

    def _create_sequential_instance(self, index):
        return Link.objects.create(
            link_type       = Link.LINK_TYPE_EXTERNAL,
            title           = 'Test Link #{0}'.format(index),
            external_url    = 'http://www.site-{0}.com'.format(index)
        )

    def get(self, params=None):
        if not params:
            params = {}

        return self.client.get(
            reverse('wagtailadmin_choose_page_external_link'),
            params
        )

class TestEmailLinkChosenView(tests.BaseTestChosenView):
    url_namespace   = 'wagtaillinks'
    template_dir    = 'wagtaillinks/chooser'
    model_class     = Link

    def _get_instance(self):
        return Link.objects.create(
            link_type   = Link.LINK_TYPE_EMAIL,
            title       = 'Test Email',
            email       = 'somebody@something.com'
        )

class TestExternalLinkChosenView(tests.BaseTestChosenView):
    url_namespace   = 'wagtaillinks'
    template_dir    = 'wagtaillinks/chooser'
    model_class     = Link

    def _get_instance(self):
        return Link.objects.create(
            link_type       = Link.LINK_TYPE_EXTERNAL,
            title           = 'Test Link',
            external_url    = 'http://www.test.com'
        )
