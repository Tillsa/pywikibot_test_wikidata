import argparse
import csv
import pywikibot
from pywikibot.data import api
import pprint

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("transcript_file", help="the file, that contains the transcript information")
    parser.add_argument("strain_name", help="please type in the correct name of the strand")
    
    args = parser.parse_args()

    bab = BacterialAnnotationBot(args.transcript_file, args.strain_name)

    #bab.read_csv()

    strain = Strain(args.strain_name)


    strain.create_strain_item_id_list()
  
    strain.create_strain_item()
  
   
class BacterialAnnotationBot():

    def __init__(self, transcript_file, strain_name):
        self.transcript_file = transcript_file
        self.strain_name = strain_name

    def read_csv(self):
        transcript_file = self.transcript_file
        with open(transcript_file) as csvfile:
            transcript_dict = csv.DictReader(csvfile, delimiter="\t")
            for row in transcript_dict:
                site = pywikibot.Site("en", "TillsWiki")
                
    def create_new_item(self):

                data = {
                    'labels': {
                        'en': {
                            'language': 'en',
                            'value': row['Name']
                        }
                    },
                    'descriptions': {
                        'en': {
                            'language': 'en',
                            'value': 'bacterial transcript found in ' + self.strain_name
                        }
                    }
                }

                item = pywikibot.ItemPage(site)
                item.editEntity(data)

    def getItems(site, itemtitle):
        params = { 'action' :'wbsearchentities' , 'format' : 'json' , 'language' : 'en', 'type' : 'item', 'search': itemtitle}
        request = api.Request(site=site,**params)
        return request.submit()
                
                #print(row['strain'],"\n")
                #print(row)
class Strain():
    
    def __init__(self, strain_name):
        self.strain_name = strain_name
        self.site = pywikibot.Site("test", "wikidata") # 'test' needs to be replaced by 'wikidata'
        self.repo = self.site.data_repository()
        self.strain_item_id_list = []
        self.strain_item_candidates = []
        

    def _search_item_by_label(self, site, strainname):
        params = { 'action' :'wbsearchentities' , 'format' : 'json' , 'language' : 'en', 'type' : 'item', 'search': strainname}
        request = api.Request(site=site,**params)
        return request.submit()    
     
    def create_strain_item_id_list(self):
        Strain_name_Entries = self._search_item_by_label(self.site, self.strain_name)
        strain_items_with_matching_label = []
        for list_item in Strain_name_Entries['search']:
            if list_item['label'] == self.strain_name:
                strain_items_with_matching_label.append(list_item['id'])
            else:
                continue
        if strain_items_with_matching_label == []:
            print("there are no items with the exact name as your strain_name")
        else:
            print("items that match the strain name:", strain_items_with_matching_label)
        for ID in strain_items_with_matching_label:
            item = pywikibot.ItemPage(self.site, ID)
            item_id = item.getID()
            item_dict = item.get()
            item_en_description = item_dict['descriptions']['en']
            if item_en_description == "bacterial strain":
                print("item {} matches the strain name and has description 'bacterial strain'".format(ID, item_en_description))
                self.strain_item_id_list.append(ID)
                
            else:
                print("item {} matches the strain name, but has no description 'bacterial strain'".format(ID, item_en_description))
                
                


    def create_strain_item(self):
        if self.strain_item_id_list == []:
            print("suitable strain item does not exist")
            data = {
                'labels': {
                    'en': {
                        'language': 'en',
                        'value': self.strain_name
                    }
                },
                'descriptions': {
                    'en': {
                        'language': 'en',
                        'value': 'bacterial strain'
                    }
                }
            }

            
            
            item = pywikibot.ItemPage(self.repo)
            item.editEntity(data)
            item_id = item.getID()
            new_item = pywikibot.ItemPage(self.repo, item_id)
            claim = pywikibot.Claim(self.repo, u"P82") # P82(test)-> instance of = P31(wikidata)-> instance of
            target = pywikibot.ItemPage(self.repo, u"Q2308") # Q2308(test) -> strain = Q855769(wikidata) -> strain
            claim.setTarget(target)
            new_item.addClaim(claim)
            
            print("created item {} for strain {}".format(item_id, self.strain_name))

        else:
            print("no need for creating new strain item; make use of the item {}".format(self.strain_item_id_list[0]))
                


    
                
main()
