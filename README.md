[![pycmc heading image from Musicfox](https://storage.googleapis.com/musicfox-github/pycmc-header.png)](https://pycmc.docs.musicfox.io)

# `pycmc` Python Chartmetric Client
[![codecov](https://codecov.io/gh/musicfox/pycmc/branch/develop/graph/badge.svg?token=COEMV82GV9)](https://codecov.io/gh/musicfox/pycmc)

A Python client for the Chartmetric API. Query artists, their music,
and where their fans listen, by [Musicfox](https://musicfox.io).

And do it all in Python.

## Installation
We highly recommend you install [`pycmc`](https://github.com/musicfox/pycmc)
into some type of [virtual environment](https://docs.python.org/3/library/venv.html).

Then you should use pip or the like:
```python
pip install pycmc
```
_or_
```python
pipenv install pycmc # latest release
```
> Using [`Pipenv`](https://github.com/pypa/pipenv) you may need to pin the version, unless you allow for pre-releases. We don't have a beta or alpha qualifier but view this software
> as such. 

And don't forget you need an API subscription and subsequently, auth keys for Chartmetric -- [see below](#authentication).
> &#9888; **Remember: You're not done yet; you'll need to set an authentication environment variable for queries.** 

## Quick start 
If you're already setup with your environment variable, you can query Rihanna's metadata with a quick call to the `artist` module:

```python
>>> import pycmc
>>> rihanna_metadata = pycmc.artist.metadata(cmid=2316)
```

Yep, it's that simple.

> "You should remember that it's peace of mind you're after and not just a fixed machine." 
> _-- Robert Pirsig, via Phaedrus_


### Authentication
Chartmetric requires an authorization process to query their API. You can
see their [docs here](https://api.chartmetric.com/apidoc/#api-Authorization-GetAccessToken). 


#### Add the `CMCREDENTIALS` environment variable

For [`pycmc`](https://pycmc.docs.musicfox.io) you need to set a single
environment variable, `CMCREDENTIALS`, to equal your JSON authentication string of the following:

```json
{
    "token":"",
    "scope":"",
    "expires_in":"",
    "refreshtoken":"your-chartmetric-token-here",
}
```
> 🔎 _Be sure the above is a **string** when you set your environment variable._

#### How to set up `pycmc` authentication

1. Save the JSON file above to disk and note the absolute directory.
2. Using your absolute directory below,
```bash
# REQUIRED - Set your environment variable
export CMCREDENTIALS=$(cat path/to/credentials/file.json)
# OPTIONAL - Remove the .json file you created
rm -rf path/to/credentials/file.json
```

## Design 

To somewhat follow the API design of chartmetric and make our lives easier here,
we'll roughly adhere to the following module design where the `pycmc` package 
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
to the chartmetric.com API, (mostly) labelled as their GET endpoints.  

For example,
```python
>>> 'API ALBUM META URL' = 'https://api.charmetric.io/api/album/:id'
```
#### Album Metadata 
To get an album's metadata just call the metadata function:
```
>>> import pycmc
>>> pycmc.album.metadata('chartmetricID') # return dict of album metatdata
```
#### Spotify top charts

Obviously we'll start with the elephant in the room and get the top
charts from Spotify.

*What was the US jamming to on the first day of the new year?*
```{Python}
>>> cstracks = pycmc.charts.spotify.tracks(date='2019-01-01', ) 
```
#### Apple Music videos charts 

What videos are charting in Apple Music on the same day as above?
```{Python}
>>> applemusic_vcharts = pycmc.charts.itunes.videos(date='2019-01-01')
```
#### Track metatdata

Let's get some metadata on the track _Believe It_ by PARTYNEXTDOOR and Rihanna: 
```{Python}
>>> believe_it = pycmc.track.metadata(cmid='28856569', )
```

## Reference Documentation

We have hosted documentation over at our docs site
[pycmc.docs.musicfox.io](https://pycmc.docs.musicfox.io), which review the many endpoints offered by
the Chartmetric API.

## Problems? Ideas?

We'd love to hear your feedback. Please use the Github for communication about `pycmc`.

### &#128027; Bug Reports &#128030;

Please report bugs or problems in our [issues](https://github.com/musicfox/pycmc/issues) in the Github repository.

### &#127848; Feature Requests
If you have an idea for a feature or suggestion, please open an issue the Github repository. Please describe _what_ you're trying to
accomplish and your idea to fix it with `pycmc`. We'll work through next steps on our end, or together if you'd like to contribute. 


## Contibutions to `pycmc`

Contributions are quite welcome and it's very easy to get started.

### We &#10084; community contributions!

Do note, we do require a contributor license agreement such
that contributors' contributions are protected property, outside of the
"open-source" MIT license covering code here. 

Please see our [`CONTRIBUTING.md`](CONTRIBUTING.md)
to get started.

## `pycmc` development

### Environment setup

- Create an `.env` file in the application directory: `touch pycmc/.env` and populate with:
  ```sh
  export CMCREDENTIALS="your-key"
  ```
- Jump into your dev shell:
  ```sh
  pipenv shell
  ```
- And populate your environment: 
  ```sh
  source pycmc/.env
  ```

🎉 🎸 You're ready to rock! 🎸 🎉

### Running the test suite

You'll obviously need to have an API key for Chartmetric to run tests. 
> ℹ️ The test suite is slowed to ~6s per request to the Chartmetric
API to protect production usage of the same keys, likely an issue (which we've handled herein) since
the API is rate limited.️

**Run tests**
```sh
pytest --cov=pycmc tests
```

#### Upload to the coverage tracker manually

First, DM [@thinkjrs](https://github.com/thinkjrs) for the codecov token, which you'll need
to set below.

Coverage is typically updated automagically but if you need to manually generate the coverage on
https://codecov.io/gh/musicfox/pycmc, run:
```bash
export CODECOV_TOKEN="token-from-@thinkjrs"
./upload_coverage.bash
```
from your bash shell after running tests.

#### CI/CD on GCP
`pycmc` has a runner that builds a Python container, runs tests, and builds
the documentation site when new commits are pushed. As of December 2020 this is private
within the Musicfox Google Cloud Platform account. 

Currently, you can track these builds in the action platform after you've been
given access to the repo. 

> Coming soon! We are planning to migrate to another
solution in the near future along with full tox-support (multiple python package build tests).  