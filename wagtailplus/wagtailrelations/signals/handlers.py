"""
Contains application signal handlers.
"""
from django.contrib.contenttypes.models import ContentType
from django.apps import apps
from django.db.models import signals

from taggit.models import TaggedItemBase


def get_entry(instance):
    """
    Returns Entry instance corresponding to specified instance.

    :param instance: the instance.
    :rtype: wagtailplus.wagtailrelations.models.Entry.
    """
    from ..models import Entry

    obj = instance.content_object

    return Entry.objects.get_or_create(
        content_type    = ContentType.objects.get_for_model(obj),
        object_id       = obj.pk
    )

#noinspection PyUnusedLocal
def create_entry_tag(sender, instance, created, **kwargs):
    """
    Creates EntryTag for Entry corresponding to specified
    TaggedItemBase instance.

    :param sender: the sending TaggedItemBase class.
    :param instance: the TaggedItemBase instance.
    """
    from ..models import EntryTag

    entry, created = get_entry(instance)

    if not created:
        entry.save()

    tag = instance.tag

    if not EntryTag.objects.filter(tag=tag, entry=entry).exists():
        EntryTag.objects.create(tag=tag, entry=entry)

#noinspection PyUnusedLocal
def delete_entry_tag(sender, instance, **kwargs):
    """
    Deletes EntryTag for Entry corresponding to specified
    TaggedItemBase instance.

    :param sender: the sending TaggedItemBase class.
    :param instance: the TaggedItemBase instance.
    """
    from ..models import EntryTag

    entry   = get_entry(instance)[0]
    tag     = instance.tag

    EntryTag.objects.filter(tag=tag, entry=entry).delete()

#noinspection PyUnusedLocal
def delete_entry(sender, instance, **kwargs):
    """
    Deletes Entry instance corresponding to specified instance.

    :param sender: the sending class.
    :param instance: the instance being deleted.
    """
    from ..models import Entry

    Entry.objects.filter(
        content_type    = ContentType.objects.get_for_model(instance),
        object_id       = instance.pk
    ).delete()

for model in apps.get_models():
    # Connect signals to TaggedItemBase classes.
    if issubclass(model, TaggedItemBase):
        # Create EntryTag instance.
        signals.post_save.connect(
            create_entry_tag,
            sender          = model,
            dispatch_uid    = 'wagtailrelations_create_entry_tag'
        )

        # Delete EntryTag instance.
        signals.post_delete.connect(
            delete_entry_tag,
            sender          = model,
            dispatch_uid    = 'wagtailrelations_delete_entry_tag'
        )

    # Connect signals to classes with a "tags" field.
    meta = getattr(model, '_meta')

    if 'tags' in meta.get_all_field_names():
        # Delete Entry instance.
        signals.post_delete.connect(
            delete_entry,
            sender          = model,
            dispatch_uid    = 'wagtailrelations_delete_entry'
        )
