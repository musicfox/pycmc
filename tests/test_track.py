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

def test_metadata():
    test = pycm.track.metadata('15678739') # Khalid - Angels
    assert isinstance(test, type(dict()))
    assert len(test.keys()) > 0
    assert test['name'] is not ''
    assert test['artists'][0]['name'] is not ''

def test_tunefind():
    test = pycm.track.tunefind('15678739') # Khalid - Angels
    assert isinstance(test, type(list()))
    assert len(test) > 0
#    assert test['name'] is not ''
#    assert test['artists'][0]['name'] is not ''

def test_playlists(dates):
    """
    Unfortunately CM's exemplar is incorrect here...
    https://api.chartmetric.io/apidoc/#api-Track-GetCurrentPlaylistsByTracks
    """
    # playlist placement
    #test = pycm.track.playlists('3308',
    #                            dates['start'],
    #                            dates['end']) # Khalid - Angels
    #assert isinstance(test, type(list()))
    #assert len(test) > 0
