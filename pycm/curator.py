#import pycm.utilities as utilities
from . import utilities
import requests
import json

def lists(stype, limit=100, offset=0, indie=False, social=True):
    """
    Query the chartmetric.com API curator endpoint.

    https://api.chartmetric.com/api/curator/:streamingType/lists

    :param stype:       string 'spotify', 'applemusic', or 'deezer'
    :param limit:       integer number to return
    :param offset:      integer offset entries to be returned
    :param indie:       boolean True to return non-label
    :param social:      boolean True to return social url data

    :returns:           list of dictionary playlist curator data
    """
    indie = 'true' if indie else 'false'
    social = 'true' if social else 'false'
    urlhandle = f"/curator/{stype}/lists"
    params = {
        'indie': indie, 
        'limit': limit,
        'offset': offset,
        'withSocialUrls': social,
    }
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)

def metadata(cmid, stype):
    urlhandle = f"/curator/{stype}/{cmid}"
    params = None
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)

def playlists(cmid, stype):
    urlhandle = f"/curator/{stype}/{cmid}/playlists"
    params = None
    data = utilities.RequestData(urlhandle, params)
    response = requests.get(
        data['url'], headers=data['headers'], params=data['params']
    )
    if not response.ok:
        response.raise_for_status()
    return json.loads(response.text)
