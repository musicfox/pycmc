from . import utilities
import datetime


def albums(cmid):
    """
    # `albums`
    Get the albums for the artist given CMID.

    https://api.chartmetric.com/api/artist/:id/albums

    ## Parameters
    - `cmid`:    string or int Chartmetric artist ID

    ## Returns
    dictionary of artist metatdata
    """
    urlhandle = f"/artist/{cmid}/albums"
    params = None
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)


def cpp_data(cmid, cpp_stat, start_date=None, end_date=None):
    """
    # `cpp_data`
    Get the historical CPP data for the given artist.

    https://api.chartmetric.com/api/artist/:id/cpp

    ## Parameters
    - `cmid`:           string or int Chartmetric artist ID
    - `cpp_stat`:       string CPP statistic to pull, 
                            choose from 'rank', 'score'
    - `start_date`:     string of start data in ISO format
    - `end_date`:       string of end date in ISO format

    ## Returns
    list of dictionaries with the specific CPP statistics for the given artist
    """
    urlhandle = f"/artist/{cmid}/cpp"
    params = {
        "stat": cpp_stat,
        "since": start_date,
        "until": end_date,
    }
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)


def charts(chart_type, cmid, start_date, end_date=None):
    """
    # `charts`
    Get the given type of charts for the artist.

    https://api.chartmetric.com/api/artist/:id/:type/charts

    ## Parameters
    - `chart_type`:     string type of charts to pull, choose from
                            'spotify_viral_daily', 'spotify_viral_weekly',
                            'spotify_top_daily', 'spotify_top_weekly',
                            'applemusic_top', 'applemusic_daily',
                            'applemusic_albums', 'itunes_top',
                            'itunes_albums', 'shazam', 'beatport'
    - `cmid`:           string or int Chartmetric artist ID
    - `start_date`:     string of start data in ISO format
    - `end_date`:       string of end date in ISO format

    ## Returns
    list of dictionaries of specific type of charts for the given artist
    """
    urlhandle = f"/artist/{cmid}/{chart_type}/charts"
    params = {
        "since": start_date,
        "until": end_date if end_date else utilities.strDateToday(),
    }
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)["data"]


def fanmetrics(
    cmid, start_date, end_date="today", dsrc="instagram", valueCol=None
):
    """
    # `fanmetrics`
    Query the Chartmetric API for artist fan metrics.

    https://api.chartmetric.com/api/artist/:id/stat/:source

    ## Parameters
    - `cmid`:        string or int Chartmetric artist ID
    - `start_date`:  string ISO date %Y-%m-%d
    - `dsrc`:        string data source, choose from
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

    - `valueCol`:    None or string specific data field returned, choose from
                        'followers', 'popularity', 'listeners',
                        'talks', 'subscribers'

    ## Returns
    nested dict, {valueCol: [fanmetrics]}, fanmetrics are dictionaries of time-series stats
    """
    if end_date == "today":
        # date w/o timestamp
        end_date = str(datetime.datetime.today()).split(" ")[0]
    urlhandle = f"/artist/{cmid}/stat/{dsrc}"
    params = dict(since=start_date, until=end_date,)
    if valueCol is not None:
        params["field"] = valueCol
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)


def get_artist_ids(id_type, specific_id):
    """
    # `get_artist_ids`
    Get all the linked artist IDs using a given type of ID.

    https://api.chartmetric.com/api/artist/:type/:id/get-ids

    ## Parameters
    - `id_type`:         string type of input ID, choose from
                            'chartmetric', 'spotify', 'itunes', 'deezer'
    - `specific_id`:     specific ID corresponding to the id_type

    ## Returns
    list of dictionaries of linked artist IDs
    """
    urlhandle = f"/artist/{id_type}/{specific_id}/get-ids"
    data = utilities.RequestData(urlhandle, params=None)
    return utilities.RequestGet(data)


