"""
These endpoints do not work as listed on the cm documentation. 04-22-2019.
https://cm-test-node-api.herokuapp.com/apidoc/#api-Playlist-GetPlaylistMetadata
"""

import pytest
import pycm


@pytest.fixture
def projpath(path=None):
    if path is not None:
        if path[-1] != '/': # add trailing slash
            path += '/'
        return path
    return utilities.ProjectRootDir()


@pytest.fixture
def dates():
    return {'start': '2018-03-01', 'end': '2018-03-03'}

    
@pytest.fixture
def dta():
    return {'cmid':'179228', 'stype':'spotify'}


def test_metadata(dta):
    """
    This endpoint is breaking upstream. 04-22-2019.
    """
    test = pycm.playlist.metadata(dta['cmid'], dta['stype'])
    assert isinstance(test, type(dict()))
    assert len(test.keys()) > 0


def test_evolution(dates):
    """
    This endpoint is breaking upstream. 04-22-2019.
    """
    test = pycm.playlist.evolution(439, 'artist')

    assert isinstance(test, type(dict()))
    assert len(test.keys()) > 0


def test_lists():
    """
    chartmetric.com endpoint error -> the exact given url as "ok"
    does not work...obviously this test isn't going to pass
    """
    test = pycm.playlist.lists('spotify', )
    assert isinstance(test, type(list()))
    assert len(test) > 0


def test_snapshot(dta, dates):
    test = pycm.playlist.snapshot(dta['cmid'] ,
                                  dta['stype'],
                                  dates['start'])
    assert isinstance(test, type(list()))
    assert len(test) > 0


def test_tracks(dta):
    test = pycm.playlist.tracks(dta['cmid'], dta['stype'], 'past', )
    assert isinstance(test, type(list()))
    assert len(test) > 0

