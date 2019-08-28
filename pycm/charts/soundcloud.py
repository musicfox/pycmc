from .. import utilities 

soundcloud_charts_url = f"/charts/soundcloud"

def tracks(date, country="US", kind="top", genre="all-music"):
    """
    Get the top 200 tracks on SoundCloud chart for the given date.
    Data available ONLY on Fridays.

    https://api.chartmetric.com/api/charts/soundcloud

    :param date:        string date in ISO format %Y-%m-%d
    :param country:     string country code, e.g. 'US'
    :param kind:        string 'top' or 'trending'
    :param genre:       string genre (see CM docs)

    :return:            list of dictionary of tracks on 
                        SoundCloud chart
    """
    urlhandle = f"{soundcloud_charts_url}"
    params = {
        "country_code": country,
        "date": date,
        "kind": kind,
        "genre": genre,
    }
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)['data']
