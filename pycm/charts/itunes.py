from .. import utilities
itunes_charts_url = f"/charts/itunes"


def albums(date, country="US"):
    """
    Query the charts/itunes/albums endpoint for the given date.

    https://api.chartmetric.com/api/charts/itunes/albums

    :param date:        string date in ISO format %Y-%m-%d
    :param country:     string country code, e.g. 'US'

    :return:            list of dictionary of albums data on iTunes charts
    """
    urlhandle = f"{itunes_charts_url}/albums"
    params = {
        'country_code': country,
        'date': date,
        'genre': 'All Genres',
        'offset': 0,
    }
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)['data']


def tracks(date, country="US"):
    """
    Query the charts/itunes/tracks endpoint for the given date.

    https://api.chartmetric.com/api/charts/itunes/tracks

    :param date:        string date in ISO format %Y-%m-%d
    :param country:     string country code, e.g. 'US'

    :return:            list of dictionary of tracks data on iTunes charts
    """
    urlhandle = f"{itunes_charts_url}/tracks"
    params = {
        'country_code': country,
        'date': date,
        'genre': 'All Genres',
        'offset': 0,
    }
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)['data']


def videos(date, country="US"):
    """
    Query the charts/itunes/videos endpoint for the given date.

    https://api.chartmetric.com/api/charts/itunes/videos

    :param date:        string date in ISO format %Y-%m-%d
    :param country:     string country code, e.g. 'US'

    :return:            list of dictionary of videos data on iTunes charts
    """
    urlhandle = f"{itunes_charts_url}/videos"
    params = {
        'country_code': country,
        'date': date,
        'offset': 0,
    }
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)['data']


