import pytest
import pycm
from pycm import utilities

@pytest.fixture
def projpath(path=None):
    if path is not None:
        if path[-1] != '/': # add trailing slash
            path += '/'
        return path
    return utilities.ProjectRootDir()

def test_spotify_tracks():
    """
    Endpoint as listedn on docs is broken
    """
    test = pycm.charts.spotify.tracks('2019-02-15')
    assert isinstance(test, type(list()))
    assert len(test) > 0
    assert len(test) == 200
    assert test[0]['name'] != ''
    assert test[0]['id'] != ''

def test_SpotifyFreshFind():
#    test = cm.SpotifyFreshFind('2019-01-15')
#    assert isinstance(test, type(list()))
#    assert len(test) > 0 apparently not working?
#    assert test[0]['name'] != ''
#    assert test[0]['id'] != ''
    pass

def test_applemusic_tracks():
    test = pycm.charts.applemusic.tracks('2019-02-15', 'US')
    assert isinstance(test, type(list()))
    assert len(test) > 0
    assert len(test) == 100
    assert test[0]['name'] != ''
    assert test[0]['id'] != ''

def test_applemusic_albums():
    test = pycm.charts.applemusic.albums('2019-02-15', 'US')
    assert isinstance(test, type(list()))
    assert len(test) > 0
    assert len(test) == 99
    assert test[0]['name'] != ''
    assert test[0]['id'] != ''

def test_applemusic_videos():
    test = pycm.charts.applemusic.videos('2019-02-15', 'US')
    assert isinstance(test, type(list()))
    assert len(test) > 0
    assert len(test) == 100
    assert test[0]['name'] != ''
    assert test[0]['id'] != ''

def test_soundcloud_tracks():
    test = pycm.charts.soundcloud.tracks('2019-02-15')
    assert isinstance(test, type(list()))
    assert len(test) > 0
    assert len(test) == 100
    assert test[0]['name'] != ''
    assert test[0]['id'] != ''

def test_shazam_tracks():
    test = pycm.charts.shazam.tracks('2019-02-15')
    assert isinstance(test, type(list()))
    assert len(test) > 0
    assert len(test) == 200
    assert test[0]['rank'] != ''
    assert test[0]['shazam_track_id'] != ''
    # not joking: API only returns the Shazam ID of the track
    # no name or anything

def test_shazam_cities():
    test = pycm.charts.shazam.cities('US')
    assert isinstance(test, type(list()))
    assert len(test) > 0

def test_beatport_tracks():
    test = pycm.charts.beatport.tracks('2019-02-15')
    assert isinstance(test, type(list()))
    assert len(test) > 50
    assert len(test) < 200 
    assert test[0]['name'] != ''
    assert test[0]['id'] != ''

def test_itunes_albums():
    test = pycm.charts.itunes.albums('2019-02-15')
    assert isinstance(test, type(list()))
    assert len(test) > 100
    assert len(test) < 201
    assert test[0]['name'] != ''
    assert test[0]['id'] != ''

def test_itunes_tracks():
    test = pycm.charts.itunes.tracks('2019-02-15')
    assert isinstance(test, type(list()))
    assert len(test) > 100
    assert len(test) < 201
    assert test[0]['name'] != ''
    assert test[0]['id'] != ''

def test_iTunesVideos():
    test = pycm.charts.itunes.videos('2019-02-15')
    assert isinstance(test, type(list()))
    assert len(test) > 100
    assert len(test) < 201
    assert test[0]['name'] != ''
    #assert test[0]['id'] != ''

def test_YoutubeTrends():
    test = pycm.charts.youtube.videos('2019-02-15')
    assert isinstance(test, type(list()))
#    assert len(test) > 0
#    assert len(test) == 200
#    assert test[0]['name'] != ''
#    assert test[0]['id'] != ''

def test_youtube_videos():
    test = pycm.charts.youtube.videos('2019-02-15')
    assert isinstance(test, type(list()))
#    assert len(test) > 0
#    assert len(test) == 200
#    assert test[0]['name'] != ''
#    assert test[0]['id'] != ''

def test_youtube_artists():
    test = pycm.charts.youtube.artists('2019-02-15')
    assert isinstance(test, type(list()))
#    assert len(test) > 0
#    assert len(test) == 200
#    assert test[0]['name'] != ''
#    assert test[0]['id'] != ''
    
def test_youtube_tracks():
    test = pycm.charts.youtube.tracks('2019-02-15')
    #assert isinstance(test, type(list()))
#    assert len(test) > 0
#    assert len(test) == 200
#    assert test[0]['name'] != ''
#    assert test[0]['id'] != ''

def test_qq_insights():
    # fails because of empty return
    test = pycm.charts.qq.insights('2019-07-10')
    assert isinstance(test, type(list()))
    assert len(test) > 0

def test_amazon_tracks():
    test = pycm.charts.amazon.tracks('2019-02-15', 'popular_track', 'All Genres')
    assert isinstance(test, type(list()))
    assert len(test) > 0

def test_amazon_albums():
    test = pycm.charts.amazon.albums('2019-06-15', 'new_album', 'All Genres')
    assert isinstance(test, type(list()))
    assert len(test) > 0

def test_cm_score_tracks():
    # fails because of empty return
    test = pycm.charts.cm_score.tracks('22960734', 'applemusic-genre', '2019-06-01')
    assert isinstance(test, type(list()))
    assert len(test) > 0

def test_cm_score_artists():
    # fails because of 400 Client Error
    test = pycm.charts.cm_score.artists('3648', 'itunes-albums', '2019-06-01')
    assert isinstance(test, type(list()))
    assert len(test) > 0

def test_cm_score_albums():
    # fails because of empty return
    test = pycm.charts.cm_score.albums('2757004', 'spotify-viral', '2019-06-01')
    assert isinstance(test, type(list()))
    assert len(test) > 0

def test_deezer_insights():
    test = pycm.charts.deezer.insights('2019-06-15', 'US')
    assert isinstance(test, type(list()))
    assert len(test) > 0
