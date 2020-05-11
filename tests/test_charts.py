import pytest
import pycm
from pycm import utilities


@pytest.fixture
def projpath(path=None):
    if path is not None:
        if path[-1] != "/":  # add trailing slash
            path += "/"
        return path
    return utilities.ProjectRootDir()


def test_amazon_tracks():
    test = pycm.charts.amazon.tracks(
        "2019-02-15", "popular_track", "All Genres"
    )
    assert isinstance(test, type(list()))
    assert len(test) > 0


def test_amazon_albums():
    test = pycm.charts.amazon.albums("2019-06-15", "new_album", "All Genres")
    assert isinstance(test, type(list()))
    assert len(test) > 0


def test_applemusic_tracks():
    test = pycm.charts.applemusic.tracks("2019-02-15", "US")
    assert isinstance(test, type(list()))
    assert len(test) > 0
    assert len(test) == 100
    assert test[0]["name"] != ""
    assert test[0]["id"] != ""


def test_applemusic_albums():
    test = pycm.charts.applemusic.albums("2019-02-15", "US")
    assert isinstance(test, type(list()))
    assert len(test) > 0
    assert len(test) == 99
    assert test[0]["name"] != ""
    assert test[0]["id"] != ""


def test_applemusic_videos():
    test = pycm.charts.applemusic.videos("2019-02-15", "US")
    assert isinstance(test, type(list()))
    assert len(test) > 0
    assert len(test) == 100
    assert test[0]["name"] != ""
    assert test[0]["id"] != ""


def test_beatport_tracks():
    test = pycm.charts.beatport.tracks("2019-02-15")
    assert isinstance(test, type(list()))
    assert len(test) > 50
    assert len(test) < 200
    assert test[0]["name"] != ""
    assert test[0]["id"] != ""


def test_cm_score_tracks():
    """
    This fails because of empty return.
    """
    test = pycm.charts.cm_score.tracks("22960734", "spotify-top", "2019-06-01")
    assert isinstance(test, type(list()))
    assert len(test)


def test_cm_score_artists():
    """
    This fails because of 400 Client Error.
    Likely due to 'itunes-albums' as chart_type.
    """
    test = pycm.charts.cm_score.artists("4904", "spotify-top", "2019-06-01")
    assert isinstance(test, type(list()))
    assert len(test)


def test_cm_score_albums():
    """
    This fails because of empty return.
    """
    test = pycm.charts.cm_score.albums("2757004", "spotify-top", "2019-06-01")
    assert isinstance(test, type(list()))
    assert len(test)


def test_deezer_insights():
    test = pycm.charts.deezer.insights("2019-06-15", "US")
    assert isinstance(test, type(list()))
    assert len(test) > 0


def test_itunes_albums():
    test = pycm.charts.itunes.albums("2019-02-15")
    assert isinstance(test, type(list()))
    assert len(test) > 100
    assert len(test) < 201
    assert test[0]["name"] != ""
    assert test[0]["id"] != ""


def test_itunes_tracks():
    test = pycm.charts.itunes.tracks("2019-02-15")
    assert isinstance(test, type(list()))
    assert len(test) > 100
    assert len(test) < 201
    assert test[0]["name"] != ""
    assert test[0]["id"] != ""


def test_itunes_videos():
    test = pycm.charts.itunes.videos("2019-02-15")
    assert isinstance(test, type(list()))
    assert len(test) > 100
    assert len(test) < 201
    assert test[0]["name"] != ""
    assert test[0]["itunes_music_video"] != ""


def test_qq_insights():
    test = pycm.charts.qq.insights("2019-05-02")
    assert isinstance(test, type(list()))
    assert len(test) > 0


def test_shazam_tracks():
    test = pycm.charts.shazam.tracks("2019-02-15")
    assert isinstance(test, type(list()))
    assert len(test) > 0
    assert len(test) == 200
    assert test[0]["rank"] != ""
    assert test[0]["shazam_track_id"] != ""


def test_shazam_cities():
    test = pycm.charts.shazam.cities("US")
    assert isinstance(test, type(list()))
    assert len(test) > 0


def test_soundcloud_tracks():
    test = pycm.charts.soundcloud.tracks("2019-02-15")
    assert isinstance(test, type(list()))
    assert len(test) > 0
    assert len(test) == 100
    assert test[0]["name"] != ""
    assert test[0]["id"] != ""


def test_spotify_tracks():
    test = pycm.charts.spotify.tracks("2019-02-15")
    assert isinstance(test, type(list()))
    assert len(test) > 0
    assert len(test) == 200
    assert test[0]["name"] != ""
    assert test[0]["id"] != ""


def test_spotify_freshfind():
    test = pycm.charts.spotify.freshfind("2019-01-10")
    assert isinstance(test, type(list()))
    assert len(test) > 0
    assert test[0]["name"] != ""
    assert test[0]["id"] != ""


def test_youtube_trends():
    test = pycm.charts.youtube.videos("2019-02-14")
    assert isinstance(test, type(list()))
    assert len(test) > 0
    assert len(test) == 100
    assert test[0]["name"] != ""
    assert test[0]["id"] != ""


def test_youtube_videos():
    test = pycm.charts.youtube.videos("2019-02-21")
    assert isinstance(test, type(list()))
    assert len(test) > 0
    assert len(test) == 100
    assert test[0]["name"] != ""
    assert test[0]["id"] != ""


def test_youtube_artists():
    test = pycm.charts.youtube.artists("2019-02-21")
    assert isinstance(test, type(list()))
    assert len(test)
    assert len(test) == 100
    assert test[0]["name"] != ""
    assert test[0]["youtube_artist"] != ""


def test_youtube_tracks():
    test = pycm.charts.youtube.tracks("2019-02-21")
    assert isinstance(test, type(list()))
    assert len(test) > 0
    assert len(test) == 100
    assert test[0]["name"] != ""
    assert test[0]["id"] != ""
