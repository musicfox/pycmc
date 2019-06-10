#import pycm.utilities as utilities
from . import utilities

def metadata(cmid):
    """
    Query the track metadata endpoint given the chartmetric
    id. 
    
    https://api.chartmetric.com/api/track/:id

    :param cmid:        string chartmetric.com entity ID

    :returns:           dictionary of track metadata
    """
    urlhandle = f"/track/{cmid}"
    data = utilities.RequestData(urlhandle, params=None)
    return utilities.RequestGet(data)

def tunefind(cmid):
    """
    Query the track tunefind stats endpoint given the chartmetric id.

    https://api.chartmetric.com/api/track/:id/tunefind

    :param cmid:        string chartmetric.com entity ID
    """
    urlhandle = f"/track/{cmid}/tunefind"
    data = utilities.RequestData(urlhandle, params = None)
    return utilities.RequestGet(data)

def playlists(cmid, date, status='current', indie=False, limit=1000,):
    """
    Query the track playlist placement API endpoint.

    https://api.chartmetric.com/api/track/:id/:streamingType/:status/playlists
    :param cmid:        string chartmetric.com entity ID
    :param start_date:  string ISO date
    :param end_date:    string ISO date
    :param status:      string 'current' or 'past'
    :param indie:       Boolean true if playlist created by major labels
    :param limit:       number of entries to be returned
    """
    stype = 'spotify' # 'applemusic', 'deezer'
    urlhandle = f"/track/{cmid}/{stype}/playlists/snapshot"
    params = {
        'date': date,
        'offset': 0,
        'limit': 1000,
    }
    data = utilities.RequestData(urlhandle, params = params)
    return utilities.RequestGet(data)
