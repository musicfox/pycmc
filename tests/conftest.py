"""
pytest configuration template

import your custom module and monkeypatch the PYTHONPATH
for a test run

****************
changes required 
****************

- uncomment the import with your module name
- change your directory, e.g. if you were to cd into the directory
    you're writing and then ls you'd see the module_name and tests
    directories (amongst a few others)
"""
import pytest
import os
import pycm

@pytest.fixture(autouse=True) # run automatically prior to tests
def pythonpath(monkeypatch):
    handle = f"/Repos/pycm"
    try:
        project_path = os.environ['HOME'] + handle
        monkeypatch.setenv('PYTHONPATH', project_path) 
    except KeyError as err:
        print(f"$HOME not present -> {err}")
        raise


