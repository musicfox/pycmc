from . import utilities


def similar_playlists(
    cm_playlist_id, platform, storefront=None, indie=None, limit=None
):

    """
    Get the similar playlists for the given playlist on the given platform.

    https://api.chartmetric.com/api/playlist/:platform/:id/similarplaylists

    **Parameters**

    - `cm_playlist_id`:  string or int Chartmetric playlist ID

    - `platform`:        string streaming platform type, choose from

        'spotify', 'applemusic' or 'deezer'

    - `storefront`:     string storefront, required for AppleMusic

    - `indie`:          Boolean for whether playlist curated by major labels (Spotify only)

    - `limit`:          int number of entries to be returned, default 9; maximum acceptable input is 100 (gets 99 back)

    **Returns**              

    A list of dictionaries of similar playlists.
    """
    urlhandle = f"/playlist/{platform}/{cm_playlist_id}/similarplaylists"
    params = dict()
    if storefront != None:
        params["storefront"] = storefront
    if indie != None:
        params["indie"] = indie
    if limit != None:
        params["limit"] = limit

    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)
