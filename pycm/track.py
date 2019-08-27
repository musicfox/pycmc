from . import utilities


def charts(chart_type, cm_track_id, start_date, end_date=None):
    """
    Get the charts of certain type containing this given track
    since a specified start date.

    https://api.chartmetric.com/api/track/:id/:type/charts

    :param chart_type:  string type of chart, choose from
                        'spotify_viral_daily', 'spotify_viral_weekly', 
                        'spotify_top_daily', 'spotify_top_weekly', 
                        'applemusic_top', 'applemusic_daily', 
                        'applemusic_albums', 'itunes_top', 'amazon', 
                        'itunes_albums', 'shazam', 'beatport'
    :param cm_track_id: string or int Chartmetric track ID
    :param start_date:  string ISO date
    :param end_date:    string ISO date

    :return:            list of dictionaries of the charts data
    """
    
    urlhandle = f"/track/{cm_track_id}/{chart_type}/charts"
    params = {"since": start_date}
    if end_date != None:
        params['until'] = end_date
    data = utilities.RequestData(urlhandle, params=params)
    return utilities.RequestGet(data)['data']


def get_track_ids(id_type, matching_id):
    """
    Get all related track IDs for a given track by a specific ID.
    There can be multiple corresponding Spotify and iTunes IDs
    for some tracks.

    https://api.chartmetric.com/api/track/:type/:id/get-ids

    :param id_type:     string type of track ID,
                        'chartmetric' (for cm_track), 'isrc',
                        'spotify', 'itunes'
    :param matching_id: specific track ID that matches the type

    :return:            list of dictionaries of the related track IDs
    """
    urlhandle = f"/track/{id_type}/{matching_id}/get-ids"
    
    data = utilities.RequestData(urlhandle, params=None)
    return utilities.RequestGet(data)


def metadata(cmid):
    """
    Get the metadata for the track given CMID. 
    
    https://api.chartmetric.com/api/track/:id

    :param cmid:        string or int Chartmetric track ID

    :return:            dictionary of track metadata
    """
    urlhandle = f"/track/{cmid}"
    data = utilities.RequestData(urlhandle, params=None)
    return utilities.RequestGet(data)


def playlist_snapshot(cmid, platform, date, limit=100, offset=0):
    """
    Get the snapshot of playlists on the platform containing the track
    for a given date.

    https://api.chartmetric.com/api/track/:id/:platform/playlists/snapshot

    :param cmid:        string or int Chartmetric track ID
    :param platform:    string 'spotify', 'applemusic', 'deezer'
    :param date:        string ISO date
    :param limit:       int number of entries to be returned,
                        maximum acceptable is 100
    :param offset:      int offset of entries to be returned

    :return:            list of dictionaries of playlists data
    """
    urlhandle = f"/track/{cmid}/{platform}/playlists/snapshot"
    params = {
        'date': date,
        'limit': limit,
        'offset': offset,
    }
    data = utilities.RequestData(urlhandle, params=params)
    return utilities.RequestGet(data)


def playlists(
    cmid,
    platform, 
    status='current', 
    start_date=None,
    end_date=None,
    indie=False,
    limit=100,
    offset=0
    ):
    """
    Get the current or past playlists containing the track
    on the given streaming platform.    

    https://api.chartmetric.com/api/track/:id/:platform/:status/playlists

    :param cmid:        string or int Chartmetric track ID
    :param platform:    string 'spotify', 'applemusic', 'deezer', 'amazon'
    :param status:      string 'past' or 'current'
    :param start_date:  string ISO start date
    :param end_date:    string ISO end date, default today
    :param indie:       bool, False for playlist curated by major label
    :param limit:       int number of entries to be returned,
                        maximum acceptable is 100
    :param offset:      int offset of entries, use this to recursively acquire

    :return:            list of dictionaries of playlists data
    """
    urlhandle = f"/track/{cmid}/{platform}/{status}/playlists"
    params = {
        'since': start_date,
        'until': end_date,
        'indie': indie,
        'limit': limit,
        'offset': offset,
    }
    data = utilities.RequestData(urlhandle, params=params)
    return utilities.RequestGet(data)


def stats(cm_track_id, platform, start_date=None, end_date=None):
    """
    Get the value time-series for the given track on the given platform.
    Specifically, get popularity for Spotify, views for YouTube and
    count for Shazam.

    https://api.chartmetric.com/api/track/:id/:platform/stats

    :param cm_track_id: string or int Chartmetric track ID
    :param platform:    string of streaming platform,
                        'spotify', 'youtube', 'shazam'
    :param start_date:  string date in ISO format
    :param end_date:    string date in ISO format, default is today

    :returns:           list of dictionaries of the track 
                        value stats time-series
    """
    urlhandle = f"/track/{cm_track_id}/{platform}/stats"
    params=dict()
    if start_date != None:
        params['since'] = start_date
    if end_date != None:
        params['until'] = end_date
    data = utilities.RequestData(urlhandle, params=params)
    return utilities.RequestGet(data)


def tunefind(cmid):
    """
    Get the Tunefind stats given the track.

    https://api.chartmetric.com/api/track/:id/tunefind

    :param cmid:        string or int Chartmetric track ID

    :return:            list of dictionaries of Tunefind data
    """
    urlhandle = f"/track/{cmid}/tunefind"
    data = utilities.RequestData(urlhandle, params=None)
    return utilities.RequestGet(data)

