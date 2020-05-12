import pytest
import pycm
from pycm import utilities


def test_recommendation_similar_playlists():
    test = pycm.recommendation.similar_playlists("68810", "spotify")
    assert isinstance(test, type(list()))
    assert len(test)
