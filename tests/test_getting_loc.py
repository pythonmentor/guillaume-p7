####################################################################
# this file is a test for class ResearchLoc, can be found under
# robot repository
####################################################################

from robot.getting_loc import ResearchLoc
from robot.functions_rac import compile_list
import pytest

def test_wiki_info_does_its_job(monkeypatch):
    place = 'doesn t really matter'
    fake_result = {
           'geometry' : {
            'location' : {
                'lat' : 500,
                'lng' : 30
            }
        }        
    }
    example_list = ["my article","ok"]
    example_summary = ("résumé de mon article")
    example_url = "http://google.com"

    class FakeMediaWiki:
        def __init__(self, lang):
            pass
        
        def geosearch(self, latitude, longitude):
            return example_list
        
        def page(self, fake_title):
            self.summary = example_summary
            self.url = example_url
            return self
        

    monkeypatch.setattr('robot.getting_loc.MediaWiki', FakeMediaWiki)
    p = ResearchLoc(place)
    p.result = fake_result
    result = p.wiki_info()
    assert result[0] == example_summary
    assert result[1] == example_url
    
