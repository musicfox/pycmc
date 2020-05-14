from .. import utilities

BEATPORT_CHARTS_URL = f"/charts/beatport"
FRIDAY = 4


def tracks(date):
    """
    Query the charts/beatport/tracks endpoint for the given date.
    Data available on Fridays.

    https://api.chartmetric.com/api/charts/beatport

    **Parameters**

    - `date`:        string date in ISO format %Y-%m-%d

    **Returns**            

    A list of dictionary of tracks on Beatport charts.
    """
    urlhandle = f"{BEATPORT_CHARTS_URL}"
    params = {
        "date": utilities.strWeekday(date, FRIDAY),
        "genre": "top-100",
        "offset": 0,
    }
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)["data"]
