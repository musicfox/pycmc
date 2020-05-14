import pytest
import pycmc
import datetime
import time


def test_albums():
    test = pycmc.artist.albums("3380",)
    assert isinstance(test, type(list()))
    assert len(test) > 0


def test_cpp_data():
    test = pycmc.artist.cpp_data("3380", "rank")
    assert isinstance(test, type(list()))
    assert len(test) > 0


def test_charts(dates):
    test = pycmc.artist.charts("spotify_top_daily", "4904", dates["start"])
    assert isinstance(test, list)
    assert len(test)


def test_fanmetrics(dates):
    dsrcObj = dict(
        spotify="followers",
        bandsintown="followers",
        instagram="followers",
        twitter="followers",
        soundcloud="followers",
        wikipedia="views",
        youtube_channel="subscribers",
        # youtube_artist='views', broken as of 2020-04-30
    )

    test = pycmc.artist.fanmetrics("3380", dates["start"])
    assert isinstance(test, type(dict()))
    assert len(test.keys())
    test = pycmc.artist.fanmetrics("3380", dates["start"], dsrc="spotify")
    assert isinstance(test, type(dict()))
    assert len(test.keys())
    #   broken upstream as of 2020-04-30
    #    test = pycmc.artist.fanmetrics('3380', dates['start'], dsrc='youtube')
    #    assert isinstance(test, type(dict()))
    #    assert len(test.keys())
    test = pycmc.artist.fanmetrics("3380", dates["start"], dsrc="facebook")
    assert isinstance(test, type(dict()))
    assert len(test.keys())
    test = pycmc.artist.fanmetrics("3380", dates["start"], dsrc="deezer")
    assert isinstance(test, type(dict()))
    assert len(test.keys())
    for dsrc, valueCol in dsrcObj.items():
        time.sleep(1.5)
        test = pycmc.artist.fanmetrics(
            "3380", dates["start"], dates["end"], dsrc, valueCol
        )
        assert isinstance(test, type(dict()))
        assert len(test.keys())
    # do it again with new data
    dsrcObj = dict(
        youtube_channel="views", spotify="popularity", facebook="likes",
    )
    for dsrc, valueCol in dsrcObj.items():
        test = pycmc.artist.fanmetrics(
            "3380", dates["start"], dates["end"], dsrc, valueCol
        )
        assert isinstance(test, type(dict()))
        assert len(test.keys())


def test_get_artist_ids():
    test = pycmc.artist.get_artist_ids("chartmetric", 4031)
    assert isinstance(test, type(list()))
    assert len(test) > 0


def test_get_artists():
    test = pycmc.artist.get_artists("sp_monthly_listeners", 5000, 10000)
    assert isinstance(test, type(list()))
    assert len(test) > 0


def test_metadata():
    test = pycmc.artist.metadata("3380",)
    assert isinstance(test, type(dict()))
    assert test is not None


def test_playlists(dates):
    test = pycmc.artist.playlists("439", "spotify", dates["start"], "current")
    assert isinstance(test, type(list()))
    assert len(test) > 0


def test_related():
    test = pycmc.artist.related("3380",)
    assert isinstance(test, type(list()))
    assert len(test) > 0


def test_urls():
    test = pycmc.artist.urls("3380",)
    assert isinstance(test, type(list()))
    assert len(test) > 0


def test_tracks():
    test = pycmc.artist.tracks("3380",)
    assert isinstance(test, type(list()))
    assert len(test) > 0


def test_tunefind():
    test = pycmc.artist.tunefind("3380",)
    assert isinstance(test, type(list()))
    assert len(test) > 0


def test_listening(dates):
    test = pycmc.artist.listening("3380", dates["start"])
    assert isinstance(test, type(dict()))
    assert len(test.keys()) > 0
