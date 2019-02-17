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
    assert utilities.FindProcess('root') is not None
    # the below is bogus but should use to test a process on the machine
    assert len(utilities.FindProcess('root')) == 0

def test_BaseURL():
    assert utilities.BaseURL() == "https://api.chartmetric.io/api"
    
