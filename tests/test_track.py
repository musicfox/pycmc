import pytest
import pycmc


def test_charts(dates):
    test = pycmc.track.charts("spotify_top_weekly", "22960734", dates["start"])
    assert isinstance(test, type(list()))
    assert len(test)


def test_get_track_ids():
    test = pycmc.track.get_track_ids("chartmetric", "22782681")
    assert isinstance(test, type(list()))
    assert len(test)


def test_metadata():
    test = pycmc.track.metadata("15678739")  # Khalid - Angels
    assert isinstance(test, type(dict()))
    assert len(test.keys()) > 0
    assert test["name"] is not ""
    assert test["artists"][0]["name"] is not ""


def test_playlist_snapshot(dates):
    test = pycmc.track.playlist_snapshot("22782681", "spotify", dates["start"])
    assert isinstance(test, type(list()))
    assert len(test)


def test_playlists():
    test = pycmc.track.playlists("17919855", "spotify")
    assert isinstance(test, type(list()))
    assert len(test)


def test_stats():
    test = pycmc.track.stats("22960734", "spotify")
    assert isinstance(test, type(list()))
    assert len(test)


def test_tunefind():
    test = pycmc.track.tunefind("15678739")  # Khalid - Angels
    assert isinstance(test, type(list()))
    assert len(test)
