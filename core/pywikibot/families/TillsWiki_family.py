from pywikibot import family                                                    
                                                                                
class Family(family.Family):                                                    
    def __init__(self):                                                         
        family.Family.__init__(self)                                            
        self.name = 'TillsWiki'                                                       
        self.langs = {                                                          
            'en': 'https://wrzh182.rzhousing.uni-wuerzburg.de',                                
        }
    def scriptpath(self, code):
        return 'https://wrzh182.rzhousing.uni-wuerzburg.de/mediawiki'
    
    def protocol(self, code):
        return 'HTTPS'
    
    def ignore_certificate_error(self, code):
        return True

    def shared_data_repository(self, code, transcluded=False):
        """
        Indicate Wikidata is both a repository and its own client.
        Until 20 August 2014, Wikidata was only a data repository,
        and this method only returned a tuple with data if
        transcluded was False.
        On that date, the software was enhanced so that Wikidata
        could store sitelinks to itself.
        """
        return (code, self.name)
    def interface(self, code):
        """Return 'DataSite'."""
        return 'DataSite'      
