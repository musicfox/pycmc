"""
Defines methods for obtaining Spotify chart data from the 
chartmetric.io API.
"""
import requests
import json
import pycm.utilities as utilities

spotify_charts_url = f"/charts/spotify"

def tracks(date, country="US", viral=False):
    """
    Query the charts/spotify/tracks endpoint for the
    given date.

    :param date:        string date in ISO format %Y-%m-%y

    :returns:           list of dictionary of spotify chart data
    """

    urlhandle = f"{spotify_charts_url}/tracks/"
    params = {
        'date': date,
        'code2': country,
        'duration': 'daily',
        'type': 'viral' if viral else 'regional',
    }
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)


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
    return utilities.RequestGet(data)
