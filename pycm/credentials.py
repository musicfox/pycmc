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

@property
def CredentialsDir(filepath):
    """
    Set the credentials filepath (directory + filename.json)

    :param filepath:        string filepath e.g. /home/user/.credentials.json

    :returns:               string filepath
    """
    return filepath

def DefaultCredentials(refreshtoken):
    """
    Set and save the a default (only refreshtoken)
    .credentials.json file in the project directory or
    in a custom credentials directory, if set.

    :param refreshtoken:        string refreshtoken from 
                                chartmetric

    :returns:                   None
    """
    cust_dir = isinstance(CredentialsDir, type(str()))
    filepath = f"{ProjectRootDir()}/{Filename()}"\
        if not cust_dir else CredentialsDir

    # extract path from filepath and make the dir, if not extant
    clean = lambda p: str(p.parts[:-1]).replace("'", '').\
            replace(",",'').replace("(", "").replace(")", "").\
            replace(" ", '/')[1:] # first two chars //

    fpath = clean(Path(filepath))
    os.makedirs(fpath, exist_ok=True)
    
    # check that the token isn't already present
    if not os.path.exists(filepath): # create the empty file
        creds = {
            "token":"",
            "scope":"",
            "expires_in":"",
            "refreshtoken": refreshtoken,
        } 
        with open(filepath, 'w') as fp:
            json.dump(creds, fp)
        if not os.path.exists(filepath): # nothing works w/o auth
            raise                        # so break exec early

def ProjectRootDir():
    """
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

def Update():
    """
    Use the .credentials.json file in the project root directory
    to GET the token, lifetime, and scope attributes and subsequently
    update the .credentials.json file.

    :returns:       None
    """
    cust_dir = isinstance(CredentialsDir, type(str()))
    filename = ProjectRootDir() + Filename()\
        if not cust_dir else CredentialsDir

    # load .credentials.json
    credentials = Load()
    # get new ones
    fetched = FetchAccessToken()

    # set em and forget em, for the TTL length
    credentials["token"] = fetched["token"]
    credentials["scope"] = fetched["scope"]
    credentials["expires_in"] = fetched["expires_in"]
    credentials["refreshtoken"] = fetched["refresh_token"]

    with open(filename, "w") as fp:
        json.dump(credentials, fp)


def Load():
    """
    Load the .credentials.json file from the project root directory
    and return the credentials dictionary.
    
    :returns:       dict w/keys: token, scope, expires_in, refreshtoken
    """
    cust_dir = isinstance(CredentialsDir, type(str()))
    filepath = ProjectRootDir() + Filename()\
        if not cust_dir else CredentialsDir

    if Check(filepath):  # exists and has valid refresh so load it
        with open(filepath, "r") as fp:
            f = json.load(fp)
            return f


def Check(filepath=None):
    """
    Check that the .credentials.json file is extant within the project
    root directory. Also sets the credentials filename statically.

    It is important that this causes failure as early in the client init
    phase as possible.

    :returns:       boolean True if .credentials.json exists AND the
                    dictionary contains a non-empty string for the
                    "refreshtoken" string, otherwise False.
    """
    if filepath is None:
        filepath = f"{ProjectRootDir()}/{Filename()}"
    # import and check that refreshtoken value is a non-empty string
    if not os.path.exists(filepath):
        print(f"Bad path: {filepath} @ {datetime.now()}")
        #raise FileNotFoundError
    with open(filepath) as fp:
        credentials = json.load(fp)
    if credentials["refreshtoken"] != "":
        return True
    return False


def FetchAccessToken():
    """
    Use the refreshtoken to fetch the access and other credentials
    from chartmetric.io.

    :returns:       Request object in dictionary form with keys:
                    token, expires_in, refresh_token, and scope
    """
    authURL = f"https://api.chartmetric.io/api/token"
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


