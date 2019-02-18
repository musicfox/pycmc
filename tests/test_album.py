import pytest
import pycm

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

def test_metadata():
    pass

def test_tunefind():
    pass

def test_playlists():
    # playlist placement
    pass
