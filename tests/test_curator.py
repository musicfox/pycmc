import pytest
import pycmc


def test_lists():
    test = pycmc.curator.lists(
        "spotify",
    )
    assert isinstance(test, list)
    assert len(test) > 0


def test_metadata(dates):
    test = pycmc.curator.metadata("132426", "spotify")
    assert isinstance(test, dict)
    assert len(test.keys()) > 0


def test_playlists(dates):
    test = pycmc.curator.playlists("132426", "spotify")
    assert isinstance(test, dict)
    assert len(test) > 0
