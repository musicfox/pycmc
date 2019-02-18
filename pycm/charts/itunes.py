from pycm.api import cm
import pycm.utilities as utilities

def albums(date, country="US"):
    """
    Query the charts/itunes/albums endpoint for the
    given date.

    :param date:        string date in ISO format %Y-%m-%y
    :param country:     string country code, e.g. 'US'
    :returns:           list of dictionary of Soundcloud
                        chart data
    """
    data = {
        "url": f"{utilities.BaseURL()}/charts/itunes/albums",
        "headers": {"Authorization": f"Bearer {cm.token}"},
        "params": (("code2", country), ("date", date), ("genre", "All Genres")),
    }
    return cm._requestGet(data)


def tracks(date, country="US"):
    """
    Query the charts/itunes/tracks endpoint for the
    given date.

    :param date:        string date in ISO format %Y-%m-%y
    :param country:     string country code, e.g. 'US'
    :returns:           list of dictionary of Soundcloud
                        chart data
    """
    data = {
        "url": f"{utilities.BaseURL()}/charts/itunes/tracks",
        "headers": {"Authorization": f"Bearer {cm.token}"},
        "params": (("code2", country), ("date", date), ("genre", "All Genres")),
    }
    return cm._requestGet(data)


def videos(date, country="US"):
    """
    Query the charts/itunes/videos endpoint for the
    given date.

    :param date:        string date in ISO format %Y-%m-%y
    :param country:     string country code, e.g. 'US'
    :returns:           list of dictionary of Soundcloud
                        chart data
    """
    data = {
        "url": f"{utilities.BaseURL()}/charts/itunes/videos",
        "headers": {"Authorization": f"Bearer {cm.token}"},
        "params": (("code2", country), ("date", date)),
    }
    return cm._requestGet(data)
