"""
Unit tests for __ within the pycm module.
"""
import pytest
import json
import sys
import os

@pytest.fixture
def projpath(path=None):
        if path is not None:
        if path[-1] != '/': # add trailing slash
            path += '/'
        return path
    return f"{os.path.dirname(sys.modules['__main__'].__file__)}/"

@pytest.fixture
def credentials(projpath):
    # load credentials
    with open(f"{projpath}/.credentials.json") as fp:
        credentials = json.load(fp)
    return credentials 
