import requests
import json
import datetime
from .. import utilities
import pandas as pd


YOUTUBE_CHARTS_URL = f"/charts/youtube"
THURSDAY = 3  # datetime lib convention


def trends(date, country="US"):
    """
    Get the trends of YouTube chart.
    Data ONLY available on Thursdays.

    https://api.chartmetric.com/api/charts/youtube/trends

    **Parameters**

    - `date`:        string date in ISO format %Y-%m-%d

    - `country`:     string country code, e.g. 'US'

    **Returns**

    A list of dictionaries of YouTube chart trends.
    """
    urlhandle = f"{YOUTUBE_CHARTS_URL}/trends"
    params = {
        "date": utilities.strWeekday(date, THURSDAY),
        "country_code": country,
        "offset": 0,
    }
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)["data"]


def videos(date, country="US"):
    """
    Get the top 100 videos of YouTube chart.
    Data ONLY available on Thursdays.

    https://api.chartmetric.com/api/charts/youtube/videos

    **Parameters**

    - `date`:        string date in ISO format %Y-%m-%d
    - `country`:     string country code, e.g. 'US'

    **Returns**

    A list of dictionary of videos of YouTube chart.
    """
    urlhandle = f"{YOUTUBE_CHARTS_URL}/videos"
    params = {
        "date": utilities.strWeekday(date, THURSDAY),
        "country_code": country,
        "offset": 0,
    }
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)["data"]


def artists(date, country="US"):
    """
    Get the top 100 artists of YouTube chart.
    Data ONLY available on Thursdays.

    https://api.chartmetric.com/api/charts/youtube/artists

    **Parameters**

    `date`:        string date in ISO format %Y-%m-%d
    `country`:     string country code, e.g. 'US'

    **Returns**

    A list of dictionary of artists of YouTube charts.
    """
    urlhandle = f"{YOUTUBE_CHARTS_URL}/artists"
    params = {
        "date": utilities.strWeekday(date, THURSDAY),
        "country_code": country,
        "offset": 0,
    }
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)["data"]


def tracks(date, country="US"):
    """
    Get the top 100 tracks of YouTube charts.
    Data ONLY available on Thursdays.

    https://api.chartmetric.com/api/charts/youtube/tracks

    **Parameters**

    `date`:        string date in ISO format %Y-%m-%d
    `country`:     string country code, e.g. 'US'

    **Returns**

    A list of dictionary of tracks of YouTube charts.
    """
    urlhandle = f"{YOUTUBE_CHARTS_URL}/tracks"
    params = {
        "date": utilities.strWeekday(date, THURSDAY),
        "country_code": country,
        "offset": 0,
    }
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)["data"]
