"""
Defines methods for obtaining QQ chart data from the chartmetric API.

Usage:
======

>>> from pycm.charts import qq
>>> qq.insights('2019-01-01') # only available on Thursdays

"""
from .. import utilities

qq_music_url = f"/charts/qq"

def insights(date):
    """
    Get the top tracks on QQ music chart for the given date.
    Data ONLY available on Thursdays.

    https://api.chartmetric.com/api/charts/qq/

    :param date:        string date in ISO format %Y-%m-%d

    :return:            list of dictionary of tracks on QQ music chart
    """
    urlhandle = f"{qq_music_url}/"
    params = {
        "date": date,
    }

    data = utilities.RequestData(urlhandle, params)
    return utilities.RequestGet(data)['data']
