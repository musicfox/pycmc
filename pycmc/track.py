from . import utilities


def charts(chart_type, cm_track_id, start_date, end_date=None):
    """
    Get the charts of certain type containing this given track
    since a specified start date.

    https://api.chartmetric.com/api/track/:id/:type/charts

    **Parameters**

    - `chart_type`:  string type of chart, choose from

       'spotify_viral_daily', 'spotify_viral_weekly', 
       'spotify_top_daily', 'spotify_top_weekly', 
       'applemusic_top', 'applemusic_daily', 
       'applemusic_albums', 'itunes_top', 'amazon', 
       'itunes_albums', 'shazam', 'beatport'

    - `cm_track_id`: string or int Chartmetric track ID

    - `start_date`:  string ISO date

    - `end_date`:    string ISO date

    **Returns**

    A list of dictionaries of the charts data.
    """

    urlhandle = f"/track/{cm_track_id}/{chart_type}/charts"
    params = {"since": start_date}
    if end_date != None:
        params["until"] = end_date
    data = utilities.RequestData(urlhandle, params=params)
    return utilities.RequestGet(data)["data"]


def get_track_ids(id_type, matching_id):
    """
    Get all related track IDs for a given track by a specific ID.
    There can be multiple corresponding Spotify and iTunes IDs
    for some tracks.

    https://api.chartmetric.com/api/track/:type/:id/get-ids

    **Parameters**

    - `id_type`:     string type of track ID,

        'chartmetric' (for cm_track), 'isrc',
        'spotify', 'itunes'

    - `matching_id`: specific track ID that matches the type


    **Returns**

    A list of dictionaries of the related track IDs.
    """
    urlhandle = f"/track/{id_type}/{matching_id}/get-ids"

    data = utilities.RequestData(urlhandle, params=None)
    return utilities.RequestGet(data)


def metadata(cmid):
    """
    Get the metadata for the track given CMID. 
    
    https://api.chartmetric.com/api/track/:id

    **Parameters**

    - `cmid`:        string or int Chartmetric track ID

    **Returns**            

    dictionary of track metadata
    """
    urlhandle = f"/track/{cmid}"
    data = utilities.RequestData(urlhandle, params=None)
    return utilities.RequestGet(data)


def playlist_snapshot(cmid, platform, date, limit=100, offset=0):
    """
    Get the snapshot of playlists on the platform containing the track
    for a given date.

    https://api.chartmetric.com/api/track/:id/:platform/playlists/snapshot

    **Parameters**

    - `cmid`:        string or int Chartmetric track ID

    - `platform`:    string 'spotify', 'applemusic', 'deezer'

    - `date`:        string ISO date

    - `limit`:       int number of entries to be returned; maximum acceptable is 100

    - `offset`:      int offset of entries to be returned

    **Returns**            

    A list of dictionaries of playlists data.
    """
    urlhandle = f"/track/{cmid}/{platform}/playlists/snapshot"
    params = {
        "date": date,
        "limit": limit,
        "offset": offset,
    }
    data = utilities.RequestData(urlhandle, params=params)
    return utilities.RequestGet(data)


def playlists(
    cmid,
    platform,
    status="current",
    start_date=None,
    end_date=None,
    indie=False,
    limit=100,
    offset=0,
):
    """
    Get the current or past playlists containing the track
    on the given streaming platform.    

    https://api.chartmetric.com/api/track/:id/:platform/:status/playlists

    **Parameters**

    - `cmid`:        string or int Chartmetric track ID

    - `platform`:    string 'spotify', 'applemusic', 'deezer', 'amazon'

    - `status`:      string 'past' or 'current'

    - `start_date`:  string ISO start date

    - `end_date`:    string ISO end date, default today

    - `indie`:       bool, False for playlist curated by major label

    - `limit`:       int number of entries to be returned; maximum acceptable is 100

    - `offset`:      int offset of entries, use this to recursively acquire

    **Returns**

    A list of dictionaries of playlists data.
    """
    urlhandle = f"/track/{cmid}/{platform}/{status}/playlists"
    params = {
        "since": start_date,
        "until": end_date,
        "indie": indie,
        "limit": limit,
        "offset": offset,
    }
    data = utilities.RequestData(urlhandle, params=params)
    return utilities.RequestGet(data)


def stats(cm_track_id, platform, start_date=None, end_date=None):
    """
    Get the value time-series for the given track on the given platform.
    Specifically, get popularity for Spotify, views for YouTube and
    count for Shazam.

    https://api.chartmetric.com/api/track/:id/:platform/stats

    **Parameters**

    - `cm_track_id`: string or int Chartmetric track ID

    - `platform`:    string of streaming platform, choose from

        'spotify', 'youtube', 'shazam'

    - `start_date`:  string date in ISO format

    - `end_date`:    string date in ISO format, default is today

    **Returns**           

    A list of dictionaries of the track value stats time-series.
    """
    urlhandle = f"/track/{cm_track_id}/{platform}/stats"
    params = dict()
    if start_date != None:
        params["since"] = start_date
    if end_date != None:
        params["until"] = end_date
    data = utilities.RequestData(urlhandle, params=params)
    return utilities.RequestGet(data)


def tunefind(cmid):
    """
    Get the Tunefind stats given the track.

    https://api.chartmetric.com/api/track/:id/tunefind

    **Parameters**

    - `cmid`:        string or int Chartmetric track ID

    **Returns**            

    A list of dictionaries of Tunefind data.
    """
    urlhandle = f"/track/{cmid}/tunefind"
    data = utilities.RequestData(urlhandle, params=None)
    return utilities.RequestGet(data)
