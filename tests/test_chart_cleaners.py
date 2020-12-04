import pandas as pd
import numpy as np
import pytest
import pycmc


@pytest.fixture
def platforms():
    """
    # `platforms`
    Return a list of all the chart endpoint keys.
    """
    return ["youtube", "itunes", "spotify", "applemusic", "shazam"]


@pytest.fixture
def date(dates):
    return dates["start"]


@pytest.fixture
def cm_raw(platforms, date):
    """
    # `cm_raw`

    Pytest fixture to return a dictionary of endpoint: cm_dict dictionaries.
    """
    raw_dicts = dict()
    for platform in platforms:
        if platform == "applemusic":
            res = pycmc.charts.applemusic.tracks(date)
        if platform == "spotify":
            res = pycmc.charts.spotify.tracks(date)
        if platform == "itunes":
            res = pycmc.charts.itunes.tracks(date)
        if platform == "shazam":
            res = pycmc.charts.shazam.tracks(date)
        if platform == "youtube":
            res = pycmc.charts.youtube.tracks(date)
        raw_dicts[platform] = res
    return raw_dicts


@pytest.fixture
def parsed_df(cm_raw, dates):
    """
    # `parsed_df`

    Pytest fixture to return a dictionary of endpoint: parsed_df DataFrames.
    """
    parsed_data = dict()
    for plat, raw in cm_raw.items():
        parsed = pycmc.chart_cleaners.parse_charts(raw, date)
        parsed_data[plat] = parsed
    return parsed_data


def test_cm_raw_keys(cm_raw):
    """
    # `test_cm_raw_keys`

    Test if the dictionaries within the list of raw CM pulls
    contain all the expected data fields as keys.

    """
    youtube_keys = [
        "added_at",
        "artist_covers",
        "artist_images",
        "artist_name",
        "artist_names",
        "cm_artist",
        "cm_track",
        "code2s",
        "id",
        "image_url",
        "isrc",
        "name",
        "peak_date",
        "peak_rank",
        "position",
        "pre_rank",
        "rankStats",
        "raw_data",
        "time_on_chart",
        "view_count",
        "youtube_artist",
        "youtube_artist_ids",
        "youtube_artist_names",
        "youtube_track_id",
        "youtube_track_ids",
    ]

    apple_keys = [
        "added_at",
        "album_ids",
        "album_label",
        "album_names",
        "album_upc",
        "artist_covers",
        "artist_images",
        "artist_names",
        "cm_artist",
        "cm_track",
        "code2",
        "code2s",
        "composer_name",
        "country",
        "id",
        "image_url",
        "isrc",
        "itunes",
        "itunes_album_id",
        "itunes_album_ids",
        "itunes_artist_ids",
        "itunes_artist_names",
        "itunes_track_ids",
        "name",
        "peak_date",
        "peak_rank",
        "pre_rank",
        "rank",
        "rankStats",
        "release_dates",
        "storefronts",
        "time_on_chart",
        "track_genre",
    ]

    itunes_keys = [
        "added_at",
        "album_ids",
        "album_label",
        "album_names",
        "album_upc",
        "artist_covers",
        "artist_images",
        "artist_names",
        "cm_artist",
        "cm_track",
        "code2",
        "code2s",
        "composer_name",
        "genre",
        "id",
        "image_url",
        "isrc",
        "itunes",
        "itunes_album_id",
        "itunes_album_ids",
        "itunes_artist_ids",
        "itunes_artist_names",
        "itunes_track_ids",
        "name",
        "peak_date",
        "peak_rank",
        "pre_rank",
        "rank",
        "rankStats",
        "release_dates",
        "storefronts",
        "time_on_chart",
        "track_genre",
    ]

    shazam_keys = [
        "added_at",
        "album_ids",
        "album_label",
        "album_names",
        "album_upc",
        "artist_covers",
        "artist_images",
        "artist_names",
        "city",
        "cm_artist",
        "cm_track",
        "code2",
        "code2s",
        "composer_name",
        "id",
        "image_url",
        "isrc",
        "itunes_album_id",
        "itunes_album_ids",
        "itunes_artist_ids",
        "itunes_artist_names",
        "itunes_id",
        "itunes_track_ids",
        "name",
        "num_of_shazams",
        "peak_date",
        "peak_rank",
        "pre_rank",
        "rank",
        "rankStats",
        "release_dates",
        "shazam_track_id",
        "storefronts",
        "time_on_chart",
        "track_genre",
    ]

    spotify_keys = [
        "added_at",
        "album_ids",
        "album_label",
        "album_names",
        "album_upc",
        "artist_covers",
        "artist_images",
        "artist_names",
        "chart_name",
        "chart_type",
        "cm_artist",
        "cm_track",
        "code2",
        "code2s",
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
        "rankStats",
        "release_dates",
        "spotify",
        "spotify_album_id",
        "spotify_album_ids",
        "spotify_artist_ids",
        "spotify_artist_names",
        "spotify_duration_ms",
        "spotify_popularity",
        "spotify_track_ids",
        "time_on_chart",
        "track_genre",
    ]

    for plat, res in cm_raw.items():
        try:
            assert len(res) > 0
            keys_map = {
                "youtube": youtube_keys,
                "spotify": spotify_keys,
                "shazam": shazam_keys,
                "applemusic": apple_keys,
                "itunes": itunes_keys,
            }

            tot_test = len(res)
            err_count = 0

            for each in res:
                try:
                    assert set(each.keys()) == set(keys_map[plat])
                except AssertionError:
                    err_count += 1
                    print(
                        f"Assertion Error!"
                        f"Keys not expected for cm_track {each['cm_track']}"
                        f" -> {set(each.keys()) - set(keys_map[plat])}"
                        f"Keys not present for cm_track {each['cm_track']}"
                        f" -> {set(keys_map[plat]) - set(each.keys())}"
                        f"==========="
                    )

            print(
                f"Total occurrence of errors: {err_count}."
                f"Error rate: {err_count/tot_test}."
            )

        except AssertionError:
            print("Invalid input for testing: empty list.")


