import requests
import json
import pycm.utilities as utilities

youtube_charts_url = f"/charts/youtube"

def trends(date, country="US"):
    """
    Query the charts/youtube/trends endpoint for the
    given date.

    :param date:        string date in ISO format %Y-%m-%y
    :param country:     string country code, e.g. 'US'
    :returns:           list of dictionary of Soundcloud
                        chart data
    """
    urlhandle = f"{youtube_charts_url}/trends"
    params = {
        'date': date,
        'code2': country,
    }
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)


def videos(date, country="US"):
    """
    Query the charts/youtube/videos endpoint for the
    given date.

    :param date:        string date in ISO format %Y-%m-%y
    :param country:     string country code, e.g. 'US'
    :returns:           list of dictionary of Soundcloud
                        chart data
    """

    urlhandle = f"{youtube_charts_url}/videos"
    params = {
        'date': date,
        'code2': country,
    }
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)


def artists(date, country="US"):
    """
    Query the charts/youtube/artists endpoint for the
    given date.

    :param date:        string date in ISO format %Y-%m-%y
    :param country:     string country code, e.g. 'US'
    :returns:           list of dictionary of Soundcloud
                        chart data
    """

    urlhandle = f"{youtube_charts_url}/artists"
    params = {
        'date': date,
        'code2': country,
    }
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)


def tracks(date, country="US"):
    """
    Query the charts/youtube/tracks endpoint for the
    given date.

    :param date:        string date in ISO format %Y-%m-%y
    :param country:     string country code, e.g. 'US'
    :returns:           list of dictionary of Soundcloud
                        chart data
    """
    urlhandle = f"{youtube_charts_url}/tracks"
    params = {
        'date': date,
        'code2': country,
    }
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)
