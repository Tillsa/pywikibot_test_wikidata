import pywikibot
site = pywikibot.Site("en", "TillsWiki")
item = pywikibot.ItemPage(site, u"Transcript 0000")
dictionary = item.get()
print(dictionary)
print(dictionary.keys())
print(item)
