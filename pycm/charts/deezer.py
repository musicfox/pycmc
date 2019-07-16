from .. import utilities

deezer_music_url = f"/charts/deezer"

def insights(date, country='US'):
    """
    Query the charts/deezer/ endpoint for the
    given date.

    :param date:        string date in ISO format %Y-%m-%y
    :param country:     string country code

    :returns:           list of dictionary of Deezer music data insights
    """
    urlhandle = f"{deezer_music_url}/"
    params = {
        "country_code": country,
        "date": date,
    }

    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)['data']
