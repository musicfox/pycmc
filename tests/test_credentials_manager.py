import pytest
import json
import pycm.credentials_manager as cm
import pycm.utilities as utilities


def test_global_vars(credential):
    """
    token will be different (as designed) when project
    is running outside of running an individual test runner.

    In other words, if running just this test file, the token
    will be the same. However, if running in a test suite OR
    as a larger package, the token will be different which is the
    intended functionality (we call credentials.Update() within
    credentials_manager so the fixture here *should* be stale.
    """
    assert cm.token != credential["token"]  # see above, may fail
    assert cm.refreshtoken == credential["refreshtoken"]
    assert cm.expires_in == credential["expires_in"]
    assert cm.scope == credential["scope"]


def test_UpdateCredentials(credential):
    # update so that credentials fixture is stale
    cm.UpdateCredentials()
    assert cm.token != credential["token"]
    assert cm.refreshtoken == credential["refreshtoken"]
    assert cm.expires_in > 0  # will throw if type non numeric or 0
    assert cm.scope == "api"
