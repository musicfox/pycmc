from .. import utilities

itunes_charts_url = f"/charts/itunes"


def albums(date, country="US"):
    """
    Get the top 200 albums on iTunes charts for the given date.

    https://api.chartmetric.com/api/charts/itunes/albums

    **Parameters**

    - `date`:        string date in ISO format %Y-%m-%d

    - `country`:     string country code, e.g. 'US'

    **Returns**            

    A list of dictionary of albums data on iTunes charts.
    """
    urlhandle = f"{itunes_charts_url}/albums"
    params = {
        "country_code": country,
        "date": date,
        "genre": "All Genres",
        "offset": 0,
    }
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)["data"]


def tracks(date, country="US"):
    """
    Get the top 200 tracks on itunes charts for the given date.

    https://api.chartmetric.com/api/charts/itunes/tracks

    **Parameters**

    - `date`:        string date in ISO format %Y-%m-%d

    - `country`:     string country code, e.g. 'US'

    **Returns**            

    A list of dictionary of tracks data on iTunes charts.
    """
    urlhandle = f"{itunes_charts_url}/tracks"
    params = {
        "country_code": country,
        "date": date,
        "genre": "All Genres",
        "offset": 0,
    }
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)["data"]


def videos(date, country="US"):
    """
    Get the top 200 videos on iTunes chart for the given date.

    https://api.chartmetric.com/api/charts/itunes/videos

    **Parameters**

    - `date`:        string date in ISO format %Y-%m-%d

    - `country`:     string country code, e.g. 'US'

    **Returns**            

    A list of dictionary of videos data on iTunes charts.
    """
    urlhandle = f"{itunes_charts_url}/videos"
    params = {
        "country_code": country,
        "date": date,
        "offset": 0,
    }
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)["data"]
