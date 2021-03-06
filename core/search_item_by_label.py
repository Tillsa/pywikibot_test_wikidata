from pywikibot.data import api
import pywikibot
import pprint

def getItems(site, itemtitle):
    params = { 'action' :'wbsearchentities' , 'format' : 'json' , 'language' : 'en', 'type' : 'item', 'search': itemtitle}
    request = api.Request(site=site,**params)
    return request.submit()


site = pywikibot.Site("en", "TillsWiki")
WikidataEntries = getItems(site, "Transcript 0000")
print('\n', WikidataEntries)

if WikidataEntries['search'] == []:
    print('item with this label does not exist')
else:
    print('item with this label exists')

#print(WikidataEntries['search'][1]['id'])

#print(WikidataEntries['success']) # 1 = success



#print(dir(page))
#print(page.exists())
#item_dict = page.get()
#print(item_dict)
#print(page.title())
#print(site.page_exists(page))
#print(site.is_data_repository())
#print(site.page_exists(page))

#print(pywikibot.Page(site, u"Item with claim").exists())

#print(dir(page))

#repo = site.data_repository()

#print(site.has_data_repository)

#namespace = site.namespace(10).__contains__('Main page')
#print(namespace)
