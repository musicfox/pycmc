from . import utilities


def metadata(cmid, stype):
    """
    Get the metadata for the playlist on streaming platform given CMID.

    https://api.chartmetric.com/api/playlist/:platform/:id

    **Parameters**

    - `cmid`:        string or int Chartmetric playlist ID

    - `stype`:       string streaming platform, choose from

        'spotify', 'applemusic', or 'deezer'

    **Returns**            

    A dictionary of playlist metadata.
    """
    urlhandle = f"/playlist/{stype}/{cmid}"
    params = None
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)


def evolution(cmid, byType):
    """
    Get the playlist evolution stats, given artist, album or track CMID.

    https://api.chartmetric.com/api/playlist/by/:type/:id/playlist-evolution

    **Parameters**

    - `cmid`:        string Chartmetric {byType} ID

    - `byType`:      string type of evolution stats requested, choose from

        'artist', 'track', 'album'

    **Returns**            

    A nested dict, keys being
    - 'playlistDataPerDate' (dicts indexed by dates),

    - 'statsDataPlot' (list of lists)

    - 'playlistDataPlot' (list of lists)
    """
    urlhandle = f"/playlist/by/{byType}/{cmid}/playlist-evolution"
    params = None
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)


def lists(
    stype="spotify",
    sort="followers",
    country="US",
    limit=100,
    offset=0,
    indie=False,
):
    """
    Get the list of playlists, given the streaming platform.

    https://api.chartmetric.com/api/playlist/:streamingType/lists

    **Parameters**

    - `stype`:       string streaming platform, choose from

        'spotify', 'applemusic', 'deezer' or 'amazon'

    - `sort`:        string column to sort the playlists by, e.g. 'followers', 'last_updated'

    - `country`:     string country code

    - `limit`:       int number of playlists to return,
    
        maximum acceptable is 100

    - `offset`:      offset of entries to be returned

    - `indie`:       boolean True to return indie playlists

    **Returns**            

    A list of dicts of playlists.
    """
    indie = "true" if indie else "false"
    urlhandle = f"/playlist/{stype}/lists"
    params = {
        "indie": indie,
        "limit": limit,
        "offset": offset,
        "sortColumn": sort,
    }
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)


def snapshot(cmid, stype, date):
    """
    Get the snapshot of all tracks in a playlist given CMID
    on a given streaming platform for a given date.

    https://api.chartmetric.com/api/playlist/:platform/:id/snapshot

    **Parameters**

    - `cmid`:        string or int Chartmetric playlist ID

    - `stype`:       string streaming platform, choose from

        'spotify', 'applemusic', 'deezer' or 'amazon'

    - `date`:        string date in ISO format %Y-%m-%d

    **Returns**

    A list of dictionaries of tracks contained in the playlist.
    """
    urlhandle = f"/playlist/{stype}/{cmid}/snapshot"
    params = {"date": date}
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)


def tracks(cmid, stype, span="current"):
    """
    Get the current or past tracks contained in a playlist given CMID
    on a given streaming platform.

    https://api.chartmetric.com/api/playlist/:platform/:id/:span/tracks

    **Parameters**

    - `cmid`:        string or int Chartmetric playlist ID

    - `stype`:       string streaming platform, choose from

        'spotify', 'applemusic', 'deezer' or 'amazon'

    - `span`:        string 'past' or 'current'

    **Returns**

    A list of dictionaries of tracks contained in the playlist.
    """
    urlhandle = f"/playlist/{stype}/{cmid}/{span}/tracks"
    params = None
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)
