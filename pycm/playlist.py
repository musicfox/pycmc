# import pycm.utilities as utilities
from . import utilities


def lists(
    stype="spotify",
    sort="followers",
    country="US",
    limit=100,
    offset=0,
    indie=False,
):
    """
    Query the chartmetri.io API playlist charts endpoint

    https://api.chartmetric.com/api/playlist/:streamingType/lists

    :param stype:       string 'spotify', 'applemusic', or 'deezer'
    :param sort:        string 'followers'or 'last_updated'
    :param country:     string country code
    :param limit:       integer limit number of queries
    :param offset:      offset of entries to be returned
    :param indie:       boolean True to return indie playlists

    :returns:           list of dicts of playlists
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


def metadata(cmid, stype):
    """
    Query the chartmetric.com API playlist metatdata endpoint

    :param cmid:        string chartmetric playlist ID
    :param stype:       string 'spotify', 'applemusic', or 'deezer'

    :return:             dictionary of playlist metadata
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

    :returns:           list of dicts of tracks
    """
    urlhandle = f"/playlist/{stype}/{cmid}/{span}/tracks"
    params = None
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)


def evolution(cmid, byType):
    """
    Query the chartmetric.com API playlist/evolution endpoint

    :param cmid:        string chartmetric {byType} ID
    :param byType:      string 'artist', 'track', 'album'

    :returns:           nested dict, keys being
                        'playlistDataPerDate' (dicts indexed by dates),
                        'statsDataPlot' (list of lists)
                        and 'playlistDataPlot' (list of lists)
    """
    stype = "spotify"  # only one listed in docs...
    urlhandle = f"/playlist/{stype}/{byType}/{cmid}/evolution"
    params = None
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)
