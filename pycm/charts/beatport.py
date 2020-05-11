from .. import utilities

beatport_charts_url = f"/charts/beatport"


def tracks(date):
    """
    Query the charts/beatport/tracks endpoint for the given date.
    Data available on Fridays.

    https://api.chartmetric.com/api/charts/beatport

    :param date:        string date in ISO format %Y-%m-%d

    :return:            list of dictionary of tracks on Beatport charts
    """
    urlhandle = f"{beatport_charts_url}"
    params = {
        "date": date,
        "genre": "top-100",
        "offset": 0,
    }
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)["data"]
