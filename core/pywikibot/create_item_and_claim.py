import pywikibot

site = pywikibot.Site("en", "TillsWiki")
repo = site.data_repository()

data = {
    'labels': {
        'en': {
            'language': 'en',
            'value': 'Item with claim',
            }
        },
    'descriptions': {
        'en': {
            'language': 'en',
            'value': 'this is the item\'s description'
            }
        }
    }

item = pywikibot.ItemPage(site)
item.editEntity(data)

claim = pywikibot.Claim(site, u'P6')
target = pywikibot.ItemPage(site, u"Q9")
claim.setTarget(target)
item.addClaim(claim)

