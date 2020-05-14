# import pycm.utilities as utilities
from . import utilities
import requests
import json


def lists(stype, limit=100, offset=0, indie=False, social=True):
    """
    Get the chart of curators on the given streaming platfrorm.

    https://api.chartmetric.com/api/curator/:platform/lists

    **Parameters**

    - `stype`:       string streaming platform, choose from
    
        'spotify', 'applemusic', or 'deezer'

    - `limit`:       int number of entries returned; maximum acceptable is 100

    - `offset`:      int offset of entries returned

    - `indie`:       boolean True to return the charts not curated by major labels
    - `social`:      boolean True to return social url data

    **Returns**
    
    A Python list of dictionaries of curators.
    """
    indie = "true" if indie else "false"
    social = "true" if social else "false"
    urlhandle = f"/curator/{stype}/lists"
    params = {
        "indie": indie,
        "limit": limit,
        "offset": offset,
        "withSocialUrls": social,
    }
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)


def metadata(cmid, stype):
    """
    Get the metadata for the curator on a given streaming platform.

    https://api.chartmetric.com/api/curator/:platform/:id/

    **Parameters**

    - `cmid`:        string or int Chartmetric curator ID

    - `stype`:       string streaming platform, choose from

        'spotify', 'applemusic', 'deezer'

    **Returns**

    A dictionary of curator metadata.
    """
    urlhandle = f"/curator/{stype}/{cmid}"
    params = None
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)


def playlists(cmid, stype):
    """
    Get the playlists by the curator on the given streaming platform.

    https://api.chartmetric.com/api/curator/:platform/:id/playlists
    
    **Parameters**

    - `cmid`:        string or in Chartmetric curator ID

    - `stype`:       string streaming platform, choose from

        'spotify', 'applemusic', 'deezer'

    **Returns**

    A Python list of dictionaries of playlist by the curator
    """
    urlhandle = f"/curator/{stype}/{cmid}/playlists"
    params = None
    data = utilities.RequestData(urlhandle, params)
    response = requests.get(
        data["url"], headers=data["headers"], params=data["params"]
    )
    if not response.ok:
        response.raise_for_status()
    return json.loads(response.text)
