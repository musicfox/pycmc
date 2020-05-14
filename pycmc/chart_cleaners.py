from multiprocessing.pool import Pool
from itertools import repeat
import pandas as pd
import numpy as np


def get_composers(res):
    """
    Get the composers for the given track.

    **Parameters**

    - `res`:     string composer names for each track within charts
    
    **Returns**

    A dictionary of composers `{composer_num: composer_name}`.
    """
    if res != None:
        res = res.replace(", Jr", " Jr")
        composers = [
            name.strip()
            for first_split in res.split(", ")
            for name in first_split.split(" % ")
        ]
        return {f"composer_{i + 1}": name for i, name in enumerate(composers)}
    return {"composer_1": None}


def get_labels(res):
    """
    Get the record labels for the given track.

    **Parameters**

    - `res`:     list of string of album record labels, e.g.
                    ['Universal/Warner Bros.', 'None']
    
    **Returns**

    A dictionary of record label, `{'album_label_{num}': label_name}`.
    """
    if res != None:
        filter_none = [
            label_string
            for label_string in res
            if label_string != None
            if label_string != "None"
        ]
        joined_str = "/".join(filter_none)
        labels = [
            label.strip() for label in joined_str.split("/") if label != None
        ]
        return (
            {f"album_label_{i + 1}": label for i, label in enumerate(labels)}
            if labels != None
            else {"album_label_1": None}
        )
    return {"album_label_1": None}


def extract_rank_stats(stats):
    """
    Extract the rank and number of plays of past days. 

    **Parameters**

    - `stats`:   list of rankStats for each track within charts, 
                    each element being a dictionary containing the
                    ranks (and plays if available) of previous days

    **Returns**        

    A dictionary of previous day ranks (and plays if available), `{'ranks_{day}s_ago': ranks, 'plays_{day}s_ago': plays}`.
    """
    last = stats[-1]
    rank_stats = {"rank_today": last["rank"]}
    if "plays" in last.keys():
        rank_stats["plays_today"] = last["plays"]

    for i, stats_per_day in enumerate(stats[-2::-1]):
        rank_stats[f"rank_{i+1}d_ago"] = stats_per_day["rank"]
        if "plays" in stats_per_day.keys():
            rank_stats[f"plays_{i+1}d_ago"] = stats_per_day["plays"]
    return rank_stats


