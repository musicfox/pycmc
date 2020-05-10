"""
credentials.py

Utilities for the pycm api credentials interface.
"""
from functools import wraps
from pathlib import Path
import os
import json
import time
from datetime import datetime
import requests
import logging


@property
def CredentialsDir(filepath):
    """
    Set the credentials filepath (directory + filename.json)

    :param filepath:        string filepath e.g. /home/user/.credentials.json

    :returns:               string filepath
    """
    return filepath


def DefaultCredentials(refreshtoken: str) -> None:
    """
    # `DefaultCredentials`

    Set the default (only refreshtoken)
    into the CMCREDENTIALS environment variable, warn the user and raise
    a `KeyError` exception.

    ### Parameters
    - `refreshtoken`: the refresh token queried from the Chartmetric API

    """
    # check that the token isn't already present
    if not os.environ.get(Varname()):  # create the empty credentials if not extant
        creds = {
            "token": "",
            "scope": "",
            "expires_in": "",
            "refreshtoken": refreshtoken,
        }
        os.environ[Varname()] = json.dumps(creds)
        logging.warning(f"CMCREDENTIALS environment variable not set -> credentials.DefaultCredentials: {datetime.now()}.")
        raise KeyError("Chartmetric credentials environment varialbe is unset. Setting a default. Please see the documentation for more details.")
        # Break exec early as api credentials are not set.


def ProjectRootDir():
    """
    TODO Rewrite ProjectRootDir doctstring
    Return path to root directory of project with trailing slash.
    
    :returns:       string path with trailing /
    """
    return f"{Path(__file__).parent.parent}/"


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
    TODO Rewrite PeriodicUpdate docstring
    Wrapper method to take a TTL variable, wait, and call
    UpdateCredentials. Current chartmetric api documentation (Feb-2019)
    indicates a credential refresh is required every 3600 seconds.

    :param TTL_seconds:     integer seconds to wait between refreshes
    :param repeat:          integer loops to repeat; -1 = inf 

    :returns:               None
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
    TODO Rewrite the Update docstring
    Use the .credentials.json file in the project root directory
    to GET the token, lifetime, and scope attributes and subsequently
    update the .credentials.json file.

    :returns:       None
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

    #with open(filename, "w") as fp:
    #    json.dump(credentials, fp)
    os.environ[Varname()] = json.dumps(credentials)
    logging.info(f"Fetched and updated new Chartmetric credentials @ {datetime.now()}")

def Load():
    """
    TODO Rewrite the Load docstring
    Load the .credentials.json file from the project root directory
    and return the credentials dictionary.
    
    :returns:       dict w/keys: token, scope, expires_in, refreshtoken
    """
    if Check():  # exists and has valid refresh so load it
        credentials = json.loads(os.environ.get(Varname()))
        return credentials


def Check():
    """
    TODO Rewrite Check docstring
    Check that the .credentials.json file is extant within the project
    root directory. Also sets the credentials filename statically.

    It is important that this causes failure as early in the client init
    phase as possible.

    :returns:       boolean True if .credentials.json exists AND the
                    dictionary contains a non-empty string for the
                    "refreshtoken" string, otherwise False.
    """

    credentials = json.loads(os.environ.get(Varname()))
    if not credentials:
        # this will throw
        DefaultCredentials()
        return False
    if credentials["refreshtoken"] != "":
        return True
    return False


def FetchAccessToken():
    """
    # `FetchAccessToken`

    Use the refreshtoken to fetch the access and other credentials
    from chartmetric.com.


    ## Returns       
    - A Python Requests response object in dictionary form with keys:
        - `token`,
        - `expires_in`,
        - `refresh_token`,
        - `scope`.

    ### Notes
    - Raises for any non-200 response. See the Requests library documentation.
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


def Filename(filename=".credentials.json"):
    """
    Return the given filename.

    :param filename:        string filename w/extension

    :returns:               string given filename w/extension
    """
    return filename


def Filename(filename=".credentials.json"):
    """
    Return the given filename.

    :param filename:        string filename w/extension

    :returns:               string given filename w/extension
    """
    return filename

def Varname() -> str:
    """
    # `Varname`
    Return the set charmetric credentials environment variable name.
    """
    return "CMCREDENTIALS"