import pandas as pd
import numpy as np

def test_chartmetric_keys(res, platform):
    """
    Given a list of dictionaries of raw Chartmetric pulls, and a string indicating the 
    music platform, tests if the dictionaries within the list contain all the expected
    data fields as keys.
    
    :params res:                a list of dictionaries
    :params platform:           a string indicating the platform,
                                including youtube, applemusic, itunes, spotify and shazam  
    """
    youtube_keys = ['added_at', 'artist_covers', 'artist_images', 'artist_name', 'artist_names',
                    'cm_artist', 'cm_track', 'code2s', 'id', 'image_url', 'isrc', 'name',
                    'peak_date', 'peak_rank', 'position', 'pre_rank', 'rankStats', 'raw_data',
                    'time_on_chart', 'view_count', 'youtube_artist', 'youtube_artist_ids',
                    'youtube_artist_names', 'youtube_track_id', 'youtube_track_ids']

    apple_keys = ['added_at', 'album_ids', 'album_label', 'album_names', 'album_upc',
                  'artist_covers', 'artist_images', 'artist_names', 'cm_artist', 'cm_track',
                  'code2', 'code2s', 'composer_name', 'country', 'id', 'image_url', 'isrc',
                  'itunes', 'itunes_album_id', 'itunes_album_ids', 'itunes_artist_ids',
                  'itunes_artist_names', 'itunes_track_ids', 'name', 'peak_date', 'peak_rank',
                  'pre_rank', 'rank', 'rankStats', 'release_dates', 'storefronts',
                  'time_on_chart', 'track_genre']

    itunes_keys = ['added_at', 'album_ids', 'album_label', 'album_names', 'album_upc',
                   'artist_covers', 'artist_images', 'artist_names', 'cm_artist', 'cm_track',
                   'code2', 'code2s', 'composer_name', 'genre', 'id', 'image_url', 'isrc',
                   'itunes', 'itunes_album_id', 'itunes_album_ids', 'itunes_artist_ids',
                   'itunes_artist_names', 'itunes_track_ids', 'name', 'peak_date', 'peak_rank',
                   'pre_rank', 'rank', 'rankStats', 'release_dates', 'storefronts',
                   'time_on_chart', 'track_genre']  
    
    shazam_keys = ['added_at', 'album_ids', 'album_label', 'album_names', 'album_upc',
                   'artist_covers', 'artist_images', 'artist_names', 'city', 'cm_artist',
                   'cm_track', 'code2', 'code2s', 'composer_name', 'id', 'image_url', 'isrc',
                   'itunes_album_id', 'itunes_album_ids', 'itunes_artist_ids',
                   'itunes_artist_names', 'itunes_id', 'itunes_track_ids', 'name',
                   'num_of_shazams', 'peak_date', 'peak_rank', 'pre_rank', 'rank', 'rankStats',
                   'release_dates', 'shazam_track_id', 'storefronts', 'time_on_chart',
                   'track_genre']    
    
    spotify_keys = ['added_at', 'album_ids', 'album_label', 'album_names', 'album_upc',
                    'artist_covers', 'artist_images', 'artist_names', 'chart_name',
                    'chart_type', 'cm_artist', 'cm_track', 'code2', 'code2s',
                    'current_plays', 'duration', 'id', 'image_url', 'isrc', 'name',
                    'peak_date', 'peak_rank', 'pre_rank', 'rank', 'rankStats',
                    'release_dates', 'spotify', 'spotify_album_id', 'spotify_album_ids',
                    'spotify_artist_ids', 'spotify_artist_names', 'spotify_duration_ms',
                    'spotify_popularity', 'spotify_track_ids', 'time_on_chart', 'track_genre']

    try:
        assert len(res) > 0
        keys_map = {
            'youtube': youtube_keys,
            'spotify': spotify_keys,
            'shazam': shazam_keys,
            'applemusic': apple_keys,
            'itunes': itunes_keys
        }

        tot_test = len(res)
        err_count = 0

        for each in res:
            try:
                assert set(each.keys()) == set(keys_map[platform])
            except AssertionError:
                err_count += 1
                print("Assertion Error!")
                print(f"Keys not expected for cm_track {each['cm_track']}-> {set(each.keys()) - set(keys_map[platform])}")
                print(f"Keys not present for cm_track {each['cm_track']} -> {set(keys_map[platform]) - set(each.keys())}")
                print("===========")

        print(f"Total occurrence of errors: {err_count}. Error rate: {err_count/tot_test}.")

    except AssertionError:
        print("Invalid input for testing: empty list.")    

