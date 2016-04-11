import pywikibot

site = pywikibot.Site("en", "TillsWiki")
#repo = site.data_repository()

item = pywikibot.ItemPage(site, u"Q25")

claim = pywikibot.Claim(site, u'P6')
target = pywikibot.ItemPage(site, u"Q6")
claim.setTarget(target)
item.addClaim(claim)
