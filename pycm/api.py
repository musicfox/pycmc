"""
api.py

Client interface for the chartmetric.io API v1.0, via the ChartMetric
object.

Chartmetric docs: https://api.chartmetric.io/apidoc/

TODO:
pycm docs: https://musicfox.io/pycm/docs

TODO: update with accurate api method names (artist is a placeholder)
Usage:
======

>>> import pycm.api as api
>>> cm = api.ChartMetric()
>>> # get an artist dictionary
>>> print(cm.artist())
"""
import requests
import json
from functools import wraps
import pycm.utilities as utilities
import pycm.credentials as creds


class ChartMetric:
    """ pycm: A chartmetric.io API client. """

    def __init__(self,):
        """
        Initialize the ChartMetric API interface. This should be run
        once for an entire session of connectivity as repeated credential
        acquisition will waste resources. 
        """
        creds.Update()  # update credentials w/fresh token
        creds.PeriodicUpdate()
        self.credentials = creds.Load()
        self.token = self.credentials["token"]

    def _requestData(self, urlhandle, date, country, tp):
        """
        Internal method to build a dictionary of data for the 
        API request.

        :param urlhandle:       string additional url after base
                                with a leading and no ending slash
        :param date:            string ISO format date %Y-%m-%d
        :param country:         string country code
        :param tp:              string type 

        :returns:               dictionary w/keys:
                                url, headers, params 
        """
        return {
            "url": f"{utilities.BaseURL()}{urlhandle}",
            "headers": {"Authorization": f"Bearer {self.token}"},
            "params": (
                ("date", date),
                ("code2", country),
                ("duration", "daily"),
                ("type", tp),
            ),
        }
    def _requestGet(self, data):
        """
        Internal method to call requests.get with data.
        """
        response = requests.get(
            data["url"], headers=data["headers"], params=data["params"]
        )
        if not response.ok:  # raise internal exception if bad response
            response.raise_for_status()
        return json.loads(response.text)['obj']

    def SpotifyTracks(self, date, country="US", viral=False):
        """
        Query the charts/spotify/tracks endpoint for the
        given date.

        :param date:        string date in ISO format %Y-%m-%y

        :returns:           list of dictionary of spotify chart data
        """
        data = self._requestData(
            "/charts/spotify/tracks",
            date,
            country,
            "viral" if viral else "regional",
        )
        return self._requestGet(data)

    def SpotifyFreshFind(self, date, ):
        """
        Query the charts/spotify/freshfind endpoint for the
        given date.

        :param date:        string date in ISO format %Y-%m-%y

        :returns:           list of dictionary of spotify chart data
        """
        data = {
            'url': f"{utilities.BaseURL()}/charts/spotify/freshfind",
            'headers': {
                'Authorization': f"Bearer {self.token}",
            },
            'params': (
                ('date', date),
            ),
        }
        response = requests.get(
            data["url"], headers=data["headers"], params=data["params"]
        )
        if not response.ok:  # raise internal exception if bad response
            response.raise_for_status()
        return json.loads(response.text)

    def AppleMusicTracks(self, date, country, genre = 'All Genres'):
        """
        Query the charts/apple_music/tracks endpoint for the
        given date.

        :param date:        string date in ISO format %Y-%m-%y
        :param country:     string country code, e.g. 'US'
        :genre:             string genre (see CM docs)

        :returns:           list of dictionary of apple music chart data
        """
        data = {
            'url': f"{utilities.BaseURL()}/charts/apple_music/tracks",
            'headers': {
                'Authorization': f"Bearer {self.token}",
            },
            'params': (
                ('date', date),
                ('code2', country),
                ('genre', genre),
                ('chart_type', 'daily'),
            ),
        }
        return self._requestGet(data)

    def AppleMusicAlbums(self, date, country, genre = 'All Genres'):
        """
        Query the charts/apple_music/albums endpoint for the
        given date.

        :param date:        string date in ISO format %Y-%m-%y
        :param country:     string country code, e.g. 'US'
        :genre:             string genre (see CM docs)

        :returns:           list of dictionary of apple music chart data
        """
        data = {
            'url': f"{utilities.BaseURL()}/charts/apple_music/albums",
            'headers': {
                'Authorization': f"Bearer {self.token}",
            },
            'params': (
                ('date', date),
                ('code2', country),
                ('genre', genre),
            ),
        }
        return self._requestGet(data)

    def AppleMusicVideos(self, date, country, genre = 'All Genres'):
        """
        Query the charts/apple_music/videos endpoint for the
        given date.

        :param date:        string date in ISO format %Y-%m-%y
        :param country:     string country code, e.g. 'US'
        :genre:             string genre (see CM docs)

        :returns:           list of dictionary of apple music chart data
        """
        data = {
            'url': f"{utilities.BaseURL()}/charts/apple_music/videos",
            'headers': {
                'Authorization': f"Bearer {self.token}",
            },
            'params': (
                ('date', date),
                ('code2', country),
                ('genre', genre),
            ),
        }
        return self._requestGet(data)

