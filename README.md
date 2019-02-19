# pycm
A Pythonic interface for the`chartmetric.io` api 

## Setup

Ensure that you have a `.credentials.json` file in your toplevel project
directory containing the following:

```{json}
{
    "token":"",
    "scope":"",
    "expires_in":"",
    "refreshtoken":"your-token-here"
}
```
## Example Usage
``` {Python}

>>> import pycm
>>> pycm.api.init('credentials')
>>> post_malone_spotify_popularity = pycm.api.spotify('post malone',
                                                      'popularity',)
```

## Roadmap

To mimic the API design of chartmetric and make our lives easier here,
we'll roughly adhere to the following module design:

`pycm` package w/the following modules:
    - album
    - artist
    - charts
    - curator
    - playlist
    - track
    - credentials
    - credentials_manager
    - utilities

Each module above provides (most) methods for a specific endpoint
to the chartmetric.io API, labelled as their GET endpoints. For example,
```{Python}
>>> 'API ALBUM URL' = 'https://api.charmetric.io/api/album'
```
To get an album's metadata just call the metadata function:
```
>>> import pycm
>>> pycm.album.metadata('chartmetricID') # return dict of album metatdata
```

Some Example Usage:

**Import**
```{Python}
>>> import pycm
```
Yep, that's it. As the great Miles Davis often said, less is more.

**Spotify top charts**
Obviously we'll start with the elephant in the room and get the top
charts from Spotify.

*What was the US jamming to on the first day of the new year?*
```{Python}
>>> # spotify charts
>>> cstracks = pycm.charts.spotify.tracks(date='2019-01-01', ) 
```
**Apple Music videos charts**
What videos are charting in Apple Music on the same day as above?
```{Python}
>>> # itunes videos charts
>>> applemusic_vcharts = pycm.charts.itunes.videos(date='2019-01-01')
```
**Artist metatdata**

Let's get some metadata on Post Malone:
```{Python}
>>> post_malone_meta = pycm.artist.metadata(mcid='135326', )
```
