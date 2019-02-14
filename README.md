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

