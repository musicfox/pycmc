from .. import utilities

shazam_charts_url = f"/charts/shazam"


def tracks(date, country="US", city=None):
    """
    # `tracks`
    Get the top 200 tracks on Shazam chart for the given date.

    https://api.chartmetric.com/api/charts/shazam

    - `date`:        string date in ISO format %Y-%m-%d
    - `country`:     string country code, e.g. 'US'

    ## Returns            
    list of dictionary of tracks on Shazam chart
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
    # `cities`
    Get the list of available cities for a given country
    for use in city level filtering.

    https://api.chartmetric.com/api/charts/shazam/:country_code/cities

    ## Parameters
    - `country`:     string country code, e.g. 'US'

    ## Return            
    list of available cities for a given country
    """
    urlhandle = f"{shazam_charts_url}/{country}/cities"
    data = utilities.RequestData(urlhandle, params=None)
    return utilities.RequestGet(data)["cities"]
