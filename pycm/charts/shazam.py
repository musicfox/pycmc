from .. import utilities

shazam_charts_url = f"/charts/shazam"

def tracks(date, country="US", city=None):
    """
    Query the charts/shazam/tracks endpoint for the
    given date.

    :param date:        string date in ISO format %Y-%m-%y
    :param country:     string country code, e.g. 'US'

    :returns:           list of dictionary of Soundcloud
                        chart data
    """
    urlhandle = f"{shazam_charts_url}"
    params = {
        'date': date,
        'country_code': country,
        'offset': 0,
    }
    if city != None:
        params['city'] = city
        
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)['data']

def cities(country='US'):
    """
    Query the list of available cities for a given country to be used in city level filtering.

    :param country:     string country code, e.g. 'US'

    :returns:           list of available cities for a given country
    """
    urlhandle = f"{shazam_charts_url}/{country}/cities"
    data = utilities.RequestData(urlhandle, params=None)
    return utilities.RequestGet(data)['cities']