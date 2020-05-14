"""
Defines methods for obtaining Spotify chart data from the 
chartmetric.com API.
"""
import requests
import json
from .. import utilities


THURSDAY = 3
SPOTIFY_CHARTS_URL = f"/charts/spotify"


def tracks(date, country="US", viral=False):
    """
    Get the top 200 tracks on Spotify chart for the given date.

    https://api.chartmetric.com/api/charts/spotify

    **Parameters**

    - `date`:        string date in ISO format %Y-%m-%d

    - `country`:     string two-letter country code

    - `viral`:       if True return tracks from Spotify viral chart, otherwise return those from regional chart

    **Returns**

    A list of dictionary of tracks on Spotify chart.
    """

    urlhandle = f"{SPOTIFY_CHARTS_URL}"
    params = {
        "date": date,
        "country_code": country,
        "type": "viral" if viral else "regional",
        "interval": "daily",
        "offset": 0,
    }
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)["data"]


def freshfind(date):
    """
    Get the tracks from the Spotify Freshfind chart
    for the given date.
    Data available ONLY on Thursdays.

    https://api.chartmetric.com/api/charts/spotify/freshfind

    **Parameters**

    - `date`:        string date in ISO format %Y-%m-%d, only Thursdays

    **Returns**

    A list of dictionary of tracks on Spotify Freshfind.
    """
    urlhandle = f"{SPOTIFY_CHARTS_URL}/freshfind"
    params = {
        "date": utilities.strWeekday(date, THURSDAY),
    }

    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)
