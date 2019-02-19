from .. import utilities

beatport_charts_url = f"/charts/beatport"

def tracks(date,):
    """
    Query the charts/beatport/tracks endpoint for the
    given date.

    :param date:        string date in ISO format %Y-%m-%y

    :returns:           list of dictionary of Soundcloud
                        chart data
    """
    urlhandle = f"{beatport_charts_url}/tracks"
    params = {
        'date': date,
        'genre': 'top-100'
    }
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)
