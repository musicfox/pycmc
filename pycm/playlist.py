from . import utilities


def metadata(cmid, stype):
    """
    Get the metadata for the playlist on streaming platform given CMID.

    https://api.chartmetric.com/api/playlist/:platform/:id

    :param cmid:        string or int Chartmetric playlist ID
    :param stype:       string streaming platform, choose from
                        'spotify', 'applemusic', or 'deezer'

    :return:            dictionary of playlist metadata
    """
    urlhandle = f"/playlist/{stype}/{cmid}"
    params = None
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)


def evolution(cmid, byType):
    """
    Get the playlist evolution stats, given artist, album or track CMID.

    https://api.chartmetric.com/api/playlist/:platform/:type/:id/evolution

    :param cmid:        string Chartmetric {byType} ID
    :param byType:      string type of evolution stats requested,
                        choose from 'artist', 'track', 'album'

    :return:            nested dict, keys being
                        'playlistDataPerDate' (dicts indexed by dates),
                        'statsDataPlot' (list of lists)
                        and 'playlistDataPlot' (list of lists)
    """
    stype = "spotify"  # only one listed in docs...
    urlhandle = f"/playlist/{stype}/{byType}/{cmid}/evolution"
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

    :param stype:       string streaming platform, choose from
                        'spotify', 'applemusic', 'deezer' or 'amazon'
    :param sort:        string column to sort the playlists by,
                        e.g. 'followers', 'last_updated'
    :param country:     string country code
    :param limit:       int number of playlists to return,
                        maximum acceptable is 100
    :param offset:      offset of entries to be returned
    :param indie:       boolean True to return indie playlists

    :return:            list of dicts of playlists
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

    :param cmid:        string or int Chartmetric playlist ID
    :param stype:       string streaming platform, choose from
                        'spotify', 'applemusic', 'deezer' or 'amazon'
    :param date:        string date in ISO format %Y-%m-%d

    :return:            list of dictionaries of
                        tracks contained in the playlist
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

    :param cmid:        string or int Chartmetric playlist ID
    :param stype:       string streaming platform, choose from
                        'spotify', 'applemusic', 'deezer' or 'amazon'
    :param span:        string 'past' or 'current'

    :return:            list of dictionaries of
                        tracks contained in the playlist
    """
    urlhandle = f"/playlist/{stype}/{cmid}/{span}/tracks"
    params = None
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)
