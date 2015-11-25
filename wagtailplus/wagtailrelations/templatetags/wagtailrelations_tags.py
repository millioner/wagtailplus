"""
Contains application template tags.
"""
from django import template
from django.core import urlresolvers

from ..models import Entry


register = template.Library()

@register.assignment_tag
def get_related(page):
    """
    Returns list of related Entry instances for specified page.

    :param page: the page instance.
    :rtype: list.
    """
    related = []
    entry   = Entry.get_for_model(page)

    if entry:
        related = entry.related

    return related

@register.simple_tag
def get_related_entry_admin_url(entry):
    """
    Returns admin URL for specified entry instance.

    :param entry: the entry instance.
    :return: str.
    """
    return urlresolvers.reverse(
        'admin:{0}_{1}_change'.format(entry.content_type.app_label, entry.content_type.model),
        args=(entry.object_id,)
    )

@register.assignment_tag
def get_related_with_scores(page):
    """
    Returns list of related tuples (Entry instance, score) for
    specified page.

    :param page: the page instance.
    :rtype: list.
    """
    related = []
    entry   = Entry.get_for_model(page)

    if entry:
        related = entry.related_with_scores

    return related
