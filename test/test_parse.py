#this test refers to doc app, class parse
from robot.parse import ParseSentence
import pytest

class TestParseSentence:
    #sentence test    
    @pytest.mark.parametrize('a,result', [
        ("Bonjour GrandPy, Que sais tu sur la tour eiffel ?", 
        "bonjour grandpy, que sais tu sur la tour eiffel ?"),
        ("Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?",
         "salut grandpy ! est-ce que tu connais l'adresse d'openclassrooms ?"),
        ("Commènt vas tu GràndPy, ça va bien o`↓ pas ?",
        "commènt vas tu gràndpy, ça va bien o`↓ pas ?")
    ])

    def test_lowers(self, a, result):
        parser = ParseSentence(a)
        assert parser.lowers() == result
    
    #sentence test    
    @pytest.mark.parametrize('b,result', [
        ("bonjour grandpy, que sais tu sur la tour eiffel ?", 
        "bonjour grandpy  que sais tu sur la tour eiffel  "),
        ("salut grandpy ! est-ce que tu connais l'adresse d'openclassrooms ?",
         "salut grandpy   est ce que tu connais l adresse d openclassrooms  "),
        ("commènt%ù vas tu gràndpy^, ça va' bien o↓ pas ?",
        "comment u vas tu grandpy   ca va  bien o pas  ")
    ])

    def test_rm_accents(self, b, result):
        parser = ParseSentence(b)
        assert parser.rm_accents() == result
    
    #sentence test    
    @pytest.mark.parametrize('c,result', [
        ("bonjour grandpy  que sais tu sur la tour eiffel  ", 
        "bonjour sais tour eiffel"),
        ("salut grandpy   est ce que tu connais l adresse d openclassrooms  ",
         "salut connais adresse openclassrooms"),
        ("comment tu vas tu grandpy   ca va  bien o pas  ",
        "")
    ])

    def test_parsing_words(self, c, result) :
        parser = ParseSentence(c)
        assert parser.parsing_words() == result