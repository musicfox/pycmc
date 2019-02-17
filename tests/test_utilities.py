"""
Unit tests for __ within the pycm module.
"""
import pytest
import json
import sys
import os
import requests
import pycm.utilities as utilities

@pytest.fixture
def projpath(path=None):
    if path is not None:
        if path[-1] != '/': # add trailing slash
            path += '/'
        return path
    return utilities.ProjectRootDir()

def test_projectrootdir():
    """
    NOTE: Test *should* work on other systems but be weary...
    """
    from pathlib import Path
    assert f"{Path(__file__).parent.parent}/" == utilities.ProjectRootDir() 

def test_FindProcess():
    assert utilities.FindProcess('Python') is not None
    assert len(utilities.FindProcess('Python')) > 0

def test_BaseURL():
    assert utilities.BaseURL() == "https://api.chartmetric.io/api"
    
