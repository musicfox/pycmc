from .. import utilities


def tracks(cm_track_id, chart_type, start_date, end_date=None):
    """
    Query the charts/amazon/tracks endpoint for the
    given date.

    :param cm_track_id: Chartmetric track ID
    :param chart_type:  string chart type, taking one of
                        {'spotify-top', 'spotify-viral',
                        'applemusic-genre', 'applemusic-daily', 
                        'applemusic-albums' 'itunes', 
                        'itunes-albums', 'shazam}
    :param start_date:  string date in ISO format %Y-%m-%y
    :param end_date:    string date in ISO format %Y-%m-%y, default today

    :returns:           list of dictionary of amazon tracks
                        chart data
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
    Query the charts/amazon/tracks endpoint for the
    given date.

    :param cm_artist_id: Chartmetric artist ID
    :param chart_type:   string chart type, taking one of
                         {'spotify-top', 'spotify-viral',
                         'applemusic-genre', 'applemusic-daily', 
                         'applemusic-albums' 'itunes', 
                         'itunes-albums', 'shazam}
    :param start_date:   string date in ISO format %Y-%m-%y
    :param end_date:     string date in ISO format %Y-%m-%y, default today

    :returns:            list of dictionary of amazon tracks
                         chart data
    """
    urlhandle = f"/charts/artist/{cm_artist_id}/{chart_type}/cm-score"
    params = {
        'since': start_date,
        'until': end_date
    }
        
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)['data']


def albums(cm_album_id, chart_type, start_date, end_date=None):
    """
    Query the charts/amazon/tracks endpoint for the
    given date.

    :param cm_album_id: Chartmetric album ID
    :param chart_type:  string chart type, taking one of
                        {'spotify-top', 'spotify-viral',
                        'applemusic-genre', 'applemusic-daily', 
                        'applemusic-albums' 'itunes', 
                        'itunes-albums', 'shazam}
    :param start_date:  string date in ISO format %Y-%m-%y
    :param end_date:    string date in ISO format %Y-%m-%y, default today

    :returns:           list of dictionary of amazon tracks
                        chart data
    """
    urlhandle = f"/charts/album/{cm_album_id}/{chart_type}/cm-score"
    params = {
        'since': start_date,
        'until': end_date
    }
        
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)
