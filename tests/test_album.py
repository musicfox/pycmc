import pytest
import pycmc
import pandas as pd
import datetime
from requests.exceptions import HTTPError
import logging


@pytest.fixture
def requestkeys():
    return [
        "id",
        "name",
        "release_date",
    ]


def test_charts(dates):
    test = pycmc.album.charts("amazon", 3533190, dates["start"], dates["end"])
    assert isinstance(test, list)
    assert len(test)


def test_get_album_ids():
    test = pycmc.album.get_album_ids("chartmetric", 1119543)
    assert isinstance(test, list)
    assert len(test)


def test_metadata(requestkeys):
    test = pycmc.album.metadata("1119543")
    assert isinstance(test, dict)
    assert len(test.keys())

    # standard use
    for key in requestkeys:
        assert key in test.keys()
    assert isinstance(test["id"], int)
    assert isinstance(test["name"], str)
    assert isinstance(test["release_date"], str)
    assert isinstance(pd.to_datetime(test["release_date"]), datetime.datetime)
    # alt test examples, alt tests ~ weird stuff
    try:
        test = pycmc.album.metadata("Michael Jackson")
        assert isinstance(test, dict)
        assert len(test.keys())
    except HTTPError as err:
        logging.warning(f"pycmc.album.metadata -> {err}")
    try:
        test = pycmc.album.metadata("12394871234598762345")
        assert isinstance(test["id"], int)
        assert isinstance(test, dict)
        assert len(test.keys())
    except HTTPError as err:
        logging.warning(f"pycmc.album.metadata -> {err}")


def test_playlists(dates):
    test = pycmc.album.playlists(
        "1119543",
        dates["start"],
    )
    assert isinstance(test, list)
    assert len(test)


def test_stats():
    test = pycmc.album.stats(1119543, "spotify")
    assert isinstance(test, list)
    assert len(test)


def test_tracks():
    test = pycmc.album.tracks(1119543)
    assert isinstance(test, list)
    assert len(test)


def test_tunefind():
    test = pycmc.album.tunefind("1119543")
    assert isinstance(test, list)
    assert len(test)
