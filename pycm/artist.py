import pycm.utilities as utilities

def fanmetrics(cmid, dsrc, valueCol, start_date, ):
    """
    https://api.chartmetric.io/api/artist/:id/stat/:source
    """
    pass

def WherePeopleListen(cmid, dsrc, valueCol, start_date, ):
    """
    https://api.chartmetric.io/api/artist/:id/spWherePeopleListenInsights
    """
    pass

def tunefind(cmid):
    """
    https://api.chartmetric.io/api/artist/:id/tunefind
    """
    pass

def albums(cmid):
    """
    https://api.chartmetric.io/api/artist/:id/albums
    """
    pass

def tracks(cmid):
    """
    https://api.chartmetric.io/api/artist/:id/tracks
    """
    pass

def related(cmid, limit=1000):
    """
    https://api.chartmetric.io/api/artist/:id/relatedartists
    """
    pass

def metadata(cmid):
    """
    https://api.chartmetric.io/api/artist/:id
    """
    pass

def playlists(cmid, dsrc, valueCol, start_date, ):
    """
    https://api.chartmetric.io/api/artist/:id/:type/:status/playlists
    """
    pass

def urls(cmid):
    """
    Query the artist url endpoint given the chartmetric ID and return
    the streaming/social service URLs.
    """
    pass
