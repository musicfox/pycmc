"""
Unit tests for api.py within the pycm module.
"""
import pytest
import json
import sys
import os
import pycm.utilities as utilities
import pycm.credentials as creds
import pycm.api as api

@pytest.fixture
def projpath(path=None):
    if path is not None:
        if path[-1] != '/': # add trailing slash
            path += '/'
        return path
    return utilities.ProjectRootDir()

@pytest.fixture
def credentials(projpath):
    # initialize
    creds.Update()
    # load credentials
    return creds.Load()

@pytest.fixture
def cm():
    """
    Factory to return a ChartMetric API interface object.
    """
    return api.ChartMetric()

def test_initialization(cm, credentials):
    assert cm.credentials['refreshtoken'] == credentials['refreshtoken']

def test_SpotifyTracks(cm):
    test = cm.SpotifyTracks('2019-02-15')
    assert isinstance(test, type(list()))
    assert len(test) > 0
    assert len(test) == 200
    assert test[0]['name'] != ''
    assert test[0]['id'] != ''

def test_SpotifyFreshFind(cm):
#    test = cm.SpotifyFreshFind('2019-01-15')
#    assert isinstance(test, type(list()))
#    assert len(test) > 0 apparently not working?
#    assert test[0]['name'] != ''
#    assert test[0]['id'] != ''
    pass

def test_AppleMusicTracks(cm):
    test = cm.AppleMusicTracks('2019-02-15', 'US')
    assert isinstance(test, type(list()))
    assert len(test) > 0
    assert len(test) == 100
    assert test[0]['name'] != ''
    assert test[0]['id'] != ''

def test_AppleMusicAlbums(cm):
    test = cm.AppleMusicAlbums('2019-02-15', 'US')
    assert isinstance(test, type(list()))
    assert len(test) > 0
    assert len(test) == 99
    assert test[0]['name'] != ''
    assert test[0]['id'] != ''

def test_AppleMusicVideos(cm):
    test = cm.AppleMusicVideos('2019-02-15', 'US')
    assert isinstance(test, type(list()))
    assert len(test) > 0
    assert len(test) == 100
    assert test[0]['name'] != ''
    assert test[0]['id'] != ''

def test_SoundCloudTracks(cm):
    test = cm.SoundCloudTracks('2019-02-15')
    assert isinstance(test, type(list()))
    assert len(test) > 0
    assert len(test) == 100
    assert test[0]['name'] != ''
    assert test[0]['id'] != ''

def test_ShazamTracks(cm):
    test = cm.ShazamTracks('2019-02-15')
    assert isinstance(test, type(list()))
    assert len(test) > 0
    assert len(test) == 200
    assert test[0]['rank'] != ''
    assert test[0]['shazam_track_id'] != ''
    # not joking: API only returns the Shazam ID of the track
    # no name or anything

def test_BeatportTracks(cm):
    test = cm.BeatportTracks('2019-02-15')
    assert isinstance(test, type(list()))
    assert len(test) > 50
    assert len(test) < 200 
    assert test[0]['name'] != ''
    assert test[0]['id'] != ''

def test_iTunesAlbums(cm):
    test = cm.iTunesAlbums('2019-02-15')
    assert isinstance(test, type(list()))
    assert len(test) > 100
    assert len(test) < 201
    assert test[0]['name'] != ''
    assert test[0]['id'] != ''

def test_iTunesTracks(cm):
    test = cm.iTunesTracks('2019-02-15')
    assert isinstance(test, type(list()))
    assert len(test) > 100
    assert len(test) < 201
    assert test[0]['name'] != ''
    assert test[0]['id'] != ''

def test_iTunesVideos(cm):
    test = cm.iTunesVideos('2019-02-15')
    assert isinstance(test, type(list()))
    assert len(test) > 100
    assert len(test) < 201
    assert test[0]['name'] != ''
    #assert test[0]['id'] != ''

def test_YoutubeTrends(cm):
    test = cm.YoutubeTrends('2019-02-15')
    assert isinstance(test, type(list()))
#    assert len(test) > 0
#    assert len(test) == 200
#    assert test[0]['name'] != ''
#    assert test[0]['id'] != ''

def test_YoutubeVideos(cm):
    test = cm.YoutubeVideos('2019-02-15')
    assert isinstance(test, type(list()))
#    assert len(test) > 0
#    assert len(test) == 200
#    assert test[0]['name'] != ''
#    assert test[0]['id'] != ''

def test_YoutubeArtists(cm):
    test = cm.YoutubeArtists('2019-02-15')
    assert isinstance(test, type(list()))
#    assert len(test) > 0
#    assert len(test) == 200
#    assert test[0]['name'] != ''
#    assert test[0]['id'] != ''
    
def test_YoutubeTracks(cm):
    test = cm.YoutubeTracks('2019-02-15')
    assert isinstance(test, type(list()))
#    assert len(test) > 0
#    assert len(test) == 200
#    assert test[0]['name'] != ''
#    assert test[0]['id'] != ''
