"""
# `conftest`
The pytest test runner configuration file.

> _Note: You may alter the sleep function in the fixture `slowRoll` to make your tests run faster._
"""
import pytest
import os
import pycm
import json
import datetime


@pytest.fixture(scope="module")
def credvar():
    return "CMCREDENTIALS"


@pytest.fixture(scope="module")
def credential(credvar):
    # load credentials
    return json.loads(os.environ.get(credvar))


if not os.environ.get("CMCREDENTIALS"):
    raise KeyError("CMCREDENTIALS environment variable not set.")


@pytest.fixture(scope="function")
def slowRoll():
    time.sleep(1.2)

@pytest.fixture(scope="module")
def todayStr():
    return str(datetime.datetime.now()).split(' ')[0]

@pytest.fixture(scope="module")
def dates(todayStr):
    return dict(start='2019-06-01', end=todayStr)

@pytest.fixture(scope="module")
def timestampStr():
    return str(datetime.datetime.now()).split(' ')[1]