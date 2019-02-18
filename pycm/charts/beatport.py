from pycm.api import cm
import pycm.utilities as utilities

def tracks(date,):
    """
    Query the charts/beatport/tracks endpoint for the
    given date.

    :param date:        string date in ISO format %Y-%m-%y

    :returns:           list of dictionary of Soundcloud
                        chart data
    """
    data = {
        "url": f"{utilities.BaseURL()}/charts/beatport/tracks",
        "headers": {"Authorization": f"Bearer {cm.token}"},
        "params": (("date", date), ("genre", "top-100")),
    }
    return cm._requestGet(data)
