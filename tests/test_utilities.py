"""
Unit tests for __ within the pycmc module.
"""
import pytest
import pycmc.utilities as utilities


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


def test_strWeekday(todayStr):
    import datetime
    import pandas as pd

    testtarget = datetime.datetime.weekday(pd.to_datetime(todayStr))
    assert todayStr == utilities.strWeekday(todayStr, target=testtarget)

    aThursday = datetime.datetime.weekday(pd.to_datetime("2019-12-27")) - 1
    aSaturday = aThursday + 2
    testThursday = "2019-12-26"
    testSaturdayAfter = "2019-12-28"
    testSaturdayBefore = "2019-12-21"
    # test for Thursday
    assert testThursday == utilities.strWeekday("2019-12-27", aThursday)
    assert testSaturdayBefore == utilities.strWeekday(
        "2019-12-27", aSaturday, after=False
    )
    assert testSaturdayAfter == utilities.strWeekday(
        "2019-12-27", aSaturday, after=True
    )