def parse_track(res, date):
    """
    Parse the api query result of a single track within a chart 
    into a cleaned and structured one-row DataFrame, regardless of
    what stream service it is from.
    
    **Parameters**

    - `res`:     dictionary containing a track within a chart for

        a given date

    - `date`:    string date in ISO format

    **Returns**

    A Pandas DataFrame with one row and multiple data fields.
    """
    # define a key checker
    kc = lambda k: res[k] if k in res.keys() else None
    # define a list extender
    expand = (
        lambda k: {f"{k}_{i + 1}": name for i, name in enumerate(res[k])}
        if res[k] != None
        else {f"{k}_1": None}
    )
    # define a list extender with key check
    kc_expand = lambda k: expand(k) if k in res.keys() else {f"{k}_1": None}

    # common data fields
    parsed = {
        "date": date,
        "added_at": kc("added_at"),
        "cm_track": kc("cm_track"),
        "image_url": kc("image_url"),
        "isrc": kc("isrc"),
        "name": kc("name"),
        "peak_date": kc("peak_date"),
        "peak_rank": kc("peak_rank"),
        "pre_rank": kc("pre_rank"),
        "time_on_chart": kc("time_on_chart"),
    }

    None_tag = True
    if "id" in res.keys():
        parsed["id"] = res["id"]
        None_tag = False
    elif kc("raw_data") != None:
        if "id" in res["raw_data"].keys():
            parsed["id"] = res["raw_data"]["id"]
            None_tag = False
    if None_tag:
        parsed["id"] = None

    common_fields = [
        "artist_covers",
        "artist_images",
        "artist_names",
        "cm_artist",
        "code2s",
    ]
    for data_field in common_fields:
        expanded_dict = kc_expand(data_field)
        parsed.update(expanded_dict)

    if "rankStats" in res.keys() and len(res["rankStats"]) > 0:
        rank_stats = extract_rank_stats(res["rankStats"])
        parsed.update(rank_stats)

    # special treatment for YouTube
    if "youtube_track_id" in res.keys():
        parsed_youtube = {
            "artist_name": kc("artist_name"),
            "position": kc("position"),
            "view_count": kc("view_count"),
            "youtube_artist": kc("youtube_artist"),
            "youtube_track_id": kc("youtube_track_id"),
        }

        None_tag = True
        if kc("raw_data") != None:
            if "percent_views_change" in res["raw_data"].keys():
                parsed_youtube["percent_views_change"] = res["raw_data"][
                    "percent_views_change"
                ]
                None_tag = False
        if None_tag:
            parsed_youtube["percent_views_change"] = None

        youtube_fields = [
            "youtube_artist_ids",
            "youtube_artist_names",
            "youtube_track_ids",
        ]
        for data_field in youtube_fields:
            expanded_dict = kc_expand(data_field)
            parsed_youtube.update(expanded_dict)

        parsed.update(parsed_youtube)
    else:
        # common items except for YouTube
        parsed_not_u2b = {
            "code2": res["code2"].strip() if "code2" in res.keys() else None,
            "rank": kc("rank"),
        }
        not_u2b_fields = [
            "album_ids",
            "album_label",
            "album_names",
            "album_upc",
            "release_dates",
        ]
        for data_field in not_u2b_fields:
            expanded_dict = kc_expand(data_field)
            parsed_not_u2b.update(expanded_dict)

        None_tag = True
        if kc("track_genre") != None:
            genres_list = list(
                set(
                    res["track_genre"]
                    .replace(",Music", "")
                    .replace(",", "/")
                    .split("/")
                )
            )
            if len(genres_list):
                track_genres = {
                    f"track_genre_{i + 1}": genre
                    for i, genre in enumerate(genres_list)
                }
                None_tag = False
        if None_tag:
            track_genres = {"track_genre_1": None}

        parsed_not_u2b.update(track_genres)

        parsed.update(parsed_not_u2b)

        # common items for AppleMusic, iTunes and Shazam
        if "itunes_album_id" in res.keys():
            composers = get_composers(kc("composer_name"))
            parsed.update(composers)

            apple_fields = [
                "itunes_album_id",
                "itunes_album_ids",
                "itunes_artist_ids",
                "itunes_artist_names",
                "itunes_track_ids",
                "storefronts",
            ]
            for data_field in apple_fields:
                expanded_dict = kc_expand(data_field)
                parsed.update(expanded_dict)

            if "itunes" in res.keys():
                # common for AppleMusic and iTunes
                parsed["itunes"] = kc("itunes")
                if "country" in res.keys():
                    parsed["country"] = res["country"].strip()
                if "genre" in res.keys():
                    parsed["genre"] = res["genre"]
            else:
                # special items for Shazam
                parsed_shazam = {
                    "city": kc("city"),
                    "itunes_id": kc("itunes_id"),
                    "num_of_shazams": kc("num_of_shazams"),
                    "shazam_track_id": kc("shazam_track_id"),
                }
                parsed.update(parsed_shazam)
        else:
            # special treatment for Spotify
            parsed_spotify = {
                "chart_name": kc("chart_name"),
                "chart_type": kc("chart_type"),
                "current_plays": kc("current_plays"),
                "duration": kc("duration"),
                "spotify": kc("spotify"),
                "spotify_album_id": kc("spotify_album_id"),
                "spotify_duration_ms": kc("spotify_duration_ms"),
                "spotify_popularity": kc("spotify_popularity"),
            }
            spotify_fields = [
                "spotify_album_ids",
                "spotify_artist_ids",
                "spotify_artist_names",
                "spotify_track_ids",
            ]
            for data_field in spotify_fields:
                expanded_dict = kc_expand(data_field)
                parsed_spotify.update(expanded_dict)

            parsed.update(parsed_spotify)

    parsed_df = pd.DataFrame(parsed, index=[0])
    return parsed_df


