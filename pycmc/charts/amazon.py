from .. import utilities

amazon_charts_url = f"/charts/amazon"


def tracks(date, track_type, genre):
    """
    Query the charts/amazon/tracks endpoint for the given date.

    https://api.chartmetric.com/api/charts/amazon/tracks

    **Parameters**

    - `date`:        string date in ISO format %Y-%m-%d

    - `track_type`:  string track type,

                        taking 'popular_track' or 'new_track'

    - `genre`:       string genre, taking one of the following
                        'All Genres', 'Pop', 'Rock', 'Dance', 
                        'Latino' 'K-Pop', 'Singer/Songwriter', 
                        'Hip-Hop/Rap', 'Jazz', 'Electronic', 
                        'R&B/Soul', 'Blues', 'Country', 'Reggae', 
                        'Classical', 'Alternative', 'World', 
                        'Disney', 'J-Pop', 'Christian & Gospel', 
                        'Easy Listening', 'Children's Music', 
                        'Fitness & Workout', 'Soundtrack'

    **Returns**            

    list of dictionary of tracks on Amazon charts
    """
    urlhandle = f"{amazon_charts_url}/tracks"
    params = {
        "type": track_type,
        "date": date,
        "genre": genre,
    }

    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)["data"]


def albums(date, album_type, genre):
    """
    Query the charts/amazon/albums endpoint for the given date.

    https://api.chartmetric.com/api/charts/amazon/albums

    **Parameters**

    - `date`:        string date in ISO format %Y-%m-%d
    - `track_type`:  string album type,
                        taking 'popular_album' or 'new_album'
    - `genre`:       string genre, taking one of the following
                        'All Genres', 'Pop', 'Rock', 'Dance', 
                        'Latino' 'K-Pop', 'Singer/Songwriter', 
                        'Hip-Hop/Rap', 'Jazz', 'Electronic', 
                        'R&B/Soul', 'Blues', 'Country', 'Reggae', 
                        'Classical', 'Alternative', 'World', 
                        'Disney', 'J-Pop', 'Christian & Gospel', 
                        'Easy Listening', 'Children's Music', 
                        'Fitness & Workout', 'Soundtrack'

    **Returns**

    A list of dictionary of albums on Amazon charts.
    """
    urlhandle = f"{amazon_charts_url}/albums"
    params = {
        "type": album_type,
        "date": date,
        "genre": genre,
    }

    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)["data"]
