```bash
============================= test session starts ==============================
platform linux -- Python 3.6.8, pytest-3.6.0, py-1.5.3, pluggy-0.6.0 -- /home/jason/.miniconda3/envs/musicfox-research/bin/python
cachedir: .pytest_cache
rootdir: /home/jason/Repos/pycm, inifile:
collecting ... collected 51 items

tests/test_album.py::test_metadata PASSED                                [  1%]
tests/test_album.py::test_tunefind PASSED                                [  3%]
tests/test_album.py::test_playlists PASSED                               [  5%]
tests/test_artist.py::test_fanmetrics PASSED                             [  7%]
tests/test_artist.py::test_listening PASSED                              [  9%]
tests/test_artist.py::test_tunefind PASSED                               [ 11%]
tests/test_artist.py::test_albums PASSED                                 [ 13%]
tests/test_artist.py::test_tracks PASSED                                 [ 15%]
tests/test_artist.py::test_related FAILED                                [ 17%]
tests/test_artist.py::test_metadata PASSED                               [ 19%]
tests/test_artist.py::test_playlists FAILED                              [ 21%]
tests/test_artist.py::test_urls PASSED                                   [ 23%]
tests/test_charts.py::test_spotify_tracks PASSED                         [ 25%]
tests/test_charts.py::test_SpotifyFreshFind PASSED                       [ 27%]
tests/test_charts.py::test_applemusic_tracks PASSED                      [ 29%]
tests/test_charts.py::test_applemusic_albums PASSED                      [ 31%]
tests/test_charts.py::test_applemusic_videos PASSED                      [ 33%]
tests/test_charts.py::test_soundcloud_tracks PASSED                      [ 35%]
tests/test_charts.py::test_shazam_tracks PASSED                          [ 37%]
tests/test_charts.py::test_beatport_tracks PASSED                        [ 39%]
tests/test_charts.py::test_itunes_albums PASSED                          [ 41%]
tests/test_charts.py::test_itunes_tracks PASSED                          [ 43%]
tests/test_charts.py::test_iTunesVideos PASSED                           [ 45%]
tests/test_charts.py::test_YoutubeTrends PASSED                          [ 47%]
tests/test_charts.py::test_youtube_videos PASSED                         [ 49%]
tests/test_charts.py::test_youtube_artists PASSED                        [ 50%]
tests/test_charts.py::test_youtube_tracks PASSED                         [ 52%]
tests/test_credentials.py::test_CredentialsFilename PASSED               [ 54%]
tests/test_credentials.py::test_CheckCredentials PASSED                  [ 56%]
tests/test_credentials.py::test_LoadCredentials PASSED                   [ 58%]
tests/test_credentials.py::test_FetchAccessToken PASSED                  [ 60%]
tests/test_credentials.py::test_UpdateCredentials PASSED                 [ 62%]
tests/test_credentials.py::test_PeriodicCredentials PASSED               [ 64%]
tests/test_credentials.py::test_CredentialsDir PASSED                    [ 66%]
tests/test_credentials.py::test_DefaultCredentials PASSED                [ 68%]
tests/test_credentials_manager.py::test_global_vars PASSED               [ 70%]
tests/test_credentials_manager.py::test_UpdateCredentials PASSED         [ 72%]
tests/test_curator.py::test_lists PASSED                                 [ 74%]
tests/test_curator.py::test_metadata PASSED                              [ 76%]
tests/test_curator.py::test_playlists PASSED                             [ 78%]
tests/test_playlist.py::test_lists PASSED                                [ 80%]
tests/test_playlist.py::test_metadata FAILED                             [ 82%]
tests/test_playlist.py::test_snapshot PASSED                             [ 84%]
tests/test_playlist.py::test_tracks PASSED                               [ 86%]
tests/test_playlist.py::test_evolution FAILED                            [ 88%]
tests/test_track.py::test_metadata PASSED                                [ 90%]
tests/test_track.py::test_tunefind PASSED                                [ 92%]
tests/test_track.py::test_playlists PASSED                               [ 94%]
tests/test_utilities.py::test_projectrootdir PASSED                      [ 96%]
tests/test_utilities.py::test_FindProcess PASSED                         [ 98%]
tests/test_utilities.py::test_BaseURL PASSED                             [100%]

=================================== FAILURES ===================================
_________________________________ test_related _________________________________

    def test_related():
>       test = pycm.artist.related('3380',)

tests/test_artist.py:43: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
pycm/artist.py:103: in related
    return utilities.RequestGet(data)
pycm/utilities.py:96: in RequestGet
    response.raise_for_status()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <Response [400]>

    def raise_for_status(self):
        """Raises stored :class:`HTTPError`, if one occurred."""
    
        http_error_msg = ''
        if isinstance(self.reason, bytes):
            # We attempt to decode utf-8 first because some servers
            # choose to localize their reason strings. If the string
            # isn't utf-8, we fall back to iso-8859-1 for all other
            # encodings. (See PR #3538)
            try:
                reason = self.reason.decode('utf-8')
            except UnicodeDecodeError:
                reason = self.reason.decode('iso-8859-1')
        else:
            reason = self.reason
    
        if 400 <= self.status_code < 500:
            http_error_msg = u'%s Client Error: %s for url: %s' % (self.status_code, reason, self.url)
    
        elif 500 <= self.status_code < 600:
            http_error_msg = u'%s Server Error: %s for url: %s' % (self.status_code, reason, self.url)
    
        if http_error_msg:
>           raise HTTPError(http_error_msg, response=self)
E           requests.exceptions.HTTPError: 400 Client Error: Bad Request for url: https://api.chartmetric.com/api/artist/3380/relatedartists

../../.local/lib/python3.6/site-packages/requests/models.py:935: HTTPError
________________________________ test_playlists ________________________________

dates = {'end': '2018-03-03', 'start': '2018-03-01'}

    def test_playlists(dates):
        # this breaks upstream 04/22/2019
>       test = pycm.artist.playlists('439', 'spotify', dates['start'], 'current')

tests/test_artist.py:54: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
pycm/artist.py:138: in playlists
    return utilities.RequestGet(data)
pycm/utilities.py:96: in RequestGet
    response.raise_for_status()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <Response [400]>

    def raise_for_status(self):
        """Raises stored :class:`HTTPError`, if one occurred."""
    
        http_error_msg = ''
        if isinstance(self.reason, bytes):
            # We attempt to decode utf-8 first because some servers
            # choose to localize their reason strings. If the string
            # isn't utf-8, we fall back to iso-8859-1 for all other
            # encodings. (See PR #3538)
            try:
                reason = self.reason.decode('utf-8')
            except UnicodeDecodeError:
                reason = self.reason.decode('iso-8859-1')
        else:
            reason = self.reason
    
        if 400 <= self.status_code < 500:
            http_error_msg = u'%s Client Error: %s for url: %s' % (self.status_code, reason, self.url)
    
        elif 500 <= self.status_code < 600:
            http_error_msg = u'%s Server Error: %s for url: %s' % (self.status_code, reason, self.url)
    
        if http_error_msg:
>           raise HTTPError(http_error_msg, response=self)
E           requests.exceptions.HTTPError: 400 Client Error: Bad Request for url: https://api.chartmetric.com/api/artist/439/spotify/current/playlists?since=2018-03-01

../../.local/lib/python3.6/site-packages/requests/models.py:935: HTTPError
________________________________ test_metadata _________________________________

dta = {'cmid': '179228', 'stype': 'spotify'}

    def test_metadata(dta):
        """
        This endpoint is breaking upstream. 04-22-2019.
        """
>       test = pycm.playlist.metadata(dta['cmid'], dta['stype'])

tests/test_playlist.py:38: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
pycm/playlist.py:48: in metadata
    return utilities.RequestGet(data)
pycm/utilities.py:96: in RequestGet
    response.raise_for_status()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <Response [400]>

    def raise_for_status(self):
        """Raises stored :class:`HTTPError`, if one occurred."""
    
        http_error_msg = ''
        if isinstance(self.reason, bytes):
            # We attempt to decode utf-8 first because some servers
            # choose to localize their reason strings. If the string
            # isn't utf-8, we fall back to iso-8859-1 for all other
            # encodings. (See PR #3538)
            try:
                reason = self.reason.decode('utf-8')
            except UnicodeDecodeError:
                reason = self.reason.decode('iso-8859-1')
        else:
            reason = self.reason
    
        if 400 <= self.status_code < 500:
            http_error_msg = u'%s Client Error: %s for url: %s' % (self.status_code, reason, self.url)
    
        elif 500 <= self.status_code < 600:
            http_error_msg = u'%s Server Error: %s for url: %s' % (self.status_code, reason, self.url)
    
        if http_error_msg:
>           raise HTTPError(http_error_msg, response=self)
E           requests.exceptions.HTTPError: 400 Client Error: Bad Request for url: https://api.chartmetric.com/api/playlist/spotify/179228

../../.local/lib/python3.6/site-packages/requests/models.py:935: HTTPError
________________________________ test_evolution ________________________________

dates = {'end': '2018-03-03', 'start': '2018-03-01'}

    def test_evolution(dates):
        """
        This endpoint is breaking upstream. 04-22-2019.
        """
        test = pycm.playlist.evolution(439,
                                       'artist',
                                       dates['start'],
>                                      dates['end'])

tests/test_playlist.py:63: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
pycm/playlist.py:100: in evolution
    return utilities.RequestGet(data)
pycm/utilities.py:96: in RequestGet
    response.raise_for_status()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <Response [404]>

    def raise_for_status(self):
        """Raises stored :class:`HTTPError`, if one occurred."""
    
        http_error_msg = ''
        if isinstance(self.reason, bytes):
            # We attempt to decode utf-8 first because some servers
            # choose to localize their reason strings. If the string
            # isn't utf-8, we fall back to iso-8859-1 for all other
            # encodings. (See PR #3538)
            try:
                reason = self.reason.decode('utf-8')
            except UnicodeDecodeError:
                reason = self.reason.decode('iso-8859-1')
        else:
            reason = self.reason
    
        if 400 <= self.status_code < 500:
            http_error_msg = u'%s Client Error: %s for url: %s' % (self.status_code, reason, self.url)
    
        elif 500 <= self.status_code < 600:
            http_error_msg = u'%s Server Error: %s for url: %s' % (self.status_code, reason, self.url)
    
        if http_error_msg:
>           raise HTTPError(http_error_msg, response=self)
E           requests.exceptions.HTTPError: 404 Client Error: Not Found for url: https://api.chartmetric.com/api/playlist/spotify/by/artist/439/evolution?since=2018-03-01&until=2018-03-03

../../.local/lib/python3.6/site-packages/requests/models.py:935: HTTPError
==================== 4 failed, 47 passed in 104.60 seconds =====================
```
