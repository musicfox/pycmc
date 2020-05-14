from . import utilities
import datetime
import logging


def charts(stype, cmid, start_date, end_date=None):
    """
    Query the charts for the given album of a selected streamer type. 

    https://api.chartmetric.com/api/album/:id/:type/charts
    
    **Parameters**

    - `stype`:           string streaming platform, choose from
                        'applemusic', 'itunes' or 'amazon'

    - `cmid`:            string or int chartmetric album ID

    - `start_date`:      string start data in ISO format

    - `end_date`:        string end date in ISO format

    **Returns**              

    A list of dictionaries of the chart for the given album.
    """
    logging.info(
        f"This is known to have authentication issues when "
        f"(we suspect) dates as given are invalid. You may experience "
        f"intermittent HTTPErrors (403). Adjust dates as necessary to fix."
    )
    # strDateToday = lambda: str(datetime.datetime.today()).split(' ')[0]

    urlhandle = f"/album/{cmid}/{stype}/charts"
    params = {
        "since": start_date,
        "until": end_date
        if isinstance(end_date, str)
        else utilities.strDateToday(),
    }
    data = utilities.RequestData(urlhandle, params=params)
    return utilities.RequestGet(data)["data"]


def get_album_ids(id_type, specific_id):
    """
    Query all the related album IDs given a specific ID type.

    https://api.chartmetric.com/api/album/:type/:id/get-ids

    **Parameters**

    - `id_type`:         string of the type of ID, choose from
                         'chartmetric', 'upc', 'spotify', 'itunes', 'deezer'

    - `specific_id`:     specific ID corresponding to the id_type
    
    **Returns**

    A list of dictionaries with various types of ID.
    """
    urlhandle = f"/album/{id_type}/{specific_id}/get-ids"
    data = utilities.RequestData(urlhandle, params=None)
    return utilities.RequestGet(data)


def metadata(cmid):
    """
    Query the album metadata endpoint given the chartmetric ID. 
    
    https://api.chartmetric.com/api/album/:id

    **Parameters**

    - `cmid`:        string or int Chartmetric album ID

    **Returns**            

    A dictionary of album metadata.
    """
    urlhandle = f"/album/{cmid}"
    data = utilities.RequestData(urlhandle, params=None)
    return utilities.RequestGet(data)


def playlists(
    cmid,
    start_date,
    end_date=None,
    stype="spotify",
    status="current",
    indie=False,
    limit=100,
):
    """
    Query the album playlist placement API endpoint.

    https://api.chartmetric.com/api/album/:id/:platform/:status/playlists

    **Parameters**

    - `cmid`:        string or int Chartmetric album ID

    - `start_date`:  string ISO date

    - `end_date`:    string ISO date

    - `stype`:       string streaming platform, choose from 'spotify, 'applemusic', or 'deezer'

    - `status`:      string 'current' or 'past'

    - `indie`:       Boolean true if playlist created by major labels

    - `limit`:       int number of entries to be returned, maximum acceptable is 100

    **Returns**

    A list of dictionaries of playlists for the album.
    """
    urlhandle = f"/album/{cmid}/{stype}/{status}/playlists"
    params = {
        "since": start_date,
        "until": end_date,
        "limit": limit,
        "offset": 0,
    }
    data = utilities.RequestData(urlhandle, params=params)
    return utilities.RequestGet(data)


def stats(cmid, stype, start_date=None, end_date=None):
    """
    Query the statistics from the given streaming platform,
    specifically popularity for Spotify.

    https://api.chartmetric.com/api/album/:id/:platform/stats
    
    **Parameters**

    - `cmid`:        string or int Chartmetric album ID

    - `stype`:       string streaming platform type, only 'spotify'

    - `start_date`:  string of start date in ISO format

    - `end_date`:    string of end date in ISO format

    **Returns**

    A list of dictionaries of the statistics for an album on a streaming platform.
    """
    urlhandle = f"/album/{cmid}/{stype}/stats"
    params = {
        "since": start_date,
        "until": end_date,
    }
    data = utilities.RequestData(urlhandle, params=params)
    return utilities.RequestGet(data)


def tracks(cmid):
    """
    Query the tracks included in a given album.

    https://api.chartmetric.com/api/album/:id/tracks

    **Parametrs**

    - `cmid`:   string or int Chartmetric album ID
   
    **Returns**

    A list of dictionaries of the tracks in an album.
    """
    urlhandle = f"/album/{cmid}/tracks"
    data = utilities.RequestData(urlhandle, params=None)
    return utilities.RequestGet(data)


def tunefind(cmid):
    """
    Query the album tunefind stats given the Chartmetric ID.

    https://api.chartmetric.com/api/album/:id/tunefind

    **Parameters**

    - `cmid`:    string or int Chartmetric album ID

    **Returns**

    A list of dictionaries of tunefind stats.
    """
    urlhandle = f"/album/{cmid}/tunefind"
    data = utilities.RequestData(urlhandle, params=None)
    return utilities.RequestGet(data)
