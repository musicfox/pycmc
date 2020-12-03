from . import utilities


def search(query, limit=None, offset=None, type="all"):
    """
    Search the tracks, albums, artists, curators and playlists
    with one single query.

    https://api.chartmetric.com/api/search

    **Parameters**

    - `query`:       string of search query, can be URLs

    - `limit`:      int number of entries returned, default 10

    - `offset`:     int offset of entries returned, default 0

    - `type`:       string defining search type, must be one of

        'all' (default), 'artists', 'tracks', 'playlists',

        'curators', 'albums', 'stations' or 'cities'.

    **Returns**

    A dictionary of results, keys include

        'artists', 'playlists', 'tracks',
        'curators', 'albums', 'labels',
        'stations' and 'cities'

    """
    urlhandle = f"/search"
    params = {"q": query, "type": type}
    if limit != None:
        params["limit"] = limit
    if offset != None:
        params["offset"] = offset

    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)
