from .. import utilities

SOUNDCLOUD_CHARTS_URL = f"/charts/soundcloud"
FRIDAY = 4


def tracks(date, country="US", kind="top", genre="all-music"):
    """
    Get the top 200 tracks on SoundCloud chart for the given date.
    Data available ONLY on Fridays.

    https://api.chartmetric.com/api/charts/soundcloud

    **Parameters**

    - `date`:        string date in ISO format %Y-%m-%d

    - `country`:     string country code, e.g. 'US'

    - `kind`:        string 'top' or 'trending'

    - `genre`:       string genre (see CM docs)

    **Returns**

    A list of dictionary of tracks on SoundCloud chart.
    """
    urlhandle = f"{SOUNDCLOUD_CHARTS_URL}"
    params = {
        "country_code": country,
        "date": utilities.strWeekday(date, FRIDAY),
        "kind": kind,
        "genre": genre,
    }
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)["data"]
