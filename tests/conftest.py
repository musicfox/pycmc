"""
# `conftest`
The pytest test runner configuration file.

> _Note: You may alter the sleep function in the fixture `slowRoll` to make your tests run faster._
"""
import pytest
import os
import pycmc
import json
import datetime
import pandas as pd
import numpy as np
import time

# =============================================================================
# Function-scoped fixtures.
# These run on each test.
# =============================================================================
@pytest.fixture(scope="function", autouse=True)
def slowRoll():
    """Slow down the tests."""
    time.sleep(6)
    yield


# =============================================================================
# Module-scoped fixtures.
# These run once for the test module.
# =============================================================================
@pytest.fixture(scope="module")
def credvar():
    return "CMCREDENTIALS"


@pytest.fixture(scope="module")
def credential(credvar):
    # load credentials
    return json.loads(os.environ.get(credvar))


if not os.environ.get("CMCREDENTIALS"):
    raise KeyError("CMCREDENTIALS environment variable not set.")


@pytest.fixture(scope="module")
def todayStr():
    return str(datetime.datetime.now()).split(" ")[0]


@pytest.fixture(scope="module")
def dates(todayStr):
    return dict(start="2020-05-01", end="2020-08-07") # fridays!


@pytest.fixture(scope="module")
def date(dates):
    return dates["start"]


@pytest.fixture(scope="module")
def timestampStr():
    return str(datetime.datetime.now()).split(" ")[1]


