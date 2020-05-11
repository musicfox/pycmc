import requests
import json
from .. import utilities

youtube_charts_url = f"/charts/youtube"


def trends(date, country="US"):
    """
    Get the trends of YouTube chart.
    Data ONLY available on Thursdays.

    https://api.chartmetric.com/api/charts/youtube/trends

    :param date:        string date in ISO format %Y-%m-%d
    :param country:     string country code, e.g. 'US'

    :return:            list of dictionary of trends of YouTube chart
    """
    urlhandle = f"{youtube_charts_url}/trends"
    params = {
        "date": date,
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

    :param date:        string date in ISO format %Y-%m-%d
    :param country:     string country code, e.g. 'US'

    :return:            list of dictionary of videos of YouTube chart
    """
    urlhandle = f"{youtube_charts_url}/videos"
    params = {
        "date": date,
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

    :param date:        string date in ISO format %Y-%m-%d
    :param country:     string country code, e.g. 'US'

    :return:            list of dictionary of artists of YouTube chart
    """
    urlhandle = f"{youtube_charts_url}/artists"
    params = {
        "date": date,
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

    :param date:        string date in ISO format %Y-%m-%d
    :param country:     string country code, e.g. 'US'

    :return:            list of dictionary of tracks of YouTube chart
    """
    urlhandle = f"{youtube_charts_url}/tracks"
    params = {
        "date": date,
        "country_code": country,
        "offset": 0,
    }
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)["data"]
