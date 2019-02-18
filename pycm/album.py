import pycm.utilities as utilities

def metadata(cmid):
    """
    Query the album metadata endpoint given the chartmetric
    id. 
    
    https://api.chartmetric.io/api/album/:id

    :param cmid:        string chartmetric.io entity ID

    :returns:           dictionary of album metadata
    """

    pass

def tunefind(cmid):
    """
    Query the album tunefind stats endpoint given the chartmetric id.

    https://api.chartmetric.io/api/album/:id/tunefind

    :param cmid:        string chartmetric.io entity ID
    """
    pass

def playlists(cmid, start_date, end_date, status='past', indie=False, limit=1000,):
    """
    Query the album playlist placement API endpoint.

    https://api.chartmetric.io/api/album/:id/:streamingType/:status/playlists
    :param cmid:        string chartmetric.io entity ID
    :param start_date:  string ISO date
    :param end_date:    string ISO date
    :param status:      string 'current' or 'past'
    :param indie:       Boolean true if playlist created by major labels
    :param limit:       number of entries to be returned
    """
    pass
