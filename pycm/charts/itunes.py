from .. import utilities
itunes_charts_url = f"/charts/itunes"

def albums(date, country="US"):
    """
    Query the charts/itunes/albums endpoint for the
    given date.

    :param date:        string date in ISO format %Y-%m-%y
    :param country:     string country code, e.g. 'US'
    :returns:           list of dictionary of Soundcloud
                        chart data
    """
    urlhandle = f"{itunes_charts_url}/albums"
    params = {
        'code2': country,
        'date': date,
        'genre': 'All Genres',
    }
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)


def tracks(date, country="US"):
    """
    Query the charts/itunes/tracks endpoint for the
    given date.

    :param date:        string date in ISO format %Y-%m-%y
    :param country:     string country code, e.g. 'US'
    :returns:           list of dictionary of Soundcloud
                        chart data
    """
    urlhandle = f"{itunes_charts_url}/tracks"
    params = {
        'code2': country,
        'date': date,
        'genre': 'All Genres',
    }
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)


def videos(date, country="US"):
    """
    Query the charts/itunes/videos endpoint for the
    given date.

    :param date:        string date in ISO format %Y-%m-%y
    :param country:     string country code, e.g. 'US'
    :returns:           list of dictionary of Soundcloud
                        chart data
    """
    urlhandle = f"{itunes_charts_url}/videos"
    params = {
        'code2': country,
        'date': date,
    }
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)


