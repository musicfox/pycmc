import pytest
import pycm


def test_lists():
    test = pycm.curator.lists("spotify",)
    assert isinstance(test, type(list()))
    assert len(test) > 0


def test_metadata(dates):
    test = pycm.curator.metadata("132426", "spotify")
    assert isinstance(test, type(dict()))
    assert len(test.keys()) > 0


def test_playlists(dates):
    test = pycm.curator.playlists("132426", "spotify")
    assert isinstance(test, type(list()))
    assert len(test) > 0
