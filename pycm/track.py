import pycm.utilities as utilities

def metadata(cmid):
    """
    Query the track metadata endpoint given the chartmetric
    id. 
    
    https://api.chartmetric.io/api/track/:id

    :param cmid:        string chartmetric.io entity ID

    :returns:           dictionary of track metadata
    """

    pass

def tunefind(cmid):
    """
    Query the track tunefind stats endpoint given the chartmetric id.

    https://api.chartmetric.io/api/track/:id/tunefind

    :param cmid:        string chartmetric.io entity ID
    """
    pass

def playlists(cmid, start_date, end_date, status='past', indie=False, limit=1000,):
    """
    Query the track playlist placement API endpoint.

    https://api.chartmetric.io/api/track/:id/:streamingType/:status/playlists
    :param cmid:        string chartmetric.io entity ID
    :param start_date:  string ISO date
    :param end_date:    string ISO date
    :param status:      string 'current' or 'past'
    :param indie:       Boolean true if playlist created by major labels
    :param limit:       number of entries to be returned
    """
