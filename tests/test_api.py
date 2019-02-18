"""
Unit tests for api.py within the pycm module.
"""
import pytest
import json
import sys
import os
import pycm.utilities as utilities
import pycm.credentials as creds
import pycm.api as api
from pycm.charts import *

@pytest.fixture
def projpath(path=None):
    if path is not None:
        if path[-1] != '/': # add trailing slash
            path += '/'
        return path
    return utilities.ProjectRootDir()

@pytest.fixture
def credentials(projpath):
    # initialize
    creds.Update()
    # load credentials
    return creds.Load()

@pytest.fixture
def cm():
    """
    Factory to return a ChartMetric API interface object.
    """
    return api.chartmetric()

def test_initialization(cm, credentials):
    assert cm.credentials['refreshtoken'] == credentials['refreshtoken']
