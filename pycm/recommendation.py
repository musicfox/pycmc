from . import utilities


def similar_playlists(
    cm_playlist_id,
    platform, 
    storefront=None,
    indie=None,
    limit=None):

    """
    Request similar playlists from chartmetric.
    https://api.chartmetric.com/api/playlist/:platform/:id/similarplaylists

    :param cm_playlist_id: Chartmetric playlist ID
    :param platform:       string streaming platform type,
                           'spotify', 'applemusic' or 'deezer'
    :params storefront:    Apple Music storefront
    :params indie:         Boolean for whether playlist curated 
                           by major labels (Spotify only)
    :params limit:         the number of entries to be returned  

    :returns:              list of dictionaries containing similar playlists
    """
    urlhandle = f"/playlist/{platform}/{cm_playlist_id}/similarplaylists"
    params = dict()
    if storefront != None:
        params['storefront'] = storefront
    if indie != None:
        params['indie'] = indie
    if limit != None:
        params['limit'] = limit
        
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)