####################################################################
# this class uses the tag words of ParseSentence class and make a 
# research on googlemaps to get the location and a formated adress
# of the wanted location
####################################################################

# import modules
import os 
from random import choice

import googlemaps
from mediawiki import MediaWiki

# personnal modules, activate only for pytest
from robot.parse import ParseSentence
from robot.functions_rac import compile_dic
from robot.gen_answers import generic_loc_found, generic_no_answer

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
        
        # self.result is a dictionnary
        self.result = {}

    def return_answer(self):
        """this function returns a dictionnary
        containing {'result' : 1, 'commentary' : "sentence from bot",
        'latitude' : number,'longitude' : number, 
        "adress" : "info", "summary" : "text", "link_wiki" : "url"}
        1 = result found, 0 = not found. 
        If 1 appears, there won't be latt, lng,
        neither summary"""

        # if result from parse is null
        if self.sentence == "Error":
            self.result['result'] = 0
            self.result['commentary'] = choice(generic_no_answer)
        
        # if there is a result
        else :
            # creating googlemaps client
            gmaps = googlemaps.Client(key = os.environ.get("BACKEND_KEY", ""))
            returned_list = gmaps.geocode(self.sentence)

            # if result is empty, we're returning a message
            # and a number that will let ajax know
            if not returned_list:
                self.result['result'] = 0
                self.result['commentary'] = choice(generic_no_answer)
            # answers = 0
            else :
                #creating local var that will display first googlemaps answer
                best_result = returned_list[0]

                compile_dic(best_result, self.result)

                wikipedia = MediaWiki(lang='fr')
                t = wikipedia.geosearch(latitude=self.result["latitude"], \
                    longitude=self.result["longitude"])
                # if wiki does not have stories regarding that place
                if not t:
                    self.result['result'] = 0
                    self.result['commentary'] = choice(generic_loc_found)
                
                # if wiki has full info
                else:
                    self.result['result'] = 1
                    self.result['commentary'] = choice(generic_loc_found)

                    p = wikipedia.page(t[0])
                    self.result["summary"] = p.summary
                    self.result["link_wiki"] = p.url
        return self.result

        

if __name__ == '__main__':
    p = ResearchLoc("paris ?")
    print(p.return_answer())