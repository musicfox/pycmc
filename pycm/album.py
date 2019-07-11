# import pycm.utilities as utilities
from . import utilities


def metadata(cmid):
    """
    Query the album metadata endpoint given the chartmetric
    id. 
    
    https://api.chartmetric.com/api/album/:id

    :param cmid:        string chartmetric.com entity ID

    :returns:           dictionary of album metadata
    """

    urlhandle = f"/album/{cmid}"
    data = utilities.RequestData(urlhandle, params=None)
    return utilities.RequestGet(data)


def tunefind(cmid):
    """
    Query the album tunefind stats endpoint given the chartmetric id.

    https://api.chartmetric.com/api/album/:id/tunefind

    :param cmid:        string chartmetric.com entity ID
    """
    urlhandle = f"/album/{cmid}/tunefind"
    data = utilities.RequestData(urlhandle, params=None)
    return utilities.RequestGet(data)


def playlists(
    cmid,
    start_date,
    end_date=None,
    stype="spotify",
    status="current",
    indie=False,
    limit=100,
):
    """
    Query the album playlist placement API endpoint.

    https://api.chartmetric.com/api/album/:id/:streamingType/:status/playlists
    :param cmid:        string chartmetric.com entity ID
    :param start_date:  string ISO date
    :param end_date:    string ISO date
    :param stype:       string streaming platform 'spotify, 'applemusic', or 'deezer'
    :param status:      string 'current' or 'past'
    :param indie:       Boolean true if playlist created by major labels
    :param limit:       number of entries to be returned
    """
    urlhandle = f"/album/{cmid}/{stype}/{status}/playlists"
    params = {
        "since": start_date,
        "until": end_date,
        "limit": limit,
        "offset": 0,
    }
    data = utilities.RequestData(urlhandle, params=params)
    return utilities.RequestGet(data)


def charts(stype, cmid, start_date, end_date=None):
    """
    Query the charts for the given album of a selected streamer type. 

    https://api.chartmetric.com/api/album/:id/:type/charts
    :params stype:          string streaming platform 'applemusic', 'itunes' or 'amazon'
    :params cmid:           chartmetric album id
    :params start_date:     string start data in ISO format
    :params end_date:       string end date in ISO format

    :return:                list of dictionaries containing the charts of the given album
    """
    urlhandle = f"/album/{cmid}/{stype}/charts"
    params = {
        "since": start_date,
        "until": end_date,
    }
    data = utilities.RequestData(urlhandle, params=params)
    return utilities.RequestGet(data)['data']

def get_album_ids(stype, type_id):
    """
    Query all the album ids given a specific id type.

    https://api.chartmetric.com/api/album/:type/:id/get-ids
    :params stype: string of the type of id requesting 'chartmetric', 'upc', 'spotify', 'itunes' and 'deezer'
    :params type_id: specific type id <- I have no idea what this is
    
    :return: list of dictionaries with various types of id
    """
    urlhandle = f"/album/{stype}/{type_id}/get-ids"
    data = utilities.RequestData(urlhandle, params=None)
    return utilities.RequestGet(data)


def stats(cmid, stype, start_date=None, end_date=None):
    """
    Query the statistics from the given streaming platform (popularity for Spotify).

    https://api.chartmetric.com/api/album/:id/:platform/stats
    :params cmid: Chartmetric album id
    :params stype: string streaming platform type 'spotify'
    :params start_date: string of start date in ISO format
    :params end_date: string of end date in ISO format

    :return: list of dictionaries of the statistics of an album on a streaming platform
    """
    urlhandle = f"/album/{cmid}/{stype}/stats"
    params = {
        "since": start_date,
        "until": end_date,
    }
    data = utilities.RequestData(urlhandle, params=params)
    return utilities.RequestGet(data)


def tracks(cmid):
    """
    Query the tracks included in a given album.

    https://api.chartmetric.com/api/album/:id/tracks
    :params cmid: Chartmetric album id
   
    :return: list of dictionaries of the tracks in an album
    """
    urlhandle = f"/album/{cmid}/tracks"
    data = utilities.RequestData(urlhandle, params=None)
    return utilities.RequestGet(data)

