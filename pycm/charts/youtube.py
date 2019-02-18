import requests
import json
from pycm.api import cm
import pycm.utilities as utilities

def trends(date, country="US"):
    """
    Query the charts/youtube/trends endpoint for the
    given date.

    :param date:        string date in ISO format %Y-%m-%y
    :param country:     string country code, e.g. 'US'
    :returns:           list of dictionary of Soundcloud
                        chart data
    """
    data = {
        "url": f"{utilities.BaseURL()}/charts/youtube/trends",
        "headers": {"Authorization": f"Bearer {cm.token}"},
        "params": (("date", date), ("code2", country)),
    }
    return cm._requestGet(data)


def videos(date, country="US"):
    """
    Query the charts/youtube/videos endpoint for the
    given date.

    :param date:        string date in ISO format %Y-%m-%y
    :param country:     string country code, e.g. 'US'
    :returns:           list of dictionary of Soundcloud
                        chart data
    """
    data = {
        "url": f"{utilities.BaseURL()}/charts/youtube/videos",
        "headers": {"Authorization": f"Bearer {cm.token}"},
        "params": (("code2", country), ("date", date)),
    }
    return cm._requestGet(data)


def artists(date, country="US"):
    """
    Query the charts/youtube/artists endpoint for the
    given date.

    :param date:        string date in ISO format %Y-%m-%y
    :param country:     string country code, e.g. 'US'
    :returns:           list of dictionary of Soundcloud
                        chart data
    """
    data = {
        "url": f"{utilities.BaseURL()}/charts/youtube/artists",
        "headers": {"Authorization": f"Bearer {cm.token}"},
        "params": (("code2", country), ("date", date)),
    }
    return cm._requestGet(data)


def tracks(date, country="US"):
    """
    Query the charts/youtube/tracks endpoint for the
    given date.

    :param date:        string date in ISO format %Y-%m-%y
    :param country:     string country code, e.g. 'US'
    :returns:           list of dictionary of Soundcloud
                        chart data
    """
    data = {
        "url": f"{utilities.BaseURL()}/charts/youtube/tracks",
        "headers": {"Authorization": f"Bearer {cm.token}"},
        "params": (("date", date), ("code2", country)),
    }
    response = requests.get(
        data["url"], headers=data["headers"], params=data["params"]
    )
    if not response.ok:  # raise internal exception if bad response
        response.raise_for_status()
    return json.loads(response.text)

    return cm._requestGet(data)
