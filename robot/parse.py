####################################################################
# this class parses the sentence written by the user and sends back 
# tag words.
####################################################################

# import modules
import unicodedata
import re

#personnal modules, deactivate for pytest
from stop_words import STOP_WORDS
from functions_rac import quest_mark, fix_sent

# personnal modules. Activate only for pytest
#from robot.stop_words import STOP_WORDS
#from robot.functions_rac import quest_mark, fix_sent

class ParseSentence (object):
    """This class parses a sentence and gives back
    tag words"""

    # init function
    def __init__(self, sentence):
        self.sentence=sentence

    # function lowering sentence letters
    def lowers(self):
        """This function will return every upper character
        in this sentence to lower ones"""
        # lowers every upper character in the sentence
        self.sentence=self.sentence.lower()

        # used for the test only
        return self.sentence

    def rm_accents(self):
        """This function removes accents and replaces various characters by space"""
        # removes every accents and non letters characters
        self.sentence = unicodedata.normalize('NFD', self.sentence).encode('ascii', 'ignore')
        self.sentence = self.sentence.decode("utf8")

        #replaces special characters by spaces
        self.sentence = re.sub(r'[^a-zA-Z0-9_?]'," ",self.sentence)

        #used for the test only
        return self.sentence

    def parsing_words(self):
        """This function parses the sentence with
        the file stop_words, and removes the common
        words used in french vocabulary"""

        # split str into list
        self.sentence = self.sentence.split()
        # Removing words belonging in STOP_WORDS
        for x in STOP_WORDS:
            while x in self.sentence:
                self.sentence.remove(x)
        
        # STOP_WORDS might remove everything
        # this algorithm will fix it
        while True :
            #if self.sentence is empty, returns Error
            if "?" in self.sentence and len(self.sentence) ==1 :
                self.sentence = [["Error"]]
                break
            elif not len(self.sentence) :
                self.sentence = [["Error"]]
                break
            else :
                # getting key words for google maps
                test=quest_mark(self.sentence)
                self.sentence=[]
                while True:
                    if len(test) > 1:
                        for x in test : 
                            self.sentence.append(x)
                        break
                    else :
                        self.sentence.append(test)
                        break
            break
        
        #changing self.sentence back to a string
        self.sentence = fix_sent(self.sentence)

        #used for the pytest only
        return self.sentence
        
if __name__ == '__main__':
    pass

