# -*- coding: utf-8 -*-
"""Family module for Wikivoyage."""
from __future__ import absolute_import, unicode_literals

__version__ = '$Id: 3deafc7abd176ec6341da41f33d9524fbe88ca14 $'

# The new wikivoyage family that is hosted at wikimedia

from pywikibot import family


class Family(family.SubdomainFamily, family.WikimediaFamily):

    """Family class for Wikivoyage."""

    name = 'wikivoyage'

    def __init__(self):
        """Constructor."""
        self.languages_by_size = [
            'en', 'de', 'fa', 'it', 'fr', 'ru', 'nl', 'pt', 'pl', 'he', 'es',
            'vi', 'sv', 'zh', 'ro', 'el', 'uk',
        ]

        super(Family, self).__init__()

        # Global bot allowed languages on
        # https://meta.wikimedia.org/wiki/Bot_policy/Implementation#Current_implementation
        self.cross_allowed = ['es', 'ru', ]
