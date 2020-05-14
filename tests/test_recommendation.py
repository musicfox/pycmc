import pytest
import pycmc
from pycmc import utilities


def test_recommendation_similar_playlists():
    test = pycmc.recommendation.similar_playlists("68810", "spotify")
    assert isinstance(test, type(list()))
    assert len(test)
