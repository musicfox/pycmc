"""
Unit tests for __ within the pycm module.
"""
import pytest
import pycm.utilities as utilities


def test_projectrootdir():
    """
    NOTE: Test *should* work on other systems but be weary...
    """
    from pathlib import Path

    assert f"{Path(__file__).parent.parent}/" == utilities.ProjectRootDir()


def test_FindProcess():
    assert utilities.FindProcess("root") is not None
    # the below is bogus but should use to test a process on the machine
    assert len(utilities.FindProcess("root")) == 0


def test_BaseURL():
    assert utilities.BaseURL() == "https://api.chartmetric.com/api"


def test_strDateToday(todayStr):
    assert todayStr == utilities.strDateToday()
    try:
        # strDateToday doesn't take anything, so this should
        # throw
        assert todayStr == utilities.strDateToday("something")
    except Exception as err:
        assert isinstance(err, TypeError)
