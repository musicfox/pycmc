#import pycm.utilities as utilities
from . import utilities
def fanmetrics(cmid, start_date, dsrc='instagram', valueCol='followers', ):
    """
    Query the chartmetric API for artist fanmetrics.

    :param cmid:        string chartmetric artist id
    :param start_date:  string ISO date %Y-%m-%d
    :param dsrc:        string data source
                        spotify, facebook, twitter, instagram, youtube,
			wikipedia, bandsintown, soundcloud,
			facebook_fans_by_country, or
			facebook_storytellers_by_country 

    https://api.chartmetric.io/api/artist/:id/stat/:source
    """
    urlhandle = f"/artist/{cmid}/stat/{dsrc}"
    params = {
        'since': start_date,
    }
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)


def listening(cmid, start_date):
    """
    Query the chartmetric.io API for artist metadata.

    https://api.chartmetric.io/api/artist/:id/spWherePeopleListenInsights

    :param cmid:        string chartmetric artist ID
    :returns:           dict of artist metatdata
    """
    urlhandle = f"/artist/{cmid}/spWherePeopleListenInsights"
    params = {
        'since': start_date,
    }
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)


def tunefind(cmid):
    """
    Query the chartmetric.io API for artist metadata.

    https://api.chartmetric.io/api/artist/:id/tunefind

    :param cmid:        string chartmetric artist ID
    :returns:           dict of artist metatdata
    """
    urlhandle = f"/artist/{cmid}/tunefind"
    params = None
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)


def albums(cmid):
    """
    Query the chartmetric.io API for artist metadata.

    https://api.chartmetric.io/api/artist/:id/albums

    :param cmid:        string chartmetric artist ID
    :returns:           dict of artist metatdata
    """
    urlhandle = f"/artist/{cmid}/albums"
    params = None
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)


def tracks(cmid):
    """
    Query the chartmetric.io API for artist metadata.

    https://api.chartmetric.io/api/artist/:id/tracks

    :param cmid:        string chartmetric artist ID
    :returns:           dict of artist metatdata
    """
    urlhandle = f"/artist/{cmid}/tracks"
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)


def related(cmid, limit=100):
    """
    Query the chartmetric.io API for artist metadata.

    https://api.chartmetric.io/api/artist/:id/relatedartists

    :param cmid:        string chartmetric artist ID
    :returns:           list of related artists
    """
    urlhandle = f"/artist/{cmid}/relatedartists"
    params = {
        'limit': limit,
    }
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)


def metadata(cmid):
    """
    Query the chartmetric.io API for artist metadata.

    https://api.chartmetric.io/api/artist/:id

    :param cmid:        string chartmetric artist ID
    :returns:           dict of artist metatdata
    """
    urlhandle = f"/artist/{cmid}"
    params = None
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)


def playlists(cmid, dsrc, valueCol, start_date, ):
    """
    https://api.chartmetric.io/api/artist/:id/:type/:status/playlists
    """
    pass


def urls(cmid):
    """
    Query the artist url endpoint given the chartmetric ID and return
    the streaming/social service URLs.

    https://api.chartmetric.io/api/artist/:id/urls

    :param cmid:        string chartmetric artist ID 
    :returns:           dict of platform urls for artist
    """
    urlhandle = f"/artist/{cmid}/urls"
    params = None
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)

