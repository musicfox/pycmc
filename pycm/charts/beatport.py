from .. import utilities

beatport_charts_url = f"/charts/beatport"

def tracks(date):
    """
    Query the charts/beatport/tracks endpoint for the given date.

    https://api.chartmetric.com/api/charts/beatport

    :param date:        string date in ISO format %Y-%m-%y

    :returns:           list of dictionary of Beatport chart data
    """
    urlhandle = f"{beatport_charts_url}"
    params = {
        'date': date,
        'genre': 'top-100',
        'offset': 0,
    }
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)['data']
