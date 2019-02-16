"""
Unit tests for credentials.py within pycm.
"""
import pytest
import json
import sys
import os
import requests
import pycm.utilities as utilities
import pycm.credentials as credentials

@pytest.fixture
def projpath(path=None):
    if path is not None:
        if path[-1] != '/': # add trailing slash
            path += '/'
        return path
    return utilities.ProjectRootDir()

@pytest.fixture
def credential(projpath):
    # load credentials
    with open(f"{projpath}/.credentials.json") as fp:
        credential = json.load(fp)
    return credential

@pytest.fixture
def credentials_response(credential):
    """
    Make a request to the charmetric api for the access token and
    return the text of the response.
    """
    authURL = f"https://api.chartmetric.io/api/token"
    headers = {'Content-Type': 'application/json',}
    refreshtokenkey = 'refreshtoken'
    refreshtoken = credential[refreshtokenkey]
    data = '{' + f'"{refreshtokenkey}":"{refreshtoken}"' + '}'

    response = requests.post(authURL, headers=headers, data=data)
  
    if not response.ok: # raise if issue
        response.raise_for_status()
    return response.text
 
def test_CredentialsFilename():
    assert credentials.Filename() == '.credentials.json'

def test_CheckCredentials():
    assert credentials.Check() == True

def test_LoadCredentials(credential):
    assert credential == credentials.Load()

def test_FetchAccessToken(credentials_response):
    # bad response will throw within FetchAccessToken (and will raise
    # within the test runner execution)
    assert credentials_response is not None
    assert credentials_response != ''
    assert credentials.Load()['refreshtoken'] == credentials.FetchAccessToken()['refresh_token']

def test_UpdateCredentials():
    credentials.Update()
    assert os.path.exists(utilities.ProjectRootDir()
               + credentials.Filename()
           )
    assert credentials.Load()['scope'] != ''
    assert credentials.Load()['token'] != ''
    assert credentials.Load()['expires_in'] != ''

def test_PeriodicCredentials():
    credentials.Update()
    stale = credentials.Load()
    credentials.PeriodicUpdate(1) # wait a single second
    new = credentials.Load()
    assert new['token'] != stale['token']

