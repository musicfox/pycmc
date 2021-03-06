"""
# Unit tests for credentials.py within pycmc.
"""
import pytest
import json
import sys
import os
import requests
import time
import pycmc.utilities as utilities
import pycmc.credentials as credentials


@pytest.fixture
def credentials_response(credential):
    """
    Make a request to the charmetric api for the access token and
    return the text of the response.
    """
    authURL = f"https://api.chartmetric.com/api/token"
    headers = {
        "Content-Type": "application/json",
    }
    refreshtokenkey = "refreshtoken"
    refreshtoken = credential[refreshtokenkey]
    data = "{" + f'"{refreshtokenkey}":"{refreshtoken}"' + "}"

    response = requests.post(authURL, headers=headers, data=data)

    if not response.ok:  # raise if issue
        response.raise_for_status()
    return response.text


def test_CredentialsVariableName():
    assert credentials.Varname() == "CMCREDENTIALS"


def test_CheckCredentials():
    assert credentials.Check() == True


def test_LoadCredentials(credential):
    assert credential == credentials.Load()


def test_FetchAccessToken(credentials_response):
    # bad response will throw within FetchAccessToken (and will raise
    # within the test runner execution)
    assert credentials_response is not None
    assert credentials_response != ""
    assert (
        credentials.Load()["refreshtoken"]
        == credentials.FetchAccessToken()["refresh_token"]
    )


def test_UpdateCredentials():
    credentials.Update()

    assert credentials.Load()["scope"] != ""
    assert credentials.Load()["token"] != ""
    assert credentials.Load()["expires_in"] != ""
    assert credentials.Load()["refreshtoken"] != ""


def test_PeriodicCredentials():
    credentials.Update()
    stale = credentials.Load()
    try:
        credentials.PeriodicUpdate(1, repeat=2)  # wait a single second
        time.sleep(2)
        raise TimeoutError
    except TimeoutError as err:
        pass
    new = credentials.Load()
    assert new["token"] != stale["token"]


def test_DefaultCredentials():
    orig = credentials.Load()
    # change the dir to execution path
    try:
        credentials.DefaultCredentials("fake token")
    except KeyError as kerr:
        assert "CMCREDENTIALS" in kerr
