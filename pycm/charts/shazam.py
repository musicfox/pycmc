from pycm.api import cm
import pycm.utilities as utilities

def tracks(date, country="US"):
    """
    Query the charts/shazam/tracks endpoint for the
    given date.

    :param date:        string date in ISO format %Y-%m-%y
    :param country:     string country code, e.g. 'US'

    :returns:           list of dictionary of Soundcloud
                        chart data
    """
    data = {
        "url": f"{utilities.BaseURL()}/charts/shazam/tracks",
        "headers": {"Authorization": f"Bearer {cm.token}"},
        "params": (("code2", country), ("date", date)),
    }
    return cm._requestGet(data)
