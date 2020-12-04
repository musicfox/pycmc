import pytest
import pycmc


@pytest.fixture
def dta():
    return {"cmid": "179228", "stype": "spotify"}


def test_metadata(dta):
    test = pycmc.playlist.metadata(dta["cmid"], dta["stype"])
    assert isinstance(test, type(dict()))
    assert len(test.keys())

# deprecated upstream
#def test_evolution():
#    test = pycmc.playlist.evolution(439, "artist")
#    assert isinstance(test, list)
#    assert len(test)


def test_lists():
    test = pycmc.playlist.lists("spotify",)
    assert isinstance(test, type(list()))
    assert len(test)


def test_snapshot(dta, dates):
    test = pycmc.playlist.snapshot(dta["cmid"], dta["stype"], dates["start"])
    assert isinstance(test, type(list()))
    assert len(test)


def test_tracks(dta):
    test = pycmc.playlist.tracks(dta["cmid"], dta["stype"], "past",)
    assert isinstance(test, type(list()))
    assert len(test)
