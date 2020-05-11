import pytest
import pycm


@pytest.fixture
def projpath(path=None):
    if path is not None:
        if path[-1] != "/":  # add trailing slash
            path += "/"
        return path
    return utilities.ProjectRootDir()


@pytest.fixture
def dates():
    return {"start": "2018-03-01", "end": "2018-03-03"}


@pytest.fixture
def dta():
    return {"cmid": "179228", "stype": "spotify"}


def test_metadata(dta):
    test = pycm.playlist.metadata(dta["cmid"], dta["stype"])
    assert isinstance(test, type(dict()))
    assert len(test.keys())


def test_evolution():
    test = pycm.playlist.evolution(439, "artist")
    assert isinstance(test, list)
    assert len(test)


def test_lists():
    test = pycm.playlist.lists("spotify",)
    assert isinstance(test, type(list()))
    assert len(test)


def test_snapshot(dta, dates):
    test = pycm.playlist.snapshot(dta["cmid"], dta["stype"], dates["start"])
    assert isinstance(test, type(list()))
    assert len(test)


def test_tracks(dta):
    test = pycm.playlist.tracks(dta["cmid"], dta["stype"], "past",)
    assert isinstance(test, type(list()))
    assert len(test)
