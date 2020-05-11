from .. import utilities

shazam_charts_url = f"/charts/shazam"


def tracks(date, country="US", city=None):
    """
    Get the top 200 tracks on Shazam chart for the given date.

    https://api.chartmetric.com/api/charts/shazam

    :param date:        string date in ISO format %Y-%m-%d
    :param country:     string country code, e.g. 'US'

    :return:            list of dictionary of tracks on Shazam chart
    """
    urlhandle = f"{shazam_charts_url}"
    params = {
        "date": date,
        "country_code": country,
        "offset": 0,
    }
    if city != None:
        params["city"] = city

    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)["data"]


def cities(country="US"):
    """
    Get the list of available cities for a given country
    for use in city level filtering.

    https://api.chartmetric.com/api/charts/shazam/:country_code/cities

    :param country:     string country code, e.g. 'US'

    :return:            list of available cities for a given country
    """
    urlhandle = f"{shazam_charts_url}/{country}/cities"
    data = utilities.RequestData(urlhandle, params=None)
    return utilities.RequestGet(data)["cities"]
