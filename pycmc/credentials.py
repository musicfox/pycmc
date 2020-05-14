"""
# `credentials`

Utilities for the pycmc api credentials interface.

##### Usage

See `credentials_manager` for usage details. 
"""
from functools import wraps
from pathlib import Path
import os
import json
import time
from datetime import datetime
import requests
import logging


def DefaultCredentials(refreshtoken: str) -> None:
    """
    Set the default (only refreshtoken)
    into the CMCREDENTIALS environment variable, warn the user and raise
    a `KeyError` exception.

    **Parameters**

    - `refreshtoken`: the refresh token queried from the Chartmetric API

    """
    # check that the token isn't already present
    if not os.environ.get(
        Varname()
    ):  # create the empty credentials if not extant
        creds = {
            "token": "",
            "scope": "",
            "expires_in": "",
            "refreshtoken": refreshtoken,
        }
        os.environ[Varname()] = json.dumps(creds)
        logging.warning(
            f"CMCREDENTIALS environment variable not set -> credentials.DefaultCredentials: {datetime.now()}."
        )
        raise KeyError(
            "Chartmetric credentials environment varialbe is unset. Setting a default. Please see the documentation for more details."
        )
        # Break exec early as api credentials are not set.


def TTLwait(func,):
    @wraps(func)
    def wrapper(*args, **kwds):
        if len(args) > 0:
            time.sleep(args[0])  # TTL_seconds
        return func(*args, **kwds)

    return wrapper


@TTLwait
def PeriodicUpdate(TTL_seconds=3600, repeat=None):
    """
    Wrapper method to take a TTL variable, wait, and call
    UpdateCredentials. Current chartmetric api documentation (Feb-2019)
    indicates a credential refresh is required every 3600 seconds.

    **Parameters**

    - `TTL_seconds`     integer seconds to wait between refreshes

    - `repeat`          _default_: `None`; integer loops to repeat; -1 = inf 

    **Returns**

    - `None`
    """
    if repeat is not None and repeat > 0:
        counter = 0
        while True and counter < repeat:  # run until out of scope
            Update()
            counter += 1
    elif repeat is not None:
        while True:
            Update()
    else:  # run once, in TTL_seconds seconds
        Update()


def Update() -> None:
    """
    Use the `CMCREDENTIALS` environment variable to make a HTTP
    GET request for the token, lifetime, and scope attributes and subsequently
    update the `CMCREDENTIALS` environment variable. 

    **Returns**

    - `None`
    """
    # load .credentials.json
    credentials = Load()
    # get new ones
    fetched = FetchAccessToken()
    # set em and forget em, for the TTL length
    credentials["token"] = fetched["token"]
    credentials["scope"] = fetched["scope"]
    credentials["expires_in"] = fetched["expires_in"]
    credentials["refreshtoken"] = fetched["refresh_token"]

    os.environ[Varname()] = json.dumps(credentials)
    logging.debug(
        f"Fetched and updated new Chartmetric credentials @ {datetime.now()}"
    )


def Load():
    """
    Load the credentials from the environment
    and return the credentials dictionary.

    **Returns** 

    - `dict` of keys: 
      - `token`,
      - `scope`,
      - `expires_in`,
      - `refreshtoken`.

    """
    if Check():  # exists and has valid refresh so load it
        credentials = json.loads(os.environ.get(Varname()))
        return credentials


def Check():
    """
    Check that the `CMCREDENTIALS` environment variable is extant within the 
    environment.

    It is important that this causes failure as early in the client init
    phase as possible. `DefaultCredentials` will throw if a `refreshtoken` is
    unavailable.

    **Returns**

    - `boolean` `True` if `CMCREDENTIALS` exists AND the dictionary contains a non-empty string for the `refreshtoken` string, otherwise `False`.
    """
    try:
        credentials = json.loads(os.environ.get(Varname()))
    except json.decoder.JSONDecodeError as jderr:
        logging.warning(f"CMCREDENTIALS not found in Check. {datetime.now()}.")
        DefaultCredentials()
        return False

    if credentials["refreshtoken"] != "":
        return True
    return False


def FetchAccessToken():
    """
    Use the refreshtoken to fetch the access and other credentials
    from chartmetric.com.


    **Returns**       
    - A Python Requests response object in dictionary form with keys:
        - `token`,
        - `expires_in`,
        - `refresh_token`,
        - `scope`.

        &#57938; Raises for any non-200 response. See the Requests library documentation.
    """
    authURL = "https://api.chartmetric.com/api/token"
    headers = {"Content-Type": "application/json"}
    refreshtokenkey = "refreshtoken"
    refreshtoken = Load()[refreshtokenkey]
    data = "{" + f'"{refreshtokenkey}":"{refreshtoken}"' + "}"
    response = requests.post(authURL, headers=headers, data=data)
    if not response.ok:  # raise if issue
        response.raise_for_status()
    return json.loads(response.text)


def Varname() -> str:
    """
    **Returns**

    The set charmetric credentials environment variable name.
    """
    return "CMCREDENTIALS"