def test_parse_charts(cm_raw, keys):
    """
    Test if the parsed DataFrame contains all
    the expected data fields.
    """

    for plat, raw in cm_raw.items():
        try:
            assert len(raw) > 0
            parsed = pycmc.chart_cleaners.parse_charts(raw, date)
        except AssertionError:
            print(f"Empty list for platform {plat}, date {date}")

        tot_test = len(keys[plat])
        err_count = 0

        for k in keys[plat]:
            try:
                assert k in parsed.columns
            except AssertionError:
                err_count += 1
                print("Assertion Error!")
                print(f"Column not present in parsed data -> {k}")
                print("===========")

        print(
            f"{plat}, {date} -> Total occurrence of errors: {err_count}."
            f"Error rate: {err_count/tot_test}."
        )


def test_type_cast(parsed_df, types):
    """
    Test if the type-casted DataFrame has data fields
    with expected types.
    """
    for plat, parsed in parsed_df.items():
        try:
            assert parsed is not None
            casted = pycmc.chart_cleaners.type_cast(parsed)
        except AssertionError:
            print(f"Empty DataFrame for platform {plat}")

        tot_test = 0
        err_count = 0

        for i in range(len(casted)):
            track = casted.iloc[i]
            for k in types[plat].keys():
                try:
                    assert k in track.index
                    try:
                        tot_test += 1
                        assert type(track[k]) == types[plat][k]
                    except AssertionError:
                        err_count += 1
                        print(
                            f"{track['cm_track']}, column: {k} -> "
                            f"expected {types[plat][k]},"
                            f"got {type(track[k])}."
                        )

                except AssertionError:
                    print(
                        f"{track['cm_track']}, column: {k} -> "
                        f"key not found or nan encountered."
                    )

        print(
            f"{plat}, {date} -> Total occurrence of errors: {err_count}. "
            f"Error rate: {err_count/tot_test}."
        )
