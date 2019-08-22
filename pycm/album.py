from . import utilities


def charts(stype, cmid, start_date, end_date=None):
    """
    Query the charts for the given album of a selected streamer type. 

    https://api.chartmetric.com/api/album/:id/:type/charts
    
    :param stype:           string streaming platform, choose from
                            'applemusic', 'itunes' or 'amazon'
    :param cmid:            string or int chartmetric album ID
    :param start_date:      string start data in ISO format
    :param end_date:        string end date in ISO format

    :return:                list of dictionaries of the chart for
                            the given album
    """
    urlhandle = f"/album/{cmid}/{stype}/charts"
    params = {
        "since": start_date,
        "until": end_date,
    }
    data = utilities.RequestData(urlhandle, params=params)
    return utilities.RequestGet(data)['data']


def get_album_ids(id_type, specific_id):
    """
    Query all the related album IDs given a specific ID type.

    https://api.chartmetric.com/api/album/:type/:id/get-ids

    :param id_type:         string of the type of ID, choose from
                            'chartmetric', 'upc', 'spotify', 'itunes', 'deezer'
    :param specific_id:     specific ID corresponding to the id_type
    
    :return:                list of dictionaries with various types of ID
    """
    urlhandle = f"/album/{id_type}/{specific_id}/get-ids"
    data = utilities.RequestData(urlhandle, params=None)
    return utilities.RequestGet(data)


def metadata(cmid):
    """
    Query the album metadata endpoint given the chartmetric ID. 
    
    https://api.chartmetric.com/api/album/:id

    :param cmid:        string or int Chartmetric album ID

    :returns:           dictionary of album metadata
    """
    urlhandle = f"/album/{cmid}"
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

    https://api.chartmetric.com/api/album/:id/:platform/:status/playlists

    :param cmid:        string or int Chartmetric album ID
    :param start_date:  string ISO date
    :param end_date:    string ISO date
    :param stype:       string streaming platform, choose from
                        'spotify, 'applemusic', or 'deezer'
    :param status:      string 'current' or 'past'
    :param indie:       Boolean true if playlist created by major labels
    :param limit:       number of entries to be returned

    :return:            list of dictionaries of playlists for the album
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


def stats(cmid, stype, start_date=None, end_date=None):
    """
    Query the statistics from the given streaming platform,
    specifically popularity for Spotify.

    https://api.chartmetric.com/api/album/:id/:platform/stats
    
    :param cmid:        string or int Chartmetric album ID
    :param stype:       string streaming platform type, only 'spotify'
    :param start_date:  string of start date in ISO format
    :param end_date:    string of end date in ISO format

    :return:            list of dictionaries of the statistics
                        for an album on a streaming platform
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

    :params cmid:   string or int Chartmetric album ID
   
    :return:        list of dictionaries of the tracks in an album
    """
    urlhandle = f"/album/{cmid}/tracks"
    data = utilities.RequestData(urlhandle, params=None)
    return utilities.RequestGet(data)


def tunefind(cmid):
    """
    Query the album tunefind stats given the Chartmetric ID.

    https://api.chartmetric.com/api/album/:id/tunefind

    :param cmid:    string or int Chartmetric album ID

    :return:        list of dictionaries of tunefind stats
    """
    urlhandle = f"/album/{cmid}/tunefind"
    data = utilities.RequestData(urlhandle, params=None)
    return utilities.RequestGet(data)


