"""
utilities.py

Utilities for the pycm api interface.
"""
from functools import wraps
import time

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
    # check that .credentials.json is extant
    # load .credentials.json
    
    pass

def LoadCredentials():
    """
    Load the .credentials.json file from the project root directory
    and return the credentials dictionary.
    
    :returns:       dict w/keys: token, scope, expires_in, refreshtoken
    """
    pass

def CheckCredentials():
    """
    Check that the .credentials.json file is extant within the project
    root directory.

    :returns:       boolean True if .credentials.json exists AND the
                    dictionary contains a non-empty string for the
                    "refreshtoken" string, otherwise False.
    """

    pass 

