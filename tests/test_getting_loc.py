####################################################################
# this file is a test for class ResearchLoc, can be found under
# robot repository
####################################################################

from robot.getting_loc import ResearchLoc
from robot.functions_rac import compile_dic
from robot.gen_answers import generic_loc_found, generic_no_answer
import pytest

def test_wiki_info_does_its_job(monkeypatch):
    place = 'doesn t really matter'
    fake_parsed = "random location"

    random_info = "key_code"
    example_info_full = [{
        "geometry" : {
            "location" : {
                "lat" : 60
            ,
                "lng" : 300
            }   
        },
        "formatted_adress" : "adress random"
    }]

    example_wiki_sites = ["site1"]
    example_place_info = {
            "summary" : "text of the place",
            "link_wiki" : "url"
    }

    fake_result = {"result" : 0, 'commentary' :"Oh, je vois, Je connais cet endroit", \
        'latitude' : 60, 'longitude' : 300, 'adress' : "adress random", \
            'summary' : "text of the place", "link_wiki" : "url"
    }

    # mock for googlemaps mod
    class Fakegooglemaps:
        def __init__(self):
            pass

        def Client(self, key):
            return random_info

        def geocode(self, strings):
            return example_info_full

    # mock for MediaWiki mod
    class FakeMediaWiki:
        def __init__(self, lang):
            pass
        
        def geosearch(self, latitude, longitude):
            return example_wiki_sites
        
        def page(self, fake_title):
            return example_place_info
    


    monkeypatch.setattr('robot.getting_loc.MediaWiki', FakeMediaWiki)
    monkeypatch.setattr('robot.getting_loc.googlemaps', Fakegooglemaps)

    p = ResearchLoc(place)
    p.sentence = fake_parsed
    assert p.return_answer() == fake_result
    
