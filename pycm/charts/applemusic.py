from .. import utilities

charts_apple_music_url = f"/charts/applemusic"

def tracks(date, country='US', genre="All Genres"):
    """
    Query the charts/apple_music/tracks endpoint for the given date.

    https://api.chartmetric.com/api/charts/applemusic/tracks

    :param date:        string date in ISO format %Y-%m-%y
    :param country:     string country code, e.g. 'US'
    :genre:             string genre (see CM docs)

    :returns:           list of dictionary of apple music chart data
    """
    params = {
        "date": date,
        "country_code": country,
        "genre": genre,
        "type": "daily",
        "offset": 0,
    }
    urlhandle = f"{charts_apple_music_url}/tracks"
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)['data']


def albums(date, country="US", genre="All Genres"):
    """
    Query the charts/apple_music/albums endpoint for the given date.

    https://api.chartmetric.com/api/charts/applemusic/albums

    :param date:        string date in ISO format %Y-%m-%y
    :param country:     string country code, e.g. 'US'
    :genre:             string genre (see CM docs)

    :returns:           list of dictionary of apple music chart data
    """
    urlhandle = f"{charts_apple_music_url}/albums"
    params = {
        "date": date,
        "country_code": country,
        "genre": genre,
    }
    data = utilities.RequestData(urlhandle, params) 
    return utilities.RequestGet(data)['data']


def videos(date, country="US", genre="All Genres"):
    """
    Query the charts/apple_music/videos endpoint for the given date.

    https://api.chartmetric.com/api/charts/applemusic/videos

    :param date:        string date in ISO format %Y-%m-%y
    :param country:     string country code, e.g. 'US'
    :genre:             string genre (see CM docs)

    :returns:           list of dictionary of apple music chart data
    """
    urlhandle = f"{charts_apple_music_url}/videos"
    params = {
        "date": date,
        "country_code": country,
        "genre": genre,
    }
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)['data']