def test_parse_columns(res, platform):
    """
    Given a DataFrame of parsed charts, result of `parse_charts`, and a string indicating the 
    music platform, tests if the given DataFrame contains all the expected data fields.
    
    :params res:                a DataFrame of parsed chart data
    :params platform:           a string indicating the platform,
                                including youtube, applemusic, itunes, spotify and shazam    
    """
    youtube_keys = ['added_at', 'artist_covers_1', 'artist_images_1', 'artist_name',
                    'artist_names_1', 'cm_artist_1', 'cm_track', 'code2s_1', 'id',
                    'image_url', 'isrc', 'name', 'peak_date', 'peak_rank', 'position',
                    'pre_rank', 'rank_1d_ago', 'rank_today', 'percent_views_change',
                    'time_on_chart', 'view_count', 'youtube_artist', 'youtube_artist_ids_1',
                    'youtube_artist_names_1', 'youtube_track_id', 'youtube_track_ids_1']

    apple_keys = ['added_at', 'album_ids_1', 'album_label_1', 'album_names_1',
                  'album_upc_1', 'artist_covers_1', 'artist_images_1', 'cm_track',
                  'artist_names_1', 'cm_artist_1',  'code2', 'code2s_1','itunes', 
                  'composer_1', 'country', 'id', 'image_url', 'isrc', 'name', 
                  'itunes_album_id_1', 'itunes_album_ids_1', 'itunes_artist_ids_1',
                  'itunes_artist_names_1', 'itunes_track_ids_1', 'peak_date',
                  'peak_rank', 'pre_rank', 'rank', 'rank_1d_ago', 'rank_today',
                  'release_dates_1', 'storefronts_1', 'time_on_chart', 'track_genre_1']

    itunes_keys = ['added_at', 'album_ids_1', 'album_label_1', 'album_names_1',
                   'album_upc_1', 'artist_covers_1', 'artist_images_1', 'cm_track',
                   'artist_names_1', 'cm_artist_1', 'code2', 'code2s_1', 'genre', 
                   'composer_1', 'id', 'image_url', 'isrc', 'itunes',
                   'itunes_album_id_1', 'itunes_album_ids_1', 'itunes_artist_ids_1',
                   'itunes_artist_names_1', 'itunes_track_ids_1', 'name', 'peak_date',
                   'peak_rank', 'pre_rank', 'rank', 'rank_1d_ago', 'rank_today',
                   'release_dates_1', 'storefronts_1', 'time_on_chart', 'track_genre_1']  
    
    shazam_keys = ['added_at', 'album_ids_1', 'album_label_1', 'album_names_1',
                   'album_upc_1', 'artist_covers_1', 'artist_images_1', 'cm_track', 
                   'artist_names_1', 'city', 'cm_artist_1', 'code2', 'code2s_1',
                   'composer_1', 'id', 'image_url', 'isrc', 'itunes_album_id_1',
                   'itunes_album_ids_1', 'itunes_artist_ids_1', 'itunes_artist_names_1',
                   'itunes_id', 'itunes_track_ids_1', 'name', 'num_of_shazams', 'peak_date',
                   'peak_rank', 'pre_rank', 'rank', 'rank_1d_ago', 'rank_today',
                   'release_dates_1', 'shazam_track_id', 'storefronts_1', 'time_on_chart',
                   'track_genre_1']    
    
    spotify_keys = ['added_at', 'album_ids_1', 'album_label_1', 'album_names_1',
                    'album_upc_1', 'artist_covers_1', 'artist_images_1',
                    'artist_names_1', 'chart_name', 'chart_type', 'cm_artist_1',
                    'cm_track', 'code2', 'code2s_1', 'current_plays', 'duration', 'id',
                    'image_url', 'isrc', 'name', 'peak_date', 'peak_rank', 'pre_rank',
                    'rank', 'rank_1d_ago', 'rank_today', 'plays_1d_ago', 'plays_today',
                    'release_dates_1', 'spotify', 'spotify_album_id', 'time_on_chart', 
                    'spotify_album_ids_1', 'spotify_artist_ids_1', 'track_genre_1',
                    'spotify_artist_names_1', 'spotify_duration_ms', 'spotify_popularity',
                    'spotify_track_ids_1']

    data_field_map = {
        'youtube': youtube_keys,
        'spotify': spotify_keys,
        'shazam': shazam_keys,
        'applemusic': apple_keys,
        'itunes': itunes_keys
    }

    tot_test = len(data_field_map[platform])
    err_count = 0

    for k in data_field_map[platform]:
        try:
            assert k in res.columns
        except AssertionError:
            err_count += 1
            print("Assertion Error!")
            print(f"Column not present in parsed data -> {k}")
            print("===========")

    print(f"Total occurrence of errors: {err_count}. Error rate: {err_count/tot_test}.")

