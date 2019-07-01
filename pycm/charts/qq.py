"""
Defines methods for obtaining QQ chart data from the 
chartmetric.com API.

Usage:
======

>>> from pycm.charts import qq
>>> qq.insights('2019-01-01') # who knows what you get back!

"""
import requests
import json
from .. import utilities

qq_music_url = f"/charts/qq"

def insights(date,):
    """
    Query the charts/qq/ endpoint for the
    given date.

    :param date:        string date in ISO format %Y-%m-%y

    :returns:           list of dictionary of QQ music chart data
    """
    urlhandle = f"{qq_music_url}/"
    params = {
        "date": date,
    }

    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)['data']
