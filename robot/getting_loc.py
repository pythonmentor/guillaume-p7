####################################################################
# this class uses the tag words of ParseSentence class and make a 
# research on googlemaps to get the location and a formated adress
# of the wanted location
####################################################################

# import modules
import os 

import googlemaps
from mediawiki import MediaWiki


# personnal modules, deactivate for pytest
#from parse import ParseSentence
#from functions_rac import compile_list

# personnal modules, activate only for pytest
from robot.parse import ParseSentence
from robot.functions_rac import compile_list


class ResearchLoc(object):
    """This class returns a formated adress
    and lattitude / longitude of places 
    you're looking for"""

    # init function
    def __init__(self, sentence):
        self.sentence = sentence
        # using ParseSentence from parse.py to catch tag words
        p = ParseSentence(self.sentence)
        p.lowers()
        p.rm_accents()
        # save tag words on self.sentence
        self.sentence=p.parsing_words()
        
        # result is the answer from googlemaps
        # self.result is a dictionnary
        self.result = ""
    
    def getting_data(self):
        """this function gets data from googlemaps
        using self.sentence and saves it on
        self.data"""

        # creating googlemaps client
        gmaps = googlemaps.Client(key = os.environ.get('BACKEND_KEY', ""))
        returned_list = gmaps.geocode(self.sentence)
        self.result = returned_list[0]

    def return_adress_info(self):
        """ this function returns lattitude and longitude 
        of the desired location on a list as following :
        [lattitude, longitude, adress]"""
        
        #list that will be returned
        adress_info = []

        # using function compile_list, found
        # in file functions_rac
        compile_list(adress_info, self.result)

        # returning adress_info
        return adress_info
    
    def wiki_info(self):
        """ this functions takes lattitude and longitude 
        and returns a summary and a link of the nearest 
        location"""

        # loc is a local list that will provide informations
        # for wikipedia
        loc = []
        # wiki result will contain a summary and a link to
        # the wikipedia page relating this information
        wiki_result = []

        # gather informations from self.result
        loc.append(self.result['geometry']['location']['lat'])
        loc.append(self.result['geometry']['location']['lng'])

        wikipedia = MediaWiki(lang='fr')
        t = wikipedia.geosearch(latitude=loc[0], longitude=loc[1])

        p = wikipedia.page(t[0])
        wiki_result.append(p.summary)
        # links ne marche pas pour le moment
        wiki_result.append(p.url)

        return wiki_result

if __name__ == '__main__':
    pass

        
        
