"""
Contains application settings.
"""
from django.conf import settings


# By default, all scoring factors are weighted equally.
FACTORS = {
    'authoritative':    getattr(settings, 'AUTHORITATIVE_FACTOR', 0.2),
    'category':         getattr(settings, 'CATEGORY_FACTOR', 0.2),
    'like_type':        getattr(settings, 'LIKE_TYPE_FACTOR', 0.2),
    'spatial':          getattr(settings, 'SPATIAL_FACTOR', 0.2),
    'tag':              getattr(settings, 'TAG_FACTOR', 0.2),
}

# Normalize factors so that they add up to "1".
FACTOR_SUM = sum(FACTORS.values())

for k, v in FACTORS.iteritems():
    FACTORS[k] = float(v) / float(FACTOR_SUM)

AUTHORITATIVE_FACTOR    = FACTORS['authoritative']
CATEGORY_FACTOR         = FACTORS['category']
LIKE_TYPE_FACTOR        = FACTORS['like_type']
SPATIAL_FACTOR          = FACTORS['spatial']
TAG_FACTOR              = FACTORS['like_type']
