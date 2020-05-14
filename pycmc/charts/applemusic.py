from .. import utilities

APPLE_MUSIC_CHARTS_URL = f"/charts/applemusic"
FRIDAY = 4


def tracks(date, country="US", genre="All Genres"):
    """
    Query the charts/applemusic/tracks endpoint for the given date.

    https://api.chartmetric.com/api/charts/applemusic/tracks

    **Parameters**

    - `date`:        string date in ISO format %Y-%m-%d

    - `country`:     string country code, e.g. 'US'

    - `genre`:             string genre (see CM docs)

    **Returns**            

    list of dictionary of tracks on AppleMusic charts
    """
    params = {
        "date": date,
        "country_code": country,
        "genre": genre,
        "type": "daily",
        "offset": 0,
    }
    urlhandle = f"{APPLE_MUSIC_CHARTS_URL}/tracks"
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)["data"]


def albums(date, country="US", genre="All Genres"):
    """
    Query the charts/applemusic/albums endpoint for the given date.

    https://api.chartmetric.com/api/charts/applemusic/albums

    **Parameters**

    - `date`:        string date in ISO format %Y-%m-%d

    - `country`:     string country code, e.g. 'US'

    - `genre`:             string genre (see CM docs)


    **Returns**            

    A list of dictionary of albums on AppleMusic charts.
    """
    urlhandle = f"{APPLE_MUSIC_CHARTS_URL}/albums"
    params = {
        "date": date,
        "country_code": country,
        "genre": genre,
    }
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)["data"]


def videos(date, country="US", genre="All Genres"):
    """
    Query the charts/applemusic/videos endpoint for the given date.

    https://api.chartmetric.com/api/charts/applemusic/videos

    **Parameters**

    - `date`:        string date in ISO format %Y-%m-%d

    - `country`:     string country code, e.g. 'US'

    - `genre`:             string genre (see CM docs)

    **Returns**

    A list of dictionary of videos on AppleMusic charts.
    """
    urlhandle = f"{APPLE_MUSIC_CHARTS_URL}/videos"
    params = {
        "date": date,
        "country_code": country,
        "genre": genre,
    }
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)["data"]
