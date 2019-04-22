from .. import utilities 

soundcloud_charts_url = f"/charts/soundcloud"

def tracks(date, country="US", kind="top", genre="all-music"):
    """
    Query the charts/soundcloud/tracks endpoint for the
    given date.

    :param date:        string date in ISO format %Y-%m-%y
    :param country:     string country code, e.g. 'US'
    :param kind:        string 'top' or 'trending'
    :param genre:       string genre (see CM docs)

    :returns:           list of dictionary of Soundcloud
                        chart data
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
