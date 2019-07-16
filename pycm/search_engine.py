from . import utilities


def search(query, limit=None, offset=None):

    """
    Search tracks, albums, artists, curators, playlists with one single query. 
    https://api.chartmetric.com/api/playlist/:platform/:id/similarplaylists

    :param query:          string of search query, can be URLs
    :params limit:         the number of entries to be returned, default 10 
    :params offset:        the offset of entries to be returned, default 0

    :returns:              dictionary of results, keys being the following
                           'artists', 'playlists', 'tracks', 'curators' and 'albums'
    """
    urlhandle = f"/search"
    params = {
        'q': query
    }
    if limit != None:
        params['limit'] = limit
    if offset != None:
        params['offset'] = offset
        
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)