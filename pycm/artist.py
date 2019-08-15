# import pycm.utilities as utilities
from . import utilities


def fanmetrics(cmid, start_date, dsrc="instagram", valueCol="followers"):
    """
    Query the chartmetric API for artist fanmetrics.

    :param cmid:        string chartmetric artist id
    :param start_date:  string ISO date %Y-%m-%d
    :param dsrc:        string data source
                        spotify, facebook, twitter, instagram, youtube,
			wikipedia, bandsintown, soundcloud,
			facebook_fans_by_country, or
			facebook_storytellers_by_country 

    https://api.chartmetric.com/api/artist/:id/stat/:source
    """
    urlhandle = f"/artist/{cmid}/stat/{dsrc}"
    params = {"since": start_date}
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)


def listening(cmid, start_date):
    """
    Query the chartmetric.com API for artist metadata.

    https://api.chartmetric.com/api/artist/:id/spWherePeopleListenInsights

    :param cmid:        string chartmetric artist ID
    :returns:           dict of artist metatdata
    """
    urlhandle = f"/artist/{cmid}/where-people-listen"
    params = {"since": start_date}
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)


def tunefind(cmid):
    """
    Query the chartmetric.com API for artist metadata.

    https://api.chartmetric.com/api/artist/:id/tunefind

    :param cmid:        string chartmetric artist ID
    :returns:           dict of artist metatdata
    """
    urlhandle = f"/artist/{cmid}/tunefind"
    params = None
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)


def albums(cmid):
    """
    Query the chartmetric.com API for artist metadata.

    https://api.chartmetric.com/api/artist/:id/albums

    :param cmid:        string chartmetric artist ID
    :returns:           dict of artist metatdata
    """
    urlhandle = f"/artist/{cmid}/albums"
    params = None
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)


def tracks(cmid):
    """
    Query the chartmetric.com API for artist metadata.

    https://api.chartmetric.com/api/artist/:id/tracks

    :param cmid:        string chartmetric artist ID
    :returns:           dict of artist metatdata
    """
    urlhandle = f"/artist/{cmid}/tracks"
    params = None
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)


def related(cmid, limit=50):
    """
    Query the chartmetric.com API for artist metadata.

    https://api.chartmetric.com/api/artist/:id/relatedartists

    :param cmid:        string chartmetric artist ID
    :param limit:       int number of entries to be returned
    :returns:           list of related artists
    """
    urlhandle = f"/artist/{cmid}/relatedartists"
    params = {
        'limit': limit,
    }
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)


def metadata(cmid):
    """
    Query the chartmetric.com API for artist metadata.

    https://api.chartmetric.com/api/artist/:id

    :param cmid:        string chartmetric artist ID
    :returns:           dict of artist metatdata
    """
    urlhandle = f"/artist/{cmid}"
    params = None
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)


def playlists(cmid, dsrc, start_date, status="past"):
    """
    Query the chartmetric.com API for artist playlist data.

    https://api.chartmetric.com/api/artist/:id/:type/:status/playlists
    :param cmid:        string chartmetric artist id
    :param start_date:  string ISO date %Y-%m-%d
    :param dsrc:        string data source 'spotify', 'applemusic', or 'deezer'

    :returns:           no one knows-> it's chartmetric's API
    """
    urlhandle = f"/artist/{cmid}/{dsrc}/{status}/playlists"
    params = {
        "since": start_date,
        #'indie': False,
    }
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)


def urls(cmid):
    """
    Query the artist url endpoint given the chartmetric ID and return
    the streaming/social service URLs.

    https://api.chartmetric.com/api/artist/:id/urls

    :param cmid:        string chartmetric artist ID 
    :returns:           dict of platform urls for artist
    """
    urlhandle = f"/artist/{cmid}/urls"
    params = None
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)


def cpp_data(cmid, cpp_stat, start_date=None, end_date=None):
    """
    Query the historical CPP data for the given artist.

    https://api.chartmetric.com/api/artist/:id/cpp
    :params cmid: Chartmetric artist ID
    :params cpp_stat: string CPP statistic 'rank', 'score'
    :params start_date: string of start data in ISO format
    :params end_date: string of end date in ISO format
    """
    urlhandle = f"/artist/{cmid}/cpp"
    params = {
        "stat": cpp_stat,
        'since': start_date,
        'until': end_date,
    }
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)


def charts(chart_type, cmid, start_date, end_date=None):
    """
    Query the charts for the artist on the given type of chart.

    https://api.chartmetric.com/api/artist/:id/:type/charts
    :params chart_type:     string of the following
                            'spotify_viral_daily', 'spotify_viral_weekly',
                            'spotify_top_daily', 'spotify_top_weekly',
                            'applemusic_top', 'applemusic_daily',
                            'applemusic_albums', 'itunes_top',
                            'itunes_albums', 'shazam', 'beatport'
    :params cmid:           Chartmetric artist ID
    :params start_date:     string of start data in ISO format
    :params end_date:       string of end date in ISO format
    """
    urlhandle = f"/artist/{cmid}/{chart_type}/charts"
    params = {
        'since': start_date,
        'until': end_date,
    }
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)['data']


def get_artist_ids(id_type, specific_id):
    """
    Query all the linked artist IDs.

    https://api.chartmetric.com/api/artist/:type/:id/get-ids
    :params id_type:          string indicating the type of input id
                              'chartmetric', 'spotify', 'itunes', 'deezer'
    :params specific_id:      specific ID corresponding to the id_type
    """
    urlhandle = f"/artist/{id_type}/{specific_id}/get-ids"
    data = utilities.RequestData(urlhandle, params=None)
    return utilities.RequestGet(data)


def get_artists(filter_field, min_thres, max_thres, offset=0):
    """
    Query the list of artist IDs filtered by given metrics.

    https://api.chartmetric.com/api/artist/:type/list
    :params id_type:        string indicating the field for filtering
                            'sp_monthly_listeners' (spotify monthly listeners),
                            'sp_followers' (spotify followers),
                            'sp_popularity' (spotify popularity),
                            'sp_listeners_to_followers_ratio',
                            'fs_likes' (Facebook fan count),
                            'fs_talks' (Facebook people talking about count),
                            'ycs_views' (Youtube channel views),
                            'ycs_subscribers' (Youtube channel subscribers),
                            'ws_views' (Wikipedia pages views),
                            'ss_followers' (Soundcloud followers)
    :params min:            minimum threshold for filtering
    :params max:            maximum threshold for filtering
    :params offset:         number of offsets to shift the timeframe
    """
    urlhandle = f"/artist/{filter_field}/list"
    params = {
        'min': min_thres, 
        'max': max_thres,
        'offset': offset
    }
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)['data']

