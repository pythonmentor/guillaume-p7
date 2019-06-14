#functions for robot repository
import re

def quest_mark(liste):
    # finding ? and bookmarking 2 words before
        # for google maps
        # Notice it will return error if there is nothing in liste
        # after STOP WORDS

        #list keeping keywords for a short moment
        key_wds = []

        # if STOP_WORDS didn't removed everything
        # that would be a shame btw
        if len(liste) >= 1 :
            for x in range(len(liste)):

                if "?" in liste[x]:

                    # if ? comes after a space
                    if liste[x] == "?":

                        if len(liste) >= 3:
                            key_wds.append(liste[x-2])
                            key_wds.append(liste[x-1])

                            #clean liste and add key_words
                            liste = []
                            for x in key_wds:
                                liste.append(x)
                            #returning answer
                            return liste
                            

                        elif len(liste) == 2:
                            key_wds.append(liste[x-1])

                            # clean liste and add key_words
                            liste = []
                            liste.append(key_wds[0])
                            #returning answer
                            return liste
                            
                        else :
                            # vide donc gros problème
                            pass

                    # if ? is stucked to a word
                    else :

                        if len(liste) >= 2:
                            key_wds.append(liste[x-1])
                            key_wds.append(re.sub(r'[^a-zA-Z0-9]',"",liste[x]))

                            # clean liste and add key_words
                            liste = []
                            for x in key_wds:
                                liste.append(x)
                            #returning answer
                            return liste

                        elif liste == 1 :
                            key_wds.append(re.sub(r'[^a-zA-Z0-9]',"",liste[x]))

                            # clean liste and add key_words
                            liste = []
                            liste.append(key_wds[0])
                            
                            #returning answer
                            return liste
                
                # if it's not a question
                # or doesn't have question mark
                # we will go on the idea that it will be a question like
                # i want to know the location of xxxx
                # and we'll save the last two words of the sentence
                # and make a research on google maps
                
                # Note : Taking every gramatical way to write a sentence
                # and regex it would be too complicated anyways.
                elif "?" not in liste[x] and x+1 == len(liste):

                    if len(liste) >= 2:
                        key_wds.append(liste[-2])
                        key_wds.append(liste[-1])

                        # clean liste and add key_words
                        liste = []
                        for x in key_wds:
                            liste.append(x)
                        #returning answer
                        return liste
                    
                    if len(liste) == 1 :
                        return liste
                    break

def fix_sent(list_ans):
    fix=[]
    if len(list_ans) == 2 :
        list_ans=" ".join(list_ans)

        return list_ans
    if len(list_ans) == 1 :
        fix = list_ans[0][0]
        return fix

                    