def parse_charts(res, date=None):
    """
    Manipulate the result (res) of any track api query into a coherent 
    dataframe. This takes the actual query result of xxx.chart(date),
    using a tuple of the query and the date. The res param should
    include a list of dictionaries representing each track on the chart.
    
    **Parameters**

    - `res`:     list of dictionaries of track api query 

        results for a single date 

    - `date`:    string date in ISO format
    
    **Returns**

    Pandas DataFrame with the following columns:
    
    - For YouTube chart input:

    ```python
    ['added_at', 'artist_covers_{i}', 'artist_images_{i}',
    'artist_name', 'artist_names_{i}', 'cm_artist_{i}', 
    'cm_track', 'code2s_{i}', 'id', 'image_url', 'isrc',
    'name', 'peak_date', 'peak_rank', 'position', 'pre_rank',
    'rank_{i}d_ago', 'rank_today', 'percent_views_change',
    'time_on_chart', 'view_count', 'youtube_artist',
    'youtube_artist_ids_{i}', 'youtube_artist_names_{i}',
    'youtube_track_id', 'youtube_track_ids_{i}']
    ```

    - For Spotify chart input:
    
    ```python
    ['added_at', 'album_ids_{i}', 'album_label_{i}',
    'album_names_{i}', 'album_upc_{i}', 'artist_covers_{i}',
    'artist_images_{i}', 'artist_names_{i}', 'chart_name',
    'chart_type', 'cm_artist_{i}', 'cm_track', 'code2',
    'code2s_{i}', 'current_plays', 'duration', 'id',
    'image_url', 'isrc', 'name', 'peak_date', 'peak_rank',
    'pre_rank', 'rank', 'rank_{i}d_ago', 'rank_today',
    'plays_{i}d_ago', 'plays_today', 'release_dates_{i}',
    'spotify', 'spotify_album_id', 'time_on_chart',
    'spotify_album_ids_{i}', 'spotify_artist_ids_{i}',
    'track_genre_{i}', 'spotify_artist_names_{i}',
    'spotify_duration_ms', 'spotify_popularity',
    'spotify_track_ids_{i}']
    ```

    - For AppleMusic chart input:
    
    ```python
    ['added_at', 'album_ids_{i}', 'album_label_{i}',
    'album_names_{i}', 'album_upc_{i}', 'artist_covers_{i}',
    'artist_images_{i}', 'cm_track', 'artist_names_{i}',
    'cm_artist_{i}',  'code2', 'code2s_{i}','itunes', 
    'composer_{i}', 'country', 'id', 'image_url', 'isrc',
    'name', 'itunes_album_id_{i}', 'itunes_album_ids_{i}',
    'itunes_artist_ids_{i}', 'itunes_artist_names_{i}',
    'itunes_track_ids_{i}', 'peak_date', 'peak_rank',
    'pre_rank', 'rank', 'rank_{i}d_ago', 'rank_today',
    'release_dates_{i}', 'storefronts_{i}', 'time_on_chart',
    'track_genre_{i}']
    ```

    - For iTunes chart input:    

    ```python
    ['added_at', 'album_ids_{i}', 'album_label_{i}',
    'album_names_{i}', 'album_upc_{i}', 'artist_covers_{i}',
    'artist_images_{i}', 'cm_track', 'artist_names_{i}',
    'cm_artist_{i}', 'code2', 'code2s_{i}', 'genre', 
    'composer_{i}', 'id', 'image_url', 'isrc', 'itunes',
    'itunes_album_id_{i}', 'itunes_album_ids_{i}',
    'itunes_artist_ids_{i}', 'itunes_artist_names_{i}',
    'itunes_track_ids_{i}', 'name', 'peak_date', 'peak_rank',
    'pre_rank', 'rank', 'rank_{i}d_ago', 'rank_today',
    'release_dates_{i}', 'storefronts_{i}', 'time_on_chart',
    'track_genre_{i}']  
    ```

    - For Shazam chart input:
    
    ```python
    ['added_at', 'album_ids_{i}', 'album_label_{i}',
    'album_names_{i}', 'album_upc_{i}', 'artist_covers_{i}',
    'artist_images_{i}', 'cm_track', 'artist_names_{i}',
    'city', 'cm_artist_{i}', 'code2', 'code2s_{i}',
    'composer_{i}', 'id', 'image_url', 'isrc',
    'itunes_album_id_{i}', 'itunes_album_ids_{i}',
    'itunes_artist_ids_{i}', 'itunes_artist_names_{i}',
    'itunes_id', 'itunes_track_ids_{i}', 'name',
    'num_of_shazams', 'peak_date', 'peak_rank', 'pre_rank',
    'rank', 'rank_{i}d_ago', 'rank_today', 'release_dates_{i}',
    'shazam_track_id', 'storefronts_{i}', 'time_on_chart',
    'track_genre_{i}']    
    ```
    """
    # first ensure we have a list as input...
    try:
        assert isinstance(res, type(list()))
        assert len(res) > 0
    except AssertionError:
        print(f"Not a list or empty list for {date}: ")
        return None
    data = []

    with Pool() as p:
        data = p.starmap(parse_track, zip(res, repeat(date)))

    parsed_chart = pd.concat(data, ignore_index=True, sort=True)
    parsed_chart.replace("None", np.nan, inplace=True)  # fill string 'None'
    parsed_chart.fillna(value=np.nan, inplace=True)  # fill None

    return parsed_chart