# =============================================================================
# Various staticly declared "types", i.e. data, for our tests in chart_cleaners.
# =============================================================================
@pytest.fixture(scope="module")
def types():
    youtube_types = {
        "added_at": type(pd.to_datetime("2019-01-01")),
        "artist_covers_1": type(str()),
        "artist_images_1": type(str()),
        "artist_name": type(str()),
        "artist_names_1": type(str()),
        "cm_artist_1": type(np.float64()),
        "cm_track": type(str()),
        "code2s_1": type(str()),
        "id": type(str()),
        "image_url": type(str()),
        "isrc": type(str()),
        "name": type(str()),
        "peak_date": type(pd.to_datetime("2019-01-01")),
        "peak_rank": type(np.float64()),
        "position": type(np.float64()),
        "pre_rank": type(np.float64()),
        "rank_1d_ago": type(np.float64()),
        "rank_today": type(np.float64()),
        "percent_views_change": type(np.float64()),
        "time_on_chart": type(np.float64()),
        "view_count": type(np.float64()),
        "youtube_artist": type(str()),
        "youtube_artist_ids_1": type(str()),
        "youtube_artist_names_1": type(str()),
        "youtube_track_id": type(str()),
        "youtube_track_ids_1": type(str()),
    }

    apple_types = {
        "added_at": type(pd.to_datetime("2019-01-01")),
        "album_ids_1": type(np.float64()),
        "album_label_1": type(str()),
        "album_names_1": type(str()),
        "album_upc_1": type(str()),
        "artist_covers_1": type(str()),
        "artist_images_1": type(str()),
        "cm_track": type(str()),
        "artist_names_1": type(str()),
        "cm_artist_1": type(np.float64()),
        "code2": type(str()),
        "code2s_1": type(str()),
        "itunes": type(str()),
        "composer_1": type(str()),
        "country": type(str()),
        "id": type(str()),
        "image_url": type(str()),
        "isrc": type(str()),
        "name": type(str()),
        "itunes_album_id_1": type(np.float64()),
        "itunes_album_ids_1": type(np.float64()),
        "itunes_artist_ids_1": type(np.float64()),
        "itunes_artist_names_1": type(str()),
        "itunes_track_ids_1": type(np.float64()),
        "peak_date": type(pd.to_datetime("2019-01-01")),
        "peak_rank": type(np.float64()),
        "pre_rank": type(np.float64()),
        "rank": type(np.float64()),
        "rank_1d_ago": type(np.float64()),
        "rank_today": type(np.float64()),
        "release_dates_1": type(pd.to_datetime("2019-01-01")),
        "storefronts_1": type(str()),
        "time_on_chart": type(np.float64()),
        "track_genre_1": type(str()),
    }

    itunes_types = {
        "added_at": type(pd.to_datetime("2019-01-01")),
        "album_ids_1": type(np.float64()),
        "album_label_1": type(str()),
        "album_names_1": type(str()),
        "album_upc_1": type(str()),
        "artist_covers_1": type(str()),
        "artist_images_1": type(str()),
        "cm_track": type(str()),
        "artist_names_1": type(str()),
        "cm_artist_1": type(np.float64()),
        "code2": type(str()),
        "code2s_1": type(str()),
        "itunes": type(str()),
        "composer_1": type(str()),
        "genre": type(str()),
        "id": type(str()),
        "image_url": type(str()),
        "isrc": type(str()),
        "name": type(str()),
        "itunes_album_id_1": type(np.float64()),
        "itunes_album_ids_1": type(np.float64()),
        "itunes_artist_ids_1": type(np.float64()),
        "itunes_artist_names_1": type(str()),
        "itunes_track_ids_1": type(np.float64()),
        "peak_date": type(pd.to_datetime("2019-01-01")),
        "peak_rank": type(np.float64()),
        "pre_rank": type(np.float64()),
        "rank": type(np.float64()),
        "rank_1d_ago": type(np.float64()),
        "rank_today": type(np.float64()),
        "release_dates_1": type(pd.to_datetime("2019-01-01")),
        "storefronts_1": type(str()),
        "time_on_chart": type(np.float64()),
        "track_genre_1": type(str()),
    }

    shazam_types = {
        "added_at": type(pd.to_datetime("2019-01-01")),
        "album_ids_1": type(np.float64()),
        "album_label_1": type(str()),
        "album_names_1": type(str()),
        "album_upc_1": type(str()),
        "artist_covers_1": type(str()),
        "artist_images_1": type(str()),
        "cm_track": type(str()),
        "artist_names_1": type(str()),
        "cm_artist_1": type(np.float64()),
        "code2": type(str()),
        "code2s_1": type(str()),
        "itunes_id": type(str()),
        "composer_1": type(str()),
        "city": type(str()),
        "id": type(str()),
        "image_url": type(str()),
        "isrc": type(str()),
        "name": type(str()),
        "itunes_album_id_1": type(np.float64()),
        "itunes_album_ids_1": type(np.float64()),
        "itunes_artist_ids_1": type(np.float64()),
        "itunes_artist_names_1": type(str()),
        "itunes_track_ids_1": type(np.float64()),
        "shazam_track_id": type(str()),
        "num_of_shazams": type(np.float64()),
        "peak_date": type(pd.to_datetime("2019-01-01")),
        "peak_rank": type(np.float64()),
        "pre_rank": type(np.float64()),
        "rank": type(np.float64()),
        "rank_1d_ago": type(np.float64()),
        "rank_today": type(np.float64()),
        "release_dates_1": type(pd.to_datetime("2019-01-01")),
        "storefronts_1": type(str()),
        "time_on_chart": type(np.float64()),
        "track_genre_1": type(str()),
    }

    spotify_types = {
        "added_at": type(pd.to_datetime("2019-01-01")),
        "album_ids_1": type(np.float64()),
        "album_label_1": type(str()),
        "album_names_1": type(str()),
        "album_upc_1": type(str()),
        "artist_covers_1": type(str()),
        "artist_images_1": type(str()),
        "artist_names_1": type(str()),
        "chart_name": type(str()),
        "chart_type": type(str()),
        "cm_artist_1": type(np.float64()),
        "cm_track": type(str()),
        "code2": type(str()),
        "code2s_1": type(str()),
        "current_plays": type(np.float64()),
        "duration": type(str()),
        "id": type(str()),
        "image_url": type(str()),
        "isrc": type(str()),
        "name": type(str()),
        "peak_date": type(pd.to_datetime("2019-01-01")),
        "peak_rank": type(np.float64()),
        "pre_rank": type(np.float64()),
        "rank": type(np.float64()),
        "rank_1d_ago": type(np.float64()),
        "rank_today": type(np.float64()),
        "plays_1d_ago": type(np.float64()),
        "plays_today": type(np.float64()),
        "release_dates_1": type(pd.to_datetime("2019-01-01")),
        "spotify": type(str()),
        "spotify_album_id": type(str()),
        "time_on_chart": type(np.float64()),
        "spotify_album_ids_1": type(str()),
        "spotify_artist_ids_1": type(str()),
        "track_genre_1": type(str()),
        "spotify_artist_names_1": type(str()),
        "spotify_duration_ms": type(np.float64()),
        "spotify_popularity": type(np.float64()),
        "spotify_track_ids_1": type(str()),
    }
    return dict(
        youtube=youtube_types,
        spotify=spotify_types,
        shazam=shazam_types,
        applemusic=apple_types,
        itunes=itunes_types,
    )


