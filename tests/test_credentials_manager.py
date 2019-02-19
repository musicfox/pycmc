import pytest
import json
import pycm.credentials_manager as cm
import pycm.utilities as utilities
from pycm import credentials as creds
@pytest.fixture
def projpath(path=None):
    if path is not None:
        if path[-1] != '/': # add trailing slash
            path += '/'
        return path
    return utilities.ProjectRootDir()

@pytest.fixture
def cred(projpath):
    with open('.credentials.json', 'r') as fp:
        result = json.loads(fp.read())
    return creds.Load()

def test_global_vars(cred):
    """
    token will be different (as designed) when project
    is running outside of running an individual test runner.

    In other words, if running just this test file, the token
    will be the same. However, if running in a test suite OR
    as a larger package, the token will be different which is the
    intended functionality (we call credentials.Update() within
    credentials_manager so the fixture here *should* be stale.
    """
    assert cm.token != cred['token'] # see above, may fail
    assert cm.refreshtoken == cred['refreshtoken']
    assert cm.expires_in == cred['expires_in']
    assert cm.scope == cred['scope']

def test_UpdateCredentials(cred):
    # update so that credentials fixture is stale
    cm.UpdateCredentials()
    assert cm.token != cred['token']
    assert cm.refreshtoken == cred['refreshtoken']
    assert cm.expires_in > 0 # will throw if type non numeric or 0
    assert cm.scope == 'api'
