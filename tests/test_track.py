import pytest
import pycm


@pytest.fixture
def projpath(path=None):
    if path is not None:
        if path[-1] != "/":  # add trailing slash
            path += "/"
        return path
    return utilities.ProjectRootDir()


def test_charts():
    test = pycm.track.charts("spotify_top_weekly", "22960734", "2019-06-01")
    assert isinstance(test, type(list()))
    assert len(test) > 0


def test_get_track_ids():
    test = pycm.track.get_track_ids("chartmetric", "22782681")
    assert isinstance(test, type(list()))
    assert len(test) > 0


def test_metadata():
    test = pycm.track.metadata("15678739")  # Khalid - Angels
    assert isinstance(test, type(dict()))
    assert len(test.keys()) > 0
    assert test["name"] is not ""
    assert test["artists"][0]["name"] is not ""


def test_playlist_snapshot():
    test = pycm.track.playlist_snapshot("22782681", "spotify", "2019-08-01")
    assert isinstance(test, type(list()))
    assert len(test) > 0


def test_playlists():
    test = pycm.track.playlists("17919855", "spotify")
    assert isinstance(test, type(list()))
    assert len(test) > 0


def test_stats():
    test = pycm.track.stats("22960734", "spotify")
    assert isinstance(test, type(list()))
    assert len(test) > 0


def test_tunefind():
    test = pycm.track.tunefind("15678739")  # Khalid - Angels
    assert isinstance(test, type(list()))
    assert len(test) > 0
