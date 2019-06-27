"""
Defines methods for obtaining Spotify chart data from the 
chartmetric.com API.
"""
import requests
import json
from .. import utilities

spotify_charts_url = f"/charts/spotify"

def tracks(date, country="US", viral=False):
    """
    Query the charts/spotify/tracks endpoint for the
    given date.

    :param date:        string date in ISO format %Y-%m-%y

    :returns:           list of dictionary of spotify chart data
    """

    urlhandle = f"{spotify_charts_url}"
    params = {
        'date': date,
        'country_code': country,
        'type': 'viral' if viral else 'regional',
        'interval': 'daily',
        'offset': 0,
    }
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)['data']


def freshfind(date,):
    """
    Query the charts/spotify/freshfind endpoint for the
    given date.

    :param date:        string date in ISO format %Y-%m-%y

    :returns:           list of dictionary of spotify chart data
    """
    urlhandle = f"{spotify_charts_url}/freshfind"
    params = {
        "date": date,
    }

    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)['data']
