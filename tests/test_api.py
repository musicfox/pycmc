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

def test_initialization(credentials):
    pass
