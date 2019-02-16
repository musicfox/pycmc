"""
utilities.py

Utilities for the pycm api interface.
"""
from functools import wraps
from pathlib import Path
import os
import json
import time
import requests

def TTLwait(func, TTL_seconds = 3600):
    @wraps(func)
    def wrapper(*args, **kwds):
        time.sleep(TTL_seconds)
        return func(*args, **kwds)
    return wrapper

@TTLwait
def PeriodicUpdateCredentials():
    pass

def UpdateCredentials():
    """
    Use the .credentials.json file in the project root directory
    to GET the token, lifetime, and scope attributes and subsequently
    update the .credentials.json file.

    :returns:       None
    """
    filename = ProjectRootDir() + CredentialsFilename()
    # load .credentials.json
    credentials = LoadCredentials() 
    # get new ones
    fetched = FetchAccessToken()
    
    # set em and forget em, for the TTL length
    credentials['token'] = fetched['token']
    credentials['scope'] = fetched['scope']
    credentials['expires_in'] = fetched['expires_in']
    credentials['refreshtoken'] = fetched['refresh_token']
    
    with open(filename, 'w') as fp:
        json.dump(credentials, fp)

def LoadCredentials():
    """
    Load the .credentials.json file from the project root directory
    and return the credentials dictionary.
    
    :returns:       dict w/keys: token, scope, expires_in, refreshtoken
    """
    if CheckCredentials(): # exists and has valid refresh so load it
        with open(ProjectRootDir() + CredentialsFilename(), 'r') as fp:
            f = json.load(fp)
            return f

def CheckCredentials():
    """
    Check that the .credentials.json file is extant within the project
    root directory. Also sets the credentials filename statically.

    It is important that this causes failure as early in the client init
    phase as possible.

    :returns:       boolean True if .credentials.json exists AND the
                    dictionary contains a non-empty string for the
                    "refreshtoken" string, otherwise False.
    """
    # check that path exists
    filepath = f"{ProjectRootDir()}{CredentialsFilename()}"
    # import and check that refreshtoken value is a non-empty string
    if not os.path.exists(filepath):
        raise FileNotFoundError
    with open(filepath) as fp:
        credentials = json.load(fp)
    if credentials['refreshtoken'] != '':
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
    headers = {'Content-Type': 'application/json',}
    refreshtokenkey = 'refreshtoken'
    refreshtoken = LoadCredentials()[refreshtokenkey]
    data = '{' + f'"{refreshtokenkey}":"{refreshtoken}"' + '}'
    response = requests.post(authURL, headers=headers, data=data)
    if not response.ok: # raise if issue
        response.raise_for_status()
    return json.loads(response.text)

def CredentialsFilename(filename = '.credentials.json'):
    """
    Return the given filename.

    :param filename:        string filename w/extension

    :returns:               string given filename w/extension
    """
    return filename

def ProjectRootDir():
    """
    Return path to root directory of project with trailing slash.
    
    :returns:       string path with trailing /
    """
    return f"{Path(__file__).parent.parent}/"