def test_parse_types(res, platform):
    youtube_types = {
        'added_at': type(pd.to_datetime('2019-01-01')),
        'artist_covers_1': type(str()),
        'artist_images_1': type(str()),
        'artist_name': type(str()),
        'artist_names_1': type(str()),
        'cm_artist_1': type(np.float64()),
        'cm_track': type(str()),
        'code2s_1': type(str()),
        'id': type(str()),
        'image_url': type(str()),
        'isrc': type(str()),
        'name': type(str()),
        'peak_date': type(pd.to_datetime('2019-01-01')),
        'peak_rank': type(np.float64()),
        'position': type(np.float64()),
        'pre_rank': type(np.float64()),
        'rank_1d_ago': type(np.float64()),
        'rank_today': type(np.float64()),
        'percent_views_change': type(np.float64()),
        'time_on_chart': type(np.float64()),
        'view_count': type(np.float64()),
        'youtube_artist': type(str()),
        'youtube_artist_ids_1': type(str()),
        'youtube_artist_names_1': type(str()),
        'youtube_track_id': type(str()),
        'youtube_track_ids_1': type(str())}

    apple_types = {
        'added_at': type(pd.to_datetime('2019-01-01')), 
        'album_ids_1': type(np.float64()),
        'album_label_1': type(str()),
        'album_names_1': type(str()),
        'album_upc_1': type(str()),
        'artist_covers_1': type(str()),
        'artist_images_1': type(str()),
        'cm_track': type(str()),
        'artist_names_1': type(str()),
        'cm_artist_1': type(np.float64()),
        'code2': type(str()),
        'code2s_1': type(str()),
        'itunes': type(np.int64()),
        'composer_1': type(str()),
        'country': type(str()),
        'id': type(str()),
        'image_url': type(str()),
        'isrc': type(str()),
        'name': type(str()), 
        'itunes_album_id_1': type(np.float64()),
        'itunes_album_ids_1': type(np.float64()),
        'itunes_artist_ids_1': type(np.float64()),
        'itunes_artist_names_1': type(str()),
        'itunes_track_ids_1': type(np.float64()),
        'peak_date': type(pd.to_datetime('2019-01-01')),
        'peak_rank': type(np.float64()),
        'pre_rank': type(np.float64()),
        'rank': type(np.float64()),
        'rank_1d_ago': type(np.float64()),
        'rank_today': type(np.float64()),
        'release_dates_1': type(pd.to_datetime('2019-01-01')),
        'storefronts_1': type(str()),
        'time_on_chart': type(np.float64()),
        'track_genre_1': type(str())
        }

    itunes_types = {
        'added_at': type(pd.to_datetime('2019-01-01')), 
        'album_ids_1': type(np.float64()),
        'album_label_1': type(str()),
        'album_names_1': type(str()),
        'album_upc_1': type(str()),
        'artist_covers_1': type(str()),
        'artist_images_1': type(str()),
        'cm_track': type(str()),
        'artist_names_1': type(str()),
        'cm_artist_1': type(np.float64()),
        'code2': type(str()),
        'code2s_1': type(str()),
        'itunes': type(np.int64()),
        'composer_1': type(str()),
        'genre': type(str()),
        'id': type(str()),
        'image_url': type(str()),
        'isrc': type(str()),
        'name': type(str()), 
        'itunes_album_id_1': type(np.float64()),
        'itunes_album_ids_1': type(np.float64()),
        'itunes_artist_ids_1': type(np.float64()),
        'itunes_artist_names_1': type(str()),
        'itunes_track_ids_1': type(np.float64()),
        'peak_date': type(pd.to_datetime('2019-01-01')),
        'peak_rank': type(np.float64()),
        'pre_rank': type(np.float64()),
        'rank': type(np.float64()),
        'rank_1d_ago': type(np.float64()),
        'rank_today': type(np.float64()),
        'release_dates_1': type(pd.to_datetime('2019-01-01')),
        'storefronts_1': type(str()),
        'time_on_chart': type(np.float64()),
        'track_genre_1': type(str())
        }  
    
    shazam_types = {
        'added_at': type(pd.to_datetime('2019-01-01')), 
        'album_ids_1': type(np.float64()),
        'album_label_1': type(str()),
        'album_names_1': type(str()),
        'album_upc_1': type(str()),
        'artist_covers_1': type(str()),
        'artist_images_1': type(str()),
        'cm_track': type(str()),
        'artist_names_1': type(str()),
        'cm_artist_1': type(np.float64()),
        'code2': type(str()),
        'code2s_1': type(str()),
        'itunes_id': type(np.int64()),
        'composer_1': type(str()),
        'city': type(str()),
        'id': type(str()),
        'image_url': type(str()),
        'isrc': type(str()),
        'name': type(str()), 
        'itunes_album_id_1': type(np.float64()),
        'itunes_album_ids_1': type(np.float64()),
        'itunes_artist_ids_1': type(np.float64()),
        'itunes_artist_names_1': type(str()),
        'itunes_track_ids_1': type(np.float64()),
        'shazam_track_id': type(np.int64()),
        'num_of_shazams': type(np.float64()),
        'peak_date': type(pd.to_datetime('2019-01-01')),
        'peak_rank': type(np.float64()),
        'pre_rank': type(np.float64()),
        'rank': type(np.float64()),
        'rank_1d_ago': type(np.float64()),
        'rank_today': type(np.float64()),
        'release_dates_1': type(pd.to_datetime('2019-01-01')),
        'storefronts_1': type(str()),
        'time_on_chart': type(np.float64()),
        'track_genre_1': type(str())
        } 
    
    spotify_types = {
        'added_at': type(pd.to_datetime('2019-01-01')),
        'album_ids_1': type(np.float64()),
        'album_label_1': type(str()),
        'album_names_1': type(str()),
        'album_upc_1': type(str()),
        'artist_covers_1': type(str()),
        'artist_images_1': type(str()),
        'artist_names_1': type(str()),
        'chart_name': type(str()),
        'chart_type': type(str()),
        'cm_artist_1': type(np.float64()),
        'cm_track': type(str()),
        'code2': type(str()),
        'code2s_1': type(str()),
        'current_plays': type(np.float64()),
        'duration': type(str()),
        'id': type(str()),
        'image_url': type(str()),
        'isrc': type(str()),
        'name': type(str()),
        'peak_date': type(pd.to_datetime('2019-01-01')),
        'peak_rank': type(np.float64()),
        'pre_rank': type(np.float64()),
        'rank': type(np.float64()),
        'rank_1d_ago': type(np.float64()),
        'rank_today': type(np.float64()),
        'plays_1d_ago': type(np.float64()),
        'plays_today': type(np.float64()),
        'release_dates_1': type(pd.to_datetime('2019-01-01')),
        'spotify': type(np.int64()),
        'spotify_album_id': type(str()),
        'time_on_chart': type(np.float64()), 
        'spotify_album_ids_1': type(str()),
        'spotify_artist_ids_1': type(str()),
        'track_genre_1': type(str()),
        'spotify_artist_names_1': type(str()),
        'spotify_duration_ms': type(np.float64()),
        'spotify_popularity': type(np.float64()),
        'spotify_track_ids_1': type(str())}

    type_map = {
        'youtube': youtube_types,
        'spotify': spotify_types,
        'shazam': shazam_types,
        'applemusic': apple_types,
        'itunes': itunes_types
    }

    tot_test = 0
    err_count = 0

    for i in range(len(res)):
        track = res.iloc[i]
        for k in type_map[platform].keys():
            try:
                assert k in track.index
                try:
                    tot_test += 1
                    assert type(track[k]) == type_map[platform][k]
                except AssertionError:
                    err_count += 1
                    print(f"Assertion error at cm_track: {track['cm_track']}, column: {k} -> expected {type_map[platform][k]}, got {type(track[k])}")

            except AssertionError:
                print(f"Invalid input at cm_track: {track['cm_track']}, column: {k} -> key not found or nan encountered.")

    print(f"Total occurrence of errors: {err_count}. Error rate: {err_count/tot_test}.")


