import pytest
import pycm
import datetime


@pytest.fixture
def projpath(path=None):
    if path is not None:
        if path[-1] != '/': # add trailing slash
            path += '/'
        return path
    return utilities.ProjectRootDir()


@pytest.fixture
def dates():
    return dict(
        start = '2019-03-01', 
        end = str(datetime.datetime.today()).split(' ')[0],
    )

def test_albums():
    test = pycm.artist.albums('3380',) 
    assert isinstance(test, type(list()))
    assert len(test) > 0


def test_cpp_data():
    test = pycm.artist.cpp_data('3380', 'rank')
    assert isinstance(test, type(list()))
    assert len(test) > 0


def test_charts():
    test = pycm.artist.charts('spotify_viral_daily', '1220', '2019-01-01')
    assert isinstance(test, type(list()))
    assert len(test) > 0
    

def test_fanmetrics(dates):
    dsrcObj = dict(
        spotify='followers',
        bandsintown='followers',
        instagram='followers',
        twitter='followers',
        soundcloud='followers',
        wikipedia='views',
        youtube_channel='subscribers',
        #youtube_artist='views', broken as of 2020-04-30
    )

    test = pycm.artist.fanmetrics('3380', dates['start'])
    assert isinstance(test, type(dict()))
    assert len(test.keys())
    test = pycm.artist.fanmetrics('3380', dates['start'], dsrc='spotify')
    assert isinstance(test, type(dict()))
    assert len(test.keys())
#   broken upstream as of 2020-04-30
#    test = pycm.artist.fanmetrics('3380', dates['start'], dsrc='youtube')
#    assert isinstance(test, type(dict()))
#    assert len(test.keys())
    test = pycm.artist.fanmetrics('3380', dates['start'], dsrc='facebook')
    assert isinstance(test, type(dict()))
    assert len(test.keys())
    test = pycm.artist.fanmetrics('3380', dates['start'], dsrc='deezer')
    assert isinstance(test, type(dict()))
    assert len(test.keys())
    for dsrc, valueCol in dsrcObj.items():
        test = pycm.artist.fanmetrics('3380', dates['start'], dates['end'], dsrc, valueCol)
        assert isinstance(test, type(dict()))
        assert len(test.keys())
    # do it again with new data
    dsrcObj = dict(
        youtube_channel='views',
        spotify='popularity',
        facebook='likes',
   )
    for dsrc, valueCol in dsrcObj.items():
        test = pycm.artist.fanmetrics('3380', dates['start'], dates['end'], dsrc, valueCol)
        assert isinstance(test, type(dict()))
        assert len(test.keys())




def test_get_artist_ids():
    test = pycm.artist.get_artist_ids('chartmetric', 4031)
    assert isinstance(test, type(list()))
    assert len(test) > 0


def test_get_artists():
    test = pycm.artist.get_artists('sp_monthly_listeners', 5000, 10000)
    assert isinstance(test, type(list()))
    assert len(test) > 0


def test_metadata():
    test = pycm.artist.metadata('3380',) 
    assert isinstance(test, type(dict()))
    assert test is not None


def test_playlists(dates):
    test = pycm.artist.playlists('439', 'spotify', dates['start'], 'current') 
    assert isinstance(test, type(list()))
    assert len(test) > 0


def test_related():
    test = pycm.artist.related('3380',) 
    assert isinstance(test, type(list()))
    assert len(test) > 0


def test_urls():
    test = pycm.artist.urls('3380',) 
    assert isinstance(test, type(list()))
    assert len(test) > 0


def test_tracks():
    test = pycm.artist.tracks('3380',) 
    assert isinstance(test, type(list()))
    assert len(test) > 0


def test_tunefind():
    test = pycm.artist.tunefind('3380',) 
    assert isinstance(test, type(list()))
    assert len(test) > 0


def test_listening(dates):
    test = pycm.artist.listening('3380', dates['start'])
    assert isinstance(test, type(dict()))
    assert len(test.keys()) > 0
