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
we'll roughly adhere to the following design:

ChartMetric() API Base class w/the following children:
    - Album
    - Artist
    - Charts
    - Curator
    - Playlist
    - Track

Each child above provides various (most) methods for a specific endpoint
to the chartmetric.io API.

Example Usage:
```{Python}
>>> from pycm import api
>>> cm = api.ChartMetric()
>>> # spotify charts
>>> cstracks = cm.charts.spotify.tracks(date='2019-01-01', ) 
```