@pytest.fixture(scope="module")
def keys():
    youtube_keys = [
        "added_at",
        "artist_covers_1",
        "artist_images_1",
        "artist_name",
        "artist_names_1",
        "cm_artist_1",
        "cm_track",
        "code2s_1",
        "id",
        "image_url",
        "isrc",
        "name",
        "peak_date",
        "peak_rank",
        "position",
        "pre_rank",
        "rank_1d_ago",
        "rank_today",
        "percent_views_change",
        "time_on_chart",
        "view_count",
        "youtube_artist",
        "youtube_artist_ids_1",
        "youtube_artist_names_1",
        "youtube_track_id",
        "youtube_track_ids_1",
    ]

    apple_keys = [
        "added_at",
        "album_ids_1",
        "album_label_1",
        "album_names_1",
        "album_upc_1",
        "artist_covers_1",
        "artist_images_1",
        "cm_track",
        "artist_names_1",
        "cm_artist_1",
        "code2",
        "code2s_1",
        "itunes",
        "composer_1",
        "country",
        "id",
        "image_url",
        "isrc",
        "name",
        "itunes_album_id_1",
        "itunes_album_ids_1",
        "itunes_artist_ids_1",
        "itunes_artist_names_1",
        "itunes_track_ids_1",
        "peak_date",
        "peak_rank",
        "pre_rank",
        "rank",
        "rank_1d_ago",
        "rank_today",
        "release_dates_1",
        "storefronts_1",
        "time_on_chart",
        "track_genre_1",
    ]

    itunes_keys = [
        "added_at",
        "album_ids_1",
        "album_label_1",
        "album_names_1",
        "album_upc_1",
        "artist_covers_1",
        "artist_images_1",
        "cm_track",
        "artist_names_1",
        "cm_artist_1",
        "code2",
        "code2s_1",
        "genre",
        "composer_1",
        "id",
        "image_url",
        "isrc",
        "itunes",
        "itunes_album_id_1",
        "itunes_album_ids_1",
        "itunes_artist_ids_1",
        "itunes_artist_names_1",
        "itunes_track_ids_1",
        "name",
        "peak_date",
        "peak_rank",
        "pre_rank",
        "rank",
        "rank_1d_ago",
        "rank_today",
        "release_dates_1",
        "storefronts_1",
        "time_on_chart",
        "track_genre_1",
    ]

    shazam_keys = [
        "added_at",
        "album_ids_1",
        "album_label_1",
        "album_names_1",
        "album_upc_1",
        "artist_covers_1",
        "artist_images_1",
        "cm_track",
        "artist_names_1",
        "city",
        "cm_artist_1",
        "code2",
        "code2s_1",
        "composer_1",
        "id",
        "image_url",
        "isrc",
        "itunes_album_id_1",
        "itunes_album_ids_1",
        "itunes_artist_ids_1",
        "itunes_artist_names_1",
        "itunes_id",
        "itunes_track_ids_1",
        "name",
        "num_of_shazams",
        "peak_date",
        "peak_rank",
        "pre_rank",
        "rank",
        "rank_1d_ago",
        "rank_today",
        "release_dates_1",
        "shazam_track_id",
        "storefronts_1",
        "time_on_chart",
        "track_genre_1",
    ]

    spotify_keys = [
        "added_at",
        "album_ids_1",
        "album_label_1",
        "album_names_1",
        "album_upc_1",
        "artist_covers_1",
        "artist_images_1",
        "artist_names_1",
        "chart_name",
        "chart_type",
        "cm_artist_1",
        "cm_track",
        "code2",
        "code2s_1",
        "current_plays",
        "duration",
        "id",
        "image_url",
        "isrc",
        "name",
        "peak_date",
        "peak_rank",
        "pre_rank",
        "rank",
        "rank_1d_ago",
        "rank_today",
        "plays_1d_ago",
        "plays_today",
        "release_dates_1",
        "spotify",
        "spotify_album_id",
        "time_on_chart",
        "spotify_album_ids_1",
        "spotify_artist_ids_1",
        "track_genre_1",
        "spotify_artist_names_1",
        "spotify_duration_ms",
        "spotify_popularity",
        "spotify_track_ids_1",
    ]

    return dict(
        youtube=youtube_keys,
        spotify=spotify_keys,
        shazam=shazam_keys,
        applemusic=apple_keys,
        itunes=itunes_keys,
    )
