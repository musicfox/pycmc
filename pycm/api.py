"""
api.py

Client interface for the chartmetric.io API v1.0, via the ChartMetric
object.

Chartmetric docs: https://api.chartmetric.io/apidoc/

TODO:
pycm docs: https://musicfox.io/pycm/docs

TODO: update with accurate api method names (artist is a placeholder)
Usage:
======

>>> import pycm.api as api
>>> cm = api.ChartMetric()
>>> # get an artist dictionary
>>> print(cm.artist())
"""
import requests
import json
from functools import wraps
import pycm.utilities as utilities
import pycm.credentials as creds


class chartmetric:
    """ 
    pycm: A chartmetric.io API client. 
    
    chartmetric follows a Singleton pattern and is meant to be
    instantiated once, acting as credentials manager and pass-through
    interface for chartmetric.io various API endpoints.
    """
    from pycm import charts # access the charts module containing 
                            # provider-specific methods, e.g. iTunes
    
    def __init__(self,):
        """
        Initialize the ChartMetric API interface. This should be run
        once for an entire session of connectivity as repeated credential
        acquisition will waste resources. 
        """
        creds.Update()  # update credentials w/fresh token
        creds.PeriodicUpdate()
        self.credentials = creds.Load()
        self.token = self.credentials["token"]

    def _requestData(self, urlhandle, date, country, tp):
        """
        Internal method to build a dictionary of data for the 
        API request.

        :param urlhandle:       string additional url after base
                                with a leading and no ending slash
        :param date:            string ISO format date %Y-%m-%d
        :param country:         string country code
        :param tp:              string type 

        :returns:               dictionary w/keys:
                                url, headers, params 
        """
        return {
            "url": f"{utilities.BaseURL()}{urlhandle}",
            "headers": {"Authorization": f"Bearer {self.token}"},
            "params": (
                ("date", date),
                ("code2", country),
                ("duration", "daily"),
                ("type", tp),
            ),
        }
    def _requestGet(self, data):
        """
        Internal method to call requests.get with data.
        """
        response = requests.get(
            data["url"], headers=data["headers"], params=data["params"]
        )
        if not response.ok:  # raise internal exception if bad response
            response.raise_for_status()
        return json.loads(response.text)['obj']
# instantiate the class
cm = chartmetric()
