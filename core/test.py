import pywikibot

site = pywikibot.Site("test", "wikidata")
repo = site.data_repository()
item = pywikibot.ItemPage(repo, u"Q2306") # item:RNA
claim = pywikibot.Claim(repo, u"P82")    # instance of
target = pywikibot.ItemPage(repo, u"Q2312") # chemical compound
claim.setTarget(target)
item.addClaim(claim)



#claim =
#item.addClaim(claim)
#item_page = pywikibot.ItemPage(repo, "Q2306")
#print(dir(item_page))
#data_item = item_page.data_item()
#print(data_item)

#item_dict = item.get()
#print(dir(item_dict))
#print(item_dict.keys())
#print(item_dict['labels'])

#print(repoitem = pywikibot.ItemPage(reoi, u"Q25")
#print(dir(item))
#print(item.data_item())
#claim = pywikibot.Claim(site, u'P6')
#target = pywikibot.ItemPage(site, u"Q6")
#claim.setTarget(target)
#item.addClaim(claim)
