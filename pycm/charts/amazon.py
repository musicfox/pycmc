from .. import utilities

amazon_charts_url = f"/charts/amazon"


def tracks(date, track_type, genre):
    """
    Query the charts/amazon/tracks endpoint for the given date.

    https://api.chartmetric.com/api/charts/amazon/tracks

    :param date:        string date in ISO format %Y-%m-%d
    :param track_type:  string track type,
                        taking 'popular_track' or 'new_track'
    :param genre:       string genre, taking one of the following
                        'All Genres', 'Pop', 'Rock', 'Dance', 
                        'Latino' 'K-Pop', 'Singer/Songwriter', 
                        'Hip-Hop/Rap', 'Jazz', 'Electronic', 
                        'R&B/Soul', 'Blues', 'Country', 'Reggae', 
                        'Classical', 'Alternative', 'World', 
                        'Disney', 'J-Pop', 'Christian & Gospel', 
                        'Easy Listening', 'Children's Music', 
                        'Fitness & Workout', 'Soundtrack'

    :return:            list of dictionary of tracks on Amazon charts
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

    :param date:        string date in ISO format %Y-%m-%d
    :param track_type:  string album type,
                        taking 'popular_album' or 'new_album'
    :param genre:       string genre, taking one of the following
                        'All Genres', 'Pop', 'Rock', 'Dance', 
                        'Latino' 'K-Pop', 'Singer/Songwriter', 
                        'Hip-Hop/Rap', 'Jazz', 'Electronic', 
                        'R&B/Soul', 'Blues', 'Country', 'Reggae', 
                        'Classical', 'Alternative', 'World', 
                        'Disney', 'J-Pop', 'Christian & Gospel', 
                        'Easy Listening', 'Children's Music', 
                        'Fitness & Workout', 'Soundtrack'

    :return:            list of dictionary of albums on Amazon charts
    """
    urlhandle = f"{amazon_charts_url}/albums"
    params = {
        "type": album_type,
        "date": date,
        "genre": genre,
    }

    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)["data"]