def type_cast(parsed):
    """
    Change the data type of certain columns of the cleaned DataFrame.

    **Parameters**

    - `parsed`:      DataFrame of parsed chart with all the tracks

    **Returns**            

    A Pandas DataFrame that's parsed and type-casted.
    """
    fix_nan_str = lambda col: parsed.loc[:, col].fillna(value="").astype(str)

    str_to_date = (
        lambda d: pd.to_datetime(d[:10], errors="coerce")
        if isinstance(d, str)
        else d
    )

    findall_columns = lambda col: parsed.filter(regex=col).columns

    # common data fields
    parsed.loc[:, "date"] = parsed["date"].apply(str_to_date)
    parsed.loc[:, "added_at"] = parsed["added_at"].apply(str_to_date)
    parsed.loc[:, "cm_track"] = fix_nan_str("cm_track")
    parsed.loc[:, "id"] = fix_nan_str("id")
    parsed.loc[:, "image_url"] = fix_nan_str("image_url")
    parsed.loc[:, "isrc"] = fix_nan_str("isrc")
    parsed.loc[:, "name"] = fix_nan_str("name")
    parsed.loc[:, "peak_date"] = parsed["peak_date"].apply(str_to_date)
    parsed.loc[:, "peak_rank"] = parsed["peak_rank"].astype(float)
    parsed.loc[:, "pre_rank"] = parsed["pre_rank"].astype(float)
    parsed.loc[:, "time_on_chart"] = parsed["time_on_chart"].astype(float)

    artist_covers_cols = findall_columns("^artist_covers")
    parsed.loc[:, artist_covers_cols] = fix_nan_str(artist_covers_cols)
    artist_images_cols = findall_columns("^artist_images")
    parsed.loc[:, artist_images_cols] = fix_nan_str(artist_images_cols)
    artist_names_cols = findall_columns("^artist_names")
    parsed.loc[:, artist_names_cols] = fix_nan_str(artist_names_cols)
    cm_artist_cols = findall_columns("^cm_artist")
    parsed.loc[:, cm_artist_cols] = parsed[cm_artist_cols].astype(
        float
    )  # to get around NaNs
    code2s_cols = findall_columns("^code2s")
    parsed.loc[:, code2s_cols] = fix_nan_str(code2s_cols)

    today_cols = findall_columns("today")
    parsed.loc[:, today_cols] = parsed[today_cols].astype(float)
    days_ago_cols = findall_columns("d_ago")
    parsed.loc[:, days_ago_cols] = parsed[days_ago_cols].astype(float)

    # special for YouTube
    if "youtube_track_id" in parsed.columns:
        parsed.loc[:, "artist_name"] = fix_nan_str("artist_name")
        parsed.loc[:, "position"] = parsed["position"].astype(float)
        parsed.loc[:, "view_count"] = parsed["view_count"].astype(float)
        parsed.loc[:, "percent_views_change"] = parsed[
            "percent_views_change"
        ].astype(float)
        parsed.loc[:, "youtube_artist"] = fix_nan_str("youtube_artist")
        parsed.loc[:, "youtube_track_id"] = fix_nan_str("youtube_track_id")

        u2b_artist_ids_cols = findall_columns("^youtube_artist_ids")
        parsed.loc[:, u2b_artist_ids_cols] = fix_nan_str(u2b_artist_ids_cols)
        u2b_artist_names_cols = findall_columns("^youtube_artist_names")
        parsed.loc[:, u2b_artist_names_cols] = fix_nan_str(
            u2b_artist_names_cols
        )
        u2b_track_ids_cols = findall_columns("^youtube_track_ids")
        parsed.loc[:, u2b_track_ids_cols] = fix_nan_str(u2b_track_ids_cols)

    else:
        # common items except for YouTube
        parsed.loc[:, "code2"] = fix_nan_str("code2")
        parsed.loc[:, "rank"] = parsed["rank"].astype(float)

        release_dates_cols = findall_columns("^release_dates")
        for column in release_dates_cols:
            parsed.loc[:, column] = parsed.loc[:, column].apply(str_to_date)

        album_ids_cols = findall_columns(
            "^album_ids"
        )  # match only columns starting with album_ids
        parsed.loc[:, album_ids_cols] = parsed[album_ids_cols].astype(float)
        album_label_cols = findall_columns("^album_label")
        parsed.loc[:, album_label_cols] = fix_nan_str(album_label_cols)
        album_names_cols = findall_columns("^album_names")
        parsed.loc[:, album_names_cols] = fix_nan_str(album_names_cols)
        album_upc_cols = findall_columns("^album_upc")
        parsed.loc[:, album_upc_cols] = fix_nan_str(album_upc_cols)
        track_genre_cols = findall_columns("^track_genre")
        parsed.loc[:, track_genre_cols] = fix_nan_str(track_genre_cols)

        # common items for AppleMusic, iTunes and Shazam
        if "itunes_album_id_1" in parsed.columns:
            composer_cols = findall_columns("^composer")
            parsed.loc[:, composer_cols] = fix_nan_str(composer_cols)
            itunes_album_id_cols = findall_columns(
                "^itunes_album_id"
            )  # cast `id` and `ids` together
            parsed.loc[:, itunes_album_id_cols] = (
                parsed[itunes_album_id_cols].replace("", np.nan).astype(float)
            )
            itunes_artist_id_cols = findall_columns("^itunes_artist_id")
            parsed.loc[:, itunes_artist_id_cols] = parsed[
                itunes_artist_id_cols
            ].astype(float)
            itunes_track_ids_cols = findall_columns("^itunes_track_ids")
            parsed.loc[:, itunes_track_ids_cols] = parsed[
                itunes_track_ids_cols
            ].astype(float)
            itunes_artist_names_cols = findall_columns("^itunes_artist_names")
            parsed.loc[:, itunes_artist_names_cols] = fix_nan_str(
                itunes_artist_names_cols
            )
            storefronts_cols = findall_columns("^storefronts")
            parsed.loc[:, storefronts_cols] = fix_nan_str(storefronts_cols)

            if "itunes" in parsed.columns:
                # common for AppleMusic and iTunes

                parsed.loc[:, "itunes"] = fix_nan_str(
                    "itunes"
                )  # cast to str to prevent breaking

                if "country" in parsed.columns:
                    parsed.loc[:, "country"] = fix_nan_str("country")
                if "genre" in parsed.columns:
                    parsed.loc[:, "genre"] = fix_nan_str("genre")

            else:
                # special items for Shazam
                parsed.loc[:, "city"] = fix_nan_str("city")

                parsed.loc[:, "itunes_id"] = fix_nan_str("itunes_id")

                parsed.loc[:, "num_of_shazams"] = parsed[
                    "num_of_shazams"
                ].astype(float)

                parsed.loc[:, "shazam_track_id"] = fix_nan_str(
                    "shazam_track_id"
                )
        else:
            # special treatment for Spotify
            parsed.loc[:, "chart_name"] = fix_nan_str("chart_name")
            parsed.loc[:, "chart_type"] = fix_nan_str("chart_type")
            parsed.loc[:, "current_plays"] = parsed["current_plays"].astype(
                float
            )
            parsed.loc[:, "duration"] = fix_nan_str("duration")

            parsed.loc[:, "spotify"] = fix_nan_str("spotify")

            parsed.loc[:, "spotify_album_id"] = fix_nan_str("spotify_album_id")
            parsed.loc[:, "spotify_duration_ms"] = parsed[
                "spotify_duration_ms"
            ].astype(float)
            parsed.loc[:, "spotify_popularity"] = parsed[
                "spotify_popularity"
            ].astype(float)

            spotify_album_ids_cols = findall_columns("^spotify_album_ids")
            parsed.loc[:, spotify_album_ids_cols] = fix_nan_str(
                spotify_album_ids_cols
            )
            spotify_artist_ids_cols = findall_columns("^spotify_artist_ids")
            parsed.loc[:, spotify_artist_ids_cols] = fix_nan_str(
                spotify_artist_ids_cols
            )
            spotify_artist_names_cols = findall_columns(
                "^spotify_artist_names"
            )
            parsed.loc[:, spotify_artist_names_cols] = fix_nan_str(
                spotify_artist_names_cols
            )
            spotify_track_ids_cols = findall_columns("^spotify_track_ids")
            parsed.loc[:, spotify_track_ids_cols] = fix_nan_str(
                spotify_track_ids_cols
            )

    return parsed
