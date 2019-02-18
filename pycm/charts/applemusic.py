from pycm.api import cm
import pycm.utilities as utilities

def tracks(date, country='US', genre="All Genres"):
    """
    Query the charts/apple_music/tracks endpoint for the
    given date.

    :param date:        string date in ISO format %Y-%m-%y
    :param country:     string country code, e.g. 'US'
    :genre:             string genre (see CM docs)

    :returns:           list of dictionary of apple music chart data
    """
    data = {
        "url": f"{utilities.BaseURL()}/charts/apple_music/tracks",
        "headers": {"Authorization": f"Bearer {cm.token}"},
        "params": (
            ("date", date),
            ("code2", country),
            ("genre", genre),
            ("chart_type", "daily"),
        ),
    }
    return cm._requestGet(data)


def albums(date, country="US", genre="All Genres"):
    """
    Query the charts/apple_music/albums endpoint for the
    given date.

    :param date:        string date in ISO format %Y-%m-%y
    :param country:     string country code, e.g. 'US'
    :genre:             string genre (see CM docs)

    :returns:           list of dictionary of apple music chart data
    """
    data = {
        "url": f"{utilities.BaseURL()}/charts/apple_music/albums",
        "headers": {"Authorization": f"Bearer {cm.token}"},
        "params": (("date", date), ("code2", country), ("genre", genre)),
    }
    return cm._requestGet(data)


def videos(date, country="US", genre="All Genres"):
    """
    Query the charts/apple_music/videos endpoint for the
    given date.

    :param date:        string date in ISO format %Y-%m-%y
    :param country:     string country code, e.g. 'US'
    :genre:             string genre (see CM docs)

    :returns:           list of dictionary of apple music chart data
    """
    data = {
        "url": f"{utilities.BaseURL()}/charts/apple_music/videos",
        "headers": {"Authorization": f"Bearer {cm.token}"},
        "params": (("date", date), ("code2", country), ("genre", genre)),
    }
    return cm._requestGet(data)
