"""
Unit tests for credentials.py within pycm.
"""
import pytest
import json
import sys
import os
import requests
import time
import pycm.utilities as utilities
import pycm.credentials as credentials


@pytest.fixture
def filepath(projpath):
    return os.path.join(projpath, ".credentials.json")


@pytest.fixture
def projpath(path=None):
    if path is not None:
        if path[-1] != '/': # add trailing slash
            path += '/'
        return path
    return os.path.join(
        os.environ.get("HOME"),
        ".pycm",
    )


@pytest.fixture
def credential(filepath):
    # load credentials
    with open(filepath) as fp:
        credential = json.load(fp)
    return credential


@pytest.fixture
def credentials_response(credential):
    """
    Make a request to the charmetric api for the access token and
    return the text of the response.
    """
    authURL = f"https://api.chartmetric.com/api/token"
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


def test_CheckCredentials(filepath):
    assert credentials.Check(filepath) == True


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
    # assert os.path.exists(utilities.ProjectRootDir()
    #            + credentials.Filename()
    #        )
    homedir = os.environ.get('HOME')
    assert os.path.exists(
            os.path.join(homedir, '.pycm', credentials.Filename())
    )
    assert credentials.Load()['scope'] != ''
    assert credentials.Load()['token'] != ''
    assert credentials.Load()['expires_in'] != ''


def test_PeriodicCredentials():
    credentials.Update()
    stale = credentials.Load()
    try:
        credentials.PeriodicUpdate(1, repeat=2) # wait a single second
        time.sleep(2)
        raise TimeoutError
    except TimeoutError as err:
        pass
    new = credentials.Load()
    assert new['token'] != stale['token']


def test_CredentialsDir(filepath):
    test = credentials.CredentialsDir
    assert test != os.path.join(os.getcwd(), '.credentials.json') 
    credentials.CredentialsDir = filepath
    test2 = credentials.CredentialsDir
    assert test2 == filepath


def test_DefaultCredentials(filepath, ):
    projfilepath = os.path.join(
        os.environ.get("HOME"),
        ".pycm",
        ".credentials.json"
    )
    credentials.CredentialsDir = projfilepath
    orig = credentials.Load()
    # change the dir to execution path
    credentials.CredentialsDir = os.path.join(os.getcwd(), ".credentials.json")
    credentials.DefaultCredentials('fake token')
    bad = credentials.Load()

    assert os.path.exists(filepath)
    assert orig != bad
    assert bad['refreshtoken'] == 'fake token'
    assert len(bad.keys()) == 4

    # reset creds
    credentials.CredentialsDir = projfilepath
 
    # fail the test if we're not normal...
    assert credentials.Load()['refreshtoken'] != 'fake token'
