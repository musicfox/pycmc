# pycm
A Pythonic interface for the`chartmetric.io` api 

## Example Usage
``` {Python}

>>> import pycm
>>> pycm.api.init('credentials')
>>> post_malone_spotify_popularity = pycm.api.spotify('post malone',
                                                      'popularity',)
```

