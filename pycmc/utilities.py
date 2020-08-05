"""
utilities.py

Utilities for the pycmc api interface.
"""
from functools import wraps
from pathlib import Path
import os
import json
import time
import requests
import psutil
from importlib import reload
from . import credentials_manager
import datetime
import pandas as pd


def TTLwait(func,):
    """
    Utility waiting function for the credentials.PeriodicUpdate
    method.
    
    **Parameters**

    - `func`:    function PeriodicUpdate from the credentials.py module 
    
    **Returns**       

    credentials.PeriodicUpdate method instantiation
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
    
    **Returns**       

    string path with trailing /
    """
    return f"{Path(__file__).parent.parent}/"


def FindProcess(name):
    """
    Return a list of processes matching given name.

    **Parameters**

    - `name`:        string process name
    
    **Returns**           

    list of items matching process 'name'
    """
    it = psutil.process_iter(attrs=["name"])
    result = [p for p in it if p.info["name"] == name]
    return result


def BaseURL():
    return f"https://api.chartmetric.com/api"


def RequestData(urlhandle, params):
    """
    Build chartmetric data object and call requests.get with 
    constructed data.
    
    **Parameters**

    - `urlhandle`:       string additional url after base
                            *with a leading* and *without ending slash*
    
    - `params`:          dictionary of keyword data to send in the
                            query string, specific to the particular 
    			            api endpoint
    
    **Returns**
    
    A dictionary with keys url, headers and params.
    """
    reload(
        credentials_manager
    )  # TODO Fix side effect, this is horrible style/architecture
    return {
        "url": f"{BaseURL()}{urlhandle}",
        "headers": {"Authorization": f"Bearer {credentials_manager.token}"},
        "params": params,
    }


def RequestGet(data):
    """
    Method to call requests.get with data.

    **Parameters**

    - `data`:        dictionary with at least the following 
    
        key:value pairs: url, headers, params
    
    **Returns**           

    A dictionary of request data. 
    """
    response = requests.get(
        data["url"], headers=data["headers"], params=data["params"]
    )
    if not response.ok:  # raise internal exception if bad response
        response.raise_for_status()
    return json.loads(response.text).get("obj")


def strDateToday():
    """
    Simple method to return the string date of today as given by the datetime
    module.

    Specifically, a string is returned in ISO Year-Month-Day format.

    **Parameters**

    None

    **Returns**

    A Python `str` representing the ISO date.
    """
    return str(datetime.datetime.today()).split(" ")[0]


def strWeekday(date: str, target: int, after: bool = False,) -> str:
    """
    Given a ISO string `date` return the nearest `target` weekday.

    **Parameters**

    - `date`: The date around which the caller would like target searched.

    - `target`: Weekday number as in the `datetime` Standard Library Module.

    **Returns**

    The ISO YYYY-MM-DD string representation of the nearest given weekday.
    """
    dtdate = pd.to_datetime(date)
    if datetime.datetime.weekday(dtdate) != target:
        if not after:
            date = str(dtdate - pd.offsets.Week(weekday=target)).split(" ")[0]
        else:
            date = str(dtdate + pd.offsets.Week(weekday=target)).split(" ")[0]
    return date
