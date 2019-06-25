# pycm
A Python interface for the`chartmetric.io` API.  

## Usage

`$ pip install --no-cache-dir git+ssh://git@gitlab.com/musicfox/pycm`

## Setup

### as a `git` `submodule`
Do just one of the following:

```
# either one will work, personal preference -- though you should use keys ;-p
git submodule add [-b master] https://github.com/thinkjrs/pycm.git
```

**NOTE:** the option key/value in brackets can be left out entirely  

```{Bash}
git submodule add [-b master] git@github.com:thinkjrs/pycm.git
git submodule init
```

### as a `pip` `package`
```{Bash}
$ git clone git@github.com:thinkjrs/pycm
$ cd pycm
$ conda activate myenv # source activate myenv
$ pip install --user -e .
```

### Authentication

Ensure that you have a `.credentials.json` file in your toplevel project/repo
(the directory into which you cloned this repo) directory containing the
following:  

```{json}
{
    "token":"",
    "scope":"",
    "expires_in":"",
    "refreshtoken":"your-token-here"
}
```
## Design 

To mimic the API design of chartmetric and make our lives easier here,
we'll roughly adhere to the following module design where the `pycm` package 
contains the following modules:  
- `album`
- `artist`
- `charts`
- `curator`
- `playlist`
- `track`
- `credentials`
- `credentials_manager`
- `utilities`

Each module above provides (most) methods for a specific endpoint
to the chartmetric.io API, (mostly) labelled as their GET endpoints.  

For example,
```{Python}
>>> 'API ALBUM META URL' = 'https://api.charmetric.io/api/album/:id'
```
To get an album's metadata just call the metadata function:
```
>>> import pycm
>>> pycm.album.metadata('chartmetricID') # return dict of album metatdata
```

## More Example Usage:

#### Get started
```{Python}
>>> import pycm
```
Yep, that's it. As the great Miles Davis often said, *less is more.*

#### Spotify top charts

Obviously we'll start with the elephant in the room and get the top
charts from Spotify.

*What was the US jamming to on the first day of the new year?*
```{Python}
>>> cstracks = pycm.charts.spotify.tracks(date='2019-01-01', ) 
```
#### Apple Music videos charts 

What videos are charting in Apple Music on the same day as above?
```{Python}
>>> applemusic_vcharts = pycm.charts.itunes.videos(date='2019-01-01')
```
#### Artist metatdata

Let's get some metadata on Post Malone:
```{Python}
>>> post_malone_meta = pycm.artist.metadata(mcid='135326', )
```

### Directory hierarchy reference
```{Bash}
.
├── conftest.py
├── environment.yml
├── LICENSE
├── MANIFEST.in
├── pycm
│   ├── album.py
│   ├── artist.py
│   ├── background.py
│   ├── charts
│   │   ├── applemusic.py
│   │   ├── beatport.py
│   │   ├── itunes.py
│   │   ├── shazam.py
│   │   ├── soundcloud.py
│   │   ├── spotify.py
│   │   └── youtube.py
│   ├── credentials_manager.py
│   ├── credentials.py
│   ├── curator.py
│   ├── __init__.py
│   ├── playlist.py
│   ├── track.py
│   └── utilities.py
├── pycm.egg-info
│   ├── dependency_links.txt
│   ├── PKG-INFO
│   ├── requires.txt
│   ├── SOURCES.txt
│   └── top_level.txt
├── README.md
├── requirements.txt
├── setup.py
└── tests
    ├── conftest.py
    ├── exemplar.py
    ├── README.md
    ├── test_album.py
    ├── test_artist.py
    ├── test_charts.py
    ├── test_credentials_manager.py
    ├── test_credentials.py
    ├── test_curator.py
    ├── test_playlist.py
    ├── test_track.py
    └── test_utilities.py
```
