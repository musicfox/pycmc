import pytest
import pycmc
from pycmc import utilities


def test_amazon_tracks(dates):
    test = pycmc.charts.amazon.tracks(
        dates["start"], "popular_track", "All Genres"
    )
    assert isinstance(test, list)
    assert len(test)


def test_amazon_albums(dates):
    test = pycmc.charts.amazon.albums(
        dates["start"], "new_album", "All Genres"
    )
    assert isinstance(test, list)
    assert len(test)


def test_applemusic_tracks(dates):
    test = pycmc.charts.applemusic.tracks(dates["start"], "US")
    assert isinstance(test, list)
    assert len(test) > 90
    assert test[0]["name"] != ""
    assert test[0]["id"] != ""


def test_applemusic_albums(dates):
    test = pycmc.charts.applemusic.albums(dates["end"], "US")
    assert isinstance(test, list)
    assert len(test) > 90
    assert test[0]["name"] != ""
    assert test[0]["id"] != ""


def test_applemusic_videos(dates):
    test = pycmc.charts.applemusic.videos(dates["end"], "US")
    assert isinstance(test, list)
    assert len(test) > 90
    assert test[0]["name"] != ""
    # assert test[0]["id"] != ""


def test_beatport_tracks(dates):
    """
    # `test_beatport_tracks`

    From the Chartmetric documentation,
    > This data is updated weekly only (on Fridays).
    """
    test = pycmc.charts.beatport.tracks(dates["end"])
    assert isinstance(test, list)
    assert len(test)
    assert len(test) < 200
    assert test[0]["name"] != ""
    assert test[0]["id"] != ""


def test_cm_score_tracks(dates):
    """
    This fails because of empty return.
    """
    test = pycmc.charts.cm_score.tracks(
        "22960734", "spotify-top", "2019-06-01"
    )
    assert isinstance(test, list)
    assert len(test)


def test_cm_score_artists(dates):
    """
    This fails because of 400 Client Error.
    Likely due to 'itunes-albums' as chart_type.
    """
    test = pycmc.charts.cm_score.artists("4904", "spotify-top", "2019-06-01")
    assert isinstance(test, list)
    assert len(test)


def test_cm_score_albums(dates):
    """
    This fails because of empty return.
    """
    test = pycmc.charts.cm_score.albums("2757004", "spotify-top", "2019-06-01")
    assert isinstance(test, list)
    assert len(test)


def test_deezer_insights(dates):
    test = pycmc.charts.deezer.insights(dates["start"], "US")
    assert isinstance(test, list)
    assert len(test)


def test_itunes_albums(dates):
    test = pycmc.charts.itunes.albums(dates["end"])
    assert isinstance(test, list)
    assert len(test) > 100
    assert len(test) < 201
    assert test[0]["name"] != ""
    assert test[0]["id"] != ""


def test_itunes_tracks(dates):
    test = pycmc.charts.itunes.tracks(dates["end"])
    assert isinstance(test, list)
    assert len(test) > 100
    assert len(test) < 201
    assert test[0]["name"] != ""
    assert test[0]["id"] != ""


def test_itunes_videos(dates):
    test = pycmc.charts.itunes.videos(dates["end"])
    assert isinstance(test, list)
    assert len(test) > 100
    assert len(test) < 201
    assert test[0]["name"] != ""
    assert test[0]["itunes_music_video"] != ""


def test_qq_insights(dates):
    test = pycmc.charts.qq.insights(dates["start"])
    assert isinstance(test, list)
    assert len(test)


def test_shazam_tracks(dates):
    test = pycmc.charts.shazam.tracks(dates["start"])
    assert isinstance(test, list)
    assert len(test)
    assert len(test) > 150
    assert test[0]["rank"] != ""
    assert test[0]["shazam_track_id"] != ""


def test_shazam_cities(dates):
    test = pycmc.charts.shazam.cities("US")
    assert isinstance(test, list)
    assert len(test)


def test_soundcloud_tracks(dates):
    """
    # `test_soundcloud_tracks`
    From the Chartmetric documentation,
    > This data is updated weekly only (on Fridays).
    """
    test = pycmc.charts.soundcloud.tracks(dates["end"])
    assert isinstance(test, list)
    assert len(test)
    assert len(test) > 90
    assert test[0]["name"] != ""
    assert test[0]["id"] != ""


def test_spotify_tracks(dates):
    test = pycmc.charts.spotify.tracks(dates["start"])
    assert isinstance(test, list)
    assert len(test)
    assert len(test) > 150
    assert test[0]["name"] != ""
    assert test[0]["id"] != ""


def test_spotify_freshfind(dates):
    test = pycmc.charts.spotify.freshfind(dates["start"])
    assert isinstance(test, list)
    assert len(test)
    assert test[0]["name"] != ""
    assert test[0]["id"] != ""


def test_youtube_trends(dates):
    """
    # `test_youtube_trends`
    From the Chartmetric documentation,
    > This data is updated weekly only (on Thursdays).

    """
    test = pycmc.charts.youtube.videos(dates["start"])
    assert isinstance(test, list)
    assert len(test) > 90
    assert test[0]["name"] != ""
    assert test[0]["id"] != ""


def test_youtube_videos(dates):
    """
    # `test_youtube_videos`
    From the Chartmetric documentation,
    > This data is updated weekly only (on Thursdays).

    """
    test = pycmc.charts.youtube.videos(dates["start"])
    assert isinstance(test, list)
    assert len(test) > 90
    assert test[0]["name"] != ""
    assert test[0]["id"] != ""


def test_youtube_artists(dates):
    """
    # `test_youtube_artists`
    From the Chartmetric documentation,
    > This data is updated weekly only (on Thursdays).

    """
    test = pycmc.charts.youtube.artists(dates["start"])
    assert isinstance(test, list)
    assert len(test) > 90
    assert test[0]["name"] != ""
    assert test[0]["youtube_artist"] != ""


def test_youtube_tracks(dates):
    """
    # `test_youtube_tracks`
    From the Chartmetric documentation,
    > This data is updated weekly only (on Thursdays).

    """

    test = pycmc.charts.youtube.tracks(dates["start"])
    assert isinstance(test, list)
    assert len(test) > 90
    assert test[0]["name"] != ""
    assert test[0]["id"] != ""
