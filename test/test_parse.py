#this test refers to doc app, class parse
from robot.parse import ParseSentence
import pytest

class TestParseSentence:
    #sentence test
    @pytest.mark.parametrize('a,result', [
        ("jean", "jean"),
        ("claude", "claude"),
        ("blabli","blabli")
    ])

    def test_backword(self, a, result):

        parser = ParseSentence(a)
        assert parser.backword() == result

