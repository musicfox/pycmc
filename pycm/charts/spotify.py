"""
Defines methods for obtaining Spotify chart data from the 
chartmetric.io API.
"""
import requests
import json
import pycm.utilities as utilities
from pycm.api import cm


def tracks(date, country="US", viral=False):
    """
    Query the charts/spotify/tracks endpoint for the
    given date.

    :param date:        string date in ISO format %Y-%m-%y

    :returns:           list of dictionary of spotify chart data
    """
    data = cm._requestData(
        "/charts/spotify/tracks",
        date,
        country,
        "viral" if viral else "regional",
    )
    return cm._requestGet(data)


def freshfind(date,):
    """
    Query the charts/spotify/freshfind endpoint for the
    given date.

    :param date:        string date in ISO format %Y-%m-%y

    :returns:           list of dictionary of spotify chart data
    """
    data = {
        "url": f"{utilities.BaseURL()}/charts/spotify/freshfind",
        "headers": {"Authorization": f"Bearer {cm.token}"},
        "params": (("date", date),),
    }
    response = requests.get(
        data["url"], headers=data["headers"], params=data["params"]
    )
    if not response.ok:  # raise internal exception if bad response
        response.raise_for_status()
    return json.loads(response.text)
