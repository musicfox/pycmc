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

def TTLwait(func,):
    """
    Utility waiting function for the credentials.PeriodicUpdate
    method.
    
    :param func:    function PeriodicUpdate from the credentials.py module 
    :returns:       credentials.PeriodicUpdate method instantiation
    """
    @wraps(func)
    def wrapper(*args, **kwds):
        if len(args) > 0:
            TTL_seconds = args[0]
        else:
            TTL_seconds = 3600
        time.sleep(TTL_seconds) 
        return func(*args, **kwds)
    return wrapper

def ProjectRootDir():
    """
    Return path to root directory of project with trailing slash.
    
    :returns:       string path with trailing /
    """
    return f"{Path(__file__).parent.parent}/"
