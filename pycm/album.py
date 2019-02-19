#import pycm.utilities as utilities
from . import utilities
def metadata(cmid):
    """
    Query the album metadata endpoint given the chartmetric
    id. 
    
    https://api.chartmetric.io/api/album/:id

    :param cmid:        string chartmetric.io entity ID

    :returns:           dictionary of album metadata
    """

    urlhandle = f"/album/{cmid}"
    data = utilities.RequestData(urlhandle, params = None)
    return utilities.RequestGet(data)

def tunefind(cmid):
    """
    Query the album tunefind stats endpoint given the chartmetric id.

    https://api.chartmetric.io/api/album/:id/tunefind

    :param cmid:        string chartmetric.io entity ID
    """
    urlhandle = f"/album/{cmid}/tunefind"
    data = utilities.RequestData(urlhandle, params = None)
    return utilities.RequestGet(data)



def playlists(cmid, start_date, end_date=None, stype='spotify', status='current', indie=False, limit=100,):
    """
    Query the album playlist placement API endpoint.

    https://api.chartmetric.io/api/album/:id/:streamingType/:status/playlists
    :param cmid:        string chartmetric.io entity ID
    :param start_date:  string ISO date
    :param end_date:    string ISO date
    :param stype:       string streaming platform
                        'spotify, 'applemusic', or 'deezer'
    :param status:      string 'current' or 'past'
    :param indie:       Boolean true if playlist created by major labels
    :param limit:       number of entries to be returned
    """
    urlhandle = f"/album/{cmid}/{stype}/{status}/playlists"
    params = {
        'since': start_date,
        'until': end_date,
        'limit': limit,
        'offset': 0,
    }
    data = utilities.RequestData(urlhandle, params = params)
    return utilities.RequestGet(data)
