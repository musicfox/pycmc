from pycm.api import cm
import pycm.utilities as utilities

def tracks(date, country="US", kind="top", genre="all-music"):
    """
    Query the charts/soundcloud/tracks endpoint for the
    given date.

    :param date:        string date in ISO format %Y-%m-%y
    :param country:     string country code, e.g. 'US'
    :param kind:        string 'top' or 'trending'
    :param genre:       string genre (see CM docs)

    :returns:           list of dictionary of Soundcloud
                        chart data
    """
    data = {
        "url": f"{utilities.BaseURL()}/charts/soundcloud/tracks",
        "headers": {"Authorization": f"Bearer {cm.token}"},
        "params": (
            ("code2", country),
            ("date", date),
            ("kind", kind),
            ("genre", genre),
        ),
    }
    return cm._requestGet(data)
