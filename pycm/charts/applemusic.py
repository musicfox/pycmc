import pycm.utilities as utilities

charts_apple_music_url = f"/charts/apple_music"

def tracks(date, country='US', genre="All Genres"):
    """
    Query the charts/apple_music/tracks endpoint for the
    given date.

    :param date:        string date in ISO format %Y-%m-%y
    :param country:     string country code, e.g. 'US'
    :genre:             string genre (see CM docs)

    :returns:           list of dictionary of apple music chart data
    """
    params = {
        "date": date,
        "code2": country,
        "genre": genre,
        "chart_type": "daily",
    }
    urlhandle = f"{charts_apple_music_url}/tracks"
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)


def albums(date, country="US", genre="All Genres"):
    """
    Query the charts/apple_music/albums endpoint for the
    given date.

    :param date:        string date in ISO format %Y-%m-%y
    :param country:     string country code, e.g. 'US'
    :genre:             string genre (see CM docs)

    :returns:           list of dictionary of apple music chart data
    """
    urlhandle = f"{charts_apple_music_url}/albums"
    params = {
        "date": date,
        "code2": country,
        "genre": genre,
    }
    data = utilities.RequestData(urlhandle, params) 
    return utilities.RequestGet(data)


def videos(date, country="US", genre="All Genres"):
    """
    Query the charts/apple_music/videos endpoint for the
    given date.

    :param date:        string date in ISO format %Y-%m-%y
    :param country:     string country code, e.g. 'US'
    :genre:             string genre (see CM docs)

    :returns:           list of dictionary of apple music chart data
    """
    urlhandle = f"{charts_apple_music_url}/videos"
    params = {
        "date": date,
        "code2": country,
        "genre": genre,
    }
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)
