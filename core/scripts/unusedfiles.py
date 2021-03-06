#!/usr/bin/python
# -*- coding: utf-8  -*-
"""
This bot appends some text to all unused images and notifies uploaders.

Parameters:

-always     Don't be asked every time.

"""
#
# (C) Leonardo Gregianin, 2007
# (C) Filnik, 2008
# (c) xqt, 2011-2014
# (C) Pywikibot team, 2015
#
# Distributed under the terms of the MIT license.
#
from __future__ import absolute_import, unicode_literals

__version__ = '$Id: 3024a2a481f3ba45fde36abcbc3c0050c267ea27 $'
#

import pywikibot
from pywikibot import i18n, pagegenerators, Bot

template_to_the_image = {
    'it': u'{{immagine orfana}}',
    'fa': u'{{تصاویر بدون استفاده}}',
}

# This template message should use subst:
template_to_the_user = {
    'fa': u'\n\n{{جا:اخطار به کاربر برای تصاویر بدون استفاده|%(title)s}}--~~~~',
}


class UnusedFilesBot(Bot):

    """Unused files bot."""

    def __init__(self, site, **kwargs):
        """Constructor."""
        super(UnusedFilesBot, self).__init__(**kwargs)
        self.site = site

    def run(self):
        """Start the bot."""
        template_image = i18n.translate(self.site,
                                        template_to_the_image)
        template_user = i18n.translate(self.site,
                                       template_to_the_user)
        self.summary = i18n.twtranslate(self.site, 'unusedfiles-comment')
        if not all([template_image, template_user]):
            raise pywikibot.Error(u'This script is not localized for %s site.'
                                  % self.site)
        generator = pagegenerators.UnusedFilesGenerator(site=self.site)
        generator = pagegenerators.PreloadingGenerator(generator)
        for image in generator:
            if not image.exists():
                pywikibot.output("File '%s' does not exist (see bug T71133)."
                                 % image.title())
                continue
            # Use fileUrl() and fileIsShared() to confirm it is local media
            # rather than a local page with the same name as shared media.
            if (image.fileUrl() and not image.fileIsShared() and
                    u'http://' not in image.text):
                if template_image in image.text:
                    pywikibot.output(u"%s done already"
                                     % image.title(asLink=True))
                    continue
                self.append_text(image, u"\n\n" + template_image)
                uploader = image.getFileVersionHistory().pop(0)['user']
                user = pywikibot.User(image.site, uploader)
                usertalkpage = user.getUserTalkPage()
                msg2uploader = template_user % {'title': image.title()}
                self.append_text(usertalkpage, msg2uploader)

    def append_text(self, page, apptext):
        """Append apptext to the page."""
        if page.isRedirectPage():
            page = page.getRedirectTarget()
        if page.exists():
            text = page.text
        else:
            if page.isTalkPage():
                text = u''
            else:
                raise pywikibot.NoPage(page)

        oldtext = text
        text += apptext
        self.userPut(page, oldtext, text, summary=self.summary)


def main(*args):
    """
    Process command line arguments and invoke bot.

    If args is an empty list, sys.argv is used.

    @param args: command line arguments
    @type args: list of unicode
    """
    options = {}

    for arg in pywikibot.handle_args(args):
        if arg == '-always':
            options['always'] = True

    bot = UnusedFilesBot(pywikibot.Site(), **options)
    try:
        bot.run()
    except pywikibot.Error as e:
        pywikibot.bot.suggest_help(exception=e)
        return False
    else:
        return True


if __name__ == "__main__":
    main()
