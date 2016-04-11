import pywikibot

site = pywikibot.Site("en", "TillsWiki")
#repo = site.data_repository()
item = pywikibot.ItemPage(site, "Q10")
#print(item)
#print(dir(item))
item_dict = item.get() #Get the item dictionary
clm_dict = item_dict["claims"] # Get the claim dictionary
#print(item_dict)
#print(item_dict.keys())
#print(item_dict["claims"])

clm_list = clm_dict["P9"]
#print(clm_list)

for clm in clm_list:
    #print(lcm)
    #print(dir(clm))
    #print(clm.toJSON())
    clm_trgt = clm.getTarget()
    print(clm_trgt)
    print(type(clm_trgt))
    print(dir(clm_trgt))
    
          
