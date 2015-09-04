"""
Contains model unit tests.
"""
import decimal

from django.test import TestCase
from django.utils import timezone

from taggit.models import Tag
from wagtail.wagtailcore.models import Page
from wagtail.tests.testapp.models import TaggedPage

from ..app_settings import (
    AUTHORITATIVE_FACTOR,
    CATEGORY_FACTOR,
    LIKE_TYPE_FACTOR,
    TAG_FACTOR
)
from ..models import (
    Category,
    Entry,
    EntryTag
)


class BaseTestCase(TestCase):
    def setUp(self):
        # Create some categories.
        self.beer       = Category.add_root(name='beer')
        self.ale        = self.beer.add_child(name='ale')
        self.ipa        = self.ale.add_child(name='india pale ale')
        self.porter     = self.ale.add_child(name='porter')
        self.lager      = self.beer.add_child(name='lager')
        self.vienna     = self.lager.add_child(name='vienna lager')
        self.character  = Category.add_root(name='character')

        # Create some tags.
        self.spicy  = Tag.objects.create(name='spicy')
        self.fruity = Tag.objects.create(name='fruity')
        self.piny   = Tag.objects.create(name='piny')

class TestCategory(BaseTestCase):
    def test_str(self):
        self.assertEqual(
            str(self.ipa),
            self.ipa.name.title()
        )

    def test_has_tag(self):
        self.assertTrue(
            Tag.objects.filter(name__iexact=self.ipa.name).exists()
        )

class TestEntity(BaseTestCase):
    def setUp(self):
        super(TestEntity, self).setUp()

        # Find root page.
        self.root_page = Page.objects.get(id=2)

        # Add child page.
        self.child_page = TaggedPage(
            title   = 'Sculpin',
            slug    = 'sculpin',
        )

        self.root_page.add_child(instance=self.child_page)

        # Get corresponding Entity instance.
        self.entity = Entry.objects.get_for_model(self.child_page)[0]

    def create_related_pages(self):
        # Create some additional pages.
        pliny = self.root_page.add_child(instance=TaggedPage(
            title   = 'Pliny the Elder',
            slug    = 'pliny-elder'
        ))

        anchor_porter = self.root_page.add_child(instance=TaggedPage(
            title   = 'Anchor Porter',
            slug    = 'anchor-porter'
        ))

        # Relate pages through tags.
        for tag in [self.beer.tag, self.ale.tag, self.ipa.tag, self.fruity]:
            self.child_page.tags.through.objects.create(
                content_object  = self.child_page,
                tag             = tag
            )
        for tag in [self.beer.tag, self.ale.tag, self.ipa.tag, self.piny]:
            pliny.tags.through.objects.create(
                content_object  = pliny,
                tag             = tag
            )
        for tag in [self.beer.tag, self.ale.tag, self.porter.tag]:
            anchor_porter.tags.through.objects.create(
                content_object  = anchor_porter,
                tag             = tag
            )

        self.pliny          = pliny
        self.anchor_porter  = anchor_porter

    def test_get_for_tag(self):
        # Adding tags should create corresponding Entry and
        # EntryTag instances.
        self.child_page.tags.through.objects.create(
            content_object  = self.child_page,
            tag             = self.ipa.tag
        )

        self.assertTrue(
            self.entity
            in Entry.objects.get_for_tag(self.ipa.tag)
        )

    def test_tags_property(self):
        # Add some tags.
        tags = [
            self.beer.tag,
            self.ale.tag,
            self.ipa.tag,
            self.fruity
        ]

        for tag in tags:
            self.child_page.tags.through.objects.create(
                content_object  = self.child_page,
                tag             = tag
            )

        results = self.entity.tags

        for tag in tags:
            self.assertTrue(tag in results)

    def test_related_property(self):
        self.create_related_pages()

        entities = [
            Entry.objects.get_for_model(self.anchor_porter)[0],
            Entry.objects.get_for_model(self.pliny)[0]
        ]

        for entity in self.entity.related:
            self.assertTrue(entity in entities)

    def test_related_with_score_property(self):
        self.create_related_pages()

        entities = [
            Entry.objects.get_for_model(self.anchor_porter)[0],
            Entry.objects.get_for_model(self.pliny)[0]
        ]

        for entity, score in self.entity.related_with_scores:
            self.assertTrue(entity in entities)
            self.assertEqual(type(score), decimal.Decimal)
