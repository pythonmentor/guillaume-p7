####################################################################
# this class uses the tag words of ParseSentence class and make a 
# research on googlemaps to get the location and a formated adress
# of the wanted location
####################################################################

# import modules

# personnal modules, deactivate for pytest
from parse import ParseSentence

# personnal modules, deactivate for pytest

class ResearchLoc (object):
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

    


if __name__ == '__main__':
    pass

        
        
