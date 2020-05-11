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
