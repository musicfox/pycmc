from . import utilities
import datetime


def albums(cmid):
    """
    Get the albums for the artist given CMID.

    https://api.chartmetric.com/api/artist/:id/albums

    :param cmid:    string or int Chartmetric artist ID

    :return:        dictionary of artist metatdata
    """
    urlhandle = f"/artist/{cmid}/albums"
    params = None
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)


def cpp_data(cmid, cpp_stat, start_date=None, end_date=None):
    """
    Get the historical CPP data for the given artist.

    https://api.chartmetric.com/api/artist/:id/cpp

    :params cmid:           string or int Chartmetric artist ID
    :params cpp_stat:       string CPP statistic to pull, 
                            choose from 'rank', 'score'
    :params start_date:     string of start data in ISO format
    :params end_date:       string of end date in ISO format

    :return:                list of dictionaries with the specific 
                            CPP statistics for the given artist
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
    Get the given type of charts for the artist.

    https://api.chartmetric.com/api/artist/:id/:type/charts

    :params chart_type:     string type of charts to pull, choose from
                            'spotify_viral_daily', 'spotify_viral_weekly',
                            'spotify_top_daily', 'spotify_top_weekly',
                            'applemusic_top', 'applemusic_daily',
                            'applemusic_albums', 'itunes_top',
                            'itunes_albums', 'shazam', 'beatport'
    :params cmid:           string or int Chartmetric artist ID
    :params start_date:     string of start data in ISO format
    :params end_date:       string of end date in ISO format

    :return:                list of dictionaries of specific type of 
                            charts for the given artist
    """
    urlhandle = f"/artist/{cmid}/{chart_type}/charts"
    params = {
        'since': start_date,
        'until': end_date,
    }
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)['data']


def fanmetrics(
    cmid,
    start_date,
    end_date="today",
    dsrc="instagram",
    valueCol=None
):
    """
    Query the Chartmetric API for artist fan metrics.

    https://api.chartmetric.com/api/artist/:id/stat/:source

    :param cmid:        string or int Chartmetric artist ID
    :param start_date:  string ISO date %Y-%m-%d
    :param dsrc:        string data source, choose from
                        'spotify', 'facebook', 'twitter', 'instagram',
                        'youtube_channel', 'wikipedia', 
                        'bandsintown', 'soundcloud',
                        
                        Valid keys/fields from 
                            api.chartmetric.com/apidoc/#api-Artist-GetArtistorStat

                        spotify - followers, popularity, listeners
                        deezer - fans
                        facebook - likes, talks (This data might be outdated)
                        twitter - followers
                        youtube_channel - subscribers, views, comments, 
                            videos (this refers to the artist channel only)
                        youtube_artist - views (this includes artist channel
                            and all other videos featuring artist music)
                        instagram - followers
                        wikipedia - views
                        bandsintown - followers
                        soundcloud - followers

    :param valueCol:    None or string specific data field returned, choose from
                        'followers', 'popularity', 'listeners',
                        'talks', 'subscribers'

    :return:            nested dict, {valueCol: [fanmetrics]},
                        fanmetrics are dictionaries of time-series stats
    """
    if end_date == 'today':
        # date w/o timestamp
        end_date = str(datetime.datetime.today()).split(' ')[0]
    urlhandle = f"/artist/{cmid}/stat/{dsrc}"
    params = dict(
        since=start_date,
        until=end_date,
    )
    if valueCol is not None:
        params['field'] = valueCol
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)


def get_artist_ids(id_type, specific_id):
    """
    Get all the linked artist IDs using a given type of ID.

    https://api.chartmetric.com/api/artist/:type/:id/get-ids

    :param id_type:         string type of input ID, choose from
                            'chartmetric', 'spotify', 'itunes', 'deezer'
    :param specific_id:     specific ID corresponding to the id_type

    :return:                list of dictionaries of linked artist IDs
    """
    urlhandle = f"/artist/{id_type}/{specific_id}/get-ids"
    data = utilities.RequestData(urlhandle, params=None)
    return utilities.RequestGet(data)


def get_artists(filter_field, min_thres, max_thres, offset=0):
    """
    Get the statistics of artists filtered by given metrics.

    https://api.chartmetric.com/api/artist/:type/list

    :params id_type:    string indicating the field for filtering,
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
    :params min_thres:  minimum threshold for filtering
    :params max_thres:  maximum threshold for filtering
    :params offset:     number of offsets to shift the timeframe

    :return:            list of dictionaries of the filtered artists
    """
    urlhandle = f"/artist/{filter_field}/list"
    params = {
        'min': min_thres, 
        'max': max_thres,
        'offset': offset
    }
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)['data']


def metadata(cmid):
    """
    Query the CHartmetric API for artist metadata.

    https://api.chartmetric.com/api/artist/:id

    :param cmid:    string or int Chartmetric artist ID

    :return:        dictionary of artist metatdata
    """
    urlhandle = f"/artist/{cmid}"
    params = None
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)


def playlists(cmid, dsrc, start_date, status="past"):
    """
    Get the playlists containing the artist on the
    specific streaming platform.

    https://api.chartmetric.com/api/artist/:id/:type/:status/playlists

    :param cmid:        string or int Chartmetric artist ID
    :param dsrc:        string data source, choose from
                        'spotify', 'applemusic', or 'deezer'
    :param start_date:  string ISO date %Y-%m-%d
    :param status:      string indicating status of pulled playlists,
                        either 'current' or 'past'
    
    :return:            list of dictionaries of playlists on the data source
                        for the given artist
    """
    urlhandle = f"/artist/{cmid}/{dsrc}/{status}/playlists"
    params = {
        "since": start_date,
    }
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)


def related(cmid, limit=50):
    """
    Get the related artists for the given artist.

    https://api.chartmetric.com/api/artist/:id/relatedartists

    :param cmid:    string or int Chartmetric artist ID
    :param limit:   int number of entries to be returned,
                    maximum acceptable is 50

    :return:        list of dictionaries of related artists
    """
    urlhandle = f"/artist/{cmid}/relatedartists"
    params = {
        'limit': limit,
    }
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)


def urls(cmid):
    """
    Query the artist URL endpoint given the chartmetric ID and return
    the streaming/social/service URLs.

    https://api.chartmetric.com/api/artist/:id/urls

    :param cmid:    string or int Chartmetric artist ID 
    
    :return:        dictionary of various URLs for the artist
    """
    urlhandle = f"/artist/{cmid}/urls"
    params = None
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)


def tracks(cmid):
    """
    Get the tracks for the given artist.

    https://api.chartmetric.com/api/artist/:id/tracks

    :param cmid:    string or int chartmetric artist ID
    
    :return:        list of dictionaries of the artist's tracks
    """
    urlhandle = f"/artist/{cmid}/tracks"
    params = None
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)


def tunefind(cmid):
    """
    Query the Chartmetric API for artist tunefind data.

    https://api.chartmetric.com/api/artist/:id/tunefind

    :param cmid:    string or int Chartmetric artist ID
    
    :return:        list of dictionaries of tunefind data
                    for the given artist
    """
    urlhandle = f"/artist/{cmid}/tunefind"
    params = None
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)


def listening(cmid, start_date):
    """
    Query the Chartmetric API for Spotify's WherePeopleListen stats.

    https://api.chartmetric.com/api/artist/:id/where-people-listen

    :param cmid:            string or int chartmetric artist ID
    :param start_date:      string ISO start date for stats

    :return:                dictionary of top listening cities with stats
    """
    urlhandle = f"/artist/{cmid}/where-people-listen"
    params = {"since": start_date}
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)