def get_artists(filter_field, min_thres, max_thres, offset=0):
    """
    # `get_artists`
    Get the statistics of artists filtered by given metrics.

    https://api.chartmetric.com/api/artist/:type/list

    ## Parameters
    - `id_type`:    string indicating the field for filtering,
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
    - `min_thres`:  minimum threshold for filtering
    - `max_thres`:  maximum threshold for filtering
    - `offset`:     number of offsets to shift the timeframe

    ## Returns
    list of dictionaries of the filtered artists
    """
    urlhandle = f"/artist/{filter_field}/list"
    params = {"min": min_thres, "max": max_thres, "offset": offset}
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)["data"]


def metadata(cmid):
    """
    # `metadata`
    Query the CHartmetric API for artist metadata.

    https://api.chartmetric.com/api/artist/:id

    ## Parameters
    - `cmid`:    string or int Chartmetric artist ID

    ## Returns
    dictionary of artist metatdata
    """
    urlhandle = f"/artist/{cmid}"
    params = None
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)


def playlists(cmid, dsrc, start_date, status="past"):
    """
    # `playlists`
    Get the playlists containing the artist on the
    specific streaming platform.

    https://api.chartmetric.com/api/artist/:id/:type/:status/playlists

    ## Parameters
    - `cmid`:        string or int Chartmetric artist ID
    - `dsrc`:        string data source, choose from
                        'spotify', 'applemusic', or 'deezer'
    - `start_date`:  string ISO date %Y-%m-%d
    - `status`:      string indicating status of pulled playlists,
                        either 'current' or 'past'
    
    ## Returns
    list of dictionaries of playlists on the data source for the given artist
    """
    urlhandle = f"/artist/{cmid}/{dsrc}/{status}/playlists"
    params = {
        "since": start_date,
    }
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)


def related(cmid, limit=50):
    """
    # `related`
    Get the related artists for the given artist.

    https://api.chartmetric.com/api/artist/:id/relatedartists

    ## Parameters
    - `cmid`:    string or int Chartmetric artist ID
    - `limit`:   int number of entries to be returned,
                    maximum acceptable is 50

    ## Returns        
    list of dictionaries of related artists
    """
    urlhandle = f"/artist/{cmid}/relatedartists"
    params = {
        "limit": limit,
    }
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)


def urls(cmid):
    """
    # `urls`
    Query the artist URL endpoint given the chartmetric ID and return
    the streaming/social/service URLs.

    https://api.chartmetric.com/api/artist/:id/urls

    ## Parameters
    - `cmid`:    string or int Chartmetric artist ID 
    
    ##Returns
    dictionary of various URLs for the artist
    """
    urlhandle = f"/artist/{cmid}/urls"
    params = None
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)


def tracks(cmid):
    """
    # `tracks`
    Get the tracks for the given artist.

    https://api.chartmetric.com/api/artist/:id/tracks

    ## Parameters
    - `cmid`:    string or int chartmetric artist ID
    
    ## Returns
    list of dictionaries of the artist's tracks
    """
    urlhandle = f"/artist/{cmid}/tracks"
    params = None
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)


def tunefind(cmid):
    """
    # `tunefind`
    Query the Chartmetric API for artist tunefind data.

    https://api.chartmetric.com/api/artist/:id/tunefind

    ## Parameters
    - `cmid`:    string or int Chartmetric artist ID
    
    ## Returns
    list of dictionaries of tunefind data for the given artist
    """
    urlhandle = f"/artist/{cmid}/tunefind"
    params = None
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)


def listening(cmid, start_date):
    """
    # `listening`
    Query the Chartmetric API for Spotify's WherePeopleListen stats.

    https://api.chartmetric.com/api/artist/:id/where-people-listen

    ## Parameters
    - `cmid`:            string or int chartmetric artist ID
    - `start_date`:      string ISO start date for stats

    ## Returns
    dictionary of top listening cities with stats
    """
    urlhandle = f"/artist/{cmid}/where-people-listen"
    params = {"since": start_date}
    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)
