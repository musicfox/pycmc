from .. import utilities

shazam_charts_url = f"/charts/shazam"

def tracks(date, country="US"):
    """
    Query the charts/shazam/tracks endpoint for the
    given date.

    :param date:        string date in ISO format %Y-%m-%y
    :param country:     string country code, e.g. 'US'

    :returns:           list of dictionary of Soundcloud
                        chart data
    """
    urlhandle = f"{shazam_charts_url}/tracks"
    params = {
        'code2': country,
        'date': date,
    }
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)
