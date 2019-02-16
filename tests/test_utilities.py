"""
Unit tests for __ within the pycm module.
"""
import pytest
import json
import sys
import os
import requests
import pycm.utilities as utilities

@pytest.fixture
def projpath(path=None):
    if path is not None:
        if path[-1] != '/': # add trailing slash
            path += '/'
        return path
    return utilities.ProjectRootDir()

@pytest.fixture
def credentials(projpath):
    # load credentials
    with open(f"{projpath}/.credentials.json") as fp:
        credentials = json.load(fp)
    return credentials 

@pytest.fixture
def credentials_response(credentials):
    """
    Make a request to the charmetric api for the access token and
    return the text of the response.
    """
    authURL = f"https://api.chartmetric.io/api/token"
    headers = {'Content-Type': 'application/json',}
    refreshtokenkey = 'refreshtoken'
    refreshtoken = credentials[refreshtokenkey]
    data = '{' + f'"{refreshtokenkey}":"{refreshtoken}"' + '}'

    response = requests.post(authURL, headers=headers, data=data)
  
    if not response.ok: # raise if issue
        response.raise_for_status()
    return response.text
 
def test_CredentialsFilename():
    assert utilities.CredentialsFilename() == '.credentials.json'

def test_CheckCredentials():
    assert utilities.CheckCredentials() == True

def test_LoadCredentials(credentials):
    assert credentials == utilities.LoadCredentials()

def test_FetchAccessToken(credentials_response):
    # bad response will throw within FetchAccessToken (and will raise
    # within the test runner execution)
    assert credentials_response is not None
    assert credentials_response != ''
    assert utilities.LoadCredentials()['refreshtoken'] == utilities.FetchAccessToken()['refresh_token']

def test_UpdateCredentials():
    utilities.UpdateCredentials()
    assert os.path.exists(utilities.ProjectRootDir() + '.credentials.json')
    assert utilities.LoadCredentials()['scope'] != ''
    assert utilities.LoadCredentials()['token'] != ''
    assert utilities.LoadCredentials()['expires_in'] != ''

def test_PeriodicCredentials():
    pass

def test_projectrootdir():
    """
    NOTE: Test *should* work on other systems but be weary...
    """
    from pathlib import Path
    assert f"{Path(__file__).parent.parent}/" == utilities.ProjectRootDir() 
