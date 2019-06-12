####################################################################
# this class parses the sentence written by the user and sends back 
# tag words.
####################################################################

class ParseSentence (object) :
    """This class parses a sentence and gives back
    tag words"""

    # init function
    def __init__(self, sentence):
        self.sentence=sentence

    # function testing pytest compatibility
    def backword(self) :
        return self.sentence

#if __name__ == '__main__' :
#    K=ParseSentence("jean")
#    K.backword()

