from .. import utilities


def tracks(cm_track_id, chart_type, start_date, end_date=None):
    """
    Gets the Chartmetric Score for tracks given the CM track ID.

    https://api.chartmetric.com/api/charts/track/:type_id/:chart_type/cm-score

    :param cm_track_id:     Chartmetric track ID
    :param chart_type:      string chart type, choose from
                            'spotify-top', 'spotify-viral',
                            'applemusic-genre', 'applemusic-daily', 
                            'applemusic-albums' 'itunes', 
                            'itunes-albums', 'shazam'
    :param start_date:      string date in ISO format %Y-%m-%d
    :param end_date:        string date in ISO format %Y-%m-%d, default today

    :returns:               list of dictionary of CM scores for the track
    """
    urlhandle = f"/charts/track/{cm_track_id}/{chart_type}/cm-score"
    params = {
        'since': start_date,
        'until': end_date
    }
        
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)


def artists(cm_artist_id, chart_type, start_date, end_date=None):
    """
    Gets the Chartmetric Score for artists given the CM artist ID.

    https://api.chartmetric.com/api/charts/artist/:type_id/:chart_type/cm-score

    :param cm_artist_id:    Chartmetric artist ID
    :param chart_type:      string chart type, choose from
                            'spotify-top', 'spotify-viral',
                            'applemusic-genre', 'applemusic-daily', 
                            'applemusic-albums' 'itunes', 
                            'itunes-albums', 'shazam'
    :param start_date:      string date in ISO format %Y-%m-%d
    :param end_date:        string date in ISO format %Y-%m-%d, default today

    :returns:               list of dictionary of CM scores for the artist
    """
    urlhandle = f"/charts/artist/{cm_artist_id}/{chart_type}/cm-score"
    params = {
        'since': start_date,
        'until': end_date
    }
        
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)


def albums(cm_album_id, chart_type, start_date, end_date=None):
    """
    Gets the Chartmetric Score for albums given the CM album ID.

    https://api.chartmetric.com/api/charts/album/:type_id/:chart_type/cm-score

    :param cm_album_id:     Chartmetric album ID
    :param chart_type:      string chart type, choose from
                            'spotify-top', 'spotify-viral',
                            'applemusic-genre', 'applemusic-daily', 
                            'applemusic-albums' 'itunes', 
                            'itunes-albums', 'shazam'
    :param start_date:      string date in ISO format %Y-%m-%d
    :param end_date:        string date in ISO format %Y-%m-%d, default today

    :returns:               list of dictionary of CM scores for the album
    """
    urlhandle = f"/charts/album/{cm_album_id}/{chart_type}/cm-score"
    params = {
        'since': start_date,
        'until': end_date
    }
        
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)
