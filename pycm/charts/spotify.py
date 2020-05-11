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
    Get the top 200 tracks on Spotify chart for the given date.

    https://api.chartmetric.com/api/charts/spotify

    :param date:        string date in ISO format %Y-%m-%d
    :param country:     string two-letter country code
    :param viral:       if True return tracks from Spotify viral chart, 
                        otherwise return those from regional chart

    :return:            list of dictionary of tracks on Spotify chart
    """

    urlhandle = f"{spotify_charts_url}"
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

    :param date:        string date in ISO format %Y-%m-%d,
                        only Thursdays

    :return:            list of dictionary of tracks on Spotify Freshfind
    """
    urlhandle = f"{spotify_charts_url}/freshfind"
    params = {
        "date": date,
    }

    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)
