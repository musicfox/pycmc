# import pycm.utilities as utilities
from . import utilities


def lists(
    stype="spotify",
    sort="followers",
    country="US",
    limit=100,
    offset=0,
    indie=False,
    daysAgo=7,
):
    """
    **NOTE**

    Documentation for this endpoint is wrong. The exact given exemplar
    returns a 400 BAD_REQUEST -> need to strategize how to fix in the 
    short run.

    Query the chartmetri.io API playlist charts endpoint

    https://api.chartmetric.com/api/playlist/:streamingType/lists

    :param stype:       string 'spotify', 'applemusic', or 'deezer'
    :param sort:        string 'followers'or 'last_updated'
    :param country:     string country code
    :param limit:       integer limit number of queries
    :param offset:      offset of entries to be returned
    :param indie:       boolean True to return indie playlists
    :param daysAgo:     integer how many days ago (?? -> docs are ...)

    :returns:           dict?
    """
    indie = "true" if indie else "false"
    urlhandle = f"/playlist/{stype}/lists"
    params = {
        "daysAgo": daysAgo,
        "indie": indie,
        "limit": limit,
        "offset": offset,
        "sortColumn": sort,
    }
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)


def metadata(cmid, stype):
    """
    Query the chartmetric.com API playlist metatdata endpoint

    :param cmid:        string chartmetric playlist ID
    :param stype:       string 'spotify', 'applemusic', or 'deezer'
    """
    urlhandle = f"/playlist/{stype}/{cmid}"
    params = None
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)


def snapshot(cmid, stype, date):
    """
    Query the chartmetric.com API playlist/snapshot endpoint

    :param cmid:        string chartmetric playlist ID
    :param stype:       string 'spotify', 'applemusic', or 'deezer'
    :param date:        string date in ISO format %Y-%m-%d

    :returns:           list
    """
    urlhandle = f"/playlist/{stype}/{cmid}/snapshot"
    params = {"date": date}
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)


def tracks(cmid, stype, span="current"):
    """
    Query the chartmetric.com API playlist/current endpoint

    :param cmid:        string chartmetric track ID
    :param stype:       string 'spotify', 'applemusic', or 'deezer'
    :param span:        string 'past' or 'current'

    :returns:           list
    """
    urlhandle = f"/playlist/{stype}/{cmid}/{span}/tracks"
    params = None
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)


def evolution(cmid, byType, start_date, end_date):
    """
    Query the chartmetric.com API playlist/evolution endpoint

    :param cmid:        string chartmetric {byType} ID
    :param byType:      string 'artist', 'track', 'album'
    :param start_date:  string ISO beginning date %Y-%m-%d
    :param end_date:    string ISO ending date %Y-%m-%d

    :returns:           list
    """
    stype = "spotify"  # only one listed in docs...
    urlhandle = f"/playlist/{stype}/by/{byType}/{cmid}/evolution"
    params = {"since": start_date, "until": end_date}
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)
