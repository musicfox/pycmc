from .. import utilities

deezer_music_url = f"/charts/deezer"


def insights(date, country="US"):
    """
    Get the top 100 Deezer chart tracks for the given date

    https://api.chartmetric.com/api/charts/deezer/

    **Parameters**

    - `date`:        string date in ISO format %Y-%m-%d

    - `country`:     string country code

    **Returns**            

    A list of dictionary of tracks on Deezer chart.
    """
    urlhandle = f"{deezer_music_url}/"
    params = {
        "country_code": country,
        "date": date,
    }

    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)["data"]